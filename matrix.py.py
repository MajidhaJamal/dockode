def mat(x,y):
    c=1
    for i in range(x):
        for j in range(y):
            print(c, end=" ")
            if (j==0 and i==0) :
                c=c+2
            elif (j==(y-2) and i==(x-1)):
                c=c+2
            else:
                c=c+3
        print()
        c=(i+1)*2
x=int(input("rows"))
y=int(input("colomns"))
mat(x,y)