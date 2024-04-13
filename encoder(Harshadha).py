def encoder(values):
    encoded_values = ""
    for value in values:
        if value == "7":
            encoded_values += '0'
        elif value == "8":
            encoded_values += '1'
        elif value == "9":
            encoded_values += '3'
        else:
            encoded_values += str(int(value)+3)
    return encoded_values

def decoder(encoded_values):
    decoded_values = ""
    for value in encoded_values:
        if value == '0':
            decoded_values += '7'
        elif value == '1':
            decoded_values += '8'
        elif value == '2':
            decoded_values += '9'
        else:
            decoded_values += str(int(value)-3)
    return decoded_values

def main():
    encoded_string = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3 Quit")
        opt = int(input("Please enter an option:"))

        if opt == 1:
            values = input("Please enter your password to encode:")
            encoded_string = encoder(values)
            print("Your password has been encoded and stored!")
        if opt ==2:
            decoded_string = decoder(encoded_string)
            print(f"Then encoded password is {encoded_string}, and the original password is {decoded_string}.")
        if opt == 3:
            break
