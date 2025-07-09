




marks=[]

for i in range(3):
    marks.append(int(input("enter ur marks: ")))

sum=sum(marks)

average=sum/len(marks)
total_possible=len(marks)*100
percentage=(sum/total_possible)*100

print(marks)
print(sum)
print(average)
print(percentage)