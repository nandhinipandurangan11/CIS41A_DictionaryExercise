# CIS 41A: Dictionary Exercise: Nandhini Pandurangan

# Using lab3, replace the list with a dictionary.
# Sorting is not necessary. However, if you want to try sorting, import the OrderedDict.

import csv


# Student class contains 2 strings: the first and last name of the student
class Student:

    # constructor
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # defines how print() is used on Student objects
    def __str__(self):
        return self.first_name + " " + self.last_name

    # overloading the less than < operator to allow for comparison between student last names
    def __lt__(self, right):
        return self.last_name < right.last_name


class Course:

    # constructor
    def __init__(self):
        self.list_students = {}  # dictionary

    # reader() reads the csv file
    def reader(self, csvfile):

        k = 1  # each student is assigned a number which will be used as the key for the dictionary

        for line in csv.reader(open(csvfile)):  # iterating through file contents
            st = Student(line[0], line[1])  # calls the Student constructor using the elements of line
            self.list_students[k] = st  # storing the student object in the dictionary of students
            k += 1  # incrementing key value by 1

    # output_list() outputs the list of students in the course
    def output_list(self):
        print()
        print("---  List of students in this course:  ---")
        for i in range(1, len(self.list_students.values()) + 1):
            print(self.list_students[i])


# main() creates a Course object
def main():
    c = Course()
    c.reader("Students.txt")  # passing a csv file to reader()
    c.output_list()


# calling main()
main()
