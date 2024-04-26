import stick_main
num_of_sticks=int(input("Enter number of sticks you want to play"))
if num_of_sticks<=20:
    print('Enter sticks greater than 20')
    num_of_sticks=int(input("Enter number of sticks you want to play"))
    stick_main.stickGame(num_of_sticks)
else:
    if __name__=="__main__":
    
        stick_main.stickGame(num_of_sticks)