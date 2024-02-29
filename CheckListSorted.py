#write a function to check if a given list is sorted

def is_sorted(list1):
    if(list1==sorted(list1)):
        return True
    else:
        return False
    
x=[12,54,52,1,24,13,16,89]
x1=[5,6,8,11,24,29,50,60]
print("list ", x, " is not sorted: ", is_sorted(x))
print("list ", x1, " is not sorted: ", is_sorted(x1))
