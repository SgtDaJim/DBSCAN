#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File       : main.py
# @Time       : 2016/11/13 17:30
# @Author     : Jim
# @GitHub     : https://github.com/SgtDaJim

import dbscan
import draw
import csv
import configparser
import save_result

def main():

    config = "config.ini" # 配置文件

    data = [] # 原始数据
    Eps = 0 # 对象半径Eps
    MinPts = 0 # 给定邻域N-Eps(p)包含的点的最小数目
    clusters = None # DBSCAN后得到的簇

    # 从配置文件中读取有关配置
    dbscan_config = configparser.ConfigParser()
    dbscan_config.read(config)

    Eps = dbscan_config.get("DBSCANConfig", "Eps")
    MinPts = dbscan_config.get("DBSCANConfig", "MinPts")
    data_csv = dbscan_config.get("DBSCANConfig", "data_file")

    # 读入等待分析的数据
    with open(data_csv) as data_file:
        reader = csv.reader(data_file)
        for r in reader:
            data.append([float(r[0]),float(r[1])])

    # 创建自定义的DBSCAN对象，开始进行DBSCAN算法
    dbscan_runner = dbscan.DBSCAN(data, float(Eps), int(MinPts))
    clusters = dbscan_runner.run() # DBSCAN算法聚类后数据

    # console中输出数据
    for c in clusters:
        print("name : " + c.get_name())
        list = c.get_points()
        for p in list:
            print(p)

    # 画图，直观表现聚类后数据
    draw_runner = draw.Draw(clusters)
    draw_runner.run()

    # 将结果保存到文件
    save_result.SaveResult.save(data_csv, clusters)

if __name__ == "__main__":
    main()