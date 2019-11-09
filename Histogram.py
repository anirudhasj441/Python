import time
def histogram(p,q,r):
    print("X|",end="")
    for i in range(p):
        print("#",end="")
        time.sleep(0.01)
    print()
    print("Y|",end="")
    for i in range(q):
        print("#",end="")
        time.sleep(0.01)
    print()
    print("Z|",end="")
    for i in range(r):
        print("#",end="")
        time.sleep(0.01)
    print()
if __name__ == "__main__":
    x = int(input("x = "))
    y = int(input("y = "))
    z = int(input("z = "))
    print("histogram")
    histogram(x,y,z)