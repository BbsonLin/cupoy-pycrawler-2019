# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json

from datetime import datetime
from pathlib import Path


class JSONPipline(object):
    def open_spider(self, spider):
        spider.log('Start: open_spider ...')
        self.start_crawl_datetime = datetime.now().strftime('%Y%m%dT%H%M%S')

        self.dir_path = Path(__file__).resolve().parents[1] / 'crawled_data'
        self.temp_file_path = fr'{self.dir_path}\.tmp.json.swp'
        if not self.dir_path.exists():
            self.dir_path.mkdir(parents=True)
        spider.log('Create temp file for store JSON - {}'.format(self.temp_file_path))

        self.temp_file = open(self.temp_file_path, 'w+', encoding='utf8')
        self.temp_file.write('[\n')
        self._first_item = True
        spider.log('End: open_spider ...')

    def process_item(self, item, spider):
        spider.log('Start: process_item ...')
        if not isinstance(item, dict):
            item = dict(item)

        if self._first_item:
            self._first_item = False
        else:
            self.temp_file.write(',\n')

        self.temp_file.write(json.dumps(item, ensure_ascii=False))
        spider.log('End: process_item ...')
        return item

    def close_spider(self, spider):
        spider.log('Start: close_spider ...')
        self.end_crawl_datetime = datetime.now().strftime('%Y%m%dT%H%M%S')

        # 儲存 JSON 格式
        self.temp_file.write('\n]')
        self.temp_file.close()

        # 將暫存檔改為以日期為檔名的格式
        self.store_file_path = self.dir_path / \
            fr'{self.start_crawl_datetime}-{self.end_crawl_datetime}.json'
        self.store_file_path = str(self.store_file_path)
        os.rename(self.temp_file_path, self.store_file_path)
        spider.log('Save result at {}'.format(self.store_file_path))
        spider.log('End: close_spider ...')
