import csv

# try:
#     with open('users.csv', 'w', newline="") as file:
#         writer = csv.writer(file)
#         writer.writerows([['Id', 'Name', 'Age'],
#                          ['1', 'Divya', '20'],
#                          ['2', 'Vamshi', '22']])
# except Exception as e:
#     print(f"Something wrong: {e}")


## reading csv file content
try:
    with open('users.csv', 'r', newline="") as file:
        reader = csv.reader(file)
        print(reader)
        for row in reader:
            print(row)
except Exception as e:
    print(f"Something wrong: {e}")