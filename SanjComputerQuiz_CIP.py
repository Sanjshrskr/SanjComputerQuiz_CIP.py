#cip project
def main():
    print("Welcome to my computer quiz!")


playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
print("Answers should be in lowercase!")
print("")
score = 0

print("Question 1")
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Q2
print("Question 2")
answer = input("The smallest unit of data in a computer is ___")
if answer.lower() == "bit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Q3
print("Question 3")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Q4
print("Question 4")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Q5
print("Question 5")
answer = input("Where is RAM located? ")
if answer.lower() == "mother board":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Q6
print("Question 6")
answer = input("What is a websites main page called? ")
if answer.lower() == "homepage":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Q7
print("Question 7")
answer = input("What does URL stand for? ")
if answer.lower() == "uniform resource locator":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Q8
print("Question 8")
answer = input("What does BIOS stand for? ")
if answer.lower() == "basic input output system":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Q9
print("Question 9")
answer = input("What does HTTP stand for? ")
if answer.lower() == "hyper text transfer protocol":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Q10
print("Question 10")
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# score
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%.")
# thanks for playing
print("Thanks for playing!!")

if __name__ == "__main__":
    main()

