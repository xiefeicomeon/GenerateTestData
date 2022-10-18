# import libraries
import numpy as np
import pandas as pd
import scipy as sy
import pathlib2 as plb2
import common as cn

incomer_file_name = "P5_fault_locator.xlsx"
incomer_sheet_name = "incomer_fault_locator"
# 当前系统的目录的父目录
current_path = plb2.Path.cwd().parent
incomer_file_path = plb2.Path(current_path, incomer_file_name)


# generate test data

def generate_test_data(file_path, sheet_name):
    print()


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
        generate_test_data(incomer_file_path, incomer_sheet_name)
        calculate_theoretical_data(incomer_file_path, incomer_sheet_name)
    if state == "analyse":
        analyse_data(incomer_file_path, incomer_sheet_name)
        generate_result(incomer_file_path, incomer_sheet_name)
