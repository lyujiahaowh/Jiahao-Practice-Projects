try :
    hrs = input('Enter Hours:')
    h = float(hrs)
    rate = input('Enter Rate:')
    r = float(rate)
except :
    print('Error, please enter numeric input')
    quit()

if h <= 40 :
    pay = h * r
    print(pay)
elif h > 40 :
    pay = 40 * r + (h - 40) * r *1.5
    print(pay)