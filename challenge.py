n = int(input("enter number of student not less than 2 and not beyond 10:  "))
student_marks = {}
if int(n)<2 or int(n)>10:
	print('not enough students or too many check again')
else:
	student_marks = {}
	int(student_marks)<=0 or int(student_marks)<100
	print('not enough students or too many check again')
for d in range(n):
	line = input().split()
	name, scores = line[0], line[1:]
	scores = map(float, scores)
	student_marks[name] = scores
query_name = input()
marks=0
for i in student_marks[query_name]:
	marks=marks+i
avg=marks/3
print("%.2f"%avg)