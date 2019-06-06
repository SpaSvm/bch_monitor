import time

def readable_time(sec):
    sec = round(sec - time.time())
    mi = sec // 60
    h = mi // 60
    d = h // 24
    mo = d // 30
    y = mo // 12
    return 'Time to HardFork: {5} years {4} months {3} days {2}:{1}:{0}'.format(sec%60, mi%60, h%24, d%30, mo%12, y)
