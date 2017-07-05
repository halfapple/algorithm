# -*- coding: utf-8 -*-

# 在平均状况下，排序n个项目要Ο(n log n)次比较。
# 在最坏状况下则需要Ο(n2)次比较，但这种状况并不常见。


# 快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。
# 步骤为：
# 1. 从数列中挑出一个元素，称为"基准"（pivot），
# 2. 重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（相同的数可以到任一边）
# 3. 在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
# 递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。

def quicksort(a):
	if len(a) <= 1:
		return a

	l = [x for x in a[1:] if x < a[0]]
	r = [x for x in a[1:] if x >= a[0]]

	return quicksort(l) + [a[0]] + quicksort(r)


a = [2, 5, 9, 3, 8, 4, 7, 6]
print quicksort(a)
