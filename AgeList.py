#Create list of ages
#Sort list of ages
#Find sum of ages
#Find number of elements in list
#Divide sum by number of elements and call this Average
#print Average

Ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
Ages.sort()
Sum = 0
for age in Ages:
    Sum = Sum + age
Average = Sum / len(Ages)

print(Average)
