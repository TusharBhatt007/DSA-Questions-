array = list(map(int,input().split()))
outputArray = []

def find_missing_repeating_number(array):
    array.sort()
    i=0
    while i<len(array):
        if i==0:
           if  array[i]!=i+1:
                outputArray.append(i+1)
        else:
            if array[i]!=i+1:
                outputArray.append(i+1)
            if array[i]==array[i-1]:
                outputArray.append(array[i])
        i+=1
    return outputArray

print(find_missing_repeating_number(array))


