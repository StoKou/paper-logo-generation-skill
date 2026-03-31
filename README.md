# 论文 Logo Prompt 生成 Skill

让论文先拥有一句好 Prompt，再拥有一枚真正像项目作品的 Logo。

[![主页](https://img.shields.io/badge/项目主页-在线查看-ff7f50?style=for-the-badge)](https://stokou.github.io/paper-logo-generation-skill/)
[![Skill 目录](https://img.shields.io/badge/Skill-paper--logo--generation-1f1636?style=for-the-badge)](./paper-logo-generation/)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-/docs%20发布路径-ffc857?style=for-the-badge)](./docs/)

## 一句话介绍

`paper-logo-generation` 是一个专门面向论文项目传播的 Skill。

它读取论文 PDF、论文链接或本地论文文件夹，从摘要与核心贡献中提炼关键词，并把这些关键词填入固定的橘猫手绘参考模板，最后输出一段可直接用于 Nano Banana 2 的 Logo Prompt。

## 快速入口

[在线主页](https://stokou.github.io/paper-logo-generation-skill/)

[查看 Skill](./paper-logo-generation/SKILL.md)

[查看风格规范](./paper-logo-generation/style.md)

[查看 Prompt 模板](./paper-logo-generation/references/prompt-template.md)

## 它能做什么

它不会只停留在“总结论文”。

它会继续往前走一步，把论文里抽象的方法感、领域感和项目气质，压缩成一段更适合生成视觉 Logo 的 Prompt：

- 读取论文摘要与核心贡献
- 提炼 2 到 4 个可视化关键词
- 固定使用橘猫学术桌面画风
- 生成更像品牌概念提案的图片 Prompt

## 为什么这个项目更像作品，而不是模板

很多工具只会把论文转成一段通用的绘图描述。

这个项目更关心的是“识别度”与“传播感”：

- 哪些技术关键词值得被视觉化
- 如何把关键词变成纸面上的流程图、算法草图与符号结构
- 如何让图像结果更像项目 Logo，而不是一张普通插画

## 使用方式

你只需要提供下面任意一种输入：

- 一篇论文 PDF
- 一条 arXiv / Hugging Face 论文链接
- 一个包含论文 PDF 的本地文件夹

随后 Skill 会返回结构化结果，通常包括：

- `Title`
- `Keywords`
- `Mascot`
- `Prompt`

## 安装方式

告诉 Claude 从这个仓库安装 Skill：

`https://github.com/StoKou/paper-logo-generation-skill.git`

Skill 主体目录位于：

`paper-logo-generation/`

## 项目结构

- `README.md`：项目首页说明
- `paper-logo-generation/SKILL.md`：Skill 主流程
- `paper-logo-generation/style.md`：Logo Prompt 风格规范
- `paper-logo-generation/references/prompt-template.md`：输出模板参考
- `paper-logo-generation/meta.md`：项目元信息与后续优化方向
- `docs/`：GitHub Pages 站点目录

## 在线展示

项目主页：

`https://stokou.github.io/paper-logo-generation-skill/`

如果你想直接预览静态页面，可以从这里进入：

[打开项目主页](https://stokou.github.io/paper-logo-generation-skill/)

## GitHub Pages

这个仓库已经按 GitHub Pages 的发布方式整理完成：

- 分支：`main`
- 目录：`/docs`

站点入口文件：

- `docs/index.html`
- `docs/styles.css`
- `docs/.nojekyll`
