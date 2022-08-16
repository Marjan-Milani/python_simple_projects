n1 = int(input())
n2 = int(input())
i1 = n1
i2 = n2
barax = 0
barax1 = 0
while n1 > 0:
    temp = n1 % 10
    barax = barax * 10 + temp
    n1 = n1 // 10
while n2 > 0:
    temp1 = n2 % 10
    barax1 = barax1 * 10 + temp1
    n2 = n2 // 10
if barax>barax1:
    print(i2,"<",i1)
elif barax<barax1:
    print(i1,"<",i2)
else:
    print(i1,"=",i2)
