n=5
for i in range(n):
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    for j in range(2,i+1):
        print(j,end=" ")
    print()
    