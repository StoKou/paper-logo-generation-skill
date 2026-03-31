# 项目元信息

## 项目目标

构建一个可复用的 `paper-logo-generation` Skill，让用户输入论文后，直接获得一段适合 Nano Banana 2 的论文 Logo Prompt。

## 核心流程

1. 阅读论文摘要。
2. 阅读最能体现贡献的引言或总结段落。
3. 提取 2 到 4 个关键词。
4. 固定使用橘猫学术桌面参考画风。
5. 用论文关键词和贡献线索填充模板，输出最终图片生成 Prompt。
6. Skill 在处理论文时自动提取标题；如果有可靠标题，则将标题作为顶部文字；如果没有标题，则忽略顶部文字。

## 关键文件

- `SKILL.md`：Skill 定义与工作流
- `style.md`：Prompt 的风格规范
- `references/prompt-template.md`：输出格式参考

## 仓库地址

- GitHub：`https://github.com/StoKou/paper-logo-generation-skill.git`
- 默认分支：`main`

## 后续可优化方向

- 加强对非标准论文版式的摘要与贡献抽取能力。
- 增加更多固定画风模板，例如猫咪实验室版、猫咪黑板版、猫咪研究笔记版。
- 让关键词更稳定地映射到纸面草图、公式符号和流程图元素。
- 支持直接读取更多论文链接来源，而不仅限于 PDF。
- 增加示例集，用于持续校验 Prompt 质量。
