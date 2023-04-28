score = input('Enter Your Score:')
try :
    svalue = float(score)
    if svalue < 0 or svalue > 1:
        print('Bad Score')
    elif  svalue >= 0.9 :
        print('A')
    elif svalue >= 0.8 :
        print('B')
    elif svalue >= 0.7 :
        print('C')
    elif svalue >= 0.6 :
        print('D')
    elif 0.6 > svalue :
        print('F')
except :
    print('Bad score')
