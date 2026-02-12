# Flashcard Practice App  
# Students store terms in a list, loop through them, and check answers.

# List of flashcards stored as dictionaries (each has a name + definition)
flash_list = [
    {"name": "george Washington", "def": "First president of the U.S"},
    {"name": "anthony Guzman", "def": "Star basketball player for Hancock HS"},
    {"name": "frank Schuch", "def": "Best student of all time"},
    {"name": "lady Gaga", "def":  "Famous pop-star"}
]

# Procedure: searches the list for a matching term name
# Parameter: term_name (affects which term is returned)
# Return value: the matching dictionary OR None
def get_term(term_name):
    for term in flash_list:                 # Iteration through the list
        if term["name"].lower() == term_name.lower():  
            return term                     # Return the found term
    return None                             # Return None if not found

# Procedure: prints the contents of a flashcard
# Parameter: term (the dictionary returned by get_term)
def tell_term(term):
    print("name is " + term["name"])
    print("Definition is " + term["def"])

# Procedure: adds a new flashcard to the list
# Parameters: new_name, new_def (optional — allows flexibility)
def add_new_term(new_name=None, new_def=None): 
    print("--- Add a New Term ---") 
    
    # If no parameters were passed, ask the user for input
    if new_name is None: 
        new_name = input("Enter a new figure in history's name: ").lower() 
    if new_def is None: 
        new_def = input("Enter a short definition: ") 
    
    # Create a new dictionary and add it to the list
    new_term = { "name": new_name, "def": new_def} 
    flash_list.append(new_term) 
    print(f"Term added under category '{new_term}'!")

# Main program loop
def program():
    # Initial prompt to start reviewing flashcards
    answer = input("Do you want to review a flash card? (yes or finished): ").lower()

    # Loop continues as long as the user types "yes"
    while answer == "yes":
        # Build a list of available flashcard names
        category_list = [term["name"] for term in flash_list]
        print(f"Available categories: {', '.join(category_list)}")
        
        # User chooses a term or adds a new one
        choice = input("Choose a category or type 'add' to add a new term: ").lower()
        
        if choice == "add":
            add_new_term()                  # Calls the add procedure
        else:
            selected_term = get_term(choice)  # Uses return value from get_term
            if selected_term:
                tell_term(selected_term)      # Displays the flashcard
            else:
                print("Sorry, that term doesn't exist.")
        
        # Ask whether to continue or finish
        answer = input("Do you want to hear another term or are you finished? (yes/finished): ").lower()

    # This section runs only when the user types "finished"
    rating = int(input("Rate our flash cards from 1–10: "))
    print(str(rating * 10) + "% satisfaction rate")

    recommend = input("Would you recommend this game to a friend? (yes/no): ").lower()
    if recommend in ["yes", "maybe"]:
        print("Thanks, we appreciate it!")
    else:
        print("Sorry you did not enjoy it.")

# Start the program
program()
