hours1 = int(input("Hours: "))
min1 = int(input("Minutes: "))
sec1 = int(input("Seconds: "))
hours2 = int(input("Hours: "))
min2 = int(input("Minutes: "))
sec2 = int(input("Seconds: "))
result = (((hours2 - hours1) * 3600) + ((min2 - min1) * 60) + (sec2 - sec1))
print (str(result) + " seconds")
