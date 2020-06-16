# Игра 21(или просто очко)
import random

coloda_cards = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4  # колода карт(4 масти)
random.shuffle(coloda_cards)  # Перемешаваем колоду карт.

# Создаем списки.
comp_card = []  # Список карт компьютера.
player_card = []  # Список карт пользователя.

comp_li = []  # Карты компа для вывода на экран.
player_li = []  # Карты игрокадля вывода на экран.

print("Добро пожаловать в игру 'блэкджек'")

while True:
    new_game = input("Начинаем играть? Y-да,N-нет")
    new_game = new_game.upper()
    if new_game != "Y":
        print("Ошибка.Нераспознанная команда")
        continue
    else:

        """ 
            Выдаем 2 карты пользователю и компьютеру
            показываем их,и их сумму.
        
        """
        while True:
            if len(player_card) < 2 and len(comp_card) < 2:
                random.shuffle(coloda_cards)  # Перемешаваем колоду карт.
                new_card = coloda_cards.pop()
                player_card.append(new_card)

                random.shuffle(coloda_cards)  # Перемешаваем колоду карт.
                new_card_ = coloda_cards.pop()
                comp_card.append(new_card_)
                continue
            else:
                for x in player_card:
                    player_li.append(str(x))
                _li = " ,".join(player_li)
                print("Карты игрока {0} .Сумма {1}".format(_li, sum(player_card)))
                break

        # Выдаем по одной карте пользвателю.
        while True:
            resume = input("Вам нужна ище карта? Y-ДА,N-нет")
            resume = resume.upper()
            if resume == "Y":
                random.shuffle(coloda_cards)  # Перемешаваем колоду карт.
                new_card = coloda_cards.pop()
                player_card.append(new_card)

                player_li.append(str(new_card))
                _li = " ,".join(player_li)
                print("Карты игрока {0} .Сумма {1}".format(_li, sum(player_card)))
                continue
            elif resume == "N":
                break
            else:
                print("Ошибка.Нераспознанная команда")
                continue

        # Выдаем по одной карте компу.
        while True:
            if sum(comp_card) < 19:
                random.shuffle(coloda_cards)  # Перемешаваем колоду карт.
                new_card_ = coloda_cards.pop()
                comp_card.append(new_card_)
                continue
            else:
                break
    for x in comp_card:
        comp_li.append(str(x))
    li_c = " ,".join(comp_li)
    print('Карты компьютера {0} .Сумма {1}'.format(li_c, str(sum(comp_card))))

    #
    if sum(player_card) > 21:
        print("Увы Вы проиграли.")
    elif sum(comp_card) > 21:
        print("Ура Вы выграли.")
    elif sum(player_card) == sum(comp_card):
        print("Ничья")
    elif sum(player_card) < sum(comp_card):
        print("Увы Вы проиграли.")
    else:
        print("Поздравляю Вы выграли.")

    # Очищаем все спискис картами.
    comp_card.clear()
    player_card.clear()
    comp_li.clear()
    player_li.clear()



    break
