#  --------------- 
#  |      |      |
#  |      |      |
#  |      |      |
#  |______|______|
#  |      |      |
#  |      |      |
#  |      |      |
#  |      |      |
#  ---------------

from os import system
system("cls")
print()

w = int(input("width: "))
h = int(input("height: "))
W = w*2

for r in range(h): 
    
    for s in range(w):
        if r == 0 or r == h-1:
            print("-"*2, end="")
        elif s == w-1:
            print("  |", end="")
        elif s == 0:
            print("|", end="")
        elif s == 1 and r == ((h/2)-1):
            print("_"*w, end="")
        # elif r == (w/2) and s == (h/2):
        #     print("|")    
   
        else:
            print("  ", end="")
    print()


