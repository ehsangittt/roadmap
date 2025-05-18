number = int(input("please enter number"))
# az karbar adad migire ta barresi kone avale ya na 
if number <= 1:
    print("adad aval")
# az on jayi ke 1 aval hast pas dg 1 ro barresi nemkonim 
else:
    aval = True
    # dar marhaleye aval , dar nazar migirim ke adad vared shode aval ast baad mirim sharayet dar nazar migirm.
    for i in range(2, number):
        #baraye mesaal adad 23 varedei hast , (2,23).
        if number % i == 0:
            # barresi mikone 2,22 ro ke bar 23 bakhsh pazir hast ya na
            aval = False
            # agar adad bar i bakhshpazir bod False mishe yani on adad aval nis.
            break
            # aghar adad bakhsh pazir bod break mishe va edame peyda nemikone

    if aval:
        print("in adad aval ast")
    else:
        print("in adad aval nist")
# 0 o dorost konam 
# order zamani o o omega teta 
# soorat