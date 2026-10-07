marks=int(input("Enter your marks: "))
attendance=int(input("Enter your attendance: "))
marks_ok=marks>=60
attendance_ok=attendance>=75
print("AND: ", marks_ok and attendance_ok)
print("OR: ", marks_ok or attendance_ok)
print("NOT: ",not marks_ok)