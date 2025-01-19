#************PROBLEM 1 **************
#Store follwoing word meanings in a python dictionary
#Table: "A piece of furniture", "list of facts & figures" cat: "A small animal" 

wordMeanings = {
    "table": "A piece of furniture", 
    "fact" : "A list of facts & figures",
    "cat" : "a small animal",


}

print(wordMeanings)

# Problem 2

#You are given a list of subjects for the students. Assume one classroom is required for 1 subject. How many classrooms are required for the all students?

"Python", "Python", "Python" "Java", "Java", "C++", "Javascript"

setClass = {"Python", "Python", "Python", "Java", "Java", "C++", "Javascript", "Javascript", "C",}

requiredClassRoom = len(setClass)

print("Required classrooms are: ", requiredClassRoom)

# Problem 3 

# WAP to enter marks of 4 subjects from the user and soter ethem in a dictionary. state with an empty dictionary & add one by one subject name as key and marks as value

myDictionary = {}

firstUserSubject = input("Please enter your first subject name: ")
firstUserSubNumber = input("Please enter your first subject number: ")

SecondUserSubject = input("Please enter your second subject name: ")
SecondUserSubNumber = input("Please enter your second subject number: ")

ThirdUserSubject = input("Please enter your Third subject name: ")
ThirdUserSubNumber = input("Please enter your Third subject number: ")

myDictionary[firstUserSubject] = firstUserSubNumber
myDictionary[SecondUserSubject] = SecondUserSubNumber
myDictionary[ThirdUserSubject] = ThirdUserSubNumber
print(myDictionary)



#Figure out a way to store 9 and 9.0 as separate values in the set. You can take help from built in data types


numbersOfSet = {9, "9.0"}

print(numbersOfSet)