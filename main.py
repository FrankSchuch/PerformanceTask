
#Flashcard Practice App  
#Students store terms in a list, loop through them, and check answers.

#dictionary of flash card names and values
flash_list = [
    {"name": "George Washington", "def": "First president of the U.S"},
    {"name": "Anthony Guzman", "def": "Star basketball player for Hancock HS"},
    {"name": "Frank Schuch", "def": "Best student of all time"},
    {"name": "Lady Gaga", "def":  "Famous pop-star"}
]

def get_term(term_name):
    for term in flash_list:
        if term["name"] == term_name:
            return term
    return None 
