# RSS-GPT

[![](https://img.shields.io/github/actions/workflow/status/yinan-c/RSS-GPT/cron-job.yml?label=cron-job)](https://github.com/yinan-c/RSS-GPT/actions/workflows/cron-job.yml)
[![](https://img.shields.io/github/actions/workflow/status/yinan-c/RSS-GPT/jekyll-gh-pages.yml?label=GitHub%20Pages)](https://github.com/yinan-c/RSS-GPT/actions/workflows/jekyll-gh-pages.yml)


[Configuration Guide](https://yinan.me/rss-gpt-manual-en.html) | [中文介绍](README-zh.md) | [中文教程](https://yinan.me/rss-gpt-manual-zh.html) 

## Features

- Host your own RSS feeds on GitHub repo and GitHub Pages.
- Using ChatGPT to summarize your personalized RSS feeds. 
- Aggregate multiple RSS feeds into one.
- Add filters to your own personalized RSS feeds.

## Configuration

- Fork this repo
- Add Repository Secrets
    - U_NAME: your GitHub username
    - U_EMAIL: your GitHub email
    - WORK_TOKEN: your GitHub personal access with `repo` and `workflow` scope
    - OPENAI_API_KEY: your OpenAI API key, get it from [here](https://platform.openai.com/account/api-keys)
- Enable GitHub Actions to deploy GitHub Pages in repo settings
- Configure your RSS feeds in config.ini
- Change the links in 'main.py' to your own GitHub pages.

You can check out [here](https://yinan.me/rss-gpt-manual-en.html) for a more detailed configuration guide.

## Hosted RSS Feeds in this repo, feel free to subscribe

- https://www.ifanr.com/feed -> https://yinan-c.github.io/RSS-GPT/rss/ifanr.xml
- https://brett.trpstra.net/brettterpstra -> https://yinan-c.github.io/RSS-GPT/rss/brett-terpstra.xml
- https://meta.appinn.net/tag/chrome.rss, https://meta.appinn.net/tag/ios.rss, https://meta.appinn.net/tag/macos.rss -> https://yinan-c.github.io/RSS-GPT/rss/appinn.xml
