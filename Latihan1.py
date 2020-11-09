x = 10
y = x
for x in range (10):
    for y in range (10):
        tab = x + y
        print ("{0:>5}" .format(tab), end="")
    print()
