n = int(input())
for i in range(n//2+1):
    print((n - (i*2+1))//2*" " + (i*2+1)*"*" + (n - (i*2+1))//2*" ")
for j in range(n):
    print((j+1)*" "+(n-2)*"*")
    n=n-2