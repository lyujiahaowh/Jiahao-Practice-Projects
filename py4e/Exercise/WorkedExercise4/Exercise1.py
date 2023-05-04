def computepay(h, r):
    if h > 40:
        pay = 40 * r + (h - 40) * 1.5 * r
        return pay
    else:
        pay = h * r
        return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(float(hrs), float(rate))
print("Pay", p)
