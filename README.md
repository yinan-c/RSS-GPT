# RSS-GPT

![](https://img.shields.io/github/last-commit/yinan-c/RSS-GPT/main?label=updated)
[![](https://img.shields.io/github/actions/workflow/status/yinan-c/RSS-GPT/cron-job.yml?label=cron-job)](https://github.com/yinan-c/RSS-GPT/actions/workflows/cron-job.yml)
![](https://img.shields.io/github/stars/yinan-c/RSS-GPT)


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
    - WORK_TOKEN: your GitHub personal access with `repo` and `workflow` scope, get it from [GitHub settings](https://github.com/settings/tokens/new)
    - OPENAI_API_KEY: your OpenAI API key, get it from [OpenAI website](https://platform.openai.com/account/api-keys)
- Enable GitHub Pages in repo settings, choose GitHub Actions as the source
- Configure your RSS feeds in config.ini

You can check out [here](https://yinan.me/rss-gpt-manual-en.html) for a more detailed configuration guide.

## ChangeLog and updates

- There is a [`dev` branch](https://github.com/yinan-c/RSS-GPT/tree/dev) for manual updates on the script, auto commits will no longer be pushed to this `dev` branch. The purpose of doing this is to separate the manual updates and auto commits, so that it is easier to check the updates and pull to your repo.
- Check out the [CHANGELOG.md](CHANGELOG.md).

## Example feeds being processed

These feeds on hosted in the [`doc/` subdirectory](https://github.com/yinan-c/RSS-GPT/tree/main/docs) in this repo as well as on my [GitHub Pages](https://yinan.me/RSS-GPT/). Feel free to subscribe in your favorite RSS reader.

I will consider hosting more feeds in the future. Email me or submit an issue if there is any question using the script or any suggestions.
- https://www.ifanr.com/feed -> https://yinan-c.github.io/RSS-GPT/ifanr.xml
- https://brett.trpstra.net/brettterpstra -> https://yinan-c.github.io/RSS-GPT/brett-terpstra.xml
- https://meta.appinn.net/tag/chrome.rss, https://meta.appinn.net/tag/ios.rss, https://meta.appinn.net/tag/macos.rss -> https://yinan-c.github.io/RSS-GPT/appinn.xml
- https://rsshub.app/sspai/index -> https://yinan-c.github.io/RSS-GPT/sspai.xml
