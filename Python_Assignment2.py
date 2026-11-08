#1. List Creation
age_list = [24, 25, 26, 27, 28]

name_list = ["Jeni", "Anu", "Amal", "Arun", "Meera"]

print(age_list)
print(name_list)

#(a) Append "Yazhini" to name_list
name_list.append("Yazhini")
print(name_list)

#(b) Insert 30 at index 2 in age_list
age_list.insert(2, 30)
print(age_list)

#(c) Remove "Yazhini" from name_list
name_list.remove("Yazhini")
print(name_list)

#(d) Pop the last element from age_list
age_list.pop()
print(age_list)

#(e) Extend age_list with additional ages
age_list.extend([29, 30, 26])
print(age_list)

#(f) Sort age_list in descending order
age_list.sort(reverse=True)
print(age_list)

#(g) Find maximum, minimum and sum

print("Maximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of ages:", sum(age_list))

#3. Accessing List Elements: 
name_list = ["Jeni", "Anu", "Amal", "Arun", "Meera"]

#(a) Print first element
print(name_list[0])

#(b) Print last element
print(name_list[-1])

#(c) Print elements from index 2 to index 4
print(name_list[2:5])

#(d) Print elements in reverse order
print(name_list[::-1])

#2. Dictionary – Creation, Modification and Access

student_marks = {
    "Jeni": 85,
    "Anu": 90,
    "Amal": 75,
    "Arun": 88,
    "Meera": 95
}

print(student_marks)

#(b) Access and print a specific student's mark
print(student_marks["Jeni"])

#(c) Add a new student Janani with mark 80
student_marks["Janani"] = 80

print(student_marks)

#(d) Update an older student's mark to 82
student_marks["Amal"] = 82

print(student_marks)

#(e) Use keys(), values() and items()
print("Student Names:", student_marks.keys())

print("Student Marks:", student_marks.values())

print("Student Details:", student_marks.items())

#3. Sets – Operations

my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}

print(my_set)

#(b) Attempt to change my_set[4] = 's'

#my_set[4] = 's'

#TypeError: 'set' object does not support item assignment
#Sets are unordered collections. They don't support indexing like lists.

my_set.add('s')
print(my_set)


#(c) Create two sets
set1 = {1, 3, 5, 7, 9}

set2 = {2, 3, 5, 8, 10}

#(d) Find union and intersection

print(set1.union(set2))

print(set1.intersection(set2))

#4. Operators & Conditional Statements (IF, ELIF, ELSE)


score = int(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score! Please enter a score between 0 and 10.")

elif score > 7:
    print("Above Average: Excellent performance! Keep it up.")

elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")

else:
    print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")