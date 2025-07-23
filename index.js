
import { Client } from '@notionhq/client';
import { markdownToBlocks } from '@tryfabric/martian';
import 'dotenv/config';

import clipboardy from 'clipboardy';

const notion = new Client({ auth: process.env.NOTION_API_KEY });
const pageId = process.env.NOTION_PAGE_ID;

const markdown = clipboardy.readSync();

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
            content: 'My Markdown Page',
          },
        },
      ],
    },
    children: blocks,
  });

  console.log(response);
})();
