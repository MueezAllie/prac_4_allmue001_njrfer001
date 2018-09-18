def Timer():
    global f
    global timing
    if f == 0.5:
        timing = timing + datetime.timedelta(seconds = 0.5)
        strtime = str(timing) + '.0000000'
        strtime = strtime[2:10]
        #print(timing)
    elif f == 1:
        timing = timing + datetime.timedelta(seconds = 1)
        strtime = str(timing) + '.0000000'
        strtime = strtime[2:10]
        #print(timing)
    elif f == 2:
        timing = timing + datetime.timedelta(seconds = 2)
        strtime = str(timing) + '.0000000'
        strtime = strtime[2:10]
        #print(timing)

    return strtime
