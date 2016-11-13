#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File       : cluster.py
# @Time       : 2016/11/13 15:07
# @Author     : Jim
# @GitHub     : https://github.com/SgtDaJim


class Cluster(object):
    '''
    簇的表现类
    '''

    point_list = [] #点列表
    name = "" # 簇名

    def __init__(self, name):
        self.point_list = []
        self.name = name

    def add_point(self, point):
        self.point_list.append(point)

    def has_point(self, point):
        if point in self.point_list:
            return True

    def get_points(self):
        return self.point_list

    def get_name(self):
        return self.name
