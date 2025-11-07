 player_x = 0
 player_y = 0
 treasure_x = 5
 treasure_y = 3
 game_running = True
 print(f"Find the treasure at ({treasure_x}, {treasure_y})!")
 while game_running:
 move = input("Enter move (up/down/left/right): ")
 # TODO: update player_x and player_y based on move
   while game_running:
     input("Move Here (up/down/left/right): ")\
     if move == "right":
     player_x += 1
     if move == "left":
       player_x -= 1
     if move == "up":
       player_y += 1
     if move == "down":
       player_y -= 1

print(f"Player position: ({player_x}, {player_y})")
 # TODO: check if player has reached the treasure
if player_x == treasure_x and player_y == treasure_y:
  print("You've reached your destination")
  break
