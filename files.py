import csv

FILENAME = "users.csv"

users = [
    ["Олег", 24],
    ["Егор", 42],
]

with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows (users)

with open(FILENAME, "a", newline="") as file:
    user = ["ещё кто-то", 0]
    writer = csv.writer(file)
    writer.writerow(user)
