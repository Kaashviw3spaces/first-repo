def find_in_list(li,x):
    for i in range(0, len(li)):
        if li[i]==x:
            return i
    return None
li = [1,2,3,4,5]
x=1
print(find_in_list(li,x))