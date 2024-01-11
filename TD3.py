# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def reverse_string(input_string):
    return input_string[::-1]

def main():
    original_string = input("Entrez la chaîne à inverser : ")
    reversed_string = reverse_string(original_string)
    print("Chaîne inversée :", reversed_string)

if __name__ == "__main__":
    main()
