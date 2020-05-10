name = input("Введи свое имя, странник:")
print(name + ", Как твои дела? Хочешь сыграть?")
Yes = "Да"
No = "Нет"
answer =input("Ответь только Да или Нет:")
if answer == Yes:
    char_name =input("Придумай имя своего персонажа:")
    char_race = input("Выбери расу. Например орк или эльф:")
    char_class = input("Выбери класс. Это может быть бард, воин или следопыт")
    print("Добро пожаловать в Dungeons & Dragons, " + char_race + " " + char_class + " " + char_name)
else:
    print("Прощай, приятель!")
print(
    int(input
