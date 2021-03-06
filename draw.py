#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File       : draw.py
# @Time       : 2016/11/13 18:25
# @Author     : Jim
# @GitHub     : https://github.com/SgtDaJim

from matplotlib import pyplot as plt
import random

class Draw(object):
    '''
    画图类
    '''

    cluster = []

    def __init__(self, cluster):
        self.cluster = cluster

    def run(self):
        '''
        执行画图的方法
        :return: None
        '''

        plt.subplot(111) # 设置子图
        plt.title("DBSCAN Result")
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        name = [] # 簇名列表
        for c in self.cluster:
            name.append(c.get_name())
            points = c.get_points()
            #print(name)
            x = []
            y = []

            for p in points:
                x.append(p[0])
                y.append(p[1])

            colors = ['r', 'g', 'b', 'y', 'c', 'k', 'm', 'w']
            #print(colors)
            plt.scatter(x, y, c=random.sample(colors, 1), alpha=1, s=50) # 作散点图

        plt.legend(name, loc="lower left") # 作图例
        plt.show() # 显示图形
