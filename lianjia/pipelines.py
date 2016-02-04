# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import numpy as np

class lianjiaPipeline(object):
    def __init__(self):
        self.file = open('lianjia.csv', 'wb')
        self.file.write(
            'name_of_community' + ',' + 'layout_of_house' + ',' +
            'price_of_house' + ',' + 'area_of_house' + ',' +
            'floor_of_house' + ',' + 'time_of_construction' + '\n'
        )
 
    def process_item(self, item, spider):
    #该函数的作用有: 
        #1.将数据写入CSV文件 2.去除每个值的左右空格 
        #3.将每个值编码为utf8 4.以逗号当做分隔符
        if len(item['time_of_construction']) == 0:
            item['time_of_construction'].append('')
            item['time_of_construction'].append('')
        elif len(item['time_of_construction']) == 1:
            item['time_of_construction'].append('')
        else:
            pass

        self.file.write(
            #每个字段实际是一个列表, 如果只有一个值需要切片[0]取数
	    item['name_of_community'][0].strip().encode('utf-8') + ',' +
            item['layout_of_house'][0].strip().encode('utf-8') + ',' +
            item['price_of_house'][0].strip().encode('utf-8') + ',' +
            item['area_of_house'][0].strip().encode('utf-8') + ',' + 
            #但是也有像下面的, 列表中有两个值, 正好拆开来存储为两个字段
            item['time_of_construction'][0].strip().encode('utf-8') + ',' + 
            item['time_of_construction'][1].strip().encode('utf-8') + '\n' 
        )


        return item

    def spider_closed(self, spider):
        self.file.close()

"""
import json

class lianjiaPipeline(object):
    def __init__(self):
        self.file = open('lianjia.json', 'wb')
 
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii = False) 
        self.file.write(line.encode('utf-8') + "\n")
        return item

    def spider_closed(self, spider):
        self.file.close()
"""

