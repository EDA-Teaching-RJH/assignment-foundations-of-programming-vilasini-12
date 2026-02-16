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
  option = input("Select option: ").strip()   #asks user to input option and used .strip() to remove spaces
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
  print("{:<13} {:<13} {:<13} {:<13}".format("Name", "Ranks", "Division", "IDs"))   #prints title of the columns
  for i in range(len(names)):   #iterates through names list 
    print("{:<13} {:<13} {:<13} {:<13}".format(names[i], ranks[i], divs[i], ids[i]))    #prints each member's details in columms 

def search_crew(names, ranks, divs, ids):
  """
  This function takes input of all the lists and 
  asks user to input a search term and prints 
  any crew members' names with those terms. 
  """
  search = input("Enter term to find members: ").lower()    #asking for search term and used .lower() to make it case-insensitive
  found = False   #flag to track if match is found
  for i in range(len(names)):   #iterates through names list
    if search in str(names[i]).lower():   #used .lower() for case-insensitivity
      print(str(names[i]) + " - " + str(ranks[i]) + " - " + str(divs[i]) + " - " + str(ids[i]))   #prints name,rank,division and id for member's name containing term
      found = True    #flag to True as at least one match found
  if not found:   #if no matches after loop then say no members found
      print("No Members contain that.")

def filter_by_division(names, divs):
  """
  This function takes input of names and divs list and 
  asks user to input certain division name and prints
  members from the chosen division.
  """
  members = []    #empty list to add members name
  section = input("What division do you want to check: Command, Operations, Science: ").capitalize()    #used .capitalize() to prevent value error
  for i in range(len(divs)):    #iterates through divs list
    if divs[i] == section:    #checks if item in list matches user input
      members.append(names[i])    #add's member's name to members list
  return members

def calculate_payroll(ranks):
  """
  This function takes input of ranks list and 
  iterates through list, assign credit values to each rank 
  and calculates total cost of the crew.
  """
  total_pay = 0   #initialise variable to store total payroll cost
  for rank in ranks:    #iterates through ranks list
    if rank == "Captain": 
      total_pay += 1000    #assigning credit value to Captain
    elif rank == "Ensign":
      total_pay += 200    #assigning credit value to Ensign
    elif rank == "Lieutenant":
      total_pay += 700    #assigning credit value to Lieutenant
    elif rank == "Lt. Commander":
      total_pay += 800    #assigning credit value to Lt. Commander
    elif rank == "Commander":
      total_pay += 900    #assigning credit value to Commander
    elif rank == "Admiral":
      total_pay += 1200   #assigning credit value to Admiral
    else:
      print("Unknown rank")
  return total_pay    #return total cost of crew

def count_officers(ranks):
  """
  This function takes input of ranks list and 
  counts how many "Captains" and "Commanders" are
  in the crew.
  """
  count = 0   #initialise variable to store no of high-rank officers
  for rank in ranks:    #iterates through ranks list
    if rank == "Captain" or rank == "Commander":    #checks if rank is Captain or Commander
      count = count + 1   #count increment if rank is Captain or Commander
  return count    #returns total no of Captains and Commanders

def main():
  while True:   #infinite loop to show menu until exit chosen
    opt = display_menu()    #displays menu and stores value in opt
    if opt == "1":    #Option 1: display data 
      init_database()
    elif opt == "2":    #Option 2: Adds a new member to crew
      add_member(names, ranks, divs, ids)
    elif opt == "3":    #Option 3: Removes a member from crew
        remove_member(names, ranks, divs, ids)
    elif opt == "4":    #Option 4: Updates member's rank
        update_rank(names, ranks, ids)
    elif opt == "5":    #Option 5: Displays a formatted roster(table)
      display_roster(names, ranks, divs, ids)
    elif opt == "6":    #Option 6: Search for crew members
      search_crew(names, ranks, divs, ids)
    elif opt == "7":    #Option 7: Displays members from selected division
        print(f"Members in selected division: ", filter_by_division(names, divs))
    elif opt == "8":    #Option 8: Calculates and displays total crew payroll
      print("Total crew payroll: £", calculate_payroll(ranks))
    elif opt == "9":    #Option 9: Displays no of high ranking officers
      print("High ranking officers(Captains and Commanders): " , count_officers(ranks))
    elif opt == "10":   #Option 10: Exits program
      print("Shutting down.")
      break
    else:   #if invalid option entered, say invalid
      print("Invalid.")

main()