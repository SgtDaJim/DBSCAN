#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File       : save_result.py
# @Time       : 2016/11/15 23:14
# @Author     : Jim
# @GitHub     : https://github.com/SgtDaJim

class SaveResult(object):

    @staticmethod
    def save(file_name, clusters):
        cut = file_name[:file_name.find(".csv")]
        result_name = cut + "_solved.txt"

        with open(result_name, "w+") as f:
            for c in clusters:
                f.write(c.get_name() + "\n")
                for p in c.get_points():
                    f.write(str(p) + "\n")

        print("结果保存到" + result_name +"。")