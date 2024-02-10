import re  # Importing the regular expression module

x = open("regex_sum_42.txt")  # Opening the file named "regex_sum_42.txt"
c = 0  # Initializing a variable to store the sum of all numbers found in the file
g = 0  # Initializing a variable to store the total vowel count in the file
j = 0  # Initializing a variable to store the count of occurrences of the word "Python" in the file
num_list = []  # Initializing an empty list to store all numbers found in the file

# Looping through each line in the file
for i in x:
    i = i.rstrip()  # Removing any trailing whitespaces from the current line
    
    if re.search("^Python+", i):  # Searching for lines that start with "Python"
        print(i)  # Printing those lines
        
    a = re.findall(r"\d+", i)  # Finding all numeric substrings in the current line
    for b in a:
        c = c + int(b)  # Adding each numeric substring to the sum
        num_list.append(int(b))  # Appending each numeric substring to the list of numbers
        
    d = re.findall(r"[aeiouAEIOU]+", i)  # Finding all sequences of vowels in the current line
    for e in d:
        for f in e:
            g = g + 1  # Counting each vowel occurrence
            
    h = re.findall("Python", i)  # Finding all occurrences of the word "Python" in the current line
    for i in h:
        j = j + 1  # Counting each occurrence of the word "Python"

# Printing the results
print()
print("The sum of all numbers is", c)
print("The highest number is",max(num_list))
print("The total vowel count is", g)
print("Python word count is", j)
