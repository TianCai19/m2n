# Markdown to Notion Importer

This project provides a Node.js script to convert Markdown content from your clipboard and import it as new pages into Notion.

## Features

- Convert Markdown from clipboard to Notion blocks using the `martian` library.
- Create new Notion pages with the converted content.
- Easy configuration using a `.env` file.
- Integration with Raycast for quick access.

## Prerequisites

Before you begin, ensure you have the following:

- **Node.js** (LTS version recommended) and **npm** (Node Package Manager) installed.
- A **Notion Integration Token** (API Key).
- The **ID of the Notion page** where you want to add new content (this will be the parent page).

### Getting Notion API Credentials

1.  **Create a Notion Integration**: Go to [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations) and create a new integration.
2.  **Get the API Key**: Once you create the integration, you'll get an "Internal Integration Token". This is your Notion API key.
3.  **Get the Page ID**: The page ID is the last part of the URL of the Notion page you want to add the content to. For example, if your page URL is `https://www.notion.so/My-Page-1234567890abcdef1234567890abcdef`, the page ID is `1234567890abcdef1234567890abcdef`.
4.  **Share the page with your integration**: You need to share the page with the integration you created. Click the "Share" button on the page, and invite your integration.

## Setup

1.  **Clone the Repository** (or create the project structure manually):

    ```bash
    git clone <repository-url>
    cd markdown-to-notion
    ```

2.  **Create a `.env` file**: In the root of the project directory, create a file named `.env` and add your Notion API key and Page ID:

    ```
    NOTION_API_KEY="your_notion_api_key_here"
    NOTION_PAGE_ID="your_notion_page_id_here"
    ```

    Replace `your_notion_api_key_here` and `your_notion_page_id_here` with your actual credentials.

## Usage

1.  **Install Dependencies**:

    ```bash
    npm install
    ```

2.  **Copy Markdown to Clipboard**: Copy the Markdown content you wish to import to your system clipboard.

3.  **Run the Script**:

    ```bash
    node index.js
    ```

    This will create a new Notion page under the specified parent page with the content from your clipboard.

## Raycast Integration (macOS)

You can integrate this script with Raycast for quick access.

1.  **Open Raycast Preferences**: Go to `Raycast > Preferences > Extensions`.
2.  **Create a New Script Command**: Click the `+` button and select `Create New Script Command`.
3.  **Configure the Script Command**:
    *   **Name**: e.g., `Import Markdown to Notion`
    *   **Command**: `/path/to/your/markdown-to-notion/markdown2notion.sh`
        *Replace `/path/to/your/markdown-to-notion/` with the actual path to your project directory.*
        *Remember to make the script executable: `chmod +x /path/to/your/markdown-to-notion/markdown2notion.sh`*
    *   **Hotkey**: Assign a convenient hotkey for quick access.
    *   **Argument**: Set to `None`.
    *   **Output**: Set to `No Output` or `Show in Toast`.

Now, you can trigger the script with your assigned hotkey or by searching for its name in Raycast.

## Contributing

Feel free to contribute to this project by opening issues or pull requests.

## License

This project is licensed under the MIT License.