## 目录结构建议

```
├─.claude
│  ├─hooks
│  ├─memory
│  │  └─writing-style.md 【写作风格】
│  └─skills
│      ├─novel-brainstormer
│      ├─novel-fixer
│      ├─novel-outline
│      ├─novel-reviewer
│      └─novel-writer
├─resources 【模板与资源】
├─standards
│  ├─事件主线.md   【使用 事件主线_模板 创建事件主线】
│  ├─故事主线.md    【使用 故事主线_模板 创建故事主线】
│  ├─story-outline-short.md 【生成的大纲-简短版】
│  ├─story-outline.md        【生成的】
│  ├─人物
│  │   ├─A.md   【使用 人物_模板 创建主角主角。配角一句话即可】
│  │   └─B.md
│  └─背景经历
│      ├─A.md   【使用 背景经历_模板 创建主角背景】
│      └─B.md
├─章节 【正文】
└─草稿 【暂时存放】
```

## 使用指南

```
/novel-brainstormer 帮我设计第一章的开场
/novel-brainstormer 帮我设计主角发现真相的场景

/novel-writer 按以下场景写第3章：雨夜，主角在家中接到神秘电话，对方声称知道他父亲的死因...
/novel-writer 只读取故事主线和人物档案，写第3章...
/novel-writer 写第5章，要求：
- 场景：深夜医院，走廊尽头的ICU
- 人物：主角A（焦虑但克制）、医生B（冷漠专业）
- 事件：主角接到病危通知
- 情感基调：压抑的绝望
- 字数：3000字左右
- 注意：不要直接写哭，用动作和环境暗示

/novel-reviewer 3
/novel-fixer
/novel-outline 3

```

## 示例：从0到1写第一章

```
用户：/novel-brainstormer 帮我设计悬疑小说的第一章开场，主角是个调查记者，要体现他的职业特点和性格

[助手提供3-5个方案]

用户：用方案2，但把场景从咖啡馆改成废弃工厂

用户：/novel-writer 按修改后的方案2写第1章，3000字左右

[确认无误后移动到 章节/]


用户：/novel-reviewer 审阅第1章
用户：/novel-fixer
用户：/novel-outline 1


```
