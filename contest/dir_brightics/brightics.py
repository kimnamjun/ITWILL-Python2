from workspace.contest.dir_brightics import functions as btf

# CSV file 읽기
path = "C:/ITWILL/4_Python-II/data"
filename = "mealData_meal_test.csv"
data = btf.read_csv(path, filename)

print(data)