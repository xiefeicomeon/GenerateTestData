# import function lib
# import libraries
import numpy as np
import pandas as pd
import scipy as sy
import pathlib2 as plb2
import common as cn
# 存储测试数据文件名
feeder_file_name = "P5_fault_locator.xlsx"
# 存储测试数据表名
feeder_sheet_name = "feeder_fault_locator"
# 当前系统的目录的父目录
current_path = plb2.Path.cwd().parent
# 存储测试数据文件路径
feeder_file_path = plb2.Path(current_path, feeder_file_name)
# 故障类型
fault_type = ["A-N", "B-N", "C-N", "AB-N", "BC-N", "CA-N", "ABC-N", "AB", "BC", "CA", "ABC"]
# 故障前A相电压：幅值-相位,B、C相相位依次滞后120°
prefault_voltage_A = [20000, 30]
# 故障前A相电流： 幅值-相位，B、C相相位依次滞后120°
prefault_current_A = [100, 0]
# 单相接地故障下
# 故障相电压随短路距离的故障范围
fault_voltage_amplitude = [5000, 2000, 10000]
fault_voltage_phase = 60
# 非故障相电压
nofault_voltage1_amplitude = 25000
nofault_voltage1_phase = -90
# 另一非故障相电压
nofault_voltage2_amplitude = 25000
nofault_voltage2_phase = 150
# 故障相电流随短路距离的故障范围
fault_current_amplitude = [150, -10, 120]
fault_current_phase = 10
# 非故障相电流
nofault_current1_amplitude = 100
fault_current1_phase = -120
# 另一非故障相电流
nofault_current2_amplitude = 25000
nofault_current2_phase = 120


# generate test data

def generate_test_data(file_path, sheet_name):
    pass


# calculate theoretical impedance and distance and voltage drop
def calculate_theoretical_data(file_path, sheet_name):
    print()


# read data and analysis
def analyse_data(file_path, sheet_name):
    print()


# generate result of data analysis
def generate_result(file_path, sheet_name):
    print()


# state function
def run_state(state):
    if state == "generate":
        generate_test_data(feeder_file_path, feeder_sheet_name)
        calculate_theoretical_data(feeder_file_path, feeder_sheet_name)
    if state == "analyse":
        analyse_data(feeder_file_path, feeder_sheet_name)
        generate_result(feeder_file_path, feeder_sheet_name)
