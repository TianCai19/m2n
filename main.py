import os
import clipboard
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

# It looks like the Python version of martian is not available.
# We will need to implement a basic markdown to notion block conversion.

def markdown_to_blocks(markdown_text):
    blocks = []
    for line in markdown_text.split('\n'):
        if line.startswith('# '):
            blocks.append({
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": line[2:]
                        }
                    }]
                }
            })
        elif line.startswith('## '):
            blocks.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": line[3:]
                        }
                    }]
                }
            })
        elif line.startswith('* ') or line.startswith('- '):
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": line[2:]
                        }
                    }]
                }
            })
        else:
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": line
                        }
                    }]
                }
            })
    return blocks


def main():
    notion_token = os.getenv("NOTION_API_KEY")
    page_id = os.getenv("NOTION_PAGE_ID")

    if not notion_token or not page_id:
        print("Error: NOTION_API_KEY and NOTION_PAGE_ID must be set in a .env file.")
        return

    notion = Client(auth=notion_token)
    markdown_content = clipboard.paste()

    if not markdown_content:
        print("No content found in clipboard.")
        return

    blocks = markdown_to_blocks(markdown_content)

    new_page = notion.pages.create(
        parent={"page_id": page_id},
        properties={
            "title": [
                {
                    "text": {
                        "content": "My Markdown Page (Python)"
                    }
                }
            ]
        },
        children=blocks
    )

    print(f"Successfully created page: {new_page['url']}")

if __name__ == "__main__":
    main()
