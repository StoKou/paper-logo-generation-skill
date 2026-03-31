# 论文 Logo Prompt 生成 Skill

让论文先拥有一句好提示词，再拥有一枚真正像作品的 Logo。

`paper-logo-generation` 是一个专门为论文项目设计的 Skill。它接收论文 PDF、arXiv 链接、Hugging Face 论文页，或本地论文文件夹，然后把抽象的研究内容压缩成一段可以直接交给 Nano Banana 2 的图像生成提示词。

它不会停留在“总结论文”这一步，而是进一步完成：

- 读取论文摘要与核心贡献
- 提炼 2 到 4 个可视化关键词
- 选择一个与论文气质匹配的动漫动物主角
- 组合成一段更像品牌提案而不是通用 AI 绘图描述的 Prompt

## 安装方式

告诉 Claude 从这个 GitHub 仓库安装 Skill：

`https://github.com/StoKou/paper-logo-generation-skill.git`

Skill 主体目录：

`paper-logo-generation/`

## 使用方式

你只需要给它下面任意一种输入：

- 一篇论文 PDF
- 一条 arXiv / Hugging Face 论文链接
- 一个包含论文 PDF 的本地文件夹

随后它会返回一份结构化结果，包含：

- 论文标题
- 关键词
- 动物主角
- 最终图片生成 Prompt

## 这个项目的风格

这不是一个生成“普通海报提示词”的工具。

它更像一个轻量的视觉概念设计器，核心目标是把论文里的方法感、领域感和项目气质，转成一个足够鲜明、足够好记、也足够适合传播的 Logo 方向。

换句话说，它关注的不只是“画什么”，更是：

- 为什么这个动物适合这篇论文
- 哪几个技术关键词值得被视觉化
- 怎么让生成结果看起来像项目 Logo，而不是一张泛泛的插画

## 仓库结构

- `README.md`：项目说明与安装指引
- `paper-logo-generation/SKILL.md`：Skill 主流程
- `paper-logo-generation/style.md`：Logo Prompt 风格规范
- `paper-logo-generation/references/prompt-template.md`：输出模板参考
- `paper-logo-generation/meta.md`：项目元信息与后续优化方向
- `app/`：项目介绍前端页面

## 前端展示

仓库附带一个简单的介绍页，直接打开 `app/index.html` 就可以预览项目说明、工作流、特性和示例视觉模块。
