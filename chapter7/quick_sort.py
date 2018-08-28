#! /usr/bin/python3
# -*- coding:UTF-8 -*-

def quick_sort(num_list):
  q_sort(num_list, 0, len(num_list) - 1)

def q_sort(num_list, first, last):
  if first < last:
    split = partition(num_list, first, last)
    q_sort(num_list, first, split - 1)
    q_sort(num_list, split + 1, last)

def partition(num_list, first, last):
  # 选取列表中的第一个元素作为划分元素
  pivot = num_list[first]
  left_mark = first + 1
  right_mark = last
  while True:
    while num_list[left_mark] <= pivot:
     # 如果列表中存在与划分元素pivot相等的元素，让它位于left部分
     # 以下检测用于划分元素pivot是列表中的最大元素时
     # 防止left_mark越界
      if left_mark == right_mark:
        break
      left_mark += 1
    while num_list[right_mark] > pivot:
      # 这里不需要检测，划分元素pivot是列表中的最小元素时
      # right_mark自动停在first处
      right_mark -= 1
    if left_mark < right_mark:
      # 此时，left_mark处的元素大于pivot
      # right_mark处的元素小于等于pivot，交换两者
      num_list[left_mark], num_list[right_mark] = num_list[right_mark], num_list[left_mark]
    else:
      break
  # 交换first处的划分元素与right_mark处的元素
  num_list[first], num_list[right_mark] = num_list[right_mark], num_list[first]
  # 返回划分元素pivot的最终位置
  return right_mark

n_list = [5, -4, 6, 3, 7, 11, 1, 2]
print(f'排序之前: {str(n_list)}')
quick_sort(n_list)
print(f'排序之后: {str(n_list)}')