# import libraries
import numpy as np
import pandas as pd
import scipy as sy
import pathlib2 as plb2
import common as cn

# 最大的测试数据长度

# 存储测试数据文件名
feeder_file_name = "P5_fault_locator.xlsx"
# 存储测试数据表名
feeder_sheet_name = "feeder_fault_locator"
# 当前系统的目录的父目录
current_path = plb2.Path.cwd().parent
# 存储测试数据文件路径
feeder_file_path = plb2.Path(current_path, feeder_file_name)


# generate test data

def generate_test_data():
    pass


# calculate theoretical impedance and distance and voltage drop
def calculate_theoretical_data():
    print()


# read data and analysis
def analyse_data():
    print()


# generate result of data analysis
def generate_result():
    print()


# state function
def run_state(state):
    if state == "generate":
        generate_test_data()
        calculate_theoretical_data()
    if state == "analyse":
        analyse_data()
        generate_result()
