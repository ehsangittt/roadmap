a = 1
while a <= 20:
    if a % 3 == 0 and a % 5 == 0:
        print("hiphop")
    elif a % 3 == 0:
        print("hip")
    elif a % 5 == 0:
        print("hop")
    else:
        print(a)
    a += 1
