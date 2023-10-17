l= [i for i in range (200)]
target = int(input("Enter number: "))
left,right = 0,200
mid = (left+right)//2
while True:
    print("Range: ",left,right)
    if l[mid] ==target:
        print("Answer's index is at ",mid)
        break
    elif l[mid]>target:
        right=mid
        mid = (left+right)//2
    else:
        left=mid
        mid = (left+right)//2