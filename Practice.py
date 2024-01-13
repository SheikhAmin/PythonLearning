import re
def reverseString(String):
    rev =""
    for i in range(len(String)-1,-1,-1):
        rev +=String[i]
    return rev

def palindrome(String):
    value = re.sub("[^a-zA-z0-9]","",String).lower()
    if value == reverseString(value):
        print("Palindrome")
    else:
        print("Not Palindrome")

def sort(a):
    temp = 0
    for i in range(0,len(a),1):
        for j in range(i+1,len(a),1):
            if a[i] > a[j]:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
    print(a)

def secondHighest(ar):
    max1=0
    max2=0
    length=0
    if(ar[0]>ar[1]):
        max1=ar[0]
        max2=ar[1]
    else:
        max1=ar[1]
        max2=ar[0]

    for i in range(2,len(ar),1):
        if ar[i] > max1:
            max2=max1
            max1=ar[i]
        elif (ar[i] > max2 and ar[i] < max1):
            max2=ar[i]
    for i in range(0, len(ar),1):
        if ar[i] == max2:
            length = i
    print(length)

def fibonacci(lim):
    n1=0
    n2=1
    sum=0
    print(f"{n1}" + " " + f"{n2}", end=" ")
    for i in range(0,lim-2,1):
        sum=n1+n2
        print(f"{sum}", end=" ")
        n1=n2
        n2=sum

def factorial(n):
    sum=1
    for i in range(1,n+1,1):
        sum =sum*i
    print(sum)

def duplicateElementInArray(val):
    flag = False
    for i in range(0,len(val),1):
        for j in range(i+1,len(val),1):
            if val[i] == val[j]:
                print(f"Duplicate found: {val[i]}")
                flag = True
    if flag == False:
        print("No Duplicate Found")

def countTheWord():
    print("Enter a Sentence")
    val = input()
    count =1
    for i in range(0,len(val),1):
        if val[i] == " " and val[i+1] !=" ":
            count+=1
    print(f"Number of Word:{count}")

def linearSearch(ar,ele):
    for i in range(0,len(ar),1):
        if ar[i] == ele:
            print(f"{ele} found on index {i}")

def findMissingValue(a):
    sum1=0
    sum2=0
    for i in range(0,len(a),1):
        sum1 +=a[i]
    for i in range(min(a),max(a)+1,1):
        sum2 +=i
    print(f"Missing value:{sum2-sum1}")

def finlongestWord(s):
    longW=""
    st = s.split()
    for word in st:
        if len(word) > len(longW):
            longW= word
    print(f"Longest word:{longW}")


#print("Enter a String")
#inputStr = input()
#print(reverseString(inputStr))
#arr = [500,21,10,11,1,0,27,77,13]
#palindrome(inputStr)
#sort(arr)
#secondHighest(arr)
#fibonacci(10)
#factorial(5)
#array = ["java","c","c++","java","python","python"]
#duplicateElementInArray(array)
#countTheWord()
#linearSearch(arr,27)
#ar = [2,4,5,1]
#findMissingValue(ar)
val = "I am Momin"
finlongestWord(val)


