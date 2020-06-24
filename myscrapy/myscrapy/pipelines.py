# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class MyscrapyPipeline:
        # 初始化
        def __init__(self):
            #创建名为Novel的csv文件
            self.f = open("Novel.csv", "w")
            self.writer = csv.writer(self.f)
            self.writer.writerow([ 'novelName', 'authorName', 'novelContent'])

        def process_item(self, item, spider):
            #写入csv
            novel_list = [item['novelName'], item['authorName'], item['novelContent']]

            self.writer.writerow(novel_list)
            return item

        def close_spider(self, spider):  # 关闭
            self.writer.close()
            self.f.close()
