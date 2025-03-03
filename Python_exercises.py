""""#Simple print
print("Sachin")

#Defining variable
price = 10
price = 2
print(price) # note that python goes line by line

#
price = 10
rating = 4.9 #this is a float
name = "Sachin"
is_published = False #python is case sensitive, this is a boolean example
print(price) #no quotaion as it is printing a variable and not a string

#Assignment 1
name = "John smith"
age = 20
is_new = True

#Receiving input, input are functions built into python.
name = input("What is your name? ")
print("Hi " + name)

#Assignment
name = input("What is your name? ")
colour = input("What is your favourite colour? ")
print(name + " " + "likes" +" " + colour)

birth_year = input("Birth year : ")
print_(type(age))
age = 2019 - int(birth_year)
print(type(age))
print(age)
#int(), float(),bool()

#Assignment
weight = input("What is you weight? ")
convertion = int(weight)*2
print(convertion)

course = "python for beginners"
print(course[-1]) # Square bracket gives the position from first letter as 0 and -1 will be s here

first = "John"
last = "Smith"
message = first + '[' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(msg.upper())
print(msg.replace("J","X"))
.upper(), .lower(), title(), .find(),.replace() #  These are methods for functions

#Augmented operators
x = 10
x = x + 3
x+=3
print(x)

#If statements

is_hot = False
is_cold = False
if is_hot :
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("Enjoy your day")

#If statement Assignment
House_price = 1000000
GC = str(int(House_price*0.1))
BC = str(int(House_price*0.2))

Good_credit = False

if Good_credit:
    print("You must pay a down payment of " + GC)
else:
    print("You must pay a down payment of " + BC)

#logical operators are or,and and not
#boolean operators

temperature = 2

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

#Assignment

name = input("What is your name :")
name_character_count = len(name)

if name_character_count < 3:
    print("Name must be at least 3 characters long")
elif name_character_count >50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")

#Assignment

Weight_input = input("Weight:")
Type = input("(L)bs or (K)g :")
Weight_input = int(Weight_input)

if Type.upper() == "L":
    converted = Weight_input*0.5
    print(f"You are  {converted}  lbs")
else:
    converted = Weight_input*2
    print(f"You are {converted} pounds")

#Assignment

Entry_help = "help"
Start_car = "start"
Stop_car = "stop"
Quit = "quit"

while True:
    prompt = input(">").lower()

    if prompt == Entry_help:
        print(
#start - to start the car
#stop - to stop the car
#quit - to exit
    )
    elif prompt == Start_car:
        print("Car started... Ready to go!")
    elif prompt == Stop_car:
        print("Car stopped")
    elif prompt == Quit:
        print("Goodbye!")
        break
    else:
        print("I don't understand that")
""""""

#While loops

i = 1
while i<=5:
    print("*"*i)
    i = i+1
print("Done")

#Example
secret_number = 9
Guess_count = 0
Guess_limit = 3
while Guess_count < Guess_limit:
    guess = int(input("Guess : "))
    Guess_count += 1
    if guess == secret_number:
        print("You've won")
        break
else:   #this is only run if the while loop is completed.
    print("Sorry, you failed")
"""
####################
#For loops
"""
for item in range(5, 10, 5):
    print(item)
"""
#Assignment
""""
prices = [10,20,30]
total = 0

for i in prices:
    total+=i
print(f"total:{total}")"""

#Nested loops
""""
numbers = [5,2,5,2,2]
letter = "X"

for i in numbers:
    for y in letter:
        print(y*i)"""

# Or another way
"""
numbers = [1,1,1,1,5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output+='x'
    print(output)
"""
"""
names = ['john','bob', 'mosh','sarah','mary']
print(names[])


numbers = [1,3,111]
print(max(numbers))
"""
#2D lists
"""
numbers = [1,2,3,4,1,1]
uniques = []
for x in numbers:
    if x not in uniques:
        uniques.append(numbers)
print(uniques)
"""
# Tuples are like lists but immutable
#Unpacking is a powerful tool we can use with tuples.
"""
coordinates = (1,2,3)
x,y,z = coordinates
print(x)

#Each key should be unqiue in a dictionary

Phone_number = input("Phone :")
Numbers = {
    "1":"One",
    "2":'Two',
    "3": "Three",
    "4":"Four"
}
Output = ""
for x in Phone_number:
    Output += Numbers.get(x,"!") + " "
print(Output)

message = input(">")
words = message.split(' ')
emojis = {
    ":)":"😊",
    ":(":"😒"
}
output = ""
for words in words:
    emojis.get(words,words)
    output+=emojis.get(words,words)
print(output)

#Function is a container for a few lines of code that perform a specific task.
def greet_user ():
    print("Hi there!")
    print("Welcome abroad")


print("Start")
greet_user()
print("Finish")

#Passing info to the function
def greet_user (first_name,last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome abroad")


print("Start")
greet_user("John","Drury")
#calc_cost(total=50,shipping=5,discount=0.1) # use key word arguments to make it clear. Always use positional arguments first and THEN keyword arguments.
print("Finish")

#Return values

def square(number):
    print(number*number)
    return (number)
square(3)

#Assignment - Emoticon generator

def icon_generator (message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😒"
    }
    output = ""
    for words in words:
        output += emojis.get(words, words) + " "
    return output


message = input(">")
result = icon_generator(message)
print(result)

#Exception

try:
    age = int(input("Age:"))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print("Invalid value")

#Classes are used to define new types. Classes are capitolised and instead of an underscore, use the capitol first letter (Don't leave a space).

class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1=Point()
#Point.draw()
point1.x=10
point1.y=20
print(Point1.x)"""

