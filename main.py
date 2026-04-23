
# 13. Course
class Course:
    def __init__(self, title, students_count, capacity):
        self.title = title
        self.students_count = students_count
        self.capacity = capacity

    def enroll(self):
        if self.students_count < self.capacity:
            self.students_count += 1
            print("Ro‘yxatdan o‘tdi")
        else:
            print("Joy yo‘q")


co = Course("Python", 2, 3)
co.enroll()
co.enroll()


# 14. FileManager
class FileManager:
    def __init__(self, filename, is_open=False):
        self.filename = filename
        self.is_open = is_open

    def open_file(self):
        if self.is_open:
            print("Allaqachon ochiq")
        else:
            self.is_open = True
            print(f"{self.filename} ochildi")

    def close_file(self):
        self.is_open = False
        print(f"{self.filename} yopildi")


fm = FileManager("file.txt")
fm.open_file()
fm.open_file()
fm.close_file()

