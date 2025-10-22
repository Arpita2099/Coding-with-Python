# Enumerate Function in Python.
index=0
marks=[12,15,19,48,60]
for mark in marks:
    print(mark)
    if index==4:
        print("Arpita did good in Exam.")
    index+=1

for index, mark in enumerate(marks):
    print(mark)
    if index==4:
        print("Arpita did good in Exam.")
