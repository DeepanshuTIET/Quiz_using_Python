print("Welcome to my python quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("How do you create a virtual environment in Python? (Consider the name of the virtual environment as 'myenv') ")
if answer.lower() == "python -m venv myenv" or answer.lower() == "virtualenv myenv":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How do you install packages from a requirements file? ")
if answer.lower() == "pip install -r requirements.txt":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How do you import a specific function from a module? ")
if answer.lower() == "from module import function":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How do you sort a list in ascending order? ")
if answer.lower() == "list.sort()":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Name the most famous module that is used to fetch stock data in Python. ")
if answer.lower() == "yfinance" or answer.lower() == "yahoo finance":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%")