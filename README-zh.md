# RSS-GPT

![](https://img.shields.io/github/last-commit/yinan-c/RSS-GPT/main?label=updated)
[![](https://img.shields.io/github/actions/workflow/status/yinan-c/RSS-GPT/cron-job.yml?label=cron-job)](https://github.com/yinan-c/RSS-GPT/actions/workflows/cron-job.yml)
![](https://img.shields.io/github/stars/yinan-c/RSS-GPT)

[中文教程](https://yinan.me/rss-gpt-manual-zh.html) | [中文介绍](https://yinan.me/rss-gpt.html) | [README](README.md)

## 功能

- 在 GitHub 仓库和 GitHub Pages 上自托管 RSS 订阅源。
- 使用 ChatGPT 来总结 RSS 订阅源。
- 聚合多个 RSS 订阅源。
- 为 RSS 订阅源添加基于标题，内容，URL 的关键词过滤器。

## 配置

- Fork 这个仓库中
- 添加仓库 Secrets
    - U_NAME: 你的 GitHub 用户名
    - U_EMAIL: 你的 GitHub 邮箱
    - WORK_TOKEN: 你的 GitHub 个人访问令牌, 需要有 `repo` 和 `workflow` 权限。在 [GitHub 设置](https://github.com/settings/tokens/new)获取
    - OPENAI_API_KEY: 你的 OpenAI API 密钥, 在 [OPENAI 网站](https://platform.openai.com/account/api-keys)获取

- 在仓库设置中启用 GitHub Pages, 选择 GitHub Actions 部署
- 在 `config.ini` 中配置你的RSS订阅源

也可以参考更详细的[中文教程](https://yinan.me/rss-gpt-manual-zh.html)。

## 脚本的更新

- 本项目有一个 [`dev` 分支](https://github.com/yinan-c/RSS-GPT/tree/dev)，用于记录手动更新的内容，GitHub Actions 自动提交将不再出现这个 `dev` 分支，这样做的目的是把对脚本的手动更新和 GitHub Workflow 自动提交的内容分开, 方便检查脚本更新和 pull 到你的仓库中。

- 查看 [CHANGELOG-zh.md](CHANGELOG-zh.md) 获取最新的更新日志。

## 分享几条本项目处理后的 RSS 订阅源

我自己用此脚本总结的一些 RSS订阅源托管在本项目的[`docs/`子目录](https://github.com/yinan-c/RSS-GPT/tree/main/docs)中以及我的 [GitHub Pages](https://yinan.me/RSS-GPT/)上找到。欢迎在你的 RSS 阅读器中订阅。

如果有任何问题或有关于 rss feeds 的建议，欢迎邮件联系我。

如果你觉得本项目有帮助，欢迎 star。