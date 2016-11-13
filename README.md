DBSCAN
=====================================
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/) 

为数据挖掘课程设计而实现的一个DBSCAN聚类算法。<br>
聚类完成后有图像表示。<br>
暂时只能聚类二维点。<br>
## 依赖
    matplotlib(画图需要)
    
## 安装依赖
    pip install matplotlib
    
## 用法
    1.notepad打开config.ini，填写内容：
        data_file=待聚类数据文件(csv格式)的相对路径
        Eps=对象半径Eps
        MinPts=给定邻域N-Eps(p)包含的点的最小数目
      保存后退出。
    2.运行main.py
    3.观察console输出的簇和噪声，和matplotlib生成的散点图，得出结果。

