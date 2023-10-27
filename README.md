# RSS-GPT

[![](https://img.shields.io/github/last-commit/yinan-c/RSS-GPT/dev?label=updated)](https://github.com/yinan-c/RSS-GPT/tree/dev)
[![](https://img.shields.io/github/last-commit/yinan-c/RSS-GPT/main?label=feeds%20refreshed)](https://yinan-c.github.io/RSS-GPT/)
[![](https://img.shields.io/github/license/yinan-c/RSS-GPT)](https://github.com/yinan-c/RSS-GPT/blob/master/LICENSE)


## What is this?

[Configuration Guide](https://yinan-c.github.io/rss-gpt-manual-en.html) | [中文简介](README-zh.md) | [中文教程](https://yinan-c.github.io/rss-gpt-manual-zh.html)

Using GitHub Actions to run a simple Python script repeatedly: Calling OpenAI API to generate summaries for RSS feeds, and push the generated feeds to GitHub Pages. Easy to configure, no server needed.

### Features

- Use ChatGPT to summarize RSS feeds, and attach summaries to the original articles, support custom summary length and target language.
- Aggregate multiple RSS feeds into one, remove duplicate articles, subscribe with a single address.
- Add filters to your own personalized RSS feeds.
- Host your own RSS feeds on GitHub repo and GitHub Pages.

![](https://i.imgur.com/7darABv.jpg)

## Quick configuration guide

- Fork this repo
- Add Repository Secrets
    - U_NAME: your GitHub username
    - U_EMAIL: your GitHub email
    - WORK_TOKEN: your GitHub personal accesstoken with `repo` and `workflow` scope, get it from [GitHub settings](https://github.com/settings/tokens/new)
    - OPENAI_API_KEY(OPTIONAL, only needed when using AI summarization feature): Get it from [OpenAI website](https://platform.openai.com/account/api-keys)
- Enable GitHub Pages in repo settings, choose deploy from branch, and set the directory to `/docs`.
- Configure your RSS feeds in config.ini

You can check out [here](https://yinan-c.github.io/rss-gpt-manual-en.html) for a more detailed configuration guide.

## ChangeLog and updates

- There is a [`dev` branch](https://github.com/yinan-c/RSS-GPT/tree/dev) for manual updates on the script, auto commits will no longer be pushed to this `dev` branch. The purpose of doing this is to separate the manual updates and auto commits, so that it is easier to check the updates and pull to your repo.
- Check out the [CHANGELOG.md](CHANGELOG.md).

### Contributions are welcome!

- Feel free to submit issues and pull requests. Please submit pull requests to the `dev` branch.

## Example feeds being processed

These feeds on hosted in the [`docs/` subdirectory](https://github.com/yinan-c/RSS-GPT/tree/main/docs) in this repo as well as on my [GitHub Pages](https://yinan-c.github.io/RSS-GPT/). Feel free to subscribe in your favorite RSS reader.

I will consider hosting more feeds in the future. Email me or submit an issue if there is any question using the script or any suggestions.
- https://brett.trpstra.net/brettterpstra -> https://yinan-c.github.io/RSS-GPT/brett-terpstra.xml
- https://meta.appinn.net/tag/chrome.rss, https://meta.appinn.net/tag/ios.rss, https://meta.appinn.net/tag/macos.rss -> https://yinan-c.github.io/RSS-GPT/appinn.xml
- https://rsshub.app/sspai/index -> https://yinan-c.github.io/RSS-GPT/sspai.xml
- https://rknight.me/feed.xml -> https://yinan-c.github.io/RSS-GPT/robb-knight.xml
- https://stephanango.com/feed.xml -> https://yinan-c.github.io/RSS-GPT/steph-ango.xml
- https://lopespm.com/atom.xml -> https://yinan-c.github.io/RSS-GPT/byte-tank.xml
- https://rsshub.app/36kr/motif/327685554177, https://rsshub.app/36kr/motif/327686782977, https://rsshub.app/36kr/motif/327687077889, https://rsshub.app/36kr/motif/1366661828936836, https://rsshub.app/36kr/motif/1366662419875203, https://rsshub.app/36kr/motif/1756302767423108, https://rsshub.app/36kr/motif/327686815745, https://rsshub.app/36kr/motif/327685734401 -> https://yinan-c.github.io/RSS-GPT/36kr.xml
