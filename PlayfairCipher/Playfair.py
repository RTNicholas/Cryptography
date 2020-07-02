# Created: 28/11/2019
# Made by Rhys Nicholas
# Playfair cipher decryption tool
# Produced for University Project

# Function Description:
# Function attempts to loop through possible arrangements of input mappings
#   returns results where no arrangement conflicts were found
# Input must be a list of digraphs, where each even element is mapped to right neighbouring element
# input should lowercase
#
# playfair([xy,xz,ab,dc]) implies xy -> xz, ab -> dc, are assumed mappings


##============Useful Functions============##
def Remove(List, Indexes):
    Indexes.sort(reverse=True)

    # Removes elements in order of largest to smallest, so that no element position is changed before it's removed
    for i in range(len(Indexes)):
        del List[Indexes[i]]


# Returns the number of the letter for a=0,b=0...z=25
def letter(x):
    return ord(x) - 97


# Counts the number of a given element in a list of lists and checks if it is more than a given parameter
def size(x, f, c=""):  # x= List of lists, f = number threshold to count, c = character to count ("" if none given)
    No = 0
    for s in range(len(x)):  # Loop to count in range of list of lists
        if x[s].count(c) >= f:
            No = No + 1
    return No


# Converts Decimal to Ternary
def tern(x, L):  # Define function, x = decimal value, L = preferred length

    # Define variables
    T = []  # Variable to hold Ternary output digits
    start = L  # Variable for size of ternary, assume start at preferred length (working to 0)

    # Loop to find if preferred length of ternary is necessary length
    for i in range(L, 3 * x):  # Begin at L (preferred length) up to arbitrary value until necessary size is found
        if 2 * (3 ** i) >= x:  # Value is large enough if 2 lots of 3^value is larger than the input decimal
            start = i  # start variable takes the necessary start value
            break  # Break as loop need only run until value is found

    # Loop to obtain ternary
    for j in range(start, -1, -1):  # Loop from starting value to 0, the size of the ternary, working left to right
        for i in range(2, -1, -1):  # Loop through 2,1,0 for each element of the ternary
            if i * (
                    3 ** j) <= x:  # For 3^k for each element, left to right (decreasing size), if 2 lots is less
                # than the Decimal input there is a 2 in this position else, if 1 lot is less then there is 1 else it
                # must be a 0
                T.append(i)  # Input 2,1,0 for which ever came out as less than the decimal
                x = x - i * (3 ** j)  # Update decimal by subtracting the relevant 3^k lots
                break  # Break to assure 2 and 1 is not overwritten by the 1,0 lots of 3^k that is less than them
    # Preferred length test
    if len(T) > L:  # If Ternary is larger than preferred length
        for i in range(len(T)):  # Loop for range elements in ternary
            if T[i] == 0 and len(T) > L:  # Remove leading 0s until Preferred length is met or until a leading non zero
                T.remove(0)
            else:
                break  # Break if non zero leading value or length is now preferred

    # output ternary string
    return ''.join(str(i) for i in T)


##============Main Playfair Function============##
def playfair(x, Map=""):
    from itertools import combinations  # Tool to produce combinations

    # Alphabet, Playfair grid, List of mappings
    A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
    GRID = [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""],
            ["", "", "", "", ""]]  # List of lists, can work similar to a matrix
    PAIRS = []  # Variable to hold the input assumed mappings

    # Generations, Equal to half total digraphs put in, or the number of mappings since a mapping is 2 digraphs
    Gen = int(0.5 * len(x))

    # Covert input into list of strings such that XY -> xy = "XxYy"
    for i in range(0, Gen):
        z = [x[2 * i][0], x[2 * i + 1][0], x[2 * i][1], x[2 * i + 1][1]]
        PAIRS.append("".join(z))
    if Map != "":  # If fixed permutation used for any mapping, Print this
        print('Modied calculations:', Map)

    ##### Analysis Section:
    ##### Check Ways to reduce permutations and to assure input is valid    
    Perm = []
    for i in range(len(PAIRS)):
        if len(set(PAIRS[i])) <= 2 or len(set(PAIRS[i])) > 4 or PAIRS[i][0] == PAIRS[i][1] or PAIRS[i][2] == PAIRS[i][
            3]:  # if mapping too big or too small, or if any letter is mapped to itself
            return print("Invalid Input", PAIRS[i])  # Input doesn't work

        # Find permutations that can be avoided beforehand
        # Size 3 mappings that share an element have specific ways they can be arranged together
        else:
            for j in range(len(PAIRS)):
                if i != j and len(set(PAIRS[i])) == 3 and len(set(PAIRS[
                                                                      j])) == 3:  # Call pairs of size 3 (Row/Col),
                    # if they share first or second letters they have certain ways to be arranged together
                    if PAIRS[i][0] in PAIRS[j] or PAIRS[i][1] in PAIRS[
                        j]:  # i and j mapping must occur as oposing col/row
                        Perm.append([i, j])

    # Print initial message with info about the input
    print("Calculating for:", Gen, "Generations", tern(0, Gen), " to", tern(3 ** Gen - 1, Gen), "(", 3 ** Gen, ")")
    print("Key: 0 = Row, 1 = Column, 2 = Square")

    Invalid = 0  # Variable to test if a permutation is invalid,

    # Loop of all permutations
    # Uses ternary of size equal to the number of mappings/generations
    for i in range(0,
                   int(3 ** Gen)):  # Loops for the number of permutations of input positions that can take 3 outcomes
        if Invalid == 0 and i > 0:  # Was last permutation Valid?
            # Print Permutation and information if Valid
            print('Permutation =', tern(i - 1, Gen))
            print("Playfair =", GRID)
            if len(GRID2) != 0:
                print("Unkown Rows =", GRID2)
            if len(GRID4) != 0:
                print("Unkown Columns =", GRID4)

        # Var reset
        A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
        GRID = [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""],
                ["", "", "", "", ""]]
        Invalid = 0
        # Passionless Grids: Used when we know elements that appear together but not where they go in the Playfair grid
        GRID2 = []  # Must be same row
        GRID3 = []  # Must not be same row
        GRID4 = []  # Must be same column
        Unknown = []  # Used as a reference for cases where an letter has been used but has no location (Positionless
        # grids)

        Comb = tern(i,
                    Gen)  # Coverts current number to ternary, representing the current Row/Col/Sqaure (0/1/2)
        # Permutation

        for j in range(
                Gen):  # Loop for number of Ternary Tree Generations, For every permutation of Row/Col/Sqaure (0/1/2)
            if Invalid == 1:  # Validity check
                break

            test = Comb[j]  # Variable to determine current part of the Row/Col/Sqaure (0/1/2) permutation
            if Map != "" and Map[
                j] != 'x':  # Force outcomes of specific format, breaking without testing anything if it doesn't match
                if test != Map[j]:
                    Invalid = 1
                    break

            # From Analysis section, Checks any mappings that must occur together in a certain way do
            for p in range(len(Perm)):
                if Comb[Perm[p][0]] == Comb[Perm[p][1]] and Comb[Perm[p][0]] in ['0', '1']:
                    Invalid = 1
                    break
            # Location Variables: Used to store locaton if a letter exists in the grid already and to check if it
            # conflicts with other locations of current mapping
            Loc = ""  # Locations are in terms of Rows
            Loc2 = ""  # Location Variable for Square (Squares have 2 rows therefore need 2 variables)

            Unknown = []  # Reset variable

            # ######### This section tries tests if the current mapping filters the current mapping to the current
            # permutation of Row = 0, Column = 1, Square = 2 ###############################
            if test == "0":  # Row Permutation

                # Try and find a location in the grid
                for m in range(0, 4):  # Check each letter of current mapping
                    if PAIRS[j][m] not in A and Loc == "" and len(A[letter(PAIRS[j][
                                                                               m])]) == 2:  # If it exists in the
                        # grid then, any other location has to be in the same row
                        Loc = int(A[letter(PAIRS[j][m])][0])  # Set the location to be that row
                    if PAIRS[j][m] not in A and int(A[letter(PAIRS[j][m])][0]) != Loc and len(A[letter(
                            PAIRS[j][m])]) == 2:  # If other letter is found in different a row then there is a conflict
                        Invalid = 1  # Invalid Grid found
                        break
                    elif PAIRS[j][m] not in A and len(
                            A[letter(PAIRS[j][m])]) == 1:  # If unknowns (used but position-less), we note which letters
                        Unknown.append(PAIRS[j][m])

                # No location found -> Append mapping to position-less Rows
                if Loc == "" and Invalid == 0:
                    GRID2.append([])
                    for m in range(0, 4):  # For each element in mapping
                        if PAIRS[j][m] not in GRID2[
                            len(GRID2) - 1]:  # If not already in list (Duplicates e.g TH ->he  "ThHe" /"the"/)
                            GRID2[len(GRID2) - 1].append(PAIRS[j][m])  # Append
                            # Coordinates Will be updated after Position-less Analysis

                ##Location determined, attempt to input into Playfair Grid
                if Loc != "" and Invalid == 0:
                    for m in range(0, 4):  # For each letter in mapping
                        if Invalid == 1:  # Validity check to break loop
                            break
                        for n in range(0, 5):  # For size of playfair row
                            if GRID[Loc][n] == "" and PAIRS[j][m] not in GRID[
                                Loc]:  # If position is free and element not already here (Duplicates and overlapping
                                # mappings)
                                GRID[Loc][n] = PAIRS[j][m]  # Put non existing letter in grid in this position

                            elif GRID[Loc].count("") == 0 and PAIRS[j][m] not in GRID[
                                Loc]:  # No free position but letter to input, Invalidity found
                                Invalid = 1  # Invalid
                                break

                        # If there were unknown positions  (Position-less)
                        if len(Unknown) != 0:
                            for u in range(len(Unknown)):  # For all unknowns
                                Fix = []  # Mistake in code, used to fix rather than redesign (To save time)
                                Fix.append(int(
                                    A[letter(
                                        Unknown[u])]))  # Used to Skip if unknowns were in the same postion-less row
                                if int(A[letter(Unknown[u])]) in Fix:
                                    continue
                                for g in range(len(GRID2[int(A[letter(
                                        Unknown[u])])])):  # For position-less row of each unknown in current mapping
                                    for n in range(0, 5):  # For size of playfair row
                                        if GRID[Loc][n] == "" and GRID2[int(A[letter(Unknown[u])])][g] not in GRID[
                                            Loc]:  # If position is free and current letter not in current playfair row
                                            GRID[Loc][n] = GRID2[int(A[letter(Unknown[u])])][
                                                g]  # Put non existing letter in grid in this position

                                        elif GRID[Loc].count("") == 0 and GRID2[int(A[letter(Unknown[u])])][g] not in \
                                                GRID[Loc]:  # No free position but letter to input, Invalidity found
                                            Invalid = 1  # Invalid
                                            break

                                if Invalid == 0:  # Remove anything used from position-less in playfair grid
                                    del GRID2[int(A[letter(Unknown[u])])]

                        # Update Coordinates of everything in Playfair grid
                        for N in range(0, 5):
                            for n in range(0, 5):
                                if GRID[N][n] != "":
                                    A[letter(GRID[N][n])] = "".join([str(N), str(n)])

                                    ######################
            if test == "1":  # Column Permutation
                # Program doesn't aim to produce correct columns, column permutation just assures things that should
                # be in a column could be without conflict

                Loc = []  # Convert location into vector, Column location is treated as a list of rows (unique
                # letters of mapping must then be in different rows)
                # Find location
                GRID4.append([])  # Position-less columns
                for m in range(0, 4):  # For each letter of mapping
                    GRID4[len(GRID4) - 1].append(PAIRS[j][m])  # Append to Position-less Columns
                    # Test if any different letters share a row location
                    if PAIRS[j][m] not in A and int(A[letter(PAIRS[j][m])][0]) not in Loc and len(
                            A[letter(PAIRS[j][m])]) == 2:  # If locations exists and don't conflict (
                        Loc.append(int(A[letter(PAIRS[j][m])][0]))  # Append location
                    if PAIRS[j][m] not in A and int(A[letter(PAIRS[j][m])][0]) in Loc and PAIRS[j].count(
                            PAIRS[j][m]) == 2:  # In case of duplicate letters
                        Loc.append(int(A[letter(PAIRS[j][m])][0]))  # Append location anyway

                    if PAIRS[j][m] in A:  # If letter currently unused
                        Loc.append("")
                    if PAIRS[j][m] not in A and int(A[letter(PAIRS[j][m])][0]) in Loc and len(
                            A[letter(PAIRS[j][m])]) == 2 and PAIRS[j].count(
                        PAIRS[j][m]) != 2:  # If two different letters share a row columns aren't valid
                        Invalid = 1  # Invalid
                        break

                    # If letter exists in position-less
                    elif PAIRS[j][m] not in A and len(
                            A[letter(PAIRS[j][m])]) == 1:  # If unknowns (used but position-less), we note which letters
                        Unknown.append(PAIRS[j][m])
                        Loc.append("U")

                # Append to position-less as own row if no location for any letter in mapping
                if Invalid == 0:
                    for m in range(0, 4):
                        if Loc[m] == "" and list(PAIRS[j][
                                                     m]) not in GRID2:  # Append new letters of this permutation to
                            # postion-less row (excluding duplicates)
                            GRID2.append([PAIRS[j][m]])

                if Invalid == 0:
                    Col = list(
                        combinations(PAIRS[j], 2))  # List of combinations of size 2 of all letters in current mapping
                    for c in range(len(
                            Col)):  # Append them as lists to the anti row grid, if any of these appear together in a
                        # row, this is used to invalidate it
                        if c not in GRID3 and Col[c][0] != Col[c][1]:  # Covert to list from set
                            GRID3.append(list(Col[c]))

            ######################   
            if test == "2":  # Sqaure permutation
                if len(set(PAIRS[j])) != 4:  # Make sure current mapping has 4 unique letters to form a square
                    Invalid = 1
                else:
                    # Look for locations (2 Locations for 2 Rows)
                    for m in range(0, 4):  # For size of a mapping
                        # Makes sure 0th and 1st share a row and 2nd and 3rd share a row if a location for them exists
                        if PAIRS[j][m] not in A and len(A[letter(PAIRS[j][m])]) == 2 and m == 0:
                            Loc = A[letter(PAIRS[j][m])][0]  # Update Location
                        if PAIRS[j][m] not in A and len(A[letter(PAIRS[j][m])]) == 2 and m == 1 and Loc != int(
                                A[letter(PAIRS[j][m])][0]):
                            Invalid = 1  # Invalid (0th & 1st don't share row)
                            break
                        if PAIRS[j][m] not in A and len(A[letter(PAIRS[j][m])]) == 2 and m == 2:
                            Loc2 = A[letter(PAIRS[j][m])][0]  # Update Location 2
                        if PAIRS[j][m] not in A and len(A[letter(PAIRS[j][m])]) == 2 and m == 3 and Loc2 != int(
                                A[letter(PAIRS[j][m])][0]):
                            Invalid = 1  # Invalid (2nd & 3rd don't share row)
                            break
                        if Loc == Loc2 and Loc != "":  # Make sure the 2 locations aren't the same
                            Invalid = 1
                            break
                        if PAIRS[j][m] not in A and len(A[letter(PAIRS[j][m])]) == 1:  # In case of positionless
                            Unknown.append(PAIRS[j][m])  # Reference of unkown positions in mapping

                # Note: 1 (number), l (letter) look the same in this font
                if Invalid == 0:
                    L = [Loc, Loc2]  # List of the 2 Locations
                    for l in range(0, 2):  # Loop for 2 Locations
                        if L[l] != "":  # If there is a Location
                            for m in range(0, 2):  # For each letter each half of the square (2)
                                for n in range(0, 5):  # For size of playfair row
                                    if GRID[int(L[l])][n] == "" and PAIRS[j][m + (2 * l)] not in GRID[
                                        int(L[l])]:  # If position free and letter not already in row
                                        GRID[int(L[l])][n] = PAIRS[j][m]  # Put non exisiting letter in grid

                                    elif GRID[int(L[l])].count("") == 0 and PAIRS[j][m + (2 * l)] not in GRID[
                                        int(L[l])]:  # No free position but letter to input, Invalidity found
                                        Invalid = 1  # Invalid
                                        break
                                # If letter in postion-less attempt to put position-less row into playfair for current
                                # location
                                if PAIRS[j][m + (2 * l)] in Unknown and Invalid == 0:
                                    for g in range(len(GRID2[int(
                                            A[letter(PAIRS[j][m + (2 * l)])])])):  # for each letter in postion-less row
                                        for n in range(0, 5):  # For size of playfair row
                                            # If letter not in row (since Unknown letter already input but also in
                                            # position-less)
                                            if GRID[int(L[l])][n] == "" and GRID2[
                                                int(A[letter(PAIRS[j][m + (2 * l)])])] not in GRID[int(L[l])]:
                                                GRID[int(L[l])][n] = GRID2[int(A[letter(PAIRS[j][m + (2 * l)])])][
                                                    g]  # Put non existing letter in grid
                                            elif GRID[int(L[l])].count("") == 0 and \
                                                    GRID2[int(A[letter(PAIRS[j][m + (2 * l)])])][g] not in GRID[
                                                int(L[l])]:  # No free position but letter to input, Invalidity found
                                                Invalid = 1  # Invalid
                                                break

                            # Update Coordinates of everything in Playfair grid
                            for N in range(0, 5):
                                for n in range(0, 5):
                                    if GRID[N][n] != "":
                                        A[letter(GRID[N][n])] = "".join([str(N), str(n)])

                                        # If there isn't a location
                        if L[l] == "" and Invalid == 0:
                            GRID2.append(
                                [PAIRS[j][0 + 2 * l], PAIRS[j][1 + 2 * l]])  # Append as new to the position-less rows

                    if Invalid == 0:  # Append combinations of 4 letters that should be in columns to Anti row grid
                        GRID3.append([PAIRS[j][0], PAIRS[j][2]])
                        GRID3.append([PAIRS[j][0], PAIRS[j][3]])
                        GRID3.append([PAIRS[j][1], PAIRS[j][2]])
                        GRID3.append([PAIRS[j][1], PAIRS[j][3]])

            ##### Unknown and Position-less
            ###############################
            if len(GRID2) > 0 and Invalid == 0:  # If there are position-less elements

                Shared = 0  # Variable for while loop
                B = 0  # Variable to break double loop

                # Loop for everything in the position-less row grid and combine all lists that share elements
                while Shared == 0 and len(GRID2) > 0:
                    if B == 1 and Shared == 0:  # Break loop when complete, restart loop if reference size has
                        # changed (due to combining lists)
                        B = 0
                    for g in range(len(GRID2)):  # For each position-less row
                        if B == 1:  # Break when reference has changed
                            break
                        else:
                            for G in range(len(GRID2)):  # For each position-less row
                                if g != G and any(let in GRID2[g] for let in GRID2[
                                    G]):  # Compare two different lists (rows) in GRID2 and return true if they share
                                    # elements
                                    GRID2.append(list(set(GRID2[g]).union(set(GRID2[
                                                                                  G]))))  # Append a list that is the
                                    # combination of the two lists (without duplicates)
                                    Remove(GRID2, [G, g])  # Use remove function to correctly remove original two lists
                                    B = 1  # Restart loop as reference lists has changed
                                    break
                                elif g == len(
                                        GRID2) - 1 and G == g:  # Loop has finished combining overlaping postionless row
                                    Shared = 1  # Allow loop to end

                # Check if any letters that shouldn't be put into the same row have been put into the same postionless row
                if len(GRID3) > 0:
                    for g in range(len(GRID3)):  # For range of anti rows
                        if Invalid == 1:  # /Break if invalidity found/
                            break
                        else:
                            for G in range(
                                    len(GRID2)):  # If any of the anti grid pairs are found as a subset in postionless
                                if set(GRID3[g]) <= set(GRID2[G]):
                                    Invalid = 1  # Invalid
                                    break
                # Reset Variables
                Shared = 0
                B = 0
                # Loop for everything in the postionless column grid and combine all lists that share elements (Same Loop as prior)
                while Shared == 0 and len(GRID4) > 0:
                    if B == 1 and Shared == 0:  # Break loop when complete, restart loop if reference size has changed (due to combining lists)
                        B = 0
                    for g in range(len(GRID4)):  # For each position-less row
                        if B == 1:  # /Break when reference has changed/
                            break
                        else:
                            for G in range(len(GRID4)):  # For each position-less column
                                if g != G and any(let in GRID4[g] for let in GRID4[
                                    G]):  # Compare two different lists (columns) in GRID4 and return true if they
                                    # share elements
                                    GRID4.append(list(set(GRID4[g]).union(set(GRID4[
                                                                                  G]))))  # Append a list that is the
                                    # combination of the two lists (without duplicates)
                                    Remove(GRID4, [G, g])  # Use remove function to correctly remove original two lists
                                    B = 1  # Restart loop as reference lists has changed
                                    break
                                elif g == len(
                                        GRID4) - 1 and G == g:  # Loop has finished combining overlaping postionless
                                    # columns
                                    Shared = 1  # Allow loop to end

                for g in range(len(GRID4)):  #
                    if len(GRID4[g]) > 5:
                        Invalid = 1

                if Invalid == 1:  # Break in case of invalidity
                    break

                Pos = 0  # Variable for while loop
                B = 0  # Variable to break double loop
                while Pos == 0:
                    if B == 1 and Pos == 0:  # Break loop when complete, restart loop if reference size has changed (
                        # moving to playfair grid)
                        B = 0
                    else:
                        for g in range(len(GRID2)):  # For each position-less row
                            if B == 1:  # /Break when reference has changed/
                                break
                            else:
                                if size(GRID, len(GRID2[g])) == size(GRID, 5) and len(GRID2[
                                                                                          g]) <= 5:  # If the row
                                    # isn't too big and can only fit in rows in playfair that are empty
                                    for n in range(0, 5):  # For each row in playfair
                                        if GRID[n].count("") == 5 and B == 0:  # If free
                                            for N in range(len(GRID2[g])):  # For each element in current position-less
                                                if GRID[n][N] == "" and GRID2[g][N] not in GRID[
                                                    n]:  # If postion free and letter not already in row
                                                    GRID[n][N] = GRID2[g][N]  # Input Position-less letter to grid
                                                    A[letter(GRID[n][N])] = "".join(
                                                        [str(n), str(N)])  # Update coordinates in Alphabet
                                            GRID2.remove(GRID2[g])  # Remove row from position-less
                                            B = 1  # Restart loop - Reference has changed
                                            break

                                elif len(GRID2[g]) > 5 or size(GRID, len(
                                        GRID2[g])) == 0:  # If any row is too big or cannot fit in the playfair grid
                                    Invalid = 1  # Invalid
                                    Pos = 1  # End loop
                        if B == 0:  # Loop complete
                            Pos = 1  # Allow end

                # Update coordinates of all position-less values to element in GRID2
                if Invalid == 0:
                    for g in range(len(GRID2)):
                        if g > 9:  # Limitation, Playfair coordinate size 2, Postionless size 1, if there are 10+
                            # postionless rows then postionless is size 2 and causes error
                            print('Calculation error', Comb)  # Code tries to avoid scenario
                        for G in range(len(GRID2[g])):  # Update all position-less
                            A[letter(GRID2[g][G])] = str(g)
