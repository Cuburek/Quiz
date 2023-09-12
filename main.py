print("Добро пожаловать на квиз по играм")
print("Ответь на следующие вопросы:")

questions = ["Создатель STEAM?",
             "Игра про автоматизацию завода?",
             "Как звали главного антагониста в Atomic Heart?",
             "Что ненавидят игроки Far Cry 3 ?",
             "Как зовут последнего Босса Terraria"]

answers = ["Gabe",
           "Factorio",
           "Храз",
           "Towers",
           "Moon Lord"]
score = 0
print(questions[0])
user_answer = input("введите свой ответ: ")
if user_answer.lower() == answers[0].lower():
    score = score + 1
    print("Правильно!")
else:
    print("Неправильно.")

print(questions[1])
user_answer = input("введите свой ответ: ")
if user_answer.lower() == answers[1].lower():
    score = score + 1
    print("Правильно!")
else:
    print("Неправильно.")

print(questions[2])
user_answer = input("введите свой ответ: ")
if user_answer.lower() == answers[2].lower():
    score = score + 1
    print("Правильно!")
else:
    print("Неправильно.")

print(questions[3])
user_answer = input("введите свой ответ: ")
if user_answer.lower() == answers[3].lower():
    score = score + 1
    print("Правильно!")
else:
    print("Неправильно.")

print(questions[4])
user_answer = input("ведите свой ответ: ")
if user_answer.lower() == answers[4].lower():
    score = score + 1
    print("Правильно!")
else:
    print("Неправильно.")
print("Твой результат:", score)