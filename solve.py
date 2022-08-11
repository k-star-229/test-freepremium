'''
  author : "Karl Mattison"
  copyright   = "Copyright 11th Aug, 2022"
'''

# Code in Python3 to tell if there
# exists a pair in array whose
# sum results in x.
# Function to print pairs
def printPairs(nums, n, target):     
  rem = []
    
  for i in range(target):
    # Initializing the rem
    # values with 0's.
    rem.append(0)

  for i in range(n):
    if nums[i] < target:
      # Perform the remainder operation
      # only if the element is target, as
      # numbers greater than target can't
      # be used to get a sum target.Updating
      # the count of remainders.
      rem[nums[i] % target] += 1 
    # Traversing the remainder list from
    # start to middle to find pairs
  for i in range(1, target // 2):
    if rem[i] > 0 and rem[target - i] > 0:
        return i, target - i 
  ### Once we reach middle of
  ### remainder array, we have to
  ### do operations based on target.
  if i >= target // 2:
    if target % 2 == 0:
      if rem[target // 2] > 1:
        # If target is even and we have more
        # than 1 elements with remainder
        # target/2, then we will have two
        # distinct elements which add up
        # to target. if we dont have than 1
        # element, print "No".
        print("Yes")
        return int(target/2), int(target/2)
      else:
        print("No")
    else:
      # When target is odd we continue
      # the same process which we
      # did in previous loop.
      if rem[target // 2] > 0 and rem[target - target // 2] > 0:
        print("Yes")
        return target//2, target - target//2
      else:
        print("No")
    
# Driver Code
nums = [2,7,11,15]
target = 9
arr_size = len(nums)
 
# Function calling
printPairs(nums, arr_size, target)