import xml.etree.ElementTree as ET
import configparser
import os

def format_with_quotes(s):
    """Escape percent signs and wrap the string with quotes for configparser compatibility."""
    return f'"{s.replace("%", "%%")}"'  # Escape percent signs and wrap with quotes

def get_next_source_number(config):
    """Get the next source number to use for appending."""
    existing_sources = [section for section in config.sections() if section.startswith("source")]
    if not existing_sources:
        return 1  # Start from 1 if no sources
    max_num = max(int(source.replace('source', '')) for source in existing_sources)
    return max_num + 1  # Next number after the highest

def opml_to_ini(opml_file, ini_file):
    config = configparser.ConfigParser()

    if os.path.exists(ini_file):
        config.read(ini_file)
    
    if 'cfg' not in config:
        config['cfg'] = {
            'base': format_with_quotes('docs/'),
            'language': format_with_quotes('zh'),
            'keyword_length': format_with_quotes('5'),
            'summary_length': format_with_quotes('200')
        }

    next_source_num = get_next_source_number(config)

    tree = ET.parse(opml_file)
    root = tree.getroot()

    for i, outline in enumerate(root.findall('.//outline'), start=next_source_num):
        name = outline.attrib.get('text')
        url = outline.attrib.get('xmlUrl')

        if url is None or name is None:
            continue

        section_name = f"source{str(i).zfill(3)}"
        config[section_name] = {
            'name': format_with_quotes(name),
            'url': format_with_quotes(url),
            'max_items': format_with_quotes('0')  # Default value, adjust as necessary
        }

    with open(ini_file, 'w') as configfile:
        config.write(configfile)

import sys
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python helper.py <opml_file> <ini_file>')
        sys.exit(1)

    opml_file = sys.argv[1]
    ini_file = sys.argv[2]

    opml_to_ini(opml_file, ini_file)

