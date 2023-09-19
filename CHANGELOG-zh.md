# 更新日志

- 2023-09-19:
  - 我创建了一个新的分支，把所有自动提交的内容放在那个分支里。你可以在[这里](https://github.com/yinan-c/RSS-GPT/tree/auto-commit)查看。主分支从现在开始只包含手动提交的内容，这样可以更容易地查看脚本更新并 merge 到你的仓库中。
  - 更新了部署到 GitHub Pages 的目标路径，从 `./_site/rss/` 改为 `./_site/`。现在订阅源托管在 `your_path/RSS-GPT` 而不是 `rss/` 子目录下。更新了 README 中的 feeds 链接。

- 2023-09-15:
  - 如果你没有提供 OPENAI API，仍然可以使用这个脚本来聚合和过滤你的 RSS 订阅源，但是无法使用 AI 摘要功能。（你可以在仓库设置中删除或者随机设置一个字符串作为 OPENAI_API_KEY secret，或者在 config.ini 中设置 `max_items=0` 或者删除 max_items 参数, 默认为 0）
  - 当 OPENAI API 调用出现问题时，脚本仍然会运行并从 RSS 订阅源中获取新文章，只是无法提供 AI 摘要。
  - 当你发现你的订阅源没有摘要时，你可以检查 rss/ 目录中的日志，看看是否有来自 OPENAI 的错误信息，常见问题比如说账单问题等。