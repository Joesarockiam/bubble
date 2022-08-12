def bubblesort(a):
    for i in range(len(a)):
        for j in range(i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp

                
a=[]
n=int(input("Enter the total no of values:"))
for i in range(0,n):
    b=int(input("Enter elements:"))
    a.append(b)

bubblesort(a)
print(a)
