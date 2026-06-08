# resume apply

`resume-apply` 是一个用于中国大陆求职场景的通用 AI agent 工作流。它不是 Codex 专属；Codex、Claude Code，以及其它能够读取 Markdown 指令的 AI 工具，都可以按这个仓库里的说明使用。

它会引导用户选择一个专门存放简历的文件夹，读取简历内容，收集岗位偏好，从招聘平台和公司官网招聘页中筛选匹配岗位，并在用户明确确认后辅助完成投递。

## 适用于哪些 AI 工具

- **Codex / OpenAI agents**：读取 `SKILL.md`，并可使用 `agents/openai.yaml` 中的界面元数据。
- **Claude Code**：先读 `CLAUDE.md`，再按 `SKILL.md` 执行。
- **其它 AI agent**：先读 `AGENTS.md`，再按 `SKILL.md`、`references/` 和 `scripts/` 使用。
- **不能执行命令的工具**：仍可按工作流完成岗位筛选和投递确认，只是需要用户手动提供简历内容、JD 文本或投递结果。

## 它能做什么

- 首次使用时引导用户设置简历文件夹，不绑定 Windows 或 macOS 的固定路径。
- 将脚本配置默认保存在更通用的 `~/.resume-apply/settings.json`，并兼容旧的 Codex 配置路径。
- 从用户选择的简历文件夹中读取简历。
- 支持严格匹配、平衡匹配、广泛探索三种岗位筛选模式。
- 根据简历证据和用户偏好评估 JD 匹配度。
- 在简历文件夹内生成候选岗位清单和投递记录。
- 在任何最终投递动作前暂停，等待用户确认。

## 安全边界

这个工作流不是隐藏式的全自动海投工具，而是一个需要用户确认的求职助手。

- 不保存招聘网站账号密码。
- 不绕过验证码、短信验证、扫码登录、反自动化检查或访问限制。
- 需要用户手动登录招聘平台或公司招聘系统。
- 最终提交前必须暂停并等待用户确认。
- 将简历和投递记录视为个人隐私数据处理。

## 目录结构

```text
resume-apply/
|-- AGENTS.md
|-- CLAUDE.md
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
|-- references/
|   |-- channel-workflows.md
|   `-- matching-rubric.md
`-- scripts/
    |-- application_log.py
    `-- manage_profile.py
```

## 典型使用方式

让你的 AI 工具读取本仓库，并要求它使用 `resume-apply` 工作流，根据你的简历筛选适合的中国大陆岗位，并在你确认后辅助投递。

第一次使用时，工作流会要求你创建并提供一个专门存放简历的文件夹。后续再次使用时，如果工具支持本地配置读取，会默认复用这个文件夹。
