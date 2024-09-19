questions = ("1.Ile elementów znajduje sie w układzie okresowym pierwiastków?",
             "2.Które ze zwierzat znosi najwieksze jaja?",
             "3.Jaki jest najliczniejszy gaz w atmosferze ziemskiej?",
             "4.Jak wiele kosci jest w ludzkim ciele?",
             "5.która planeta w układzie słonecznym jest najgorętsza ?")
options = (("A.116","B.117","C.118","D.119"),
           ("A.Wieloryb","B.Krokodyl","C.Słoń","D.Struś"),
           ("A.Azot","B.Tlen","C.Dwutlenek-Węgla","D.Wodór"),
           ("A.206","B.207","C.208","D.209"),
           ("A.Merkury ","B.Wenus","C.Ziemia","D.Mars"),)
answers = ("C","D","A","A","B")
guesses = []
score = 0
questions_num = 0
for question in questions:
    print("------------------")
    print(question)
    for option in options[questions_num]:
        print(option)
    quess = input("Wprowadz (A,B,C,D):").upper()
    guesses.append(quess)
    if quess == answers[questions_num]:
        score +=1
        print("Correct")
    else:
        print("INCORRECT")
        print(f"{answers[questions_num]} is the correct answer")

    questions_num += 1
print("------------------")
print("  Wynik  ")
print("------------------")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for quess in guesses:
    print(quess, end = " ")
print()

score = int(score/len(questions)* 100)
print(f"Twój wynik to : {score}%")