'''
author:
date: 2023/09/06
description: 装载分词模型
'''

from LAC import LAC

lac = LAC(mode='lac')
lac.load_customization('lac_custom.txt', sep=None)
