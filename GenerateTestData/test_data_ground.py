# import libraries
import numpy as np
import pandas as pd
import scipy as sy
import pathlib2 as plb2
import common as cn

# 故障类型
fault_type_ground = ["A-N", "B-N", "C-N", "AB-N", "BC-N", "CA-N", "ABC-N"]

# 故障前三相电压：幅值
prefault_voltage_amplitude = [20000, 20000, 20000]
# 相位
prefault_voltage_phase = [30, -90, 150]

# 故障前三相电流：幅值
prefault_current_amplitude = [100, 100, 100]
# 相位
prefault_current_phase = [0, -120, 120]

# 单相接地故障
# 故障相电压随短路距离的故障范围
# 故障相幅值范围
fault_voltage_amplitude_1 = [5000, 2000, 10000]
# 故障相相位
fault_voltage_phase_1 = [60]
# 非故障相电压
# 非故障相幅值
nofault_voltage_amplitude_1 = [25000, 25000]
# 非故障相相位
nofault_voltage_phase_1 = [-90, 150]

# 故障相电流随短路距离的故障范围
fault_current_amplitude_1 = [150, -10, 120]
fault_current_phase_1 = [10]
# 非故障相电流
nofault_current_amplitude_1 = [100, 100]
nofault_current_phase_1 = [-120, 120]

# 两相接地故障
# 故障相电压随短路距离的故障范围
# 幅值范围
fault_voltage_amplitude_2 = [5000, 2000, 10000]
# 两故障相的相位
fault_voltage_phase_2 = [60, -60]
# 非故障相电压
nofault_voltage_amplitude_2 = [25000]
nofault_voltage_phase_2 = [-90]

# 故障相电流随短路距离的故障范围
fault_current_amplitude_2 = [150, -10, 120]
fault_current_phase_2 = [10, -170]
# 非故障相电流
nofault_current_amplitude_2 = [100]
nofault_current_phase_2 = [-120]

# 三相接地故障
# 故障相电压随短路距离的故障范围
fault_voltage_amplitude_3 = [5000, 2000, 10000]
fault_voltage_phase_3 = [60, 60, 60]

# 故障相电流随短路距离的故障范围
fault_current_amplitude_3 = [150, -10, 120]
fault_current_phase_3 = [10, 10, 10]
# 零序电流
neutral_current_amplitude = 0
neutral_current_phase = 0

# 故障后三相电流：幅值
prefault_current_amplitude = [80, 80, 80]
# 相位
prefault_current_phase = [0, -120, 120]

# 数据最大长度
fault_number_g = len(fault_type_ground)
max_length_g = 10 *fault_number_g

# 当前数据索引
now_index = 0

# 故障前相电压相量数组
prefault_voltage_A = cn.generate_phasor_constant_data(prefault_voltage_amplitude[0], prefault_voltage_phase[0],
                                                      (2, max_length_g))
prefault_voltage_B = cn.generate_phasor_constant_data(prefault_voltage_amplitude[1], prefault_voltage_phase[1],
                                                      (2, max_length_g))
prefault_voltage_C = cn.generate_phasor_constant_data(prefault_voltage_amplitude[2], prefault_voltage_phase[2],
                                                      (2, max_length_g))

# 故障相电压相量数组
fault_voltage_A = np.full([2, max_length_g], np.nan)
fault_voltage_B = np.full([2, max_length_g], np.nan)
fault_voltage_C = np.full([2, max_length_g], np.nan)

# 故障相电流相量数组
fault_current_A = np.full([2, max_length_g], np.nan)
fault_current_B = np.full([2, max_length_g], np.nan)
fault_current_C = np.full([2, max_length_g], np.nan)


def generate_test_data_1n():
    """
产生单相接地故障数据，并写入数组
    """
    # 产生单相接地故障数据
    # 故障相电压
    fault_voltage_1 = cn.generate_phasor_data(fault_voltage_amplitude_1, fault_voltage_phase_1[0], 0)
    shape_1 = fault_voltage_1.shape
    # 非故障相电压（其中一相）
    nofault1_voltage_1 = cn.generate_phasor_constant_data(nofault_voltage_amplitude_1[0], nofault_voltage_phase_1[0],
                                                          shape_1)
    # 非故障相电压（另外一相）
    nofault2_voltage_1 = cn.generate_phasor_constant_data(nofault_voltage_amplitude_1[1], nofault_voltage_phase_1[1],
                                                          shape_1)
    # 故障相电流
    fault_current_1 = cn.generate_phasor_data(fault_current_amplitude_1, fault_current_phase_1[0], 0)
    shape_1 = fault_current_1.shape
    # 非故障相电流（其中一相）
    nofault1_current_1 = cn.generate_phasor_constant_data(nofault_current_amplitude_1[0], nofault_current_phase_1[0],
                                                          shape_1)
    # 非故障相电流（另外一相）
    nofault2_current_1 = cn.generate_phasor_constant_data(nofault_current_amplitude_1[1], nofault_current_phase_1[1],
                                                          shape_1)

