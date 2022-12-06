inp = """1000434
17,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,983,x,29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,x,x,397,x,x,x,x,x,37,x,x,x,x,x,x,13"""

import math
import re
import time
from collections import defaultdict

minTs_in = 1000434
busses_in = [17, 41, 983, 29, 19, 23, 397, 37, 13]
busses = {
    17: [],
    41: [],
    983: [],
    29: [],
    19: [],
    23: [],
    397: [],
    37: [],
    13: []
}
buss_min = {
    17: 0,
    41: 0,
    983: 0,
    29: 0,
    19: 0,
    23: 0,
    397: 0,
    37: 0,
    13: 0
}


def process_input(input_line):
    stripped_input = input_line.rstrip()
    raw_list = re.split(',', stripped_input)
    times = list()
    for j, i in enumerate(raw_list):
        if i == 'x':
            pass
        else:
            times.append((int(i), j))
    return times


if __name__ == '__main__':
    for bus in busses_in:
        buss_min[bus] = math.ceil(1000434 / bus) * bus
    print(buss_min)

    for i in range(24421):
        if i > 24399:
            print(i * 41)

    print((1000440 - 1000434) * 397)
    print((1000441 - 1000434) * 13)
    print((1000441 - 1000434) * 41)

    busses_inp = inp.split(",")

    busses_min = {
        17: 0,
        41: 0,
        983: 0,
        29: 0,
        19: 0,
        23: 0,
        397: 0,
        37: 0,
        13: 0
    }
    for i, bus_id in enumerate(busses_inp):
        if bus_id != 'x':
            busses_min[int(bus_id)] = i

    print(busses_min)

    for bus in busses_in:
        buss_min[bus] = math.ceil(1000434 / bus) * bus

    run = True
    times = defaultdict(list)

    while run:
        for bus in busses_min:
            times[busses_min[bus]].append(bus)
            busses_min[bus] += bus
            #         print(busses_min)
            if len(times[bus]) > 1:
                print(times[busses_min[bus]])
                run = False
                break
            print(times)
            time.sleep(2)

    schedule = process_input(inp)

    ref_time = schedule[0][0]
    time_fixed = 0
    for bus in schedule:
        flag = 1
        i = 0
        while flag == 1:
            if (time_fixed + ref_time * i + bus[1]) % bus[0] == 0:
                flag = 0
            else:
                i += 1
        time_fixed = time_fixed + ref_time * i
        if bus[1] != 0:
            ref_time = ref_time * bus[0]

    print('Problem 2: The earliest valid timestamp is', time_fixed)
