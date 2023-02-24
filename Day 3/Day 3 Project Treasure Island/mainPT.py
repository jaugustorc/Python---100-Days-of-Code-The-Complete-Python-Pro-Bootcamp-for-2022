print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input('Você está em uma encruzilhada. Onde você quer ir? Digite "esquerda" ou "direita" \n').lower()
if choice1 == "esquerda":
  choice2 = input('Você veio a um lago. Há uma ilha no meio do lago. Digite "wait" para aguardar um barco. Digite "swim" para nadar. \n').lower()
  if choice2 == "wait":
    choice3 = input("Você chega ileso à ilha. Há uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. Qual cor você escolhe? \n").lower()
    if choice3 == "vermelho":
      print("É uma sala cheia de fogo. Game Over.")
    elif choice3 == "amarelo":
      print("Você encontrou o tesouro! Você ganha!")
    elif choice3 == "azul":
      print("Você entra em uma sala de feras. Game Over.")
    else:
      print("Você escolheu uma porta que não existe. Game Over.")
  else:
    print("Você é atacado por uma truta furiosa. Fim de jogo.")
else:
  print("Você caiu em um buraco. Fim de jogo.")
