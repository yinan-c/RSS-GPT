# RSS-GPT

[![](https://img.shields.io/github/actions/workflow/status/yinan-c/RSS-GPT/cron-job.yml?label=cron-job)](https://github.com/yinan-c/RSS-GPT/actions/workflows/cron-job.yml)
[![](https://img.shields.io/github/actions/workflow/status/yinan-c/RSS-GPT/jekyll-gh-pages.yml?label=GitHub%20Pages)](https://github.com/yinan-c/RSS-GPT/actions/workflows/jekyll-gh-pages.yml)


[Configuration Guide](https://yinan.me/rss-gpt-manual-en.html) | [中文介绍](README-zh.md) | [中文教程](https://yinan.me/rss-gpt-manual-zh.html) 

## Features

- Host your own RSS feeds on GitHub repo and GitHub Pages.
- Using ChatGPT to summarize your personalized RSS feeds. 
- Aggregate multiple RSS feeds into one.
- Add filters to your own personalized RSS feeds.

## ChangeLog

Check out the [CHANGELOG.md](CHANGELOG.md) for the latest changes.

## Configuration

- Fork this repo，uncheck the “only copy the main branch” option to fork both branches.
- Add Repository Secrets
    - U_NAME: your GitHub username
    - U_EMAIL: your GitHub email
    - WORK_TOKEN: your GitHub personal access with `repo` and `workflow` scope, get it from [GitHub settings](https://github.com/settings/tokens/new)
    - OPENAI_API_KEY: your OpenAI API key, get it from [OpenAI website](https://platform.openai.com/account/api-keys)
- Enable GitHub Pages in repo settings, choose the `auto-commit` branch `/docs` folder as source.
- Configure your RSS feeds in config.ini

You can check out [here](https://yinan.me/rss-gpt-manual-en.html) for a more detailed configuration guide.

## Example feeds being processed

These feeds on hosted in the rss/ directory of the [auto-commit branch](https://github.com/yinan-c/RSS-GPT/tree/auto-commit) of this repo in order to separate the manually committed content from the automatically committed content for easier checking and merging updates to your repo.
You can check out the [CHANGELOG.md](CHANGELOG.md) for more details about this update on 2023-09-19.

The feeds are also on my [GitHub Pages](https://yinan.me/RSS-GPT/). Feel free to subscribe in your favorite RSS reader.

I will consider hosting more feeds in the future. Email me or submit an issue if there is any question using the script or any suggestions.
