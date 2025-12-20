print("Welcome to 5 point quiz!")

score = 0
Quiz = {
    "world's largest country": 'Russia',
    "the most used language" : 'English',
    "What is the name of the largest ocean on Earth?" : 'Pacific',
    "What is the chemical symbol for gold?" : 'Au',
    "What year did the Berlin Wall fall?" : "1989"
}

for question, answer in Quiz.items():
    n = input("Give the answer for " + question + ": ")
    if answer.lower() == n.lower():
        score = score + 1
    else:
        print("Nice try")
        
print(f"Nice, you are awesome , you got a score {score}")
    