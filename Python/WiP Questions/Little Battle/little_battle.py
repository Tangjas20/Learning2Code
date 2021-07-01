import sys



def config_data_search(line):
  config_data = open(sys.argv[1], 'r')
  data_line = config_data.readlines()
  data_line = data_line[line].split()
  data_line.pop(0)
  config_data.close()
  return data_line


# Please implement this function according to Section "Read Configuration File"
def load_config_file(filepath):
  try:
    config_file = open(filepath, 'r')
  except:
    raise FileNotFoundError("")
  resources = ["Frame: ", "Water: ", "Wood: ", "Food: ", "Gold: "]
  lines = 0
  config_lines = config_file.readlines()

  widthxheight = config_lines[0][7:10]
  widthxheight = list(widthxheight)
  width = widthxheight[0]
  height = widthxheight[2]
  #width = config_lines[0][7]
  #height = config_lines[0][9]
  def config_data_search(line):
    data_line = config_lines
    data_line = data_line[line].split()
    data_line.pop(0)
    return data_line
  for line in config_lines:
      if line != "\n":
        lines += 1

####Checks For Format Errors####
  if lines != 5:
    raise SyntaxError("Invalid Configuration File: format error!")
  if config_lines[0][0:7] != resources[0]:
    raise SyntaxError("Invalid Configuration File: format error!")
  elif config_lines[1][0:7] != resources[1]:
    raise SyntaxError("Invalid Configuration File: format error!")
  elif config_lines[2][0:6] != resources[2]:
    raise SyntaxError("Invalid Configuration File: format error!")
  elif config_lines[3][0:6] != resources[3]:
    raise SyntaxError("Invalid Configuration File: format error!")
  elif config_lines[4][0:6] != resources[4]:
    raise SyntaxError("Invalid Configuration File: format error!")

#### Checks for Frame Format Errors widthxheight####
  if widthxheight[1] == 'x':
    try:
      width = int(width)
      height = int(height)
    except:
      raise SyntaxError("Invalid Configuration File: frame should be in format widthxheight")
  else:
    raise SyntaxError("Invalid Configuration File: frame should be in format widthxheight")

####Checks for Frame Boundary Errors 5-7####
  try:
      if int(width) in range(5, 8) and int(height) in range(5,8):
            pass
      else:
            raise ArithmeticError("Invalid Configuration File: width and height should range from 5 to 7!")
  except:
      raise ArithmeticError("Invalid Configuration File: width and height should range from 5 to 7!")

####Checks for non-integer errors in lines####
  for x in config_lines[1][7:]:
        waterlist = []
        waterlist.append(x)
        for x in waterlist:
          if x == "\n" or x == " ":
            waterlist.remove(x)
        for x in waterlist:
          try:
            x == int(x)
          except:
            raise ValueError("Invalid Configuration File: Water contains non integer characters")

  for x in config_lines[2][6:]:
        woodlist = []
        woodlist.append(x)
        for x in woodlist:
          if x == "\n" or x == " ":
            woodlist.remove(x)
        for x in woodlist:
          try:
            x = int(x)
          except:
            raise ValueError("Invalid Configuration File: Wood contains non integer characters")

  for x in config_lines[3][6:]:
        foodlist = []
        foodlist.append(x)
        for x in foodlist:
          if x == "\n" or x == " ":
            foodlist.remove(x)
        for x in foodlist:
          try:
            x == int(x)
          except:
            raise ValueError("Invalid Configuration File: Food contains non integer characters")
            
  for x in config_lines[4][6:]:
        goldlist = []
        goldlist.append(x)
        for x in goldlist:
          if x == "\n" or x == " ":
            goldlist.remove(x)
        for x in goldlist:
          try:
            x == int(x)
          except:
            raise ValueError("Invalid Configuration File: Gold contains non integer characters")
            
