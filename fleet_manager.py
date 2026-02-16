names = ["Picard", "Riker", "Data", "Worf"]
ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
divs = ["Command", "Command", "Operations", "Science"]
ids = ["PC34", "RC29", "DO76", "WS43"]


def count_officers(ranks):
  count = 0
  for rank in ranks:
    if rank == "Captain" or rank == "Commander":
      count = count + 1
  return count

def main():
  while True:
    print("\n--- MENU ---")
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. ")
    print("5. ")
    print("6. ")
    print("7. ")
    print("8. ")
    print("9. ")
    print("10. Analyse Data: No of Captains and Commanders")
    print("11. Exit")

    opt = input("Select option: ")

    #if opt == "1":

    #elif opt == "2":

    #elif opt == "3":

    #elif opt == "4":

    #elif opt == "5":

    #elif opt == "6":

    #elif opt == "7":

    #elif opt == "8":

    #elif opt == "9":

    if opt == "10":
      print("High ranking officers(Captains and Commanders): " , count_officers(ranks))
    elif opt == "11":
      print("Shutting down.")
      break
    else:
      print("Invalid.")


main()