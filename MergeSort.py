a = [3,7,2,8,5,9,1,6,10]
# print(a[1])
# a.sort()
# print(len(a))
length = len(a)
# j = 1
# print((1,2,3 )if 100>1000 else (4,5,6,j +=1))

# 传入参数为待排序数组a, 和数组a的长度
def MergeSort(a, length):
    auxi = [0]*length
    SortProcess(a, auxi, 0, length-1)
    # print(a)

# 传入的参数为待排序数组a，辅助排序数组auxi，左边界L，右边界R(数组中的右边界，不是数的右边界，即从0开始)
def SortProcess(a, auxi, L, R):
    # 该函数是将待排序数组a中的[L, R]区间的数进行归并排序，并将结果放到辅助排序数组auxi中
    if(L == R):
        return
    midle = int((L+R)/2)
    SortProcess(a, auxi, L, midle)
    SortProcess(a, auxi, midle+1, R)
    Merge(a, auxi, L, midle, R)   # 归并函数

# 传入的参数为数组a, 辅助排序数组auxi, 左边界L，中间值midle，右边界R
def Merge(a, auxi, L, midle, R):
    # 将数组a中 [L, midle] 和 [midle+1, R]两边的已经排好序的数组进行归并，放到辅助数组auxi中，然后放回到a中
    i=L     # 辅助数组中的位置指针，大小排序
    p1 = L      # 左边的指针
    p2 = midle+1        # 右边的指针
    # 当右边的数小时，右边的指针向右移动一位，左边数小则左边向右移，直到有一端的指针移动到末尾
    while p1 <= midle and p2 <= R:
        if a[p1] < a[p2]:
            auxi[i] = a[p1]
            p1 += 1
        else:
            auxi[i] = a[p2]
            p2 += 1
        i += 1

    while p1 <= midle :
        auxi[i] = a[p1]
        i = i+1
        p1 = p1+1
    while p2 <= R :
        auxi[i] = a[p2]
        i = i+1
        p2 = p2+1
    # 把排好序的数组放回原数组中
    i = L
    while i <= R :
        a[i] = auxi[i]
        i += 1

MergeSort(a, length)
print(a)
# ***************************************
# def merge(arr, l, m, r):
#     n1 = m - l + 1
#     n2 = r - m
#
#     # 创建临时数组
#     L = [0] * (n1)
#     R = [0] * (n2)
#
#     # 拷贝数据到临时数组 arrays L[] 和 R[]
#     for i in range(0, n1):
#         L[i] = arr[l + i]
#
#     for j in range(0, n2):
#         R[j] = arr[m + 1 + j]
#
#         # 归并临时数组到 arr[l..r]
#     i = 0  # 初始化第一个子数组的索引
#     j = 0  # 初始化第二个子数组的索引
#     k = l  # 初始归并子数组的索引
#
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
#
#     # 拷贝 L[] 的保留元素
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#
#     # 拷贝 R[] 的保留元素
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1
#
#
# def mergeSort(arr, l, r):
#     if l < r:
#         m = int((l + (r - 1)) / 2)
#
#         mergeSort(arr, l, m)
#         mergeSort(arr, m + 1, r)
#         merge(arr, l, m, r)
#
#
# arr = [12, 11, 13, 5, 6, 7]
# n = len(arr)
# print("给定的数组:",arr)
#
#
# mergeSort(arr, 0, n - 1)
# print("\n\n排序后的数组:",arr)
