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

        plt.subplot(111)
        plt.title("DBSCAN Algorithm")
        name = []
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
            plt.scatter(x, y, c=random.sample(colors, 1), alpha=1, s=50)

        plt.legend(name, loc="lower left")
        plt.show()
