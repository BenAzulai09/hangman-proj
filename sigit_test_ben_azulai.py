
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if (check_valid_input(letter_guessed, old_letters_guessed) == True):
        old_letters_guessed += letter_guessed
        return letter_guessed
    else:
        print("     X")
        print("     letters that already have been guessed: ")
        old_letters_guessed.sort()
        x = "-> ".join(old_letters_guessed)
        print("     "+x)
        letter_guessed = input("       type vaild char: ")
        return try_update_letter_guessed(letter_guessed, old_letters_guessed)



def check_valid_input(letter_guessed, old_letters_guessed):
    if (letter_guessed.isalpha() == True) and (len(letter_guessed) > 1 ):
        return False
    elif (letter_guessed.isalpha() != True) and (len(letter_guessed) == 1 ):
        return False
    elif (len(letter_guessed) > 1) and (any(c.isalpha() for c in letter_guessed)):
        return False
    elif (old_letters_guessed.count(letter_guessed) >= 1):
        return False
    else:
        return True
def get_and_check_input():
    guess = input("Enter a letter: ")
    if len(guess) != 1:
        print("E1")
    elif not guess.isalpha():
        print("E2")
    elif not guess.isascii():
        print("E3")
    else:
        print(guess.lower())


def show_hidden_word(secret_word, old_letters_guessed):
    ret_str = ""
    i=0
    str_to_pass= str(secret_word)
    for po in range(len(str_to_pass)):
        if(old_letters_guessed.count(str_to_pass[i]) >= 1):
            ret_str += " "+ str_to_pass[i]
        else:
            ret_str += " _";
        i+=1
    return ret_str

def check_win(secret_word, old_letters_guessed):
    ret_str = ""
    i = 0
    str_to_pass = str(secret_word)
    for po in range(len(str_to_pass)):
        if (not(old_letters_guessed.count(str_to_pass[i]) >= 1)):
            return False
        i += 1
    return True


HANGMAN_PHOTOS = {1 :  "x-------x" , 2 : """
x-------x
|
|
|
|
|""" , 3 : """
x-------x
|       |
|       0
|
|
|
""" , 4 : """
x-------x
|       |
|       0
|       |
|
|
""", 5: """
x-------x
|       |
|       0
|      /|\\
|
|
""" , 6 : """
x-------x
|       |
|       0
|      /|\\
|      /
|
""" , 7 : """
x-------x
|       |
|       0
|      /|\\
|      / \\
|
"""}

def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])

def choose_word(file_path, index):
    with open(file_path, "r") as file_open:
        txt = file_open.read()
        x = txt.split(" ")
        x = list(dict.fromkeys(x))
        if(index > len(x)):
            while index > len(x):
                index = index - len(x)

        return (len(x), x[(index-1)% len(x)])

def main():
    HANGMAN_ASCII_ART = """Welcome to the game Hangman
 _    _                                         
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/"""
    MAX_TRIES = 6
    old_letters_guessed = []
    num_of_tries =0
    print(HANGMAN_ASCII_ART, " \n", MAX_TRIES)
    #input for path_to_file C:\Users\benaz\Documents\HANGMAN.txt
    path_to_file = input("please enter path to file: ")
    index = int(input("please enter index: "))
    secret_word = choose_word(path_to_file,index)[1]
    word_ = len(secret_word) * '_ '
    print_hangman(1)
    print(word_)
    while num_of_tries <=MAX_TRIES:
        guess_letter = input("Guess one letter and type it here: ")
        guess_letter = try_update_letter_guessed(guess_letter, old_letters_guessed)
        print(show_hidden_word(secret_word,old_letters_guessed))
        if secret_word.__contains__(guess_letter)==False:
            print(":(")
            num_of_tries = num_of_tries+1
            print_hangman(num_of_tries)
        if check_win(secret_word,old_letters_guessed)==True:
            print("!!!!!!!!!!!!!!!!!!WIN!!!!!!!!!!!!!!!!!!")
            break
    if check_win(secret_word,old_letters_guessed)==False:
        print("-------------------LOSE-------------------")



if __name__ == "__main__":
    main()

