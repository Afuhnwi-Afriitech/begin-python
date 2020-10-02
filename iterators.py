list_interator = [1, 2, 3]
for i in list_interator:
    print(i, end=" ")
new = iter(list_interator)
print("")
for item in range(0, len(list_interator)):
    print(next(new))
