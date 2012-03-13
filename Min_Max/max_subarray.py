#!/usr/bin/python

#Given an array of both positive and negative integers, try to find the maximum sum of all its subarraya. Requirement: O(n) time efficiency


# Kadane's algorithm , Carnegie-Mellon University (Bentley 1984).
def max_subarray(A):
    max_so_far = max_ending_here = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

#Test 
a = [1,-8,6,3,-1,5,7,-2,0,1]
print max_subarray(a)

