from typing import List

def run_fish_naive(fish_list: List[int], days: int) -> int:
  # print(f'days left: {days}, fish: {len(fish_list)}')
  if days > 0:
    new_fish = []
    for fish in fish_list:
      if fish > 0:
        new_fish.append(fish - 1)
      else:
        new_fish.append(8)
        new_fish.append(6)
    return run_fish_naive(new_fish, days - 1)
  else:
    return len(fish_list)

def bucket_fish(fish_list: List[int]):
  bucket = {}
  for fish in fish_list:
    if fish in bucket:
      bucket[fish] += 1
    else:
      bucket[fish] = 1
  return bucket

def run_fish_optimized(fish_bucket: dict, days: int):
  if days > 0:
    new_bucket = {}
    for bucket in fish_bucket:
      if bucket > 0:
        bucket_val = new_bucket[bucket-1]+fish_bucket[bucket] if (bucket-1) in new_bucket else fish_bucket[bucket]
        new_bucket[bucket-1] = bucket_val
      else:
        new_bucket[8] = fish_bucket[bucket]
        new_bucket[6] = new_bucket[6]+fish_bucket[bucket] if (6) in new_bucket else fish_bucket[bucket]
    return run_fish_optimized(new_bucket, days-1)
  else:
    return sum(fish_bucket.values())

def p1():
  with open('input.txt') as f:
    fish = [int(x) for x in f.read().strip( '\n').split(',')]
  print(run_fish_naive(fish, 80))

def p2():
  with open('input.txt') as f:
    fish = [int(x) for x in f.read().strip( '\n').split(',')]
  print(run_fish_optimized(bucket_fish(fish), 256))

p1()
p2()