# import libraries
import numpy as np
import cmath

# some variables
function_name = "feeder"
function_array = ["feeder", "incomer", "exit"]
# state of function: generate or analyse
state = ""


def generate_phasor_data(amplitude, phase, mode):
    """
    生成测试数据，幅值和相位, np数组第一行为幅值，第二行为相位
    :param amplitude: 如果mode=0或者2，相量幅值范围，类型为数组，[初始值，最终值,步长]，如果mode=1,为常数
    :param phase:如果mode=1或者2，相量相位范围，类型为数组，[初始值，最终值,步长]，如果mode=0,为常数
    :param mode:0-仅对幅值进行插值，1-仅对相位进行插值，2-对赋值与相位进行同步插值
    :return: phasor_ploar-相量,第一行代表幅值，第二行代表相位
    """
    phasor_ploar = np.full((1, 1), np.nan)
    if mode == 0:
        if len(amplitude) == 3:
            phasor_amplitude = np.arange(amplitude[0], amplitude[1], amplitude[2])
            phasor_phase = np.full((1, phasor_amplitude.size), phase)
            phasor_ploar = np.zeros((2, phasor_amplitude.size), dtype=float)
            phasor_ploar[[0], :] = phasor_amplitude
            phasor_ploar[[1], :] = phasor_phase

        else:
            print("parameters is illegal")

    if mode == 1:
        if len(phase) == 3:
            phasor_phase = np.arange(phase[0], phase[1], phase[2])
            phasor_amplitude = np.full((1, phasor_phase.size), amplitude)
            phasor_ploar = np.zeros((2, phasor_phase.size), dtype=float)
            phasor_ploar[[0], :] = phasor_amplitude
            phasor_ploar[[1], :] = phasor_phase
        else:
            print("parameters is illegal")

    if mode == 2:
        if (len(amplitude) == 3) and (len(phase) == 3):
            phasor_amplitude = np.arange(amplitude[0], amplitude[1], amplitude[2])
            phasor_phase = np.arange(phase[0], phase[1], phase[2])
            number = min(phasor_amplitude.size, phasor_phase.size)
            phasor_ploar = np.zeros((2, number), dtype=float)
            phasor_ploar[[0], :] = phasor_amplitude[0:number:1]
            phasor_ploar[[1], :] = phasor_phase[0:number:1]
        else:
            print("parameters is illegal")

    return phasor_ploar


def convert_ri_to_ap(phasor_ri):
    """
    将直角坐标系相量转换为极坐标系
    :param phasor_ri: 输入np相量数组，第一行为实部即电阻，第二行为虚部即电抗
    :return: phasor_ploar-相量,第一行代表幅值，第二行代表相位
    """
    phasor_ploar = np.full((1, 1), np.nan)
    # 幅值与相位数组
    amplitude = []
    phase = []
    if phasor_ri.any != np.nan:
        # 遍历phasor_ri的实部与虚部
        for i in range(0, phasor_ri[0].size):
            z_ploar = cmath.polar(complex(phasor_ri[0, i], phasor_ri[1, i]))
            amplitude.append(z_ploar[0])
            phase.append(z_ploar[1] * 180/cmath.pi)
        # print(amplitude)
        # print(phase)
        phasor_ploar = np.array([amplitude, phase], dtype=float)
    return phasor_ploar


def convert_ap_to_ri(phasor_ploar):
    """
    将极坐标系相量转换为直角坐标系
    :param phasor_ploar: 第一行代表幅值，第二行代表相位
    :return:phasor_ri 第一行为实部即电阻，第二行为虚部即电抗
    """
    phasor_ri = np.full((1, 1), np.nan)
    # 实部与虚部数组
    real = []
    imag = []
    if phasor_ploar.any != np.nan:
        # 将相位转换为弧度
        phasor_ploar[1] = (phasor_ploar[1] / 180)*cmath.pi
        # 遍历phasor_ploar的幅值与相位
        for i in range(0, phasor_ploar[0].size):
            rect = cmath.rect(phasor_ploar[0, i], phasor_ploar[1, i])
            real.append(rect.real)
            imag.append(rect.imag)
        # print(real)
        # print(imag)
        phasor_ri = np.array([real, imag], dtype=float)
        phasor_ploar[1] = (phasor_ploar[1] / cmath.pi)*180
    return phasor_ri


def convert_phasor_to_string(phasor_ploar):
    """
    将数字转换为便于阅读的文本
    :param phasor_ploar: 第一行代表幅值，第二行代表相位
    :return: phasor_ploar_str-文本形式例如幅值220，相位30 则转换为220<30
    """
    phasor_ploar_str = np.full((1, 1), np.nan)
    phasor_str_temp = []

    if phasor_ploar.any != np.nan:
        # 遍历phasor_ploar的幅值与相位
        for i in range(0, phasor_ploar[0].size):
            amplitude = round(phasor_ploar[0, i], 2)
            phase = round(phasor_ploar[1, i], 2)
            str_temp = str(amplitude) + "<" + str(phase)
            phasor_str_temp.append(str_temp)
    phasor_ploar_str = np.array([phasor_str_temp])
    return phasor_ploar_str


def convert_string_to_phasor(phasor_ploar_str):
    """
    将文本转换为数字
    :param phasor_ploar_str: 文本形式220<30
    :return: phasor_ploar-第一行代表幅值，第二行代表相位
    """
    phasor_ploar = np.nan
    amplitude = []
    phase = []
    if phasor_ploar_str.any != np.nan:
        for i in range(0, phasor_ploar_str.size):
            phasor = phasor_ploar_str[0, i].split("<")
            if len(phasor) == 2:
                amplitude.append(float(phasor[0]))
                phase.append(float(phasor[1]))
    if len(amplitude) != 0:
        phasor_ploar = np.array([amplitude, phase], dtype=float)
    return phasor_ploar


def add_phasor(phasor_a, phasor_b, phasor_mode):
    """
    相量相加
    :param phasor_a:相量一
    :param phasor_b:相量二
    :param phasor_mode:[0,0],[0,1],[1,0],[1,1] 0-直角坐标系相量， 1-极坐标系相量,
    :return: phasor_a+phasor_b
    """
    phasor_ret = np.full((1, 1), np.nan)
    phasor_ta = phasor_a
    phasor_tb = phasor_b
    if phasor_a.shape == phasor_b.shape:
        if phasor_mode[0] == 1:
            phasor_ta = convert_ap_to_ri(phasor_a)
        if phasor_mode[1] == 1:
            phasor_tb = convert_ap_to_ri(phasor_b)
        phasor_ret = phasor_ta + phasor_tb

    return phasor_ret


def sub_phasor(phasor_a, phasor_b, phasor_mode):
    """
    相量相减
    :param phasor_a:相量一
    :param phasor_b:相量二
    :param phasor_mode:[0,0],[0,1],[1,0],[1,1] 0-直角坐标系相量， 1-极坐标系相量,
    :return: phasor_a-phasor_b
    """

    phasor_ret = np.full((1, 1), np.nan)
    phasor_ta = phasor_a
    phasor_tb = phasor_b
    if phasor_a.shape == phasor_b.shape:
        if phasor_mode[0] == 1:
            phasor_ta = convert_ap_to_ri(phasor_a)
        if phasor_mode[1] == 1:
            phasor_tb = convert_ap_to_ri(phasor_b)
        phasor_ret = phasor_ta - phasor_tb
    return phasor_ret


def mul_phasor(phasor_a, phasor_b, phasor_mode):
    """
    相量相乘
    :param phasor_a:相量一
    :param phasor_b:相量二
    :param phasor_mode:[0,0],[0,1],[1,0],[1,1] 0-直角坐标系相量， 1-极坐标系相量,
    :return: phasor_a*phasor_b
    """
    phasor_ret = np.full((1, 1), np.nan)
    phasor_ta = phasor_a
    phasor_tb = phasor_b
    if phasor_a.shape == phasor_b.shape:
        if phasor_mode[0] == 0:
            phasor_ta = convert_ri_to_ap(phasor_a)
        if phasor_mode[1] == 0:
            phasor_tb = convert_ri_to_ap(phasor_b)
        # print(phasor_ta+phasor_tb)
        phasor_amplitude = phasor_ta[0]*phasor_tb[0]
        phasor_phase = phasor_ta[1]+phasor_tb[1]
        # print(phasor_amplitude)
        # print(phasor_phase)
        phasor_ret = convert_ap_to_ri(np.array([phasor_amplitude, phasor_phase]))
    return phasor_ret


def div_phasor(phasor_a, phasor_b, phasor_mode):
    """
    相量相除
   :param phasor_a:相量一
    :param phasor_b:相量二
    :param phasor_mode:[0,0],[0,1],[1,0],[1,1] 0-直角坐标系相量， 1-极坐标系相量,
    :return: phasor_a/phasor_b
    """

    phasor_ret = np.full((1, 1), np.nan)
    phasor_ta = phasor_a
    phasor_tb = phasor_b
    if phasor_a.shape == phasor_b.shape:
        if phasor_mode[0] == 0:
            phasor_ta = convert_ri_to_ap(phasor_a)
        if phasor_mode[1] == 0:
            phasor_tb = convert_ri_to_ap(phasor_b)
        phasor_amplitude = phasor_ta[0] / phasor_tb[0]
        phasor_phase = phasor_ta[1] - phasor_tb[1]
        # print(phasor_amplitude)
        # print(phasor_phase)
        phasor_ret = convert_ap_to_ri(np.array([phasor_amplitude, phasor_phase]))
    return phasor_ret


