def revarr_arr(arr): # with using 1 additional array
    arr1=[]
    i=-1
    while i >= -(len(arr)):
        arr1.append(arr[i])
        i-=1
    return(arr1)

def revarr_v(arr):  # with using 1 variable  (better time complexcity)
    for i in range(len(arr)//2):
        temp=arr[i]
        arr[i]= arr[-i-1]
        arr[-i-1]= temp
    return arr

a = [0,1,2,3,4,5,6]
print(revarr_arr(a))
print(revarr_v(a))