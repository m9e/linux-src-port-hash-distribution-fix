#!/usr/bin/python3

res = {}
mod=10

# linux ports are even 32768-60999 by default
for i in range(0,mod):
  res[i]=0

for i in range(32768,60999+1):
  if (i%2!=0):
    continue
  v = i%mod 
  res[v]=res[v]+1

for i in range(0,mod):
  print("%d: %d" % (i, res[i]))

print("\n")
# fix?
for i in range(0,mod):
  res[i]=0

for i in range(32768,60999+1):
  if (i%2==0):
    continue
  v = (i >> 1)%mod 
  res[v]=res[v]+1

for i in range(0,mod):
  print("%d: %d" % (i, res[i]))

# output:
# 0: 2823
# 1: 0
# 2: 2823
# 3: 0
# 4: 2823
# 5: 0
# 6: 2823
# 7: 0
# 8: 2824
# 9: 0
# 
# 
# 0: 1411
# 1: 1411
# 2: 1411
# 3: 1411
# 4: 1412
# 5: 1412
# 6: 1412
# 7: 1412
# 8: 1412
# 9: 1412
