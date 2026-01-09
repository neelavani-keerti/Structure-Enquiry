def calculate_library_fine(student_name, book_name, days_late):
    if days_late <= 5:
        fine = days_late * 2
    elif days_late <= 10:
        fine = days_late * 5
    else:
        fine = days_late * 10

    print("Student Name :", student_name)
    print("Book Name    :", book_name)
    print("Days Late    :", days_late)
    print("Total Fine   : ₹", fine)


if __name__ == "__main__":
    student_name = input("Enter student name: ")
    book_name = input("Enter book name: ")
    days_late = int(input("Enter days late: "))

    calculate_library_fine(student_name, book_name, days_late)
