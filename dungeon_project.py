import random

def get_locations():
  monster = None
  door= None
  player = None

  return monster, door, player

def move_player(plaver, move):

  return player # (location)

def get_moves(player):
  moves= ["ARRIBA","ABAJO", "IZQUIERDA", "DERECHA"]

  return moves

while True:
  print("Bienvenido al Calabozo!")
  print("Estás en la mazmorra número {}") #format to players position
  print("puedes moverte a {}") #format with available moves
  print("<<<<<pulsa Q para salir>>>>>")

  move = input("> ")
  move = move.upper()

  if move == 'QUIT"
    break

#grid generator custom function
def grid_generator(number):
  grid=[]
  for i in range(number):
    for x in range(number):
      grid.append((x,i))

  #print(grid)
  return grid
