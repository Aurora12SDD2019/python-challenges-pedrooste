""" Python code including all functions for the 20 excersizes
- see this link: https://www.w3resource.com/python-exercises/python-functions-exercises.php
"""

__author__ = "Pedro Oste"
__license__ = "GPL"
__version__ = "1.0.2"
__email__ = "Pedro.oste@education.nsw.com.au"
__status__ = "Alpha"

list = [1,4,5,4,9] #list of numbers
number = 6 #single number
rangeofN = [0,12] #range to check between
string = "Pedro Is Rad"
def maximum(list):
    '''finds the maximum and and the index'''
    i = 1
    max = list[0]
    while i < len(list):
        if max < list[i]:
            max = list[i]
            break
        i +=1
    print(max,i)
    return max,i

def sum(list):
    '''finds the total sum of the list'''
    i = 0
    total = 0
    while i < len(list):
        total += list[i]
        i +=1
    print(total)
    return total

def reverse(list):
    '''reverses all contentents within a list'''
    first = 0
    last = len(list)-1
    print("before "+str(list))
    while first < last:
        temp = list[last]
        list[last] = list[first]
        list[first] = temp
        first +=1
        last -=1
    print("after "+str(list))
    return list

def multiply(list):
    '''multiplys all contents within a list'''
    i = 0
    total = 1
    while i < len(list):
        print(i)
        total = total*list[i]
        i +=1
    print(total)
    return total

def factorial(number):
    '''finds the factorial of a number (n!), extra: also does negative numbers'''
    total = 1
    if number < 0:
        number = number*-1
        total = -1
        
    while number > 0:
        total = total*number
        number -=1
    print(total)
    return total

def checkRange(number,range):
    ''' checks whether a given number is within the given range'''
    inRange = False
    if number >= range[0]:
        if number <= range[1]:
            inRange = True
    print(inRange)
    return inRange

def checkUpperLower(string):
    '''Checks how many upper and lower case characters within a string, had a brain fart with this one'''
    upperCount = 0
    lowerCount = 0
    for character in string:
        if character.isupper():
            upperCount +=1
        if character.islower():
            lowerCount +=1
    print('Upper count: '+str(upperCount))
    print('lower count: '+str(lowerCount))
    return upperCount,lowerCount

def uniqueList(list):
    '''removes any repeated varaibles within a list'''
    uniqueList = []
    for i in list:
        if i in uniqueList:
            pass
        else:
            uniqueList.append(i)
            
    print(list)
    print(uniqueList)
    return uniqueList

def checkPrime(number):
    ''' checks wether a number is prime or not'''
    if number == 1:
        prime = True
    elif number == 2:
        prime = True
    else:
        for i in range(2,number):
            if number % i == 0:
                prime = False
                break
            else:
                prime = True
    print(number)
    print('prime is '+ str(prime))
    return prime

def printEven(list):
    i = 0
    while i < len(list):
        if list[i] % 2 == 0:
            print(str(list[i])+ " is even at index " + str(i))
        i +=1

def checkPerfect(number):
    ''' Checks whether the number is perfect or not
    this includes checking if the divisors of the number adds to the number'''
    divisors = []
    for i in range(1,number): #note that this wont include 6
        if number % i == 0:
            divisors.append(i)
    total = sum(divisors) 
    if total == number:
        perfect = True
    else:
        perfect = False
    print('Is ' + str(number) + " perfect : " + str(perfect))
    return perfect

def checkPalindrome(string):
    '''checks whether a string is palindrome, a palindrome is a string that reads backwards'''
    first = 0
    last = len(string)-1
    while first < last:
        if string[first] == string[last]:
            palindrome = True
        else:
            palindrome = False
            break
        first +=1
        last -=1
    print('is '+string+' a palindrome : '+str(palindrome))
    return palindrome  
