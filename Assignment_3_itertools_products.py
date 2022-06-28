import itertools
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
cross = list(itertools.product(list1,list2))
for i in cross:
    print(i,end=' ')