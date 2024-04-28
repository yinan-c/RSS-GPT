import configparser
import os
from jinja2 import Template
from bs4 import BeautifulSoup
import datetime
import xml.etree.ElementTree as ET
from datetime import datetime


def check_existing_report(base_path, date):
    """
    Check if a report for the given date already exists in the docs folder.
    """
    # Format date as YYYY-MM-DD
    formatted_date = date.strftime("%Y-%m-%d")
    # Check for an XML file with that date in the base directory (docs)
    file_path = os.path.join(base_path, f"{formatted_date}.xml")
    return os.path.exists(file_path)


def get_selected_sources(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    selected_sources = config.get("General", "selected_sources").split(",")
    # build a dictionary of {source: name} for selected sources
    sources = {}
    for source in selected_sources:
        name = config.get(source, "name", fallback=None)
        if not name:
            raise Exception(f"Error: Source {source} not found in config file.")
        sources[source] = name.strip('"')
    return sources


def find_xml_files(base_path, sources):
    xml_files = {}
    for key, name in sources.items():
        xml_path = os.path.join(base_path, f"{name}.xml")
        print(xml_path)
        if os.path.exists(xml_path):
            xml_files[name] = xml_path
    return xml_files


# Step 3: Extract Summaries from Local XML Files


def extract_summaries_from_xml(files, date: datetime):
    summaries = []
    for file in files:
        print(file)
        tree = ET.parse(file)
        root = tree.getroot()
        for idx, item in enumerate(root.findall(".//item")):
            title = item.find("title").text
            link = item.find("link").text
            pub_date_str = item.find("pubDate").text
            pub_date = datetime.strptime(pub_date_str, "%a, %d %b %Y %H:%M:%S %Z")
            if pub_date.date() != date.date():
                continue
            content_encoded = item.find(
                "{http://purl.org/rss/1.0/modules/content/}encoded"
            )
            if content_encoded is not None:
                soup = BeautifulSoup(content_encoded.text, "html.parser")
                divs = soup.select('div:-soup-contains("总结")')
                if divs:
                    summary = divs[0].text
                    summaries.append({"title": title, "summary": summary, "link": link})
    return summaries


def generate_daily_report(base_path, date, summaries):
    # Format date as YYYY-MM-DD
    formatted_date = date.strftime("%Y-%m-%d")
    # Check for an XML file with that date in the base directory (docs)
    file_path = os.path.join(base_path, f"{formatted_date}.xml")
    template = Template(open("template.xml").read())
    # transform summaries object into a format can be used by the template
    entries = [
        {
            "title": summary["title"],
            "link": summary["link"],
            "summary": summary["summary"],
        }
        for summary in summaries
    ]
    with open(file_path, "w") as f:
        rss = template.render(
            feed={
                "feed": {
                    "title": "Daily Report",
                    "link": "https://example.com",
                    "description": "Daily Report",
                    "language": "en",
                }
            },
            append_entries=entries,
            existing_entries=[],
        )
        f.write(rss)


if __name__ == "__main__":
    # Step 1: Check for Existing Report
    base_path = "docs"
    date = datetime.now()
    if check_existing_report(base_path, date):
        print("Report already exists for today.")
        exit(0)

    # Step 2: Get Selected Sources from Config
    sources = get_selected_sources("config.ini")

    # Step 3: Find XML Files for Selected Sources
    xml_files = find_xml_files(base_path, sources)

    # Step 4: Extract Summaries from Local XML Files
    summaries = extract_summaries_from_xml(xml_files.values(), date)

    # Step 5: Generate Daily Report
    generate_daily_report(base_path, date, summaries)
    print("Daily report generated successfully.")
