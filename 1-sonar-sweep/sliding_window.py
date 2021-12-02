# check for increases in a 3-number sliding window

with open('input.txt') as file:
  contents = file.read()

# print(contents)
nums = [int(x) for x in contents.split('\n') if x != '']

# this isn't the cleanest way of doing it, but it should work
n1 = nums[0]
n2 = nums[1]
n3 = nums[2]

index = 3
count = 0
while index < len(nums):
  last_sum = n1+n2+n3
  next_sum = n2+n3+nums[index]
  if next_sum > last_sum:
    count += 1
  n1 = nums[index-2]
  n2 = nums[index-1]
  n3 = nums[index]
  index += 1

print(count)
  