# Look more into constructors and classes

"""def get_protein_length(protein_sequence):
    amino_acids = AA_Sequence.split()
    length = len(amino_acids)
    return length

AA_Sequence = input("Enter the 3 letter amino acid code:")
length = get_protein_length(AA_Sequence)
print(f"The length of the protein is: {length}")"""

"""a = int(input("Please enter the value for a: "))
triangle = int(((2*a)*(a))/2)
circle = float(3.14*(a*a))
shaded_area = triangle-circle
print(shaded_area)

Codon_mapping = {
    'UUU': 'F', 'UUC': 'F',
    'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA' : 'S', 'UCG' : 'S',
    'UAU': 'Y', 'UAC': 'Y',
    'UAA': 'Stop', 'UAG': 'Stop',
    'UGU': 'C', 'UGC': 'C',
    'UGA': 'Stop', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L','CUA': 'L','CUG': 'L',
    'CCU': 'P', 'CCC': 'P','CCA': 'P','CCG': 'P',
    'CAU': 'H', 'CAC': 'H',
    'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R','CGA': 'R','CGG': 'R',
    'AUU': 'I', 'AUC': 'I','AUA': 'I',
    'AUG': 'M',
    'ACU': 'T', 'ACC': 'T','ACA': 'T','ACG': 'T',
    'AAU': 'N', 'AAC': 'N',
    'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S',
    'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V','GUA': 'V','GUG': 'V',
    'GCU': 'A', 'GCC': 'A','GCA': 'A','GCG': 'A',
    'GAU': 'D', 'GAC': 'D',
    'GAG': 'E','GAA': 'E',
    'GGU': 'G', 'GGC': 'G','GGA': 'G', 'GGG': 'G',
}

result = ""
RNA_String = input("Please enter the RNA string:")
Seperate = [RNA_String[i:i+3] for i in range(0, len(RNA_String), 3)]
print(Seperate)

if len(RNA_String) % 3 != 0:
    print("Error: RNA string length must be a multiple of 3.")
else:
    result = ""

for Letter in Seperate:
    if Letter in Codon_mapping:
        result+= "".join(Codon_mapping[Letter])
    elif Letter not in Codon_mapping:
        print("Please re-check the input string")
        break
print(result)


### counting the number of DNA nucleotides in a string
###Method 1

DNA_String = str(input("Please enter the DNA string : "))
count_A = DNA_String.count("A")
count_C = DNA_String.count("C")
count_G = DNA_String.count("G")
count_T = DNA_String.count("T")

print(count_A, count_C, count_T, count_G)

### Method 2

DNA_String = str(input("Please enter the DNA string : "))

Count_A = 0
Count_T = 0
Count_C = 0
Count_G = 0
for letter in DNA_String:
    if letter == "A":
        Count_A += 1
    elif letter == "T":
        Count_T += 1
    elif letter == "C":
        Count_C += 1
    elif letter == "G":
        Count_G += 1
print(Count_A, Count_T, Count_G, Count_C)

### Return a sequence of numbers, starting at 3, up to (and including, if appropriate), the argument last_number
        
        Example use: generate_number_list()
        Example output: 3 6 9 12 15 18 21
        Example use: generate_number_list(25)
        Example output: 3 6 9 12 15 18 21 24###

def generate_number_list(last_number: int = 30) -> list[int]:
    return list(range(3, last_number + 1, 3))
print(generate_number_list())

#Write a function that returns lines in a sequence, sorted in lexicographical order.
try:
    with open(r"C:\Users\Sachin\Desktop\GOSH\multi_seqs.txt", "r") as file:
        sequences = file.read().splitlines()
    sorted_sequences = sorted(sequences)
    print(sorted_sequences)
except FileNotFoundError:
    print("Error: File not found.")"""

