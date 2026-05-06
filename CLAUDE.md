---
project: 小说写作助手
version: 2.0
---

# 小说写作项目指导

## 项目结构

```
novel-project/
  ├── CLAUDE.md              # 本配置指南
  ├── .claude/               # Claude Code 配置（ skills/ memory/ settings.json）
  ├── standards/             # 参考上下文
  ├── 章节/                  # 已完成
  ├── 草稿/                  # 草稿
```

## 可用命令

| 命令                  | 用途                       |
| --------------------- | -------------------------- |
| `/novel-brainstormer` | 设计剧情、场景、角色发展   |
| `/novel-writer`       | 撰写/扩写小说章节          |
| `/novel-reviewer`     | 审阅章节质量               |
| `/novel-fixer`        | 根据上下文修改，不修改原文 |
| `/novel-outline`      | 生成大纲                   |
