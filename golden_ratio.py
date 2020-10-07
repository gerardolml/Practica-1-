from fibonacci import fiboo
import math as mt
def phy():
    i=2
    while i>=2:
        n=i
        i+=1
        ph =round((1+mt.sqrt(5))/2,6)
        print(round(fiboo(n)[n-1]/fiboo(n-1)[n-2],6))
        if round(fiboo(n)[n-1]/fiboo(n-1)[n-2],6)== ph:
            break
    return print('A partir de f_ %d / f_ %d la division empieza converger a %f ' % (n,n-1,ph))
phy()