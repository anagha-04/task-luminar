
sub1 = int(input("enter your mark of sub1: "))
sub2 = int(input("enter your mark of sub2: "))
sub3 = int(input("enter your mark of sub3: "))
sub4 = int(input("enter your mark of sub4: "))
sub5 = int(input("enter your mark of sub5: "))


if 0<=sub1<=50 and 0<=sub2<=50 and 0<=sub3<=50 and 0<=sub4<=50 and 0<=sub5<=50 :

    avg = (sub1+sub2+sub3+sub4+sub5) /5
    if avg>=45:
        grade ="A" 

    elif avg>=36 :

        grade ="B"
    elif avg>=30 :

        grade ="C"
    elif avg>=23 :

        grade ="D"

    else:
       grade ="Fail"
    print(f"Marks {sub1,sub2,sub3,sub4,sub5}")

    print(f"Average {avg}")

    print(f"Grade {grade}")

else:
      
      print("Invalid Plz enter mark between 0 and 50")
