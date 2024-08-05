from random import choice
from time import sleep
from playsound import playsound


letters = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж",
           "З", "И", "Й", "К", "Л", "М", "Н", "О",
           "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц",
           "Ч", "Ш", "Щ", "Э", "Ю", "Я"]
gone = []
players = []
players_words = []
players_letters = []
n_round = 1


def play():
    global letters, players, players_words, players_letters
    for n_player in range(len(players)):
        current_letter = choice(letters)
        players_letters[n_player] += current_letter + ", "
        letters.remove(current_letter)
        print(f"\nИгрок: {players[n_player]}. Буква: {current_letter}")
        sleep(30)
        print("Стоп, время закончилось!")
        playsound('C:/Users/ezuba/Documents/Hobby programms/TableTimeImpro/na_bukvu/budilnik/1.mp3')
        players_words[n_player] += int(input("Сколько слов получилось: "))


def goodbye():
    global players, players_words, players_letters
    for i in range(len(players)-1):
        for j in range(len(players)-i-1):
            if players_words[j] < players_words[j+1]:
                players[j], players[j+1] = players[j+1], players[j]
                players_words[j], players_words[j + 1] = players_words[j + 1], players_words[j]
                players_letters[j], players_letters[j + 1] = players_letters[j + 1], players_letters[j]
    print("Игра окончена, букв осталось меньше чем игроков.")
    print("Спасибо за игру! Вот отсортированный список игроков по количеству слов:")
    for n in range(len(players)):
        print(f"{n+1}. {players[n]} - {players_words[n]}. Буквы: {players_letters[n][:-2]}")


def main():
    global n_round, players, players_words, letters, players_letters
    print("""Приветствую!
Эта программа создана по мотивам игры \"На букву\" от Сергея Борисовича Матвиенко из седьмой серии третьего сезона сериала Тейбл Тайм.
Правила просты: выбирается буква русского алфавита (любая кроме \"Ъ\", \"Ы\" и \"Ь\") случайным образом.
Игроку даётся 30 секунд, за это время игрок должен назвать как можно больше слов на данную букву. После этого
буква выбывает из списка (её нельзя будет выбить повторно). Игра заканчивается, когда букв остаётся меньше чем игроков.
Перед началом каждого раунда есть возможность завершить игру досрочно. Удачной игры!\n""")
    players = [i for i in input("Введите имена игроков разделяя их \", \": ").split(", ")]
    players_words = [0] * len(players)
    players_letters = [""] * len(players)
    while len(letters) >= len(players):
        quit_or_not = input(f"\nРаунд {n_round}. Если хотите закончить, напишите \"q\", иначе нажмите Enter ")
        if quit_or_not == "q":
            goodbye()
            return 0
        else:
            play()
            n_round += 1
    goodbye()


if __name__ == '__main__':
    main()
