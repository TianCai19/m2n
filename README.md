[English](README_en.md)

# Markdown 到 Notion 导入器

本项目提供了一个 Node.js 脚本，用于将剪贴板中的 Markdown 内容转换为 Notion 页面并导入。

## 功能

- 使用 `martian` 库将剪贴板中的 Markdown 转换为 Notion 块。
- 创建包含转换后内容的新 Notion 页面。
- 使用 `.env` 文件进行简便配置。
- 集成 Raycast 以实现快速访问。

## 前提条件

在开始之前，请确保您具备以下条件：

- 已安装 **Node.js**（推荐 LTS 版本）和 **npm**（Node 包管理器）。
- 一个 **Notion 集成令牌**（API 密钥）。
- 您希望添加新内容的 Notion 页面的 **ID**（这将是父页面）。

### 获取 Notion API 凭据

1.  **创建 Notion 集成**：访问 [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations) 并创建一个新的集成。
2.  **获取 API 密钥**：创建集成后，您将获得一个“内部集成令牌”。这就是您的 Notion API 密钥。
3.  **获取页面 ID**：页面 ID 是您希望添加内容的 Notion 页面 URL 的最后一部分。例如，如果您的页面 URL 是 `https://www.notion.so/My-Page-1234567890abcdef1234567890abcdef`，则页面 ID 是 `1234567890abcdef1234567890abcdef`。
4.  **与您的集成共享页面**：您需要将页面与您创建的集成共享。点击页面上的“共享”按钮，然后邀请您的集成。

## 设置

1.  **克隆仓库**（或手动创建项目结构）：

    ```bash
    git clone <repository-url>
    cd markdown-to-notion
    ```

2.  **创建 `.env` 文件**：在项目根目录下，创建一个名为 `.env` 的文件，并添加您的 Notion API 密钥和页面 ID：

    ```
    NOTION_API_KEY="your_notion_api_key_here"
    NOTION_PAGE_ID="your_notion_page_id_here"
    ```

    将 `your_notion_api_key_here` 和 `your_notion_page_id_here` 替换为您的实际凭据。

## 使用方法

1.  **安装依赖**：

    ```bash
    npm install
    ```

2.  **复制 Markdown 到剪贴板**：将您希望导入的 Markdown 内容复制到系统剪贴板。

3.  **运行脚本**：

    ```bash
    node index.js
    ```

    这将在指定的父页面下创建一个新的 Notion 页面，其中包含您剪贴板中的内容。

## Raycast 集成 (macOS)

您可以将此脚本与 Raycast 集成，以便快速访问。

1.  **打开 Raycast 偏好设置**：前往 `Raycast > Preferences > Extensions`。
2.  **创建新的脚本命令**：点击 `+` 按钮并选择 `Create New Script Command`。
3.  **配置脚本命令**：
    *   **名称**：例如，`Import Markdown to Notion`
    *   **命令**：`/path/to/your/markdown-to-notion/markdown2notion.sh`
        *将 `/path/to/your/markdown-to-notion/` 替换为您的项目目录的实际路径。*
        *请记住使脚本可执行：`chmod +x /path/to/your/markdown-to-notion/markdown2notion.sh`*
    *   **快捷键**：分配一个方便的快捷键以便快速访问。
    *   **参数**：设置为 `None`。
    *   **输出**：设置为 `No Output` 或 `Show in Toast`。

现在，您可以通过分配的快捷键或在 Raycast 中搜索其名称来触发脚本。

## 贡献

欢迎通过提出问题或提交拉取请求来为本项目做出贡献。

## 许可证

本项目采用 MIT 许可证。
