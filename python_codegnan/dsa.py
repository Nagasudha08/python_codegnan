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
# def binary_search(arr, target):
#     left=0
#     right=len(arr)-1
#     while left<=right:
#         mid=(left+right)//2
#         if arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#             left=mid+1
#         else:
#             right=mid-1
#     return -1
# arr=[10,20,30,40,50]
# target=30
# result=binary_search(arr, target)
# if result !=-1:
#     print("element found at index: ", result)
# else:
#     print("element not found")

#bubble sort
# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j], arr[j+1]=arr[j+1], arr[j]
#     return arr
# arr=[5,2,4,1]
# print(bubble_sort(arr))

#selection sort
# def selection_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         min_index=i
#         for j in range(i+1, n):
#             if arr[j]<arr[min_index]:
#                 min_index=j
#         arr[i], arr[min_index]=arr[min_index], arr[i]
#     return arr
# arr=[5,1,2,4]
# print(selection_sort(arr))

#insertion sort
def insertion_sort(arr):
    n=len(arr)
    for i in range(1, n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
arr=[5,2,4,1]
print(insertion_sort(arr))

#merge sort
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    #divide arr by two parts
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    #recrusively sort arrays
    left=merge_sort(left)
    right=merge_sort(right)
    #merge to halves
    return merge(left,right)
#this method is mainly for comparison of values
def merge(left, right):
    result=[]
    i=0
    j=0
    #compare elements from both arrays
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])



    