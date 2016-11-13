#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File       : dbscan.py
# @Time       : 2016/11/13 15:19
# @Author     : Jim
# @GitHub     : https://github.com/SgtDaJim


import cluster


class DBSCAN(object):

    data_set = []       # 数据集
    clusters = []       # 簇
    Eps = 0             # 对象半径Eps
    MinPts = 0          # 给定邻域N-Eps(p)包含的点的最小数目

    visited_points = [] # 已访问点
    num = 0             # 簇的序号

    def __init__(self, data_set, Eps, MinPts):
        self.data_set = data_set
        self.Eps = Eps
        self.MinPts = MinPts

    def run(self):

        noise = cluster.Cluster("Noise") # 这里将所有噪声点也当作一个簇来对待。创建噪声点簇。
        for point in self.data_set:
            if point not in self.visited_points: # 判断点是否已经被处理过
                self.visited_points.append(point)
                neighbors = self.find_neighbors(point) # 检查邻域

                if len(neighbors) < self.MinPts: # 若邻域中包含的对象数少于Minpts则标记为噪声
                    noise.add_point(point)

                else:
                    new_cluster = cluster.Cluster("Cluster " + str(self.num)) # 创建新的簇
                    self.num += 1 # 簇的序号加一
                    new_cluster.add_point(point) # 将点放入新簇中
                    self.form_cluster(neighbors, new_cluster) # 将符合条件的点加入新簇

        self.clusters.append(noise) # 噪声簇也加入簇列表中

        return self.clusters

    def find_neighbors(self, point):

        neighbors = [] # 邻域点列表

        for p in self.data_set:
            temp = ((point[0] - p[0])**2 + (point[1] - p[1])**2)**0.5 # 计算距离(使用两点间的直线距离公式)
            if temp <= self.Eps: # 若距离小于Eps，则为邻域中的点
                neighbors.append(p)

        return neighbors

    def form_cluster(self, neighbors, new_cluster):

        for n in neighbors: # 检查邻域中的点
            if n not in self.visited_points: # 检查该点是否已经被标记过
                self.visited_points.append(n)
                n_neighbors = self.find_neighbors(n) # 找出该点邻域
                if len(n_neighbors) >= self.MinPts:
                    for nn in n_neighbors:
                        neighbors.append(nn)

            #将未归入任何一个簇的对象加入簇中
            if len(self.clusters) == 0:
                if not new_cluster.has_point(n):
                    new_cluster.add_point(n)

            else:
                cflag = False
                for c in self.clusters:
                    if c.has_point(n):
                        cflag = True
                if cflag is False:
                    if not new_cluster.has_point(n):
                        new_cluster.add_point(n)

        self.clusters.append(new_cluster) # 在簇列表中加入新簇


