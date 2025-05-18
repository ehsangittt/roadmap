def practice(num):
    if num >= 0:
        print("mosbat")
    else:
        print("manfi")

    if num % 2 == 0:
        print("zoj")
    else:
        print("fard")
    
    if num % 3 == 1 :
        print ( " like")
    else:
        print ("dilike")

    if 10 <= num <= 20:
        print (" adad beyn 10 ta 20 ")
num = int(input("adad? "))
practice(num)
