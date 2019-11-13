a = (int(input("Enter a number A")))
b = (int(input("Enter a number B")))
if (a < b ):
    for x in range(a,b + 1):
        print(x)
    else:
        for x in range (a,b - 1, -1):
            print(x)