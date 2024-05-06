from GameController import GameController

def main():
    level = input("Choose the level:\n 1.Easy\n 2.Medium\n 3.Hard\n")
    depth = 1
    if (level == 1):
        depth = 1
    elif (level == 2):
        depth = 3
    else:
        depth = 5

    gameController = GameController(depth)
    n = 60
    while(n > 0):
        gameController.play()
    


if __name__ == "__main__":
    main()
