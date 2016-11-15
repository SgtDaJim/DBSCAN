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
        '''
        往簇中加入点
        :param point: 要加入的点
        :return: None
        '''
        self.point_list.append(point)

    def has_point(self, point):
        '''
        判断某点是否在簇中
        :param point: 需要判断的点
        :return: 判断结果
        '''
        if point in self.point_list:
            return True

    def get_points(self):
        '''
        返回簇中的点
        :return: 簇中的点
        '''
        return self.point_list

    def get_name(self):
        '''
        返回簇的名字
        :return: 簇的名字
        '''
        return self.name
