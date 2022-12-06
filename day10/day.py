inp = [
    138,
    3,
    108,
    64,
    92,
    112,
    44,
    53,
    27,
    20,
    23,
    77,
    119,
    62,
    121,
    11,
    2,
    37,
    148,
    34,
    83,
    24,
    10,
    79,
    96,
    98,
    127,
    7,
    115,
    19,
    16,
    78,
    133,
    61,
    82,
    91,
    145,
    39,
    33,
    13,
    97,
    55,
    141,
    1,
    134,
    40,
    71,
    54,
    103,
    101,
    26,
    47,
    90,
    72,
    126,
    124,
    110,
    131,
    58,
    12,
    142,
    105,
    63,
    75,
    50,
    95,
    69,
    25,
    68,
    144,
    86,
    132,
    89,
    128,
    135,
    65,
    125,
    76,
    116,
    32,
    18,
    6,
    38,
    109,
    111,
    30,
    70,
    143,
    104,
    102,
    120,
    31,
    41,
    17
]

from collections import Counter, defaultdict


def get_diff(inp):
    diff = []

    for i, val in enumerate(inp):
        if i == 0:
            continue
        diff.append(val - inp[i - 1])
    return diff


if __name__ == '__main__':
    s_inp = sorted(inp)
    s_inp.append(0)
    s_inp.append(max(inp) + 3)
    s_inp = sorted(s_inp)

    diff1 = sum([1 for x in diff if x == 1])
    diff2 = sum([1 for x in diff if x == 2])
    diff3 = sum([1 for x in diff if x == 3])

    print(diff1* diff3)

    dif3 = sum([1 for x in get_diff(sorted(inp)) if x == 3])
    print(dif3)

    sorted_adapters = s_inp
    combinations = defaultdict(int)

    combinations[0] = 1

    for i in sorted_adapters[1:]:
        combinations[i] = combinations[i-1] + combinations[i-2] + combinations[i-3]

    print(combinations[max(sorted_adapters)])