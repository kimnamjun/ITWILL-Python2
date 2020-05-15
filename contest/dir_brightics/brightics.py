from workspace.contest.dir_brightics import functions as func

# CSV file 읽기
path = "C:/ITWILL/4_Python-II/data"
filename = "mealData_meal_test.csv"
data = func.read_csv(path, filename)

print(data)

# table 모양 변경
table = func.create_table(data)
print(table)

func.test(table)