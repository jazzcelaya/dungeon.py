import os
import random

#grid generator custom function
def grid_generator(number):
  grid=[]
  for i in range(number):
    for x in range(number):
      grid.append((x,i))
  return grid

players_path = []

def ask_debug():
  debug_question = input("¿Quieres acceder al modo DEBUG? Sí/ No   ")
  if debug_question.lower() == "si":
    DEBUG = True
  else:
    DEBUG = False
  print(DEBUG)
  input("PRESS ENTER")

def draw_map(monster, player, door,players_path):
  print(" _" * grid_size)
  tile = "|{}"

  for cell in CELLS:
    x,  y = cell
    if x < grid_size-1:
      line_end = ""
      if cell == monster:
        output = tile.format("X")
      elif cell == player:
        output = tile.format("%")
      elif cell in players_path:
        output = tile.format("*")
      else:
        output = tile.format("_")
    else:
      line_end = "\n"
      if cell == monster:
        output = tile.format("X|")
      elif cell == player:
        output = tile.format("%|")
      else:
        output = tile.format("_|")

    print(output, end=line_end)


def clear_screen():
  os.system('cls' if os.name == 'nto' else 'clear')

def get_locations():
  return random.sample(CELLS, 3)
  return monster, door, player

def random_monster(monster):
  moves = get_moves(monster)
  move = random.choice(moves)
  x, y = monster
  if move == "IZQUIERDA":
      x -= 1
  if move == "DERECHA":
      x += 1
  if move == "ARRIBA":
      y -= 1
  if move == "ABAJO":
      y += 1
  return x,y


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

def get_moves(character):
  moves= ["ARRIBA","ABAJO", "IZQUIERDA", "DERECHA"]
  x, y = character
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
  players_path.append(player)
  playing = True

  while playing:
    clear_screen()
    draw_map(player, monster, door, players_path)
    valid_moves = get_moves(player)
    print("Estás en la mazmorra número {}".format(player)) #format to players position
    if DEBUG == True:
      print("*******DEBUG*******")
      print("La puerta está en la casilla {}".format(door))
    print("Puedes moverte hacia {}".format(", ".join(valid_moves))) #format with available moves
    print("<<<<<escribe SALIR para salir>>>>>")
    move = input("> ")
    move = move.upper()

    if move == "SALIR":
      print("****** Adiós, u_U ******* ")
      break

    if move in valid_moves:
      player = move_player(player, move)
      players_path.append(player)
      monster = random_monster(monster)
      draw_map(monster, player, door, players_path)

      if player == monster:
        clear_screen()
        print("Te ha comido el monstruo")
        playing = False
      if player == door:
        clear_screen()
        print("Felicidades, has escapado del calabozo")
        playing = False

    else:
      print("\n ¡Las paredes son duras, ten cuidado! \n ")
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
DEBUG = ask_debug()
clear_screen()
#call grid_generator and assign its result to CELLS,
CELLS = grid_generator(grid_size)
game_loop()


