n = int(input())
students = []

for n in range(n):
  input_data = list(input().split())
  my_dict = {
    "name": input_data[0],
    "score": input_data[1]
  }
  students.append(my_dict)

students.sort(key=lambda x: x['score'])

for student in students:
  print(student["name"], end=" ")
