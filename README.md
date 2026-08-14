小红书 AI 知识图文 Skill

一个面向 Codex 的小红书知识图文制作 Skill。它会先分析关键词、长文、文件、截图和图片等混合素材，判断真正值得发布的主题，再完成事实核验、内容脚本、3:4 视觉生成、成图质检与发布文案。

它不是把素材机械改写成图片，而是先做一次编辑选题。

## 能做什么

- 从关键词、文章、笔记片段、文件、截图或混合素材中提炼选题
- 为 AI 初学者解释 Agent、RAG、AIGC 等概念与知识片段
- 在写稿前检索并交叉验证事实，优先使用官方文档、论文和一手来源
- 规划不少于 4 页的图文结构，常规概念解释默认推荐 6 页
- 先生成封面并锁定风格，再逐页生成完整轮播图
- 输出 3:4 竖版图片、1 个推荐标题、2 个备选标题、200 字以内正文和关键词
- 检查画幅、分辨率、页码、文案准确性与整体一致性

## 默认视觉体系

- 画幅：3:4 竖版，目标尺寸 1080 × 1440 或更高等比例分辨率
- 风格：色彩丰富的弥散渐变 + C4D 毛绒材质
- 层级：封面主标题居中，主体词放大；解释文字位于顶部或底部
- 固定角标：`2026`、`GuangYing`、`AI`、`{{关键词}}`
- 中部区域：优先承载人物、物体、场景或视觉隐喻
- 文字特例：需要详细解释时，可使用无装饰的纯文字页，以标题、编号分段和一句总结呈现

视觉规范、生成提示词与质检要求分别位于 `references/` 目录。

## 工作流程

1. 读取并理解全部输入，不默认把所有素材塞进一篇笔记。
2. 推荐最适合初学者的主选题；必要时提供一到两个备选方向。
3. 联网检索并交叉验证事实；遇到歧义或多义词时先向用户确认。
4. 规划故事线、页面数量、逐页文案和视觉隐喻。
5. 先生成封面，经用户确认后锁定配色、字体材质和版式。
6. 分页生成图片，不生成拼图或联系表。
7. 逐张检查中文文字、角标、层级、画幅和风格一致性。
8. 输出可直接发布的标题、正文和关键词，并保存按发布顺序编号的成图。

## 安装

将仓库克隆到 Codex 的 Skills 目录：

```bash
git clone https://github.com/rongtaocheng32-ctrl/xiaohongshu-ai-carousel.git ~/.codex/skills/xiaohongshu-ai-carousel
```

重新打开 Codex 任务后，即可在可用 Skills 中看到该 Skill。

如果只想在某个项目中使用，可以克隆到项目的 `.agents/skills/` 目录：

```bash
git clone https://github.com/rongtaocheng32-ctrl/xiaohongshu-ai-carousel.git .agents/skills/xiaohongshu-ai-carousel
```

## 使用示例

显式调用：

```text
使用 $xiaohongshu-ai-carousel，分析我提供的材料，先推荐选题和页数，不要立刻出图。
```

关键词输入：

```text
使用 $xiaohongshu-ai-carousel，面向 AI 小白解释 RAG。先联网核验，再给我 6 页方案。
```

混合素材输入：

```text
使用 $xiaohongshu-ai-carousel，分析这篇文章和两张截图，告诉我最适合发什么，并给出完整图文方案。
```

纯文字解释页：

```text
沿用已经确认的整体风格，把最后一页改成无装饰、只有文字的详细解释页，生成后先让我审核。
```

## 输出内容

一次完整交付通常包括：

- 选题分析与推荐理由
- 页面数量和逐页脚本
- 按发布顺序编号的 3:4 图片
- 1 个推荐标题和 2 个备选标题
- 200 字以内的小红书正文
- 一组聚焦且不过度堆砌的关键词或话题标签

## 项目结构

```text
xiaohongshu-ai-carousel/
├── SKILL.md                         # Skill 核心工作流
├── agents/openai.yaml               # Codex 界面元数据
├── references/
│   ├── editorial-workflow.md        # 选题与内容策划
│   ├── prompt-templates.md          # 图片生成提示词模板
│   ├── quality-checklist.md         # 发布前质检清单
│   └── visual-system.md             # 统一视觉规范
├── scripts/validate_carousel.py     # 成图文件校验脚本
├── README.md                        # GitHub 项目说明
└── LICENSE                          # CC0 1.0 Universal
```

## 校验成图

```bash
python3 scripts/validate_carousel.py /path/to/output-folder
```

校验脚本会检查图片数量、文件命名、画幅比例和分辨率等基础要求。内容准确性、文字可读性和视觉一致性仍需结合质检清单逐张检查。

## 许可证

本项目采用 [CC0 1.0 Universal](LICENSE)。你可以自由复制、修改、商用和再分发，通常无须申请授权或保留署名。

CC0 仅适用于本仓库中权利人有权放弃的内容，不自动覆盖用户提供的素材、参考图片、字体、商标或其他第三方内容。生成和发布作品时，请自行确认相关权利与平台规则。

`SKILL.md` 是 Codex 执行该 Skill 时读取的核心文件；`README.md` 仅用于 GitHub 项目展示、安装与使用说明。
