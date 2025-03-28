# 汉诺塔问题。
# def hanoi(n, a, b, c):
#     if n>0:
#         hanoi(n - 1, a, c, b)
#         print('从 %s 移动到 %s' % (a, c))
#         hanoi(n - 1, b, a, c)
#
#
# hanoi(3, 'A', 'B', 'C')



# 二分查找，也称为折半查找。
# def binary_search(li, val):
#     left = 0
#     right = len(li) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if li[mid] == val:
#             return mid
#         elif li[mid] > val:
#             right = mid - 1
#         else:  # 条件为li[mid] < val
#             left = mid + 1
#     else:
#         return None
#
#
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(binary_search(li, 3))



# 冒泡排序
# def bubble_sort(array):
#     global exchange
#     for i in range(len(array) - 1):
#         exchange = False
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:  # 如果要从小到大排序则把 > 变成  < 既可以。
#                 array[j], array[j + 1] = array[j + 1], array[j]
#                 exchange = True
#         print(array)
#         if not exchange:
#             return
#
#
# array = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
# bubble_sort(array)



# 选择排序
# def select_sort(li):
#     new_li = []
#     for i in range(len(li)):
#         min_val = min(li)
#         new_li.append(min_val)
#         li.remove(min_val)
#     return new_li


# def select_sort(li):
#     for i in range(len(li) - 1):
#         min_loc = i
#         for j in range(i + 1, len(li)):
#             if li[j] < li[min_loc]:
#                 min_loc = j
#         li[min_loc], li[i] = li[i], li[min_loc]
#     # return li
#
#
# li = [3, 1, 2, 6, 5, 4, 7]
# select_sort(li)
# print(li)


#　插入排序
# def insert_sort(li):
#     for i in range(1, len(li)):
#         tam = li[i]
#         j = i - 1
#         while j >= 0 and li[j] > tam:
#             li[j + 1] = li[j]
#             j -= 1
#         li[j + 1] = tam
#
#
# li = [3, 1, 2, 6, 5, 4, 7]
# insert_sort(li)
# print(li)

# def quick_sort(li):

# def partition(li, left, right):
#     tam = li[0]
#     while left < right:
#         if li[left] <= li[right]:
#
#
# mp = {')': '(', ']': '[', '}': '{'}
# for i in mp:
#     print(i)
from collections import Counter

s = "banana"
char_counter = Counter(s)
print(char_counter)