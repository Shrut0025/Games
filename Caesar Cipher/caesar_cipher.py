print("WELCOME TO CAESAR CIPHER , A TECHNIQUE TO SEND SOMEONE SECRET MESSAGE WITH THE HELP OF ENCRYPTION AND DECRYPTED")

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text,shift_key):
    cipher_text = " "
    for char in plain_text:
        position = alphabet.index(char)
        new_position = (position + shift_key) % 26
        cipher_text += alphabet[new_position]
    print(f"Cipher text = {cipher_text}")

def decryption(cipher_text,shift_key):
    plain_text = " "
    for char in cipher_text:
        position = alphabet.index(char)
        new_position = (position - shift_key) % 26
        plain_text += alphabet[new_position]
    print(f"Plain text = {plain_text}")

end = False
while not end:
    to_do = input("Enter 'e' for encryption , 'd' for decryption : ").lower()
    text = input("Enter your message : ").lower()
    shift = int(input("Enter the shift key = "))

    if to_do == 'e':
        encryption(plain_text=text,shift_key=shift)
    elif to_do == 'd':
        decryption(cipher_text=text,shift_key=shift)

    play_again = input("Enter 'y' for yes and 'n' for no : ")
    if play_again == 'n' :
        end = True
        print("THnak you. Have a good day ahead!")    