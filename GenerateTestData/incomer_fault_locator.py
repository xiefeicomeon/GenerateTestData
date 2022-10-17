# import function lib
# import libraries
import numpy as np
import pandas as pd
import scipy as sy
import pathlib2 as plb2
import common as cn

# read data file
def read_file(filepath):
    print()


# generate test data

def generate_test_data(filepath):
    print()


# calculate theoretical impedance and distance and voltage drop
def calculate_theoretical_data(filepath):
    print()


# read data and analysis
def analyse_data(filepath):
    print()


# generate result of data analysis
def generate_result(filepath):
    print()


# state function
def run_state(state):
    if state == "generate":
        read_file(cn.incomer_file_path)
        generate_test_data(cn.incomer_file_path)
        calculate_theoretical_data(cn.incomer_file_path)
    if state == "analyse":
        analyse_data(cn.incomer_file_path)
        generate_result(cn.incomer_file_path)
