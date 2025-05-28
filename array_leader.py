array = list(map(int,input().split()))
leader_array = list()
greatestSoFar = -1

def find_leader(array,greatestSoFar,leader_array):
    j=len(array)-1
    while j>=0:
        if j==len(array)-1:
            leader_array.append(array[j])
            greatestSoFar = array[j]
        else:
            if array[j] > greatestSoFar:
                leader_array.append(array[j])
                greatestSoFar = array[j]
        j-=1

    return leader_array

print(find_leader(array,greatestSoFar,leader_array))
