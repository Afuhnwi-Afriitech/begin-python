
with open("newSample2.txt", "w") as notes:
    for i in range(2, 13):
        for j in range(2, 13):
            print("{0} times {1} is {2}".format(i, j, i * j), file=notes)
        print("=" * 20, file=notes)

notes.close()
