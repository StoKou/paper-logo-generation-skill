# 项目元信息

## 项目目标

构建一个可复用的 `paper-logo-generation` Skill，让用户输入论文后，直接获得一段适合 Nano Banana 2 的论文 Logo Prompt。

## 核心流程

1. 阅读论文摘要。
2. 阅读最能体现贡献的引言或总结段落。
3. 提取 2 到 4 个关键词。
4. 为论文挑选一个动漫风动物主角。
5. 输出最终图片生成 Prompt。

## 关键文件

- `SKILL.md`：Skill 定义与工作流
- `style.md`：Prompt 的风格规范
- `references/prompt-template.md`：输出格式参考

## 仓库地址

- GitHub：`https://github.com/StoKou/paper-logo-generation-skill.git`
- 默认分支：`main`

## 后续可优化方向

- 加强对非标准论文版式的摘要与贡献抽取能力。
- 丰富不同研究领域到动物主角的映射表。
- 增加多种 Prompt 风格分支，例如极简 Logo、徽章感 Logo、宣传海报感 Logo。
- 支持直接读取更多论文链接来源，而不仅限于 PDF。
- 增加示例集，用于持续校验 Prompt 质量。
