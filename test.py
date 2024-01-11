def reverse_string(input_string):
    return input_string[::-1]

def main():
    original_string = input("Entrez la chaîne à inverser : ")
    reversed_string = reverse_string(original_string)
    print("Chaîne inversée :", reversed_string)

if __name__ == "__main__":
    main()

