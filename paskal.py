# lst=[1] 
# x=int(input())
# if 1 <= x <= 10:
#     for i in range(x): 
#         print(lst) 
#         mylist=[] 
#         mylist.append(lst[0]) 
#         for i in range(len(lst)-1): 
#             mylist.append(lst[i]+lst[i+1]) 
#         mylist.append(lst[-1]) 
#         lst=mylist
# else:
#     exit()


n = int(input())
prior_row = []
current_row = []

for i in range(1, n+1):
    if i == 1:
        current_row.append(1)
    elif i == 2:
        prior_row = current_row.copy()
        current_row = [1, 1]
    else:
        prior_row = current_row.copy()
        current_row = [1]
        for j in range(1, len(prior_row)):
            current_row.append(prior_row[j]+prior_row[j-1])
        current_row.append(1)
    for c in current_row:
        print(c, end=" ")
    print("\n", end="")