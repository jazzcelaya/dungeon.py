import os
import random


def clear_screen():
  os.system('cls' if os.name == 'nto' else 'clear')

def get_locations():
  return random.sample(CELLS, 3)

  return monster, door, player

def move_player(player, move):
  x, y = player
  if move == "IZQUIERDA":
    x -= 1
  if move == "DERECHA":
    x += 1
  if move == "ARRIBA":
    y -= 1
  if move == "ABAJO":
    y += 1
  return x, y # (location)

def get_moves(player):
  moves= ["ARRIBA","ABAJO", "IZQUIERDA", "DERECHA"]
  x, y = player
  if x == 0:
    moves.remove("IZQUIERDA")
  if x == grid_size:
    moves.remove("DERECHA")
  if y == 0:
    moves.remove("ARRIBA")
  if y == grid_size:
    moves.remove("ABAJO")

  return moves

#grid generator custom function
def grid_generator(number):
  grid=[]
  for i in range(number):
    for x in range(number):
      grid.append((x,i))

  #print(grid)
  return grid

#save number of cells in variable
grid_size = int(input("¿De cuántas filas quieres la mazmorra? "))

#call grid_generator and assign its result to CELLS,
CELLS = grid_generator(grid_size)

# getting random locations
monster, player, door = get_locations()

while True:
  valid_moves = get_moves(player)
  clear_screen()
  print("Bienvenido al Calabozo!")
  print("Estás en la mazmorra número {}".format(player)) #format to players position
  print("Puedes moverte a la {}".format(", ".join(valid_moves))) #format with available moves
  print("<<<<<pulsa Q para salir>>>>>")

  move = input("> ")
  move = move.upper()

  if move == "QUIT":
    break

  if move in valid_moves:
    player = move_player(player, move)
  else:
    print("\n ¡Las paredes son duras, ouch! \n ")
    continue

