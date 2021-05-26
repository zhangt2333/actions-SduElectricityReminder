# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Copyright 2021 ZhangT. All Rights Reserved.
# Author: zhangt2333
# main.py 2021/5/25 0:25

import json
import re
import sys
import spider

if __name__ == '__main__':
    data = json.loads(re.sub('#(.*)\n', '\n', sys.argv[1]).replace("'", '"'))
    print(spider.query(data['account'], data['building'], data['room']))