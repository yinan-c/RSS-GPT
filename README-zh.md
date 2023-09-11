# RSS-GPT

[![](https://img.shields.io/github/actions/workflow/status/yinan-c/RSS-GPT/cron-job.yml?label=cron-job)](https://github.com/yinan-c/RSS-GPT/actions/workflows/cron_job.yml)
[![](https://img.shields.io/github/actions/workflow/status/yinan-c/RSS-GPT/jekyll-gh-pages.yml?label=GitHub%20pages)](https://github.com/yinan-c/RSS-GPT/actions/workflow/jekyll-gh-pages.yml)

[中文教程](https://yinan.me/RSS-GPT-manual-zh.html) | [中文介绍](https://yinan.me/rss-gpt.html)

## 功能

- 在GitHub仓库和GitHub Pages上托管自己的RSS订阅源。

- 使用ChatGPT来总结你的个性化RSS订阅源。 

- 聚合多个RSS订阅源到一个里面。

- 为RSS订阅源添加过滤器。

## 配置

- Fork这个仓库

- 添加仓库Secrets

    - U_NAME: 你的GitHub用户名

    - U_EMAIL: 你的GitHub邮箱

    - WORK_TOKEN: 你的GitHub个人访问令牌,需要有`repo`和`workflow`权限

    - OPENAI_API_KEY: 你的OpenAI API密钥,在[这里](https://platform.openai.com/account/api-keys)获取

- 在仓库设置中启用GitHub Actions访问Pages

- 在config.ini中配置你的RSS订阅源

- 把'main.py'中的链接改成你自己的GitHub Pages链接。

也可以参考更详细的[中文教程](https://yinan.me/RSS-GPT-manual-zh/)。
