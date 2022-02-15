print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')

print("Welcome to the treasure island, your mission is to find the treasure.")

turn = input("You are in a crossroad. Where do you turn, left or right?\n").lower()
if turn == 'left':
    action = input("At the end of the road, you see a lake. What do you do, swim or wait?\n").lower()
    if action == 'wait':
        color = input("A ghost ship appears with three doors, red, blue and yellow, which one do you choose?\n").lower()
        if color == 'yellow':
            print("You found the treasure just inside the ship. You are so lucky! You win!\nGame Over!")
        elif color == 'red':
            print("Burned by file.\nGame Over!")
        elif color == 'blue':
            print("Eaten by beasts.\nGame Over!")
        else:
            print("This is Schrodinger's door.\nGame Over!")
    else:
        print("Attacked by a trout.Game Over!\n")
else:
    print("You fell into a hole.\nGame Over!")