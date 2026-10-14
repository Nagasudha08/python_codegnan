#linear search
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i
#     return -1
# arr=[10,50,20,30]
# target=20
# result=linear_search(arr, target)
# print("Element found at index: ", result)

#binary search
def binary_search(arr, target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=[10,20,30,40,50]
target=30
result=binary_search(arr, target)
if result !=-1:
    print("element found at index: ", result)
else:
    print("element not found")