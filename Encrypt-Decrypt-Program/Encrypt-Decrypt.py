alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt_decrypt(given_text, shift_amount, chosen_method):
    end_text = ""
    if chosen_method == "decrypt":
        shift_amount *= -1
    for char in given_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {chosen_method}ion is successfully finished")
    print(f"The result is {end_text}.")

print("Welcome to Encrypt-Decrypt program !")
while True:
    method = input("Do you want to Encrypt or Decrypt ? \n: ").lower()
    text = input("Type your message \n: ").lower()
    shift = int(input("Type the shift amount \n: "))
    if shift > 26:
        shift %= 26
    encrypt_decrypt(given_text=text, shift_amount=shift, chosen_method=method)
    user_decision = input("Do you want to do another Encryption or Decryption ? y/n \n: ").lower()
    if user_decision == "n":
        print("Leaving program...")
        break
