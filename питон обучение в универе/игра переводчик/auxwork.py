from random import randint
def main():
    game_dict = {}

    def load(trdict):
        with open('game_dict.txt', 'r', encoding='utf-8') as gameDict:
            for i in gameDict.readlines():
                key, value = i.strip().split(':')
                trdict[key] = value

    def game(maindict):
        solveddict = list(maindict.keys())
        curWord = randint(0, len(solveddict))
        r = 1
        s = len(solveddict)
        score = 0

        while r != '0' and s!=1:
            print(solveddict[curWord])
            r = str(input('Перевод слова на русский: '))
            if maindict[solveddict[curWord]] == r:
                score += 1
                solveddict.pop(curWord)
                print('Верно! +1 очко!')
                s -= 1
                curWord = randint(0, len(solveddict)-1)
            else:
                score -= 1
                solveddict.pop(curWord)
                curWord = randint(0, len(solveddict)-1)
                print('Неверно! -1 очко!')

        print('Очков набрано: ', score)

    def game_menu(trdict):
        print('Вам будут даваться слова на английском языке. '
              'Ваша задача - написать их перевод на русском. \n'
              'Будьте внимательны - вам необходимо отписывать ответ только строчными буквами!\n'
              'Вы всегда можете завершить игру, вписав 0.\n'
              '1. Начать игру\n'
              '0. Покинуть игру\n')
        ch = int(input())
        if ch == 1:
            game(trdict)

    def dict_show(trdict):
        print(trdict)

    def dict_append(trdict):
        english = str(input('Введите слово на английском: '))
        russian = str(input('Введите его перевод на русском: '))
        new_el = {english:russian}
        trdict.update(new_el)

    def dict_del(trdict):
        key = str(input('Слово на английском для удаления: '))
        trdict.pop(key)

    def dict_clear(trdict):
        trdict.clear()
        with open('game_dict.txt', 'w', encoding='utf-8') as gameDict:
            gameDict.write('')

    def dict_save(trdict):
        with open('game_dict.txt', 'w', encoding='utf-8') as gameDict:
            for key, value in trdict.items():
                gameDict.write(f'{key}:{value}\n')

    def menu():
        ch = 1
        while ch != 0:
            ch = int(input('\nПереводчик\n'
                           '1: Начать игру \n'
                           '2: Просмотреть список словаря \n'
                           '3: Добавить слова в словарь\n'
                           '4: Удалить слова из словаря\n'
                           '5: Очистить словарь\n'
                           '6: Сохранить словарь\n'
                           '0: Закрыть игру\n'))
            if ch == 1:
                game_menu(game_dict)
            if ch == 2:
                dict_show(game_dict)
            if ch == 3:
                dict_append(game_dict)
            if ch == 4:
                dict_del(game_dict)
            if ch == 5:
                dict_clear(game_dict)
            if ch == 6:
                dict_save(game_dict)

    load(game_dict)
    menu()

main()