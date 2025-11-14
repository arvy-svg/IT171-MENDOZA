player_arvy = 0
player_abby = 0
treasure_x = 1
treasure_y = 3
game_running = True
print("Welcome to Mendoza's Maze")
print(f"Find the treasure at ({treasure_x}, {treasure_y})!")
while game_running:
    move = input("Enter move (w = up/s = down/a = left/d = right): ")
   
    if move == "d":
        player_arvy += 1
    if move == "a":
        player_arvy-= 1
    if move == "w":
        player_abby += 1
    if move == "s":
        player_abby -= 1

    print(f"Player position: ({player_arvy}, {player_abby})")
    if player_arvy == treasure_x and player_abby == treasure_y:
        print("You've reached your destination")
        break
    if move == "q":
        print("You have exit the game")
        break
