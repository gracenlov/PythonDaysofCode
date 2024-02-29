#create a program that implements the bubble sort algorithm


def bubble_sort(list1):
    n=len(list1)
    length=n
    while(n>1):
        nNew=0
        for i in range(n-1):
            if(list1[i]>list1[i+1]):
                temp=list1[i]
                list1[i]=list1[i+1]
                list1[i+1]=temp
                nNew=i+1
        n=nNew
    return list1

x=[51,54,1,0,45,5,8,18,91]
print("sorted list: ", bubble_sort(x))
x=[101,52,1,100,455,15,38,11,91]
print("sorted list: ", bubble_sort(x))
x=[51,54,1,0,45,5,8,18,91,108,95,85,74,15,45,6]
print("sorted list: ", bubble_sort(x))
