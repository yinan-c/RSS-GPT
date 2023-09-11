import feedparser
import configparser
import os
from openai import ChatCompletion
from jinja2 import Template
from bs4 import BeautifulSoup
import re
import datetime
#from dateutil.parser import parse

def get_cfg(sec, name, default=None):
    value=config.get(sec, name, fallback=default)
    if value:
        return value.strip('"')

def set_cfg(sec, name, value):
    config.set(sec, name, '"%s"' % value)

def clean_html(html_content):
    """
    This function is used to clean the HTML content.
    It will remove all the <script>, <style>, <img>, <a>, <video>, <audio>, <iframe>, <input> tags.
    Returns:
        Cleaned text for summarization
    """
    soup = BeautifulSoup(html_content, "html.parser")

    for script in soup.find_all("script"):
        script.decompose()

    for style in soup.find_all("style"):
        style.decompose()

    for img in soup.find_all("img"):
        img.decompose()

    for a in soup.find_all("a"):
        a.decompose()

    for video in soup.find_all("video"):
        video.decompose()

    for audio in soup.find_all("audio"):
        audio.decompose()
    
    for iframe in soup.find_all("iframe"):
        iframe.decompose()
    
    for input in soup.find_all("input"):
        input.decompose()

    return soup.get_text()

def filter_entry(entry, filter_apply, filter_type, filter_rule):
    """
    This function is used to filter the RSS feed.

    Args:
        entry: RSS feed entry
        filter_apply: title, article or link
        filter_type: include or exclude or regex match or regex not match
        filter_rule: regex rule or keyword rule, depends on the filter_type

    Raises:
        Exception: filter_apply not supported
        Exception: filter_type not supported
    """
    if filter_apply == 'title':
        text = entry.title
    elif filter_apply == 'article':
        text = entry.article
    elif filter_apply == 'link':
        text = entry.link
    elif not filter_apply:
        return True
    else:
        raise Exception('filter_apply not supported')

    if filter_type == 'include':
        return re.search(filter_rule, text)
    elif filter_type == 'exclude':
        return not re.search(filter_rule, text)
    elif filter_type == 'regex match':
        return re.search(filter_rule, text)
    elif filter_type == 'regex not match':
        return not re.search(filter_rule, text)
    elif not filter_type:
        return True
    else:
        raise Exception('filter_type not supported')

def read_entry_from_file(sec):
    """
    This function is used to read the RSS feed entries from the feed.xml file.

    Args:
        sec: section name in config.ini
    """
    out_dir = os.path.join(BASE, get_cfg(sec, 'name'))
    try:
        with open(out_dir + '.xml', 'r') as f:
            rss = f.read()
        feed = feedparser.parse(rss)
        return feed.entries
    except:
        return []

def truncate_entries(entries, max_entries):
    if len(entries) > max_entries:
        entries = entries[:max_entries]
    return entries

def gpt_summary(query,model,language):
    if language == "zh":
        messages = [
            {"role": "user", "content": query},
            {"role": "assistant", "content": f"请用中文总结这篇文章，先提取出{keyword_length}个关键词，在同一行内输出，然后换行，用中文在{summary_length}字内写一个简短总结，包含全部要点，按照以下格式输出'<br><br>总结:'，<br>是HTML的换行符，输出时必须保留2个，并且必须在'总结:'二字之前"}
        ]
    else:
        messages = [
            {"role": "user", "content": query},
            {"role": "assistant", "content": f"Please summarize this article in {language} language, first extract {keyword_length} keywords, output them in the same line like 'keyword1, keyword2, keyword3 ...'. Then write a short summary in {summary_length} words, and output in the following format '<br><br>Summary:' in target language {language} , <br> is the line break of HTML, 2 must be retained when output, and it must be before the word 'Summary:'"}
        ]
    chat = ChatCompletion.create(
        model=model,
        api_key=OPENAI_API_KEY,
        messages=messages,
    )
    return chat["choices"][0]["message"]["content"]

def output(sec, language):
    """ output
    This function is used to output the summary of the RSS feed.

    Args:
        sec: section name in config.ini

    Raises:
        Exception: filter_apply, type, rule must be set together in config.ini
    """
    log_file = os.path.join(BASE, get_cfg(sec, 'name') + '.log')
    out_dir = os.path.join(BASE, get_cfg(sec, 'name'))
    # read rss_url as a list separated by comma
    rss_urls = get_cfg(sec, 'url')
    rss_urls = rss_urls.split(',')

    # RSS feed filter apply, filter title, article or link, summarize title, article or link
    filter_apply = get_cfg(sec, 'filter_apply')

    # RSS feed filter type, include or exclude or regex match or regex not match
    filter_type = get_cfg(sec, 'filter_type')

    # Regex rule or keyword rule, depends on the filter_type
    filter_rule = get_cfg(sec, 'filter_rule')

    # filter_apply, type, rule must be set together
    if filter_apply and filter_type and filter_rule:
        pass
    elif not filter_apply and not filter_type and not filter_rule:
        pass
    else:
        raise Exception('filter_apply, type, rule must be set together')

    # Max number of items to summarize
    max_items = int(get_cfg(sec, 'max_items'))
    cnt = 0
    existing_entries = read_entry_from_file(sec)
    with open(log_file, 'a') as f:
        f.write('------------------------------------------------------\n')
        f.write(f'Started: {datetime.datetime.now()}\n')
        f.write(f'Existing_entries: {len(existing_entries)}\n')
    existing_entries = truncate_entries(existing_entries, max_entries=max_entries)
    # Be careful when the deleted ones are still in the feed, in that case, you will mess up the order of the entries.
    # Truncating old entries is for limiting the file size, 1000 is a safe number to avoid messing up the order.
    append_entries = []

    for rss_url in rss_urls:
        with open(log_file, 'a') as f:
            f.write(f"Fetching from {rss_url}\n")
            print(f"Fetching from {rss_url}")
        feed = feedparser.parse(rss_url)
        if feed.status != 200:
            with open(log_file, 'a') as f:
                f.write(f"Feed error: {feed.status}\n")
            continue
        if feed.bozo:
            with open(log_file, 'a') as f:
                f.write(f"Feed error: {feed.bozo_exception}\n")
            continue
        for entry in feed.entries:
            if cnt > max_entries:
                with open(log_file, 'a') as f:
                    f.write(f"Skip from: [{entry.title}]({entry.link})\n")
                break

            if entry.link in [x.link for x in existing_entries]:
                continue

            if entry.link in [x.link for x in append_entries]:
                continue

            try:
                entry.article = entry.content[0].value
            except:
                entry.article = entry.description
            cleaned_article = clean_html(entry.article)

            if not filter_entry(entry, filter_apply, filter_type, filter_rule):
                with open(log_file, 'a') as f:
                    f.write(f"Filter: [{entry.title}]({entry.link})\n")
                continue

            with open(log_file, 'a') as f:
                f.write(f"Append: [{entry.title}]({entry.link})\n")

#            # format to Thu, 27 Jul 2023 13:13:42 +0000
#            if 'updated' in entry:
#                entry.updated = parse(entry.updated).strftime('%a, %d %b %Y %H:%M:%S %z')
#            if 'published' in entry:
#                entry.published = parse(entry.published).strftime('%a, %d %b %Y %H:%M:%S %z')

            cnt += 1
            if cnt > max_items:
                entry.summary = None
            else:
                token_length = len(cleaned_article)
                if token_length > 16000:
                    entry.summary = gpt_summary(cleaned_article[:16000],model="gpt-3.5-turbo-16k", language=language)
                    with open(log_file, 'a') as f:
                        f.write(f"Token length: {token_length}\n")
                        f.write(f"Truncate to 16k token length\n")
                        f.write(f"Summarized using GPT-3.5-turbo-16k\n")
                else:
                    try:
                        entry.summary = gpt_summary(cleaned_article,model="gpt-3.5-turbo", language=language)
                        with open(log_file, 'a') as f:
                            f.write(f"Token length: {token_length}\n")
                            f.write(f"Summarized using GPT-3.5-turbo\n")
                    except:
                        entry.summary = gpt_summary(cleaned_article,model="gpt-3.5-turbo-16k", language=language)
                        with open(log_file, 'a') as f:
                            f.write(f"Token length: {token_length}\n")
                            f.write(f"Summarized using GPT-3.5-turbo-16k\n")
            append_entries.append(entry)

    with open(log_file, 'a') as f:
        f.write(f'append_entries: {len(append_entries)}\n')

    template = Template(open('template.xml').read())
    
    try:
        rss = template.render(feed=feed, append_entries=append_entries, existing_entries=existing_entries)
        with open(out_dir + '.xml', 'w') as f:
            f.write(rss)
        with open(log_file, 'a') as f:
            f.write(f'Finish: {datetime.datetime.now()}\n')
    except:
        with open (log_file, 'a') as f:
            f.write(f"error when rendering xml, skip {out_dir}\n")
            print(f"error when rendering xml, skip {out_dir}\n")

config = configparser.ConfigParser()
config.read('config.ini')
secs = config.sections()
# Maxnumber of entries to in a feed.xml file
max_entries = 1000


OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

BASE =get_cfg('cfg', 'BASE')
keyword_length = int(get_cfg('cfg', 'keyword_length'))
summary_length = int(get_cfg('cfg', 'summary_length'))
language = get_cfg('cfg', 'language')

try:
    os.mkdir(BASE)
except:
    pass

readme ="README.md"
feeds = []
links = []
with open(os.path.join(BASE, 'index.html'), 'w') as f:
    for x in secs[1:]:
        output(x, language=language)
        feed = {"url": get_cfg(x, 'url').replace(',','<br>'), "name": get_cfg(x, 'name')}
        feeds.append(feed)
        links.append("- "+ get_cfg(x, 'url').replace(',',', ') + " -> https://yinan-c.github.io/RSS-GPT/rss/" + feed['name'] + ".xml\n")

    template = Template(open('template.html').read())
    html = template.render(update_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), feeds=feeds)
    f.write(html)

f = open(readme, "r+", encoding="UTF-8")
list1 = f.readlines()
list1= list1[:29] + links

f = open(readme, "w+", encoding="UTF-8")
f.writelines(list1)
f.close()
