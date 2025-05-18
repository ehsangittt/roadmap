def grade_to_letter(score):
    if score >= 17 :
        print ( "Grade A")
    elif score < 17 and score >=14 :
        print ( " Grade B")
    elif score < 14 and score >=10 :
        print ("Grade C")
    else :
        print ("Error")

score = int(input("score?"))

grade_to_letter(score)