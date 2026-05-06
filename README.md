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

## skill使用指南

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

1. 根据模板创建事件主线、故事主线、人物、背景经历
2. 执行技能

```
用户：/novel-brainstormer 第18章 我希望xxx，结果是xxx，请给我几个情节发展方案

[
    继续提示进行微调
    --我想选择方案1
    --我想结合方案1和方案2
    --用方案2，但把场景从咖啡馆改成废弃工厂
    请给我一个更完整的情节方案
]
[最好把结果复制到某个文件中，然后自行进行微调]


用户：/novel-writer 参考情节方案[引用路径]，给我完成第x章，3000字左右

[确认无误后移动到 章节/]


用户：/novel-reviewer [章节数]
用户：/novel-fixer
用户：/novel-outline [章节数]

```
