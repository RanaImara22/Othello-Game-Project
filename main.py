from GameController import GameController

def main():
    print ("Choose the level:\n 1.Easy\n 2.Medium\n 3.Hard\n")
    level = int(input())
    depth = 1
    if (level == 1):
        depth = 1
    elif (level == 2):
        depth = 3
    else:
        depth = 5

    # print(level)
    gameController = GameController(depth)
    n = 60
    while(n > 0):
        gameController.play()
    


if __name__ == "__main__":
    main()
