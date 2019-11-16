#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/9/25 16:50 MongoEngine
# @Author : Ahrist 
# @Site :  
# @File : main.py 
# @Software: PyCharm

import os
import sys

from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", 'crawl', 'xmxxk'])