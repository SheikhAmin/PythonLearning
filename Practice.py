import re


def reverse_string(string):
    rev = ""
    for i in range(len(string) - 1, -1, -1):
        rev += string[i]
    return rev


def palindrome(string):
    value = re.sub("[^a-zA-z0-9]", "", string).lower()
    if value == reverse_string(value):
        print("Palindrome")
    else:
        print("Not Palindrome")


def sort(a):
    temp = 0
    for i in range(0, len(a), 1):
        for j in range(i + 1, len(a), 1):
            if a[i] > a[j]:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
    print(a)


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


def find_missing_value(a):
    sum1 = 0
    sum2 = 0
    for i in range(0, len(a), 1):
        sum1 += a[i]
    for i in range(min(a), max(a) + 1, 1):
        sum2 += i
    print(f"Missing value:{sum2 - sum1}")


def find_longest_word(s):
    long_w = ""
    st = s.split()
    for word in st:
        if len(word) > len(long_w):
            long_w = word
    print(f"Longest word:{long_w}")


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
val = "I am Momin"
find_longest_word(val)
