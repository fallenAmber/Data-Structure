def binary_search(a,s):
    left=0
    right=n-1
    while(left<=right):
        mid=(left+right)//2
        if a[mid] is s:
            return mid
        else:
            if(s<a[mid]):
                right=right-1
            else:
                left=left+1
    return -1
a=[]
n=int(input('How many elements would you like to add? '))
for i in range(n):
    data=int(input('Enter the data item:'))
    a.append(data)
s=int(input('Enter the number to be searched: '))
p = binary_search(a,s)
if(p==-1):
    print("Number can't be traced")
else:
    print("The number can be traced")