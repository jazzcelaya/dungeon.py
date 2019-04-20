import os
import random

#grid generator custom function
def grid_generator(number):
  grid=[]
  for i in range(number):
    for x in range(number):
      grid.append((x,i))

  #print(grid)
  return grid


def draw_map(player):
  print(" _" * grid_size)
  tile = "|{}"

  for cell in CELLS:
    x,  y = cell
    if x < grid_size-1:
      line_end = ""
      if cell == player:
        output = tile.format("X")
      else:
        output = tile.format("_")
    else:
      line_end = "\n"
      if cell == player:
        output = tile.format("X|")
      else:
        output = tile.format("_|")

    print(output, end=line_end)


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
  if x == grid_size-1:
    moves.remove("DERECHA")
  if y == 0:
    moves.remove("ARRIBA")
  if y == grid_size-1:
    moves.remove("ABAJO")

  return moves


def game_loop():
  # getting random locations
  monster, player, door = get_locations()
  playing = True

  while playing:
    clear_screen()
    draw_map(player)
    valid_moves = get_moves(player)
    print("Estás en la mazmorra número {}".format(player)) #format to players position
    print("Puedes moverte hacia {}".format(", ".join(valid_moves))) #format with available moves
    print("<<<<<escribe SALIR para salir>>>>>")
    move = input("> ")
    move = move.upper()

    if move == "SALIR":
      print("****** Adiós, vaquero u_U ******* ")
      break

    if move in valid_moves:
      player = move_player(player, move)

      if player == monster:
        print("Te ha comido el monstruo")
        playing = False
      if player == door:
        print("Felicidades, has escapado del calabozo")
        playing = False

    else:
      print("\n ¡Las paredes son duras, ouch! \n ")
      input("pulsa ENTER para continuar")
      clear_screen()
      continue

  else:

    if input("Quieres jugar de nuevo? Sí / No ").lower() != "no":
      game_loop()


clear_screen()
print("Bienvenido al Calabozo!")
grid_size = int(input("¿De cuántas filas quieres la mazmorra? "))
clear_screen()
#save number of cells in variable
clear_screen()
#call grid_generator and assign its result to CELLS,
CELLS = grid_generator(grid_size)
game_loop()


