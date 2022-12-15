students = {"Mark": "Male", "John": "Male", "Mary": "Female", "Alice": "Female"}
marks = {"Mark": 5, "John": 3, "Mary": 4, "Alice": 3}

for i in marks:
    print(i, marks[i])
print()
for i in marks:
    if marks[i] == 4 or marks[i] == 5: # Если отличник или хорошист, то молодец!
        print(i, "Well done!")
    if (marks[i] == 4 or marks[i] == 5) and students[i] == "Male": # Если отличник или хорошист да ещё и мужчина, то большой молодец!
        print("You are good boy! " + i)
