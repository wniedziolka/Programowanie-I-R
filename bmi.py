masa = float(input("podaj masę ciała w kilogramach: "))
wzrost = float(input("podaj wzorst w metrach: "))
bmi = masa/(wzrost**2)
print("BMI = {0}".format(bmi))
if bmi > 30:
    print("Otyłość")
elif bmi > 25:
    print("Nadwaga")
elif bmi > 18.5:
    print("Waga prawidłowa")
else:
    print("Niedowaga")