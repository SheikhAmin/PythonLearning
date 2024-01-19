import copy
import re


def reverse_string(string):
    rev = ""
    for i in range(len(string) - 1, -1, -1):
        rev += string[i]
    return rev


def palindrome(string):
    value = re.sub("[^a-zA-z0-9]", "", string).lower()
    rev = " "
    for i in range(len(string) - 1, -1, -1):
        rev += string[i]
    if value == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")


def sort(ar):
    temp = 0
    for i in range(0, len(ar), 1):
        for j in range(i + 1, len(ar), 1):
            if ar[i] > ar[j]:
                temp = ar[j]
                ar[j] = ar[i]
                ar[i] = temp
    print(ar)


def second_highest(ar):
    max1 = 0
    max2 = 0
    length = 0
    if ar[0] > ar[1]:
        max1 = ar[0]
        max2 = ar[1]
    else:
        max1 = ar[1]
        max2 = ar[0]

    for i in range(2, len(ar), 1):
        if ar[i] > max1:
            max2 = max1
            max1 = ar[i]
        elif max2 < ar[i] < max1:
            max2 = ar[i]
    for i in range(0, len(ar), 1):
        if ar[i] == max2:
            length = i
    print(length)


def fibonacci(lim):
    n1 = 0
    n2 = 1
    total = 0
    print(f"{n1}" + " " + f"{n2}", end=" ")
    for i in range(0, lim - 2, 1):
        total = n1 + n2
        print(f"{total}", end=" ")
        n1 = n2
        n2 = total


def factorial(n):
    total = 1
    for i in range(1, n + 1, 1):
        total = total * i
    print(total)


def duplicate_element_in_array(value):
    flag = False
    for i in range(0, len(value), 1):
        for j in range(i + 1, len(value), 1):
            if value[i] == value[j]:
                print(f"Duplicate found: {value[i]}")
                flag = True
    if not flag:
        print("No Duplicate Found")


def count_the_word():
    print("Enter a Sentence")
    value = input()
    count = 1
    for i in range(0, len(value), 1):
        if value[i] == " " and value[i + 1] != " ":
            count += 1
    print(f"Number of Word:{count}")


def linear_search(ar, ele):
    for i in range(0, len(ar), 1):
        if ar[i] == ele:
            print(f"{ele} found on index {i}")


def find_missing_value(ar):
    sum1 = 0
    sum2 = 0
    for i in range(0, len(ar), 1):
        sum1 += ar[i]
    for i in range(min(ar), max(ar) + 1, 1):
        sum2 += i
    print(f"Missing value:{sum2 - sum1}")


def find_longest_word(s):
    long_w = ""
    st = s.split()
    for word in st:
        if len(word) > len(long_w):
            long_w = word
    print(f"Longest word:{long_w}")


def binary_search(ar, val):
    ar.sort()
    low = 0
    high = len(ar) - 1
    flag = False

    while low <= high:
        m = int((low + high) / 2)
        if ar[m] == val:
            print("element found")
            flag = True
            break
        if val > ar[m]:
            low = m + 1
        if val < ar[m]:
            high = m - 1
    if not flag:
        print("element not found")


def prime_number(num):
    count = 0
    if num > 1:
        for i in range(1, num + 1, 1):
            if num % i == 0:
                count += 1
        if count == 2:
            print("prime number")
        else:
            print("not a prime number")
    else:
        print("not a prime number")


def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(arr, left, right)


def merge(arr, l, r):
    i = 0  # for left array
    j = 0  # for right array
    k = 0  # merged array
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            arr[k] = l[i]
            k += 1
            i += 1
        else:
            arr[k] = r[j]
            k += 1
            j += 1
    while i < len(l):
        arr[k] = l[i]
        k += 1
        i += 1
    while j < len(r):
        arr[k] = r[j]
        k += 1
        j += 1


# print("Enter a String")
# inputStr = input()
# print(reverseString(inputStr))
# arr = [500,21,10,11,1,0,27,77,13]
# palindrome(inputStr)
# sort(arr)
# secondHighest(arr)
# fibonacci(10)
# factorial(5)
# array = ["java","c","c++","java","python","python"]
# duplicateElementInArray(array)
# countTheWord()
# linearSearch(arr,27)
# ar = [2,4,5,1]
# findMissingValue(ar)
# val = "I am Moin"
# find_longest_word(val)
# binary_search(ar,4)
# prime_number(2)
# a = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(a)
# print(a)

                                                              # Apna College Python Course

# Taking Input from user
name = input("What is your name? => ")
print("Hello " + name)
old_age = input("Enter you old age: ")
new_age = int(old_age) + 2
print(new_age)
print(float(new_age))
print(name.lower())
print(name.upper())
# String Manipulation
print(name.find('n'))  # .find() returns index number
print(name.replace("n", "m"))  # .replace() changes a given char to another char
# Keywords
print("min" in name)
# Arithmetic Operator
print(5 // 2)  # point value bad diye dey
print(5 ** 2)  # means 5^2
print(5 % 2)  # remainder
print((2 + 3) * 8)
# List. Denotes by {}
marks = [95, 96, 97, "Bangla"]
print(marks)
print(marks[0:2])
for score in marks:
    print(score)
marks.append(99)
print(marks)
marks.insert(1, 85)
print(marks)
print(99 in marks)
print(len(marks))
# continue
for score in marks:
    if score == "Bangla":
        continue
    print(score)
# Tuple. It is like List but it is immutable. Denotes by (). Also, can be denoted by another approach. Follow 1
marks = (95, 98, 97, 100, 97, 98)
print(marks.count(97))
print(marks.index(98))
mark = "amin", "momin"
print(mark)
# Set is denote by {}. Stores unique value. It doesn't have index. So unordered
marks = {95, 98, 97, 100, 97, 98}
print(marks)
# Dictionary. Stores value as Key and value. Almost like JS object. Denotes by {}
score = {"english": 70, "math": 85, "social_science": 88}
print(score["math"])
score["physics"] = 80  # adding value or can change value to the dictionary
print(score)
