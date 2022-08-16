n=float(input())
m=float(input())
BMI= round((n/(m*m)), 2)
if (1<=n<=200) and (1<=m<=10):
    if BMI<18.5:
        print(BMI,"Underweight",sep="\n")
    elif 18.5<=BMI<=25:
        print(BMI , "Normal",sep="\n")
    elif 25 <= BMI <30:
        print(BMI , "Overweight",sep="\n")
    elif 30 <= BMI:
        print(BMI , "Obese",sep="\n")
else:
    exit()