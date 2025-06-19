questions=("what is the capital of Tamil Nadu",
           "which of the dynasties did not rule tamil nadu",
           "which of the languages is the official language of Tamil Nadu",
           "where is the brihadeeshwar temple located",
           "which city is known as 'the city that never sleeps?'")
options=(("Trichy","Salem","Madurai","Chennai"),
         ("Cholas","Cheras","Pandyas","Axomiya"),
         ("Telegu","Tulu","Malay","Tamil"),
         ("Tanjore","Kanchi","Karur","Avadi"),
         ("Madurai","Chennai","Tirupur","Neyveli"))

answers=("Chennai","Axomiya","Tamil","Tanjore","Madurai")
guesses=[]
score=0
qnum=0
qunum=0
for q in questions:
    print("-----------------------")
    print(q)
    for option in options[qnum]:
        print(option)

    qnum=qnum+1
    guess=input("Enter your answer")
    guesses.append(guess)

for answer in answers:
    for guess in guesses:
        if answer==guess:
            score+=1
print(f"you scored {score}")
