students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])

# using list with loops

students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)

# using list with loops and lens

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

#using list with dict

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Darco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")


#create like a table mode

students = [
    {"name": "Hermione", "houses": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "houses": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "houses": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Darco", "houses": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["houses"], student["patronus"], sep = ", ")