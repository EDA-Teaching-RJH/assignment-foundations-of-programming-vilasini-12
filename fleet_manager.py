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

def display_menu():
  user_name = input("Type your full name: ").title()
  print(f"Welcome {user_name}, please view the MENU: \n1. View Crew\n2. Add Member\n3. Remove Member\n4. Update Rank"
        "\n5. Display Roster\n6. Search Crew\n7. Members in Certain Division\n8. Crew Payroll" 
        "\n9. Analyse Data: No of Captains and Commanders\n10. Exit")
  option = input("Select option: ")
  return option


def add_member(names, ranks, divs, ids):
  new_name = input("Name: ").capitalize()
  new_rank = input("Rank: ").capitalize()
  new_div = input("Division: ").capitalize()
  new_id = input("ID: ").upper()
  new_id = str(new_id)
  if new_id in ids:
    print("ID already exists")
    return
  if new_rank not in ["Ensign", "Lieutenant", "Lt. Commander", "Commander", "Captain", "Admiral"]:
    print("Not valid rank")
    return
  names.append(new_name)
  ranks.append(new_rank)
  divs.append(new_div)
  ids.append(new_id)

def remove_member(names, ranks, divs, ids):
    rem = input("Type in ID of member to remove: ").upper()
    if rem in ids:
        idx = ids.index(rem)
        names.pop(idx)
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx)
        print("Member removed.")

def update_rank(names, ranks, ids):
  update = input("Enter ID of member to update rank: ").upper()
  if update in ids:
    idx = ids.index(update)
    name = names[idx]
    new_rank = input("Enter new rank: ").capitalize()
    if new_rank not in ["Ensign", "Lieutenant", "Lt. Commander", "Commander", "Captain", "Admiral"]:
      print("Not valid rank")
      return
    ranks[idx] = new_rank
    print(f"{name}'s Rank updated.")
  else:
    print("No ID match found")

def display_roster(names, ranks, divs, ids):
  print("Name - Ranks - Division - IDs")
  for i in range(len(names)):
    print(str(names[i]) + " - " + str(ranks[i]) + " - " + str(divs[i]) + " - " + str(ids[i]))

def search_crew(names, ranks, divs, ids):
  search = input("Enter term to find members: ")
  found = False
  for i in range(len(names)):
    if search in str(names[i]):
      print(str(names[i]) + " - " + str(ranks[i]) + " - " + str(divs[i]) + " - " + str(ids[i]))
      found = True
  if not found:
      print("No Members contain that.")

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
    opt = display_menu()

    if opt == "1":
      init_database()
    elif opt == "2":
      add_member(names, ranks, divs, ids)
    elif opt == "3":
        remove_member(names, ranks, divs, ids)
    elif opt == "4":
        update_rank(names, ranks, ids)
    elif opt == "5":
      display_roster(names, ranks, divs, ids)
    elif opt == "6":
      search_crew(names, ranks, divs, ids)
    elif opt == "7":
        print(f"Members in selected division: ", filter_by_division(names, divs))
    elif opt == "8":
      print("Total crew payroll: £", calculate_payroll(ranks))
    elif opt == "9":
      print("High ranking officers(Captains and Commanders): " , count_officers(ranks))
    elif opt == "10":
      print("Shutting down.")
      break
    else:
      print("Invalid.")

main()