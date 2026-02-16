names = ["Picard", "Riker", "Data", "Worf"]
ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
divs = ["Command", "Command", "Operations", "Science"]
ids = ["PC34", "RC29", "DO76", "WS43"]

def init_database():
  """
  Displays the 4 lists with data stored
  """
  print("Current Crew List:")
  for i in range(10):
    list_length = len(names)  #finding length of names list
    if i >= list_length:
      break    #prevents IndexError if the list index out of range
    else:
      print(str(names[i]) + " - " + str(ranks[i]) + " - " + str(divs[i]) + " - " + str(ids[i]))   #prints name,rank,division and id for each member

def display_menu():
  """
  This function takes input of user's full name 
  and gives options for user to select from.
  Returns the user's selected option.
  """
  user_name = input("Type your full name: ").title()  #using .title() capitalises first letter of each name part
  print(f"Welcome {user_name}, please view the MENU: \n1. View Crew\n2. Add Member\n3. Remove Member\n4. Update Rank"
        "\n5. Display Roster\n6. Search Crew\n7. Members in Certain Division\n8. Crew Payroll" 
        "\n9. Analyse Data: No of Captains and Commanders\n10. Exit")
  option = input("Select option: ")   #asks user to input option
  return option


def add_member(names, ranks, divs, ids):
  """
  This function takes input of all the lists and 
  asks user to give new data to add onto the lists.
  new ID and new rank are validated before adding data onto 4 lists
  """
  new_name = input("Name: ").capitalize()   #using .capitalize() to prevent value error
  new_rank = input("Rank: ").capitalize()
  new_div = input("Division: ").capitalize()
  new_id = input("ID: ").upper()    #using .upper() to prevent value error
  if new_id in ids:
    print("ID already exists")  #validating that ID is unique
    return
  if new_rank not in ["Ensign", "Lieutenant", "Lt. Commander", "Commander", "Captain", "Admiral"]:
    print("Not valid rank")   #validating that rank follows TNG rank
    return
  names.append(new_name)    #adding new name to name list
  ranks.append(new_rank)    #adding new rank to rank list
  divs.append(new_div)    #adding new division to divs list
  ids.append(new_id)    #adding new ID to ids list

def remove_member(names, ranks, divs, ids):
    """
    This function takes input of all the lists and 
    asks user to give ID of member to remove. 
    Index is found using ID and details of member 
    removed from all lists using index.
    """
    rem = input("Type in ID of member to remove: ").upper()
    if rem in ids:    #checks if id matches with ids list
        idx = ids.index(rem)  #this is the index of the member
        names.pop(idx)    #removes name in that index
        ranks.pop(idx)    #removes rank in that index
        divs.pop(idx)     #removes division in that index
        ids.pop(idx)    #removes id in that index
        print("Member removed.")
    else:   #prints string if id not found
      print("Invalid ID")

def update_rank(names, ranks, ids):
  """
  This function takes input of names, ranks and ids lists.
  Takes user's input of ID to update the corresponding 
  member's ranking.
  """
  update = input("Enter ID of member to update rank: ").upper()   #used .upper() to prevent value error
  if update in ids:   #checks if id matches with ids list
    idx = ids.index(update)   #uses index to find member's name
    name = names[idx]
    new_rank = input("Enter new rank: ").capitalize()   #using .capitalise() to prevent value error
    if new_rank not in ["Ensign", "Lieutenant", "Lt. Commander", "Commander", "Captain", "Admiral"]:
      print("Not valid rank")   #validates rank follows TNG rank
      return
    ranks[idx] = new_rank   #replaces old rank with new rank
    print(f"{name}'s Rank updated.")
  else:   #if wrong id entered, prints match not found
    print("No ID match found")

def display_roster(names, ranks, divs, ids):
  """
  This function takes input of all the lists and 
  iterates through the list using 'range(len(names))'
  and prints a formatted table of crew.
  """
  print("{:<13} {:<13} {:<13} {:<13}".format("Name", "Ranks", "Division", "IDs"))
  for i in range(len(names)):   #iterates through list 
    #print(str(names[i]) + " - " + str(ranks[i]) + " - " + str(divs[i]) + " - " + str(ids[i]))    #prints name,rank,division and id for each member
    print("{:<13} {:<13} {:<13} {:<13}".format(names[i], ranks[i], divs[i], ids[i]))

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