####Checks Odd Number Of Elements Error####
  waters = config_data_search(1)
  if len(waters) % 2 != 0:
    raise SyntaxError("Invalid Configuration File: Water has an odd number of elements!")
  woods = config_data_search(2)
  if len(woods) % 2 != 0:
    raise SyntaxError("Invalid Configuration File: Wood has an odd number of elements!")
  foods = config_data_search(3)
  if len(foods) % 2 != 0:
    raise SyntaxError("Invalid Configuration File: Food has an odd number of elements!")
  golds = config_data_search(4)
  if len(golds) % 2 != 0:
    raise SyntaxError("Invalid Configuration File: Gold has an odd number of elements!")


####Checks For If Position Is Out Of Map####
  water1 = waters[::2]
  water2 = waters[1::2]
  watercoords = list(zip(water1,water2))

  woods1 = woods[::2]
  woods2 = woods[1::2]
  woodcoords = list(zip(woods1,woods2))

  foods = config_data_search(3)
  foods1 = foods[::2]
  foods2 = foods[1::2]
  foodcoords = list(zip(foods1,foods2))

  golds = config_data_search(4)
  golds1 = golds[::2]
  golds2 = golds[1::2]
  goldcoords = list(zip(golds1,golds2))
  for n in water1:
      if int(n) >= int(width):
        raise ArithmeticError("Invalid Configuration File: Water contains a position that is out of map")
  for n in water2:
      if int(n) >= int(height):
        raise ArithmeticError("Invalid Configuration File: Water contains a position that is out of map")
  for n in woods1:
      if int(n) >= int(width):
        raise ArithmeticError("Invalid Configuration File: Wood contains a position that is out of map")
  for n in woods2:
      if int(n) >= int(height):
        raise ArithmeticError("Invalid Configuration File: Wood contains a position that is out of map")
  for n in foods1:
      if int(n) >= int(width):
        raise ArithmeticError("Invalid Configuration File: Food contains a position that is out of map")
  for n in foods2:
      if int(n) >= int(height):
        raise ArithmeticError("Invalid Configuration File: Food contains a position that is out of map")
  for n in golds1:
      if int(n) >= int(width):
        raise ArithmeticError("Invalid Configuration File: Gold contains a position that is out of map")
  for n in golds2:
      if int(n) >= int(height):
        raise ArithmeticError("Invalid Configuration File: Gold contains a position that is out of map")
      
####Checks for Position Near Home Base Occupied####

  for x in watercoords:
      if x == ('1', '1') or x == ('0', '1') or x == ('2', '1') or x == ('1', '2') or x == ('1', '0'):
        raise ValueError("Invalid Configuration File: The positions of home bases or the positions next to the home bases are occupied")
      elif x == (str(int(width)-2), str(int(height)-2)) or x == (str(int(width)-2), str(int(height)-3)) or x == (str(int(width)-1), str(int(height)-2)) or x == (str(int(width)-2), str(int(height)-1)) or x == (str(int(width)-3), str(int(height)-2)): 
        raise ValueError("Invalid Configuration File: The positions of home bases or the positions next to the home bases are occupied")
  for x in woodcoords:
      if x == ('1', '1') or x == ('0', '1') or x == ('2', '1') or x == ('1', '2') or x == ('1', '0'):
        raise ValueError("Invalid Configuration File: The positions of home bases or the positions next to the home bases are occupied")
      elif x == (str(int(width)-2), str(int(height)-2)) or x == (str(int(width)-2), str(int(height)-3)) or x == (str(int(width)-1), str(int(height)-2)) or x == (str(int(width)-2), str(int(height)-1)) or x == (str(int(width)-3), str(int(height)-2)): 
        raise ValueError("Invalid Configuration File: The positions of home bases or the positions next to the home bases are occupied")
  for x in foodcoords:
      if x == ('1', '1') or x == ('0', '1') or x == ('2', '1') or x == ('1', '2') or x == ('1', '0'):
        raise ValueError("Invalid Configuration File: The positions of home bases or the positions next to the home bases are occupied")
      elif x == (str(int(width)-2), str(int(height)-2)) or x == (str(int(width)-2), str(int(height)-3)) or x == (str(int(width)-1), str(int(height)-2)) or x == (str(int(width)-2), str(int(height)-1)) or x == (str(int(width)-3), str(int(height)-2)): 
        raise ValueError("Invalid Configuration File: The positions of home bases or the positions next to the home bases are occupied")
  for x in goldcoords:
      if x == ('1', '1') or x == ('0', '1') or x == ('2', '1') or x == ('1', '2') or x == ('1', '0'):
        raise ValueError("Invalid Configuration File: The positions of home bases or the positions next to the home bases are occupied")
      elif x == (str(int(width)-2), str(int(height)-2)) or x == (str(int(width)-2), str(int(height)-3)) or x == (str(int(width)-1), str(int(height)-2)) or x == (str(int(width)-2), str(int(height)-1)) or x == (str(int(width)-3), str(int(height)-2)): 
        raise ValueError("Invalid Configuration File: The positions of home bases or the positions next to the home bases are occupied")

####Checks For Duplicate Position####



  waters, woods, foods, golds = watercoords, woodcoords, foodcoords, goldcoords # list of position tuples
  # It should return width, height, waters, woods, foods, golds based on the file
  # Complete the test driver of this function in file_loading_test.py
  return waters, woods, foods, golds

  #######################################################
  ########MAIN LITTLE BATTLE FUNCTION STARTS HERE########
  #######################################################
if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python3 little_battle.py <filepath>")
  elif len(sys.argv) == 2:
    try:
      load_config_file(sys.argv[1])
    except:
      print("Test file not found")
      sys.exit()
    config_file = open(sys.argv[1], 'r')
    config_lines = config_file.readlines()
    widthxheight = config_lines[0][7:10]
    widthxheight = list(widthxheight)
    width = int(widthxheight[0])
    height = int(widthxheight[2])
    armyspearman1 = []
    armyarcher1 = []
    armyknight1 = []
    armyscout1 = []
    spearmanstring = "  Spearman:"
    archerstring = "  Archer:"
    knightstring = "  Knight:"
    scoutstring = "  Scout:"
    def split(word):
        return [char for char in word]
    
    def resourchecker1():
      if player == 1:
        print(printmyassets(player1Assets))
        if ((player1Assets[0] == player1Assets[1] == 0) or (player1Assets[0] == player1Assets[2] == 0) or (player1Assets[1] == player1Assets[2] == 0)):
          print("No resources to reruit any armies.")
          rss = False
        elif scaledboard[0][1] != "  " and scaledboard[1][0] == "  " and scaledboard[2][1] == "  " and scaledboard[1][2] == "  ":
          print("No place to recruit new armies.")
          space = False
      elif player == 2:
        print(printmyassets(player2Assets))
        if ((player2Assets[0] == player2Assets[1] == 0) or (player2Assets[0] == player2Assets[2] == 0) or (player2Assets[1] == player2Assets[2] == 0)):
          print("No resources to reruit any armies.")
          rss = False
        elif scaledboard[-2][-1] != "  " and scaledboard[-3][-2] != "  " and scaledboard[-2][-3] != "  " and scaledboard[-1][-2] != "  ":
          print("No place to recruit new armies.")
          space = False

    def config_data_search(line): #This searches the config files for the data and acts as a search and assigning function when called
      config_data = open('config.txt', 'r')
      data_line = config_data.readlines() 
      data_line = data_line[line].split() #Splits the values into separate elements in a list
      data_line.pop(0) #Removes the first index
      config_data.close() #Closes the file that was opened
      return data_line # returns the value 


    def boardspaces(): #Creates a nested list which has positions based on height and width
      scaledboard = []
      for y_axis in range(0, height):
          board = []
          for x_axis in range(0, width):
            board.append("  ")
          scaledboard.append(board)
      return scaledboard

      
    def print_game_board(): #Uses the boardspaces() to print a game board 
        print("Please check the battlefield, commander.")
        first_line ="  X"
        for no in range(0, width):
          first_line += "0" + str(no) + " "
        first_line = first_line[:-1] + "X"
        print(first_line)
        
        second_line = " Y+"
        for no in range(0, width):
          second_line += "---"
        second_line = second_line[:-1] + "+"
        print(second_line)

        for height_val in range(0, height):
          boardline = "|"
          for width_val in range(0, width):
            boardline += str(scaledboard[height_val][width_val]) + "|"
          print("0" + str(height_val) + boardline)
        print(second_line)

    def armyprices():
      print('''Recruit Prices:
  Spearman (S) - 1W, 1F
  Archer (A) - 1W, 1G
  Knight (K) - 1F, 1G
  Scout (T) - 1W, 1F, 1G''')

    def printmyassets(n):
        return "[Your Asset: Wood - " + str(n[0]) + " Food - " + str(n[1]) + " Gold - " + str(n[2])+ "]"


    scaledboard = boardspaces()

    scaledboard[1][1] = "H1"
    scaledboard[-2][-2] = "H2"


    waters = config_data_search(1)
    water1 = waters[::2]
    water2 = waters[1::2]
    watercoords = list(zip(water1,water2))
    for n in watercoords:
        scaledboard[int(n[1])][int(n[0])] = "~~"

    woods = config_data_search(2)

    woods1 = woods[::2]
    woods2 = woods[1::2]
    woodcoords = list(zip(woods1,woods2))
    for n in woodcoords:

        scaledboard[int(n[1])][int(n[0])] = "WW"

    foods = config_data_search(3)
    foods1 = foods[::2]
    foods2 = foods[1::2]
    foodcoords = list(zip(foods1,foods2))
    for n in foodcoords:
        scaledboard[int(n[1])][int(n[0])] = "FF"

    golds = config_data_search(4)
    golds1 = golds[::2]
    golds2 = golds[1::2]
    goldcoords = list(zip(golds1,golds2))
    for n in goldcoords:
        scaledboard[int(n[1])][int(n[0])] = "GG"

    ####Initialisation of Program####
    gameyear = 617 # Needs to increment every year
    gamewon = False
    print("Configuration file {} was loaded.".format(sys.argv[1]))
    print("Game Started: Little Battle! (enter QUIT to quit the game)")
    print("")
    print_game_board()
    print("(enter DIS to display the map)\n")
    armyprices()
    print("(enter PRIS to display the price list)\n")

    

    ####Player 1 Assets/Army####
    player = 1
    player1Assets = [2, 2, 2] #Wood, Food, Gold in that order
    player1Army = [0, 0, 0, 0]
    '''
    1 - Spearman (S)
    2 - Archer (A)
    3 - Knight (K)
    4 - Scout (T)
    '''
    ####Initial Player 2 Assets/Army####
    player2Assets = [2, 2, 2] #W F G
    player2Army = [0, 0, 0, 0]


    ####This section Tests for Sufficient Resources####
    while gamewon == False:
      print("-Year {}-".format(gameyear))
      print("")
      print("+++Player {}'s Stage: Recruit Armies+++".format(player))
      print("")
      rss = True
      space = True
      if player == 1:
          print(printmyassets(player1Assets))
          print("")
          if ((player1Assets[0] == player1Assets[1] == 0) or (player1Assets[0] == player1Assets[2] == 0) or (player1Assets[1] == player1Assets[2] == 0)):
                print("No resources to reruit any armies.")
                rss = False
      ####Checks if the 4 spots near H1 is empty or not####
          elif scaledboard[0][1] != "  " and scaledboard[1][0] == "  " and scaledboard[2][1] == "  " and scaledboard[1][2] == "  ":
                print("No place to recruit new armies.")
                space = False
                
      ####Checks if Player 2 has resources or not####
      if player == 2:
          print(printmyassets(player2Assets))
          if (player2Assets[0] < 2 or player2Assets[1] < 2 or player2Assets[2] < 2):
                print("No resources to reruit any armies.")
                rss = False
        ####Checks if the 4 spots near H2 is empty or not####
          elif scaledboard[-2][-1] != "  " and scaledboard[-3][-2] != "  " and scaledboard[-2][-3] != "  " and scaledboard[-1][-2] != "  ":
                print("No place to recruit new armies.")
                space = False


      army = ["S", "A", "K", "T"]
      recruitvalid = False

      if rss == True and space == True: #Add recruitment section here
          troopvalid = False
          while troopvalid == False and rss == True:
            print("Which type of army to recruit, (enter) ‘S’, ‘A’, ‘K’, or ‘T’? Enter ‘NO’ to end this stage.")
            recruit = input("")
            if recruit == "QUIT":
              sys.exit()
            elif recruit == "DIS":
              print_game_board()
              print("")
            elif recruit == "PRIS":
              armyprices()
              print("")
            elif recruit == 'NO':
              troopvalid = True
              print("")
            elif recruit == "S" and player1Assets[0] > 0 and player1Assets[1] > 0:
                  recruitvalid = True
                  n = player1Army[0]
                  name = "Spearman"

            elif recruit == "S" and (player1Assets[0] == 0 or player1Assets[1]) == 0:
                    print("Insufficient resources. Try again.\n")
                    troopvalid = False

            elif recruit == "A" and player1Assets[0] > 0 and player1Assets[2] > 0:
                  n = player1Army[1]
                  recruitvalid = True
                  name = "Archer"

            elif recruit == "A" and (player1Assets[0] == 0 or player1Assets[2] == 0):
                  print("Insufficient resources. Try again.\n")
                  troopvalid = False

            elif recruit == "K" and (player1Assets[1] > 0 and player1Assets[2] > 0):
                  n = player1Army[2]
                  name = "Knight"
                  recruitvalid = True
                  troopvalid = True
            
            elif recruit == "K" and (player1Assets[0] == 0 or player1Assets[2] == 0):
                  print("Insufficient resources. Try again.\n")
                  troopvalid = False

            elif recruit == "T" and player1Assets[1] > 0 and player1Assets[2] > 0 and player1Assets[0] > 0:
                  n = player1Army[3]
                  name = "Scout"
                  recruitvalid = True
                  troopdvalid = True

            elif recruit == "T" and (player1Assets[0] == 0 or player1Assets[2] == 0 or player1Assets[1] == 0):
                  print("Insufficient resources. Try again.\n")
                  troopvalid = False
            else:
                  print("Sorry, invalid input. Try again.\n")

      #####This needs to be in a new loop or smth
            while recruitvalid == True:
                print("")
                print("You want to recruit a {}. Enter two integers as format ‘x y’ to place your army.".format(name))
                recruitposition = input("")
                splitposition = recruitposition.split()
                try:
                  if recruitposition == "DIS":
                        print_game_board()
                  elif len(splitposition) > 2:
                    print("Sorry, invalid input. Try again.")
                  elif scaledboard[int(splitposition[1])][int(splitposition[0])] == "  " and (tuple(splitposition) == ('0','1') or tuple(splitposition) == ('1','0') or tuple(splitposition) == ('2','1') or tuple(splitposition) == ('1','2')):
                      recruitvalid = True
                      print("")
                      if recruit == "S":
                        player1Assets[0] -= 1
                        player1Assets[1] -= 1
                        print("You has recruited a Spearman.\n")
                        recruitvalid = False
                        player1Army[0] += 1
                        if spearmanstring == "  Spearman:":
                          spearmanstring += " ({}, {})".format(splitposition[0],splitposition[1])
                        else:
                          spearmanstring += ", ({}, {})".format(splitposition[0],splitposition[1])
                        armyspearman1.append(splitposition)
                        scaledboard[int(splitposition[1])][int(splitposition[0])] = "S1"
                        print(printmyassets(player1Assets))

                        if ((player1Assets[0] == player1Assets[1] == 0) or (player1Assets[0] == player1Assets[2] == 0) or (player1Assets[1] == player1Assets[2] == 0)):
                          print("No resources to recruit any armies.\n")
                          rss = False

                      elif scaledboard[int(splitposition[0])][int(splitposition[1])] != "  " and (tuple(splitposition) == ('0','1') or tuple(splitposition) == ('1','0') or tuple(splitposition) == ('2','1') or tuple(splitposition) == ('1','2')):
                          print("You must place your newly recruited unit in an unoccupied position next to your base. Try again.")

                      elif recruit == "A":
                        player1Assets[0] -= 1
                        player1Assets[2] -= 1
                        print("You has recruited a Archer.\n")
                        scaledboard[int(splitposition[1])][int(splitposition[0])] = "A1"
                        recruitvalid = False
                        troopvalid = False
                        player1Army[1] += 1
                        if archerstring == "  Archer:":
                          archerstring += " ({}, {})".format(splitposition[0],splitposition[1])
                        else:
                          archerstring += ", ({}, {})".format(splitposition[0],splitposition[1])
                        armyarcher1.append(splitposition)
                        print(printmyassets(player1Assets))
                        print("")
                        if ((player1Assets[0] == player1Assets[1] == 0) or (player1Assets[0] == player1Assets[2] == 0) or (player1Assets[1] == player1Assets[2] == 0)):
                          print("No resources to recruit any armies.\n")
                          rss = False


                      elif recruit == "K":
                        player1Assets[1] -= 1
                        player1Assets[2] -= 1
                        recruitvalid = False
                        troopvalid = False
                        armyknight1.append(splitposition)
                        print("You has recruited a Knight.\n")
                        scaledboard[int(splitposition[1])][int(splitposition[0])] = "K1"
                        player1Army[2] += 1
                        if knightstring == "  Knight:":
                          knightstring += " ({}, {})".format(splitposition[0],splitposition[1])
                        else:
                          knightstring += ", ({}, {})".format(splitposition[0],splitposition[1])
                        print(printmyassets(player1Assets))
                        if ((player1Assets[0] == player1Assets[1] == 0) or (player1Assets[0] == player1Assets[2] == 0) or (player1Assets[1] == player1Assets[2] == 0)):
                          print("No resources to recruit any armies.\n")
                          rss = False


                      elif recruit == "T":
                        player1Assets[1] -= 1
                        player1Assets[0] -= 1
                        player1Assets[2] -= 1
                        scaledboard[int(splitposition[1])][int(splitposition[0])] = "T1"
                        recruitvalid = False
                        troopvalid = False
                        armyscout1.append(splitposition)
                        print("You has recruited a Scout.\n")
                        player1Army[3] += 1
                        if scoutstring == "  Scout:":
                          scoutstring += " ({}, {})".format(splitposition[0],splitposition[1])
                        else:
                          scoutstring += ", ({}, {})".format(splitposition[0],splitposition[1])
                        print(printmyassets(player1Assets))
                        print("")
                        if ((player1Assets[0] == player1Assets[1] == 0) or (player1Assets[0] == player1Assets[2] == 0) or (player1Assets[1] == player1Assets[2] == 0)):
                          print("No resources to recruit any armies.\n")
                          rss = False


                  else:
                    print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
          

                except:
                    print("Sorry, invalid input. Try again.\n")




      ####Move Army Stage####

      if player == 1:
        print("===Player 1's Stage: Move Armies===")
      if player == 2:
        print("+++Player 2's Stage: Move Armies+++")
      print("")
      if player1Army != [0,0,0,0]:
        print("Armies to Move:")
      if armyspearman1 != []:
        print(spearmanstring)
      if armyarcher1 != []:
        print(archerstring)
      if armyknight1 != []:
        print(knightstring)
      if armyscout1 != []:
        print(scoutstring)
      if player1Army != [0,0,0,0]:
        print("")

      if player == 1 and player1Army == [0,0,0,0]: #THIS NEEDS TO BE WORKED ON
            print("No Army to Move: next turn.")
            print("")
            player == 2
      elif player == 1:
            moves = sum(player1Army)
            armies_tomove = []

            while moves != 0:
              print("Enter four integers as a format ‘x0 y0 x1 y1’ to represent move unit from (x0, y0) to (x1, y1) or ‘NO’ to end this turn.")
              armymove = input("")
              if armymove == "NO":
                moves = 0
              elif armymove == "QUIT":
                exit()
              elif armymove == "DIS":
                print_game_board()
              else:
                  try:
                    int(armymove[0])
                    int(armymove[2])
                    int(armymove[4])
                    int(armymove[6])
                    if armymove[1] == " " and armymove[3] == " " and armymove[5] == " ":
                        splitarmymove = armymove.split()
                        initialposition = (int(splitarmymove[0]),int(splitarmymove[1]))
                        n = initialposition[0]
                        m = initialposition[1]
                        targetposition = (int(splitarmymove[2]),int(splitarmymove[3]))
                        j = targetposition[0]
                        k = targetposition[1]
                        if scaledboard[n][m] == "S1" and ((j == n+1 and m == k) or (j == n and k == m+1) or (j == n-1 and k == m) or (j ==n and k == m-1)) and (j <= (width-1)) and (k <= (height-1)):
                            if scaledboard[j][k] == "  ":
                              scaledboard[n][m] == "  "
                              scaledboard[j][k] == "S1"

                            elif scaledboard[j][k] == "FF":
                              scaledboard[n][m] == "  "
                              scaledboard[j][k] == "S1"
                              player1Assets[1] += 2
                              print("Good. we collected 2 Food.")

                            elif scaledboard[j][k] == "GG":
                              scaledboard[n][m] == "  "
                              scaledboard[j][k] == "S1"
                              player1Assets[2] += 2
                              print("Good. we collected 2 Gold.")

                            elif scaledboard[j][k] == "WW":
                              scaledboard[n][m] == "  "
                              scaledboard[j][k] == "S1"
                              player1Assets[0] += 2
                              print("Good. we collected 2 Wood.")

                            elif scaledboard[j][k] == "~~":
                              scaledboard[n][m] == "  "
                              print("We lost the army Spearman due to your command!")
                              player1Army[0] -= 1

                            elif scaledboard[j][k] == "A2":
                              scaledboard[n][m] == "  "
                              scaledboard[j][kl] == "A2"
                              print("We lost the army Spearman due to your command")
                              player1Army[0] -= 1
                            
                            elif scaledboard[j][k] == "K2":
                              scaledboard[n][m] == "  "
                              scaledboard[j][k] == "S1"
                              print("Great! We defeated the enemy Knight!")

                            elif scaledboard[j][k] == "S2":
                              scaledboard[n][m] == "  "
                              scaledboard[j][k] == "  "
                              print("We destroyed the enemy Spearman with massive loss!")
                            
                            elif scaledboard[j][k] == "H2":
                              scaledboard[n][m] == "  "
                              scaledboard[j][k] == "S1"
                              print("The army Spearman captured the enemy's capital.\n")
                              EmpName = input("What's your name, commander?\n")
                              print("***Congratulation! Emperor {} unified the country in {}***".format(EmpName, gameyear))
                              exit()



                        elif scaledboard[n][m] == "A1" and ((j == n+1 and m == k) or (j == n and k == m+1) or (j == n-1 and k == m) or (j ==n and k == m-1)):
                          pass
                        elif scaledboard[n][m] == "K1" and ((j == n+1 and m == k) or (j == n and k == m+1) or (j == n-1 and k == m) or (j ==n and k == m-1)):
                          pass
                        elif scaledboard[n][m] == "T1" and ((j == n+1 and m == k) or (j == n and k == m+1) or (j == n-1 and k == m) or (j ==n and k == m-1)):
                          pass
                  except:
                    print("Invalid move. Try again")  
                    pass

      player = 2
                        #armymoveable = "Spearman"
                      #elif scaledboard[initialposition[0][initialposition[1]] == "A1":
                      #armymoveable == "Archer"

                      #elif scaledboard[initialposition[0][initialposition[1]] == "K1":
                      #armymoveable == "Knight"

            #   except:
                #  print("Fail")

                # print("You have moved {} from {} to {} ")

    #elif (player == 2) and player2Army == [0,0,0,0]:
    #     print("No Army to Move: next turn")
      #    print("")
      #    player == 1


