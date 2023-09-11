# RSS-GPT

[中文](README-zh.md)

## Features
- Host your own RSS feeds on GitHub repo and GitHub Pages.
- Using ChatGPT to summarize your personalized RSS feeds. 
- Aggregate multiple RSS feeds into one.
- Add filters to your own personalized RSS feeds.

## Configuration

### 1. Fork this repo

### 2. Add Repository Secrets

- U_NAME: your GitHub username
- U_EMAIL: your GitHub email
- WORK_TOKEN: your GitHub personal access with `repo` and `workflow` scope
- OPENAI_API_KEY: your OpenAI API key, get it from [here](https://platform.openai.com/account/api-keys)

### 3. Enable GitHub Actions to access Pages in repo settings

### 4. Configure your RSS feeds in config.ini
There is a step-by-step [manual](https://yinan.me/RSS-GPT-manual-en/).

### 5. Change the links in 'main.py' to your own GitHub pages.

## Hosted RSS Feeds in this repo, feel free to subscribe

- https://www.ifanr.com/feed -> https://yinan.me/RSS-GPT/rss/ifanr.xml
- https://brett.trpstra.net/brettterpstra -> https://yinan.me/RSS-GPT/rss/brett-terpstra.xml
- https://meta.appinn.net/tag/chrome.rss, https://meta.appinn.net/tag/ios.rss, https://meta.appinn.net/tag/macos.rss -> https://yinan.me/RSS-GPT/rss/appinn.xml
