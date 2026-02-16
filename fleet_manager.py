names = ["Picard", "Riker", "Data", "Worf"]
ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
divs = ["Command", "Command", "Operations", "Science"]
ids = ["PC34", "RC29", "DO76", "WS43"]

def init_database():
  print("Current Crew List:")
  for i in range(10):
    list_length = len(names)
    if i >= list_length:
      break
    else:
      print(str(names[i]) + " - " + str(ranks[i]) + " - " + str(divs[i]) + " - " + str(ids[i]))

def filter_by_division(names, divs):
  members = []
  section = input("What division do you want to check: Command, Operations, Science: ").capitalize()
  for i in range(len(divs)):
    if divs[i] == section:
      members.append(names[i])
  return members

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
    print("1. View Crew")
    print("2. ")
    print("3. ")
    print("4. ")
    print("5. ")
    print("6. ")
    print("7. ")
    print("8. Members in Certain Division")
    print("9. Crew Payroll")
    print("10. Analyse Data: No of Captains and Commanders")
    print("11. Exit")

    opt = input("Select option: ")

    if opt == "1":
      init_database()
    #elif opt == "2":

    #elif opt == "3":

    #elif opt == "4":

    #elif opt == "5":

    #elif opt == "6":

    #elif opt == "7":

    elif opt == "8":
        print(f"Members in selected division: ", filter_by_division(names, divs))
    elif opt == "9":
      print("Total crew payroll: £", calculate_payroll(ranks))
    elif opt == "10":
      print("High ranking officers(Captains and Commanders): " , count_officers(ranks))
    elif opt == "11":
      print("Shutting down.")
      break
    else:
      print("Invalid.")


main()