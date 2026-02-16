names = ["Picard", "Riker", "Data", "Worf"]
ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
divs = ["Command", "Command", "Operations", "Science"]
ids = ["PC34", "RC29", "DO76", "WS43"]

def calculate_payroll(ranks):
  total_pay = 0
  for rank in ranks:
    if rank == "Captain":
      total_pay += 1000
    elif rank == "Ensign":
      total_pay += 200
    elif rank == "Lieutenant":
      total_pay += 700
    elif rank == "Lt. Commander":
      total_pay += 800
    elif rank == "Commander":
      total_pay += 900
    elif rank == "Admiral":
      total_pay += 1200
    else:
      print("Unknown rank")
  return total_pay

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

    if opt == "9":
      print("Total crew payroll: £", calculate_payroll(ranks))
    elif opt == "10":
      print("High ranking officers(Captains and Commanders): " , count_officers(ranks))
    elif opt == "11":
      print("Shutting down.")
      break
    else:
      print("Invalid.")


main()