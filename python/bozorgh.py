def find_max(a, b, c):
    if a >= b and a >= c:
        print("a bozorgtarin ast")
    elif b >= a and b >= c:
        print("b bozorgtarin ast")
    else:
        print("c bozorgtarin ast")

a = int(input("num? "))
b = int(input("num? "))
c = int(input("num? "))

find_max(a, b, c)
