#function to calc pay
def computepay(h,r):

        if h >= 40:
            normh = 40.00 * r
            overh = (h - 40.00) * (r * 1.5)
            p = normh + overh
            return p

        else:
            p = h * r
            return p

#get input, calculate to float
hrs = input("Enter Hours:")
h = float(hrs)
rate = input('Enter Rate:')
r = float(rate)



print("Pay", computepay(h, r))
