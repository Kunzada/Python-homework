pole = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
while True:
    while True:
        if ((pole[0][0] == pole[0][1] == pole[0][2] == "O") or \
                    (pole[1][0] == pole[1][1] == pole[1][2] == "O") or \
                    (pole[2][0] == pole[2][1] == pole[2][2] == "O") or \
                    (pole[0][0] == pole[1][0] == pole[2][0] == "O") or \
                    (pole[0][1] == pole[1][1] == pole[2][1] == "O") or \
                    (pole[0][2] == pole[1][2] == pole[2][2] == "O") or \
                    (pole[0][0] == pole[1][1] == pole[2][2] == "O") or \
                    (pole[0][2] == pole[1][1] == pole[2][0] == "O")):
                        
                        break
        if (pole[0][0] == pole[0][1] == pole[0][2] == "X") or \
                (pole[1][0] == pole[1][1] == pole[1][2] == "X") or \
                (pole[2][0] == pole[2][1] == pole[2][2] == "X") or \
                (pole[0][0] == pole[1][0] == pole[2][0] == "X") or \
                (pole[0][1] == pole[1][1] == pole[2][1] == "X") or \
                (pole[0][2] == pole[1][2] == pole[2][2] == "X") or \
                (pole[0][0] == pole[1][1] == pole[2][2] == "X") or \
                (pole[0][2] == pole[1][1] == pole[2][0] == "X"):
                    
                    break
        if all(all(cell != " " for cell in row) for row in pole):
            print("Ничья!")
            break
        else:
           
            
            while True:
                if ((pole[0][0] == pole[0][1] == pole[0][2] == "O") or \
                    (pole[1][0] == pole[1][1] == pole[1][2] == "O") or \
                    (pole[2][0] == pole[2][1] == pole[2][2] == "O") or \
                    (pole[0][0] == pole[1][0] == pole[2][0] == "O") or \
                    (pole[0][1] == pole[1][1] == pole[2][1] == "O") or \
                    (pole[0][2] == pole[1][2] == pole[2][2] == "O") or \
                    (pole[0][0] == pole[1][1] == pole[2][2] == "O") or \
                    (pole[0][2] == pole[1][1] == pole[2][0] == "O")):
                        print("O выиграл")
                        break
                firstPlayer = input("Введите свой ход:(1-3) X: ")
                if firstPlayer.isdigit() and len(firstPlayer) == 2:
                    row = int(firstPlayer[0]) - 1
                    col = int(firstPlayer[1]) - 1

                    if 0 <= row < 3 and 0 <= col < 3:
                        print("Вы выбрали строку:", firstPlayer)
                        if pole[row][col] != " ":
                            print("Данное поле занято")
                        else:
                            pole[row][col] = "X"
                            for p in pole:
                                print(p)
                            break
                    else:
                        print("Некорректный ввод. Введите числа от 1 до 3 для строки и столбца.")
                else:
                    print("Некорректный ввод. Пример: 11")

            while True: 
                if (pole[0][0] == pole[0][1] == pole[0][2] == "X") or \
                (pole[1][0] == pole[1][1] == pole[1][2] == "X") or \
                (pole[2][0] == pole[2][1] == pole[2][2] == "X") or \
                (pole[0][0] == pole[1][0] == pole[2][0] == "X") or \
                (pole[0][1] == pole[1][1] == pole[2][1] == "X") or \
                (pole[0][2] == pole[1][2] == pole[2][2] == "X") or \
                (pole[0][0] == pole[1][1] == pole[2][2] == "X") or \
                (pole[0][2] == pole[1][1] == pole[2][0] == "X"):
                    print("X выиграл")
                    break
                    
                secondPlayer = input("Введите свой ход:(1-3) O: ")
                if secondPlayer.isdigit() and len(secondPlayer) == 2:
                    row = int(secondPlayer[0]) - 1
                    col = int(secondPlayer[1]) - 1

                    if 0 <= row < 3 and 0 <= col < 3:
                        print("Вы выбрали строку:", secondPlayer)
                        if pole[row][col] != " ":
                            print("Данное поле занято")
                        else:
                            pole[row][col] = "O"
                            for p in pole:
                                print(p)
                            break
                    else:
                        print("Некорректный ввод. Введите числа от 1 до 3 для строки и столбца.")
                else:
                    print("Некорректный ввод. Пример: 11")

    play_again = input("Хотите сыграть еще раз? (да/нет): ")
    if play_again.lower() != "да":
        break
    else:
        pole=[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        
