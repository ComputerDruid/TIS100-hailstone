def hailstones(x):
    while x > 1:
        yield x
        if x % 2 == 0:
            x = x // 2
        else:
            x = x * 3 + 1

for i in range(2,999):
  if max(hailstones(i))>999:
    print(i)
    break

