#!/usr/bin/python

#CLRS Chapter 4 Divide-and-Conquer 3rd Edition p68
def find_max_crossing_subarray(A,low,mid,high):
	#find leftside max subarray
	left_sum = None
	sum = 0
	max_left = mid
	for i in range(mid,low-1,-1):
		sum = sum + A[i]
		if left_sum == None:
			left_sum = sum
			max_left = i
		else:
			if sum > left_sum:
				left_sum = sum
				max_left = i
	
	#find rightside max subarray
	right_sum = None
	sum = 0
	max_right = mid + 1
	for j in range(mid+1,high+1):
		sum = sum + A[j]
		if right_sum == None:
			right_sum = sum
			max_right = j
		else:
			if sum > right_sum:
				right_sum = sum
				max_right = j
	return [max_left,max_right,left_sum + right_sum]

def find_max_subarray(A,low,high):
	if high == low:
		return [low,high,A[low]]  #base case: only one element
	else:
		mid = (low + high)/2
		left = find_max_subarray(A,low,mid)
		right = find_max_subarray(A,mid+1,high)
		cross = find_max_crossing_subarray(A,low,mid,high)
		
		if left[2] >= right[2] and left[2] >= cross[2]:
			return left
		elif right[2] >= left[2] and right[2] >= cross[2]:
			return right
		else:
			return cross

A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

print find_max_subarray(A,0,15)
