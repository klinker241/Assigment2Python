print("Task 1")

numbers = []
for i in range(5):
    num = float(input("Enter number: "))
    numbers.append(num)

avg = sum(numbers) / len(numbers)
print("Average:", avg)
print("Max:", max(numbers))
print("Min:", min(numbers))

count = 0
for n in numbers:
    if n > avg:
        count += 1

print("Greater than average:", count)

print("\nTask 2")

users = set()

while True:
    name = input("Enter username (or 'exit'): ")
    if name == "exit":
        break
    users.add(name)

print("Unique users:", len(users))

check = input("Enter username to check: ")
if check in users:
    print("User exists")
else:
    print("User not found")

print("\nTask 3")

products = {
    "apple": 100,
    "banana": 80,
    "milk": 250
}

while True:
    print("\n1 Add\n2 Change\n3 Remove\n4 Show\n5 Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Product name: ")
        price = float(input("Price: "))
        products[name] = price

    elif choice == "2":
        name = input("Product: ")
        if name in products:
            products[name] = float(input("New price: "))

    elif choice == "3":
        name = input("Remove: ")
        products.pop(name, None)

    elif choice == "4":
        for k, v in products.items():
            print(k, "-", v)

    elif choice == "5":
        break

print("\nTask 4")

point1 = (2, 3)
point2 = (5, 7)

print(point1)
print(point2)

print("\nTask 5")

note = input("Enter note: ")

with open("notes.txt", "a") as f:
    f.write(note + "\n")

print("All notes:")
with open("notes.txt", "r") as f:
    print(f.read())

print("\nTask 6")

import os

if not os.path.exists("data"):
    os.mkdir("data")

for i in range(3):
    with open(f"data/file{i}.txt", "w") as f:
        f.write("Hello")

print("Files:", os.listdir("data"))

os.rename("data/file0.txt", "data/newfile.txt")
os.remove("data/file1.txt")

print("\nTask 7")

import csv

data = [
    ["Ali", 85],
    ["Aruzhan", 90],
    ["Dias", 78],
    ["Madi", 88],
    ["Amina", 95]
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "grade"])
    writer.writerows(data)

grades = []

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["grade"])
        grades.append(int(row["grade"]))

print("Max:", max(grades))
print("Average:", sum(grades)/len(grades))

print("\nTask 8")

import json

user = {
    "name": "Ali",
    "age": 20,
    "skills": ["Python", "Java"]
}

with open("user.json", "w") as f:
    json.dump(user, f)

with open("user.json", "r") as f:
    data = json.load(f)

data["skills"].append("C++")

with open("user.json", "w") as f:
    json.dump(data, f)

print("\nTask 9")

expenses = []

while True:
    print("\n1 Add\n2 Show\n3 Total\n4 Save\n5 Load\n6 Exit")
    ch = input("Choose: ")

    if ch == "1":
        name = input("Expense: ")
        amount = float(input("Amount: "))
        expenses.append({"name": name, "amount": amount})

    elif ch == "2":
        for e in expenses:
            print(e["name"], "-", e["amount"])

    elif ch == "3":
        total = sum(e["amount"] for e in expenses)
        print("Total:", total)

    elif ch == "4":
        with open("expenses.json", "w") as f:
            json.dump(expenses, f)

    elif ch == "5":
        try:
            with open("expenses.json", "r") as f:
                expenses = json.load(f)
        except:
            print("No file")

    elif ch == "6":
        break