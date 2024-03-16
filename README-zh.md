# RSS-GPT

[![](https://img.shields.io/github/last-commit/yinan-c/RSS-GPT/dev?label=updated)](https://github.com/yinan-c/RSS-GPT/tree/dev)
[![](https://img.shields.io/github/last-commit/yinan-c/RSS-GPT/main?label=feeds%20refreshed)](https://yinan-c.github.io/RSS-GPT/)
[![](https://img.shields.io/github/license/yinan-c/RSS-GPT)](https://github.com/yinan-c/RSS-GPT/blob/master/LICENSE)


## 这是什么？

[中文介绍](https://yinan-c.github.io/rss-gpt.html) | [中文教程](https://yinan-c.github.io/rss-gpt-manual-zh.html) | [README](README.md)

使用 GitHub workflow 自动运行一个简单的 Python 脚本，调用 OpenAI API 为 RSS 订阅源生成摘要，然后将新生成的 RSS 订阅源推送到 GitHub Pages。配置简单快速，无需服务器。

### 功能及示例

- 使用 ChatGPT 来总结 RSS 订阅源, 生成关键词，摘要附在原文前面，支持自定义摘要长度，自定义语言。
- 聚合多个 RSS 订阅源，去除重复文章，用单一地址订阅。
- 为 RSS 订阅源添加基于标题，内容，URL 的关键词过滤器。
- 在 GitHub 仓库和 GitHub Pages 上自托管 RSS 订阅源。

![](https://i.imgur.com/7darABv.jpg)

## 快速部署

- Fork 这个仓库中
- 添加仓库 Secrets
    - U_NAME: 你的 GitHub 用户名
    - U_EMAIL: 你的 GitHub 邮箱
    - WORK_TOKEN: 你的 GitHub 个人访问令牌, 需要有 `repo` 和 `workflow` 权限。在 [GitHub 设置](https://github.com/settings/tokens/new)获取
    - OPENAI_API_KEY(可不填, 只有在使用 AI 摘要功能时需要): 你的 OpenAI API 密钥, 在 [OPENAI 网站](https://platform.openai.com/account/api-keys)获取
- 在仓库设置中启用 GitHub Pages， 选择 deploy from branch，设置目录为 `/docs`.
- 在 `config.ini` 中配置你的RSS订阅源

也可以参考更详细的[中文教程](https://yinan-c.github.io/rss-gpt-manual-zh.html)。

## 脚本的更新

- 本项目有一个 [`dev` 分支](https://github.com/yinan-c/RSS-GPT/tree/dev)，用于记录手动更新的内容，GitHub Actions 自动提交将不再出现这个 `dev` 分支，这样做的目的是把对脚本的手动更新和 GitHub Workflow 自动提交的内容分开, 方便检查脚本更新和 pull 到你的仓库中。

- 由于 OpenAI 在 2023-11-06 发布了新版本的 `openai` 包，[新版本包含了更强大的模型](https://openai.com/blog/new-models-and-developer-products-announced-at-devday)，调用 API 的方式也发生了变化。因此，旧版本的脚本将无法使用最新版本的 `openai` 包，需要更新。否则，你可以在 `requirements.txt` 中设置 `openai==0.27.8` 来使用旧版本。
- 在更新的版本中，**长度超过 16k 个 token 的文章不再被截断，而是使用最新的 `gpt-4-1106-preview` 模型。** 如果你不喜欢这样的改变，可以联系我，我会考虑添加自定义选项来选择是否截断或者使用 `gpt-4-1106-preview` 模型。

- 查看 [CHANGELOG-zh.md](CHANGELOG-zh.md) 获取最新的更新日志。

### 欢迎贡献!

- 欢迎提交 issue 和 pull request。请尽量提交 pull request 到 `dev` 分支。

## 分享几条本项目处理后的 RSS 订阅源

我自己用此脚本总结的一些 RSS订阅源托管在本项目的[`docs/`子目录](https://github.com/yinan-c/RSS-GPT/tree/main/docs)中以及我的 [GitHub Pages](https://yinan-c.github.io/RSS-GPT/)上找到。欢迎在任何 RSS 阅读器中订阅。

如果有任何问题或有关于 RSS feeds 的建议，欢迎邮件联系我。

如果你觉得本项目有帮助，欢迎 star。

- https://rss.panewslab.com/zh/gtimg/rss -> https://ICBMICBM.github.io/RSS-GPT/1.xml
- https://rss.app/feeds/wUQN1BEONEifvDV7.xml -> https://ICBMICBM.github.io/RSS-GPT/2.xml
- https://techcrunch.com/tag/bitcoin/feed -> https://ICBMICBM.github.io/RSS-GPT/3.xml
- https://blog.chainalysis.com/feed -> https://ICBMICBM.github.io/RSS-GPT/4.xml
- https://messari.io/rss -> https://ICBMICBM.github.io/RSS-GPT/5.xml
- https://techflowpost.mirror.xyz/feed/atom -> https://ICBMICBM.github.io/RSS-GPT/6.xml
- https://rss.app/feeds/HoQia6sxXDppjb98.xml -> https://ICBMICBM.github.io/RSS-GPT/7.xml
- https://www.newsbtc.com/feed -> https://ICBMICBM.github.io/RSS-GPT/8.xml
- https://news.crunchbase.com/sections/crypto/feed -> https://ICBMICBM.github.io/RSS-GPT/9.xml
- https://www.blocktempo.com/feed -> https://ICBMICBM.github.io/RSS-GPT/10.xml
- https://www.coindesk.com/arc/outboundfeeds/rss -> https://ICBMICBM.github.io/RSS-GPT/11.xml
- https://www.coindesk.com/arc/outboundfeeds/rss -> https://ICBMICBM.github.io/RSS-GPT/12.xml
- https://bitcoinist.com/feed -> https://ICBMICBM.github.io/RSS-GPT/13.xml
- https://www.trustnodes.com/feed -> https://ICBMICBM.github.io/RSS-GPT/14.xml
- https://cointelegraph.com/rss -> https://ICBMICBM.github.io/RSS-GPT/15.xml
- https://cointelegraph.com/rss -> https://ICBMICBM.github.io/RSS-GPT/16.xml
- https://www.chainfeeds.xyz/rss -> https://ICBMICBM.github.io/RSS-GPT/17.xml
- https://en.foresightnews.pro/feed -> https://ICBMICBM.github.io/RSS-GPT/18.xml
