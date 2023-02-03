def test1():
    x = input('per-')
    perc = int(x)
    if perc > 85:
        print ('A')
    elif perc > 70 and perc <= 85: 
        print ('B')
    elif perc > 60 and perc <= 70:       #if 60 <perc <=70
        print ('C')
    elif perc > 45 and perc <= 60:
        print ('D')
    elif perc > 0 and perc <= 45:   
        print ('E')
def test2():
    x = input('per-')
    perc = int(x)
    if perc > 85:
        print ('A')
    elif perc > 70 and perc <= 85:       # elif means if not this do this
        print ('B')
    elif perc > 60 and perc <= 70:       #if 60 <perc <=70
        print ('C')
    elif perc > 45 and perc <= 60:
        print ('D')
    else :                                # use of else in place of elif
        print ('E')
