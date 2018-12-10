import random

fd = open("Words", "r")
random = random.randint(0, 9)
temp_solution = ""
solution = list()
progress = list()
view_progress = list()
lives = 6
wrong_letters = ""

index = 0
for line in fd:
    if index == random:
        temp_solution = line
    index += 1

for i in range(len(temp_solution)-1):
    if temp_solution[i] == " ":
        view_progress.append(" ")
    else:
        view_progress.append("_")
        progress.append("")
        solution.append(temp_solution[i])

print(view_progress)
print()
while True:
    letter = input("Please enter a letter: ")
    index_with_space = 0
    index = 0
    correct = False
    for character in solution:
        if temp_solution[index_with_space] == " ":
            index_with_space += 1
        if character == letter:
            view_progress[index_with_space] = letter
            progress[index] = letter
            correct = True
        index_with_space += 1
        index += 1
    if correct:
        print()
        print(view_progress)
        print()
        if progress == solution:
            print("YOU WON!")
            break
    else:
        lives -= 1
        if lives == 0:
            print()
            print("YOU HANGED THE MAN GAME OVER")
            print()
            print("The real word was", solution)
            break
        else:
            wrong_letters += letter + " "
            print()
            print("WRONG. You have", lives, "attempts...")
            print("Wrong letters:", wrong_letters)
            print()
            print(view_progress)
            print()