# Originally Created: 2017
# Modified: 2019
# Made by Rhys Nicholas
# Shift cipher decryption tool
# Produced for a University Project

# Function Description:
# Function attempts to find pattern in frequent letters in cipher text with that of english
#
# Caesar(Text) where Text is the cipher text

def Caesar(Text):  # Define function
    from collections import Counter  # import code too count characters
    Shift = []

    # This loop takes each letter from the input string and makes them all lowercase, then inputs them into the list
    # called Shift[]
    for i in range(len(Text)):  # for each character in string
        if ord(Text[i]) in range(65, 91):  # if a capital letter in encrypted text (using on ascii)
            Shift.append(chr(ord(Text[i]) + 32))  # convert to lowercase and add to the list Shift[]
        if ord(Text[i]) in range(97, 123):  # if already lowercase in encrypted text (using ascii)
            Shift.append(Text[i])  # add to the list Shift
    # count all used letters giving a list of how many times each is used
    Frequency_List = Counter(Shift).most_common()
    # reduced list containing only used letters in order of frequency
    Frequency_Reduced = [elem[0] for elem in Frequency_List]

    # Let the five most frequent letters be the following variables
    First = Frequency_Reduced[0]
    Second = Frequency_Reduced[1]
    Third = Frequency_Reduced[2]
    Fourth = Frequency_Reduced[3]
    Fifth = Frequency_Reduced[4]
    Most_Frequent = [First, Second, Third, Fourth, Fifth]  # List of five most frequent shifted letters

    # reference list of four most frequent English letters after the letter "e" as "e" will be assumed in  loop
    Common_Letters = ["t", "a", "o", "i"]
    Predict = False  # set variable predict to false as this variable will be used to break the loop in case of success

    # Assumes most common letter in cipher text is "e", determines a shift key that yields another common letter in
    # cipher text with common letter in english
    for i in range(0, 6):  # Range of five for the five most frequent shifted letters
        # The most frequent shifted letters (in order) are assumed to be
        Assume_E_Cipher = (101 - ord(Most_Frequent[i])) % 26
        # "e" and the resultant shift number is saved to this variable
        for k in range(1, 6):  # Range of 4 for the remaining four most frequent shifted letters
            # The current Decipher of "e" is used on the remaining frequent shifted letters
            Assume_Letter = chr(((ord(Most_Frequent[(k % 5)]) - 97) + Assume_E_Cipher) % 26 + 97)
            if Assume_Letter in Common_Letters:  # If one one of these un-shifted letters are one of the remaining
                # Frequent English letters, then the current decipher has a good chance of being correct
                Predict = True  # Success is found, update success variable
                break  # break internal loop
        if Predict:
            break  # break external loop in case of success

    if Predict:  # In case of success
        print("Success")
        return (26 - Assume_E_Cipher) % 26  # Using the success decipher, return relevant shift

    if not Predict:  # In case of no success
        print("No Success")
        return (26 - (101 - ord(
            First))) % 26  # Assume most frequent shifted letter is "e", return relevant shift
