################################   solution__1
# n=int(input())
# n=n-2
# for i in range(n):
#     print((n-i)*" "+(((i+1)*2)-1)*"*")
# for j in range(n):
#     print((j+2)*" "+(2*n-(((j+1)*2)-1))*"*")


################################   solution__2

Lozi = int(input())
if 1 <= Lozi <= 19:
    if (Lozi%2)==1:
        for i in range(1, Lozi+1):
            i = i - (Lozi//2 +1)
            if i < 0:
                i = -i
            print(" " * i + "*" * (Lozi - i*2) + " "*i,end="")
            print(" " * i + "*" * (Lozi - i*2) + " "*i)




################################   solution__3
# h = int(input())
# for i in range(h):
#     print(" "*(h-i), "*"*(i*2+1))
# for i in range(h-2, -1, -1):

################################   solution__4
# def lowzi(rows):
#     for i in range(rows):
#         print(' '*(rows-i-1)+(2*i+1)*"*")
#     for i in reversed(range(rows)):
#         print(' '*(rows-i-1)+(2*i+1)*"*")

# lowzi(int(input()))