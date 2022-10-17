import feeder_fault_locator as ffl
import incomer_fault_locator as ifl
import common as cn
amplitude = [100, 150, 10]
phase = [30, 90, 10]

def input_console_parameters():
    print(cn.function_array)
    print("please choose a function(input function name):")
    cn.function_name = input()
    if cn.function_name in cn.function_array:
        if cn.function_name != "exit":
            print("please choose a function state(generate or analyse):")
        cn.state = input()


def choose_fault_locator():
    while True:
        input_console_parameters()
        if cn.function_name == "feeder":
            print("the feeder function is executing")
        if cn.function_name == "incomer":
            print("the incomer function is executing")
        if cn.function_name == "exit":
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # choose_fault_locator()
    phasor = cn.generate_phasor_data(amplitude, phase[0], 0)
    print(phasor)
    phasor_str = cn.convert_phasor_to_string(phasor)
    print(phasor_str)
    # print(phasor_str.size)
    phasor_polar = cn.convert_string_to_phasor(phasor_str)
    print(phasor_polar)
    # phasor_ri = cn.convert_ap_to_ri(phasor)
    # print(phasor_ri)
    # phasor_ph = cn.convert_ri_to_ap(phasor_ri)
    # print(phasor_ph)