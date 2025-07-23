
import { Client } from '@notionhq/client';
import { markdownToBlocks } from '@tryfabric/martian';
import 'dotenv/config';

import clipboardy from 'clipboardy';

const notion = new Client({ auth: process.env.NOTION_API_KEY });
const pageId = process.env.NOTION_PAGE_ID;

const markdown = clipboardy.readSync();

  let pageTitle = '新 Markdown 页面';
  const lines = markdown.split('\n');
  for (const line of lines) {
    if (line.startsWith('# ')) {
      pageTitle = line.substring(2).trim();
      break;
    } else if (line.startsWith('## ')) {
      pageTitle = line.substring(3).trim();
      break;
    }
  }

(async () => {
  const blocks = markdownToBlocks(markdown);

  const response = await notion.pages.create({
    parent: {
      page_id: pageId,
    },
    properties: {
      title: [
        {
          text: {
            content: pageTitle,
          },
        },
      ],
    },
    children: blocks,
  });

  console.log(response);
})();
