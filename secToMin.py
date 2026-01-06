def secToMin(t):
    sec = t % 60
    mins = int((t-sec)/60)
    if len(str(sec)) == 1:
        sec = '0'+str(sec)
    return str(mins)+':'+str(sec)

print(secToMin(int(input())))
