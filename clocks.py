from datetime import datetime
import time, os, random
from uni import uni



def g_time(time, nums, spc, col_v):
    ltime = []
    for k in range(7):
        ltime.append(col_v)
        for i in time:
            if i.isdigit():
                ltime[k] += nums[i][k]
            else:
                ltime[k] += spc[k]
        ltime[k] += '\033[0m'
    return ltime

def blink():
    count = 0
    point = '  \u25E7 \u25E7  '
    spc = '       '
    while True:
        sp = [point if i == count else spc for i in range(7)]
        yield sp
        if count<6:
            count += 1
        else: 
            count = 0
blinker = blink()


def output_ltime(t):
    os.system('cls||clear')
    for k in range(7):
        print(t[k])
    print()

def main():
    while True:
        rtime = datetime.now().strftime('%X')
        do_blink = next(blinker)
        fdt = g_time(rtime, uni, do_blink, '\033[1m')
        output_ltime(fdt)
        time.sleep(1)
main()