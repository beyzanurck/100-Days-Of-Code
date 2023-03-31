#caesar-cipher: This application encode or decode your message so you can send a encryption message!
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message, jump):

    coded_word = ""
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)

            if direction == "encode":
                index += jump

                #to go back of the list
                if index > len(alphabet) - 1:
                    index = index - (len(alphabet) - 1)
                    index -= 1

            else:
                index -= jump   

            coded_word += alphabet[index]
        else:
            coded_word += char
    
    print(f"Here's the {direction}d result: {coded_word}!")
 
  
should_end = False

while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 26
    caesar(text, shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
