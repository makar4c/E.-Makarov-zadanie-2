def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i*3)+3]))
        if i < 2:
            print("-" * 9)
    print("\n")

def check_winner(board):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    
    if " " not in board:
        return "Ничья"
    
    return None

def tic_tac_toe():
    print("Добро пожаловать в игру Крестики-Нолики!")
    print("Чтобы сделать ход, введите число от 1 до 9")
    print("Поле нумеруется так:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 \n")
    
    board = [" "] * 9
    current_player = "X"
    game_over = False
    
    while not game_over:
        print_board(board)
        
        while True:
            try:
                move = int(input(f"Игрок {current_player}, ваш ход (1-9): "))
                if 1 <= move <= 9:
                    if board[move-1] == " ":
                        board[move-1] = current_player
                        break
                    else:
                        print("Эта клетка уже занята!")
                else:
                    print("Введите число от 1 до 9!")
            except ValueError:
                print("Пожалуйста, введите число!")
        
        result = check_winner(board)
        
        if result:
            print_board(board)
            if result == "Ничья":
                print("Ничья! Игра окончена.")
            else:
                print(f"Игрок {result} победил! Поздравляем!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"
    
    play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
    if play_again in ["да", "yes", "y", "д"]:
        tic_tac_toe()
    else:
        print("Спасибо за игру!")

if __name__ == "__main__":
    tic_tac_toe()
