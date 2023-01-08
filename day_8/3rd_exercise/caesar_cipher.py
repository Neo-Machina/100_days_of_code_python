alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar(message, shift_amount, crypt):
    text = ""

    for letter in message:
    # What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
        if letter in alphabet: 
            letter_position = alphabet.index(letter)
            if crypt == 'encode':
                new_letter_position = letter_position + shift_amount
                while new_letter_position > (len(alphabet) - 1):
                    new_letter_position -= (len(alphabet))
            elif crypt == 'decode':
                new_letter_position = letter_position - shift_amount
                while new_letter_position < 0:
                    new_letter_position += (len(alphabet))
            
            text += alphabet[new_letter_position]
        else:
            text += letter
                
    print(f"The {crypt}d text is {text}")

from art import logo
print(logo)
#Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
# keep_going = True
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

#What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

    caesar(message = text, shift_amount = shift, crypt = direction)
    
    run_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    while run_again != 'yes' and run_again != 'no':
        run_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    
    if run_again == 'no':
        print('Goodbye')
        break