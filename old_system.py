n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        loading = loading + 1 # adding missing increment 
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":  # changed from "=" to "=="
            print("Current Crew List:")
            
            for i in range(10):   # fixed the for loop so that it is within range
                list_length = len(n)
                if i >= list_length: 
                    break
                else: 
                    print(str(n[i]) + " - " + str(r[i]) + " - " + str(d[i]))  #n[i] and r[i] are not strings so changed them to one also added division, prevents type error

                
        elif opt == "2":
            new_name = input("Name: ").capitalize() # capitalizing all words 
            new_rank = input("Rank: ").capitalize()
            new_div = input("Division: ").capitalize()
            
           
            n.append(new_name)
            r.append(new_rank) # added new rank to the list
            d.append(new_div) # added new division to the list
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
            if rem in n:   # prevents value error if not found
                idx = n.index(rem)
                n.pop(idx)
                r.pop(idx)
                d.pop(idx)
                print("Removed.")
            else:
                print("was not found") 
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or rank =="Commander": # adding rank to commander 
                    count = count + 1
            print("High ranking officers: ", count) # changed from "+" to "," fixed type error
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")

run_system_monolith() # added "()" to call function
