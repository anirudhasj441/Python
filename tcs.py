posX = 0
posY = 0
x=0
y=0
turn=1
n = int(input("enter no of turns:"))
if n < 2 or n > 1000:
    print("turn should be between 2 and 1000")

else:

    while turn<=n:
        if turn%2!=0:
            if x%2==0:
                posX = posX + turn*10
                x+=1
            else:
                posX = posX - turn*10
        else:
            if y%2 == 0:
                posY = posY + turn*10
                y += 1
            else:
                posY = posY - turn* 10

        turn +=1

    print(posX,',',posY)  
