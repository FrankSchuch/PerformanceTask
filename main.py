#Flashcard Practice App  
#Students store terms in a list, loop through them, and check answers.

#dictionary of flash card names and values
flash_list = [
    {"name": "george washington", "def": "First president of the U.S"},
    {"name": "anthony guzman", "def": "Star basketball player for Hancock HS"},
    {"name": "frank schuch", "def": "Best student of all time"},
    {"name": "lady gaga", "def":  "Famous pop-star"}
]

def get_term(term_name):
    for term in flash_list:
        if term["name"] == term_name:
            return term
    return None 

def tell_term(term):
    print("name is " + term["name"])
    print("Definition is " + term["def"])

def add_new_term(new_name=None, new_def=None): 
    print("--- Add a New Term ---") 
    if new_name is None: 
        new_name = input("Enter a new figure in history's name: ").lower() 
    if new_def is None: 
        new_def = input("Enter a short definition: ") 
    new_term = { "name": new_name, "def": new_def} 
    flash_list.append(new_term) 
    print(f"Term added under category '{new_term}'!")

def program():
    answer = input("Do you want to review a flash card? (yes or no): ").lower()

    if answer == "no":
        done = input("Are you finished? (yes/no): ").lower()
        if done == "yes":
            answer = "finished"
        else:
            answer = "yes"

    while answer == "yes":
        category_list = [term["name"] for term in flash_list]
        print(f"Available categories: {', '.join(category_list)}")

        choice = input("Choose a category or type 'add' to add a new term: ").lower()

        if choice == "add":
            add_new_term()
        else:
            selected_term = get_term(choice)
            if selected_term:
                tell_term(selected_term)
            else:
                print("Sorry, that term doesn't exist.")

        answer = input("Do you want to hear another term? (yes/finished): ").lower()

    if answer == "finished":
        rating = int(input("Rate our flash cards from 1–10: "))
        print(str(rating * 10) + "% satisfaction rate")

        recommend = input("Would you recommend this game to a friend? (yes/no): ").lower()
        if recommend in ["yes", "maybe"]:
            print("Thanks, we appreciate it!")
        else:
            print("Sorry you did not enjoy it.")
program()
