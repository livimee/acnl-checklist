def view_fish():
    total = 0
    
    print("FISH LIST")
    print("- - - - - - - - - - - - -")
    f = open("fishlist.txt","r")
    fl = f.readlines()
    for line in fl:
        print(line)
        if "x" == line[len(line)-2]:
            total += 1 
    percentage = (total / 72) * 100
    print("- - - - - - - - - - - - -")
    print("%d / 72   %.2f %s" % (total, percentage,'%'))
    if percentage == 100:
        print("~ COMPLETE ~")
    print()

def view_bug():
    total = 0
    
    print("BUG LIST")
    print("- - - - - - - - - - - - -")
    
    f = open("buglist.txt", "r")
    fl = f.readlines()
    
    for line in fl:
        print(line)
        if "x" == line[len(line)-2]:
            total += 1
    
    percentage = (total / 72) * 100
    
    print("- - - - - - - - - - - - -")
    print("%d / 72   %.2f %s" % (total, percentage,'%'))
    print()
    
def view_fossil():
    total = 0
    
    print("FOSSIL LIST")
    print("- - - - - - - - - - - - -")
    
    f = open("fossillist.txt", "r")
    fl = f.readlines()
    
    for line in fl:
        print(line)
        if "x" == line[len(line)-2]:
            total += 1
    
    percentage = (total / 68) * 100
    
    print("- - - - - - - - - - - - -")
    print("%d / 68   %.2f %s" % (total, percentage,'%'))
    print()
    
    
def view_art():
    total = 0
    
    print("ART LIST")
    print("- - - - - - - - - - - - -")
    
    f = open("artlist.txt", "r")
    fl = f.readlines()
    
    for line in fl:
        print(line)
        if "x" == line[len(line)-2]:
            total += 1
    
    percentage = (total / 33) * 100
    
    print("- - - - - - - - - - - - -")
    print("%d / 33   %.2f %s" % (total, percentage,'%'))
    print()
    
def view_all():
    total = 0
    print("FULL LIST")
    print("- - - - - - - - - - - - -")
    
    print("FISH")
    print("- - - -")
    f = open("fishlist.txt","r")
    fl = f.readlines()
    f.close()
    for line in fl:
        print(line)
        if "x" == line[len(line)-2]:
            total += 1
            
    print()
    print("BUGS")
    print("- - - -")    
    f = open("buglist.txt","r")
    fl = f.readlines()
    f.close()
    for line in fl:
        print(line)
        if "x" == line[len(line)-2]:
            total += 1  
            
    print()
    print("FOSSILS")
    print("- - - -")        
    f = open("fossillist.txt","r")
    fl = f.readlines()
    f.close()
    for line in fl:
        print(line)
        if "x" == line[len(line)-2]:
            total += 1 
            
    print()
    print("ART")
    print("- - - -")             
    f = open("artlist.txt","r")
    fl = f.readlines()
    f.close()
    for line in fl:
        print(line)
        if "x" == line[len(line)-2]:
            total += 1 
            
    percentage = (total / 244) * 100
    
    print("- - - - - - - - - - - - -")
    print("%d / 244   %.2f %s" % (total, percentage,'%'))
    print() 
    
def update_fish():
    con = True
    
    while con == True:
        present = False
        f = open("fishlist.txt","r")
        fl = f.readlines()
        f.close()
        fish = input("Enter fish name: ")
        length = len(fish)
        newlist = []
        
        for line in fl:
            if fish == line[:length]:
                line = line[:-1]
                line = line[:-1]
                line = line + "x\n"
                present = True
            newlist.append(line)
        
        if present == True:   
            f = open("fishlist.txt", "w")
            for line in newlist:
                f.write(line)
            choice = input("List updated! Add another fish? (y/n): ")
            print()
        else:
            choice = input("Incorrect fish name! try again? (y/n): ")
            print()
        if choice == "n":
            con = False
            
def update_bug():
    con = True
    
    while con == True:
        present = False
        f = open("buglist.txt","r")
        fl = f.readlines()
        f.close()
        fish = input("Enter bug name: ")
        length = len(fish)
        newlist = []
        
        for line in fl:
            if fish == line[:length]:
                line = line[:-1]
                line = line[:-1]
                line = line + "x\n"
                present = True
            newlist.append(line)
        
        if present == True:   
            f = open("buglist.txt", "w")
            for line in newlist:
                f.write(line)
            choice = input("List updated! Add another bug? (y/n): ")
            print()
        else:
            choice = input("Incorrect bug name! try again? (y/n): ")
            print()
        if choice == "n":
            con = False
            
def update_fossil():
    con = True
    
    while con == True:
        present = False
        f = open("fossillist.txt","r")
        fl = f.readlines()
        f.close()
        fish = input("Enter fossil name: ")
        length = len(fish)
        newlist = []
        
        for line in fl:
            if fish == line[:length]:
                line = line[:-1]
                line = line[:-1]
                line = line + "x\n"
                present = True
            newlist.append(line)
        
        if present == True:   
            f = open("fossillist.txt", "w")
            for line in newlist:
                f.write(line)
            choice = input("List updated! Add another fossil? (y/n): ")
            print()
        else:
            choice = input("Incorrect fossil name! try again? (y/n): ")
            print()
        if choice == "n":
            con = False
            
def update_art():
    con = True
    
    while con == True:
        present = False
        f = open("artlist.txt","r")
        fl = f.readlines()
        f.close()
        fish = input("Enter art name: ")
        length = len(fish)
        newlist = []
        
        for line in fl:
            if fish == line[:length]:
                line = line[:-1]
                line = line[:-1]
                line = line + "x\n"
                present = True
            newlist.append(line)
        
        if present == True:   
            f = open("artlist.txt", "w")
            for line in newlist:
                f.write(line)
            choice = input("List updated! Add more art? (y/n): ")
            print()
        else:
            choice = input("Incorrect art name! try again? (y/n): ")
            print()
        if choice == "n":
            con = False
 
# START OF MAIN PROGRAM 
print("ANIMAL CROSSING COLLECTION CHECKLIST")

main_menu = True
while main_menu == True:
    print()
    print("MAIN MENU")
    print("View list (v)\nUpdate list (u)\nQuit (q)\n")
    option = input("Choose option: ")
    print()

    if option == "q":
        main_menu = False
    if option == "v":
        print("VIEW MENU")
        print("Fish (a)\nBugs (b)\nFossils (c)\nArt (d)\nAll (e)\n")
        choice = input("Choose Category: ")
        print()
        
        if choice == "a":
            view_fish()
        if choice == "b":
            view_bug()
        if choice == "c":
            view_fossil()
        if choice == "d":
            view_art()  
        if choice == "e":
            view_all()
        
        option = input("Return to main menu? (y/n): ")
        print()
        if option == "n":
            main_menu = False          
    
        
    if option == "u":
        print("UPDATE MENU")
        print("Fish (a)\nBugs (b)\nFossils (c)\nArt (d)\n")
        choice = input("Choose Category: ")
        print()
        
        if choice == "a":
            update_fish()
        if choice == "b":
            update_bug()
        if choice == "c":
            update_fossil()
        if choice == "d":
            update_art()  
        
        option = input("Return to main menu? (y/n): ")
        print()
        if option == "n":
            main_menu = False 
        
print("- - - - - - - - - - - -\nHAVE A NICE DAY !")
            
   
    

        

