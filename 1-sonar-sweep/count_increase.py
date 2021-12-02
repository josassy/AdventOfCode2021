# count the number of times a depth measurement increases from the previous measurement. 
# (There is no measurement before the first measurement.)

with open('input.txt') as file:
  contents = file.read()

# print(contents)
nums = [int(x) for x in contents.split('\n') if x != '']
# print(nums)

last_num = nums[0]
count = 0
for num in nums:
  if num > last_num:
    count += 1
  last_num = num
print(count)
