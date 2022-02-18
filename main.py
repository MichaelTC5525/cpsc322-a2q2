# Arbitrary ordering, change for initialization
ordering = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# String for each variable's value, init to 0s, each digit is the value of that variable
# Only 8 variables, so we can hardcode it as an 8-length string
# E.g. A B C D E F G H
#      | | | | | | | |
#      0 0 0 0 0 0 0 0         on init
# This string's ordering is independent of the arbitrary one specified in the above 'ordering' list
assigned = "00000000"

# Stores the found solution worlds
solutions = []

"""
Runs DFS with Pruning using the ordering list specified above as the order to assign values to variables at
increasing depth of the generated search tree.

Prints out the number of failed branches discovered, as well as the solutions that are found 
"""


def main():
    print("Order of variable assignments: %s" % ordering)
    num_failed_branches = dfsPrune(ordering, 0, assigned)

    print("Number of Failed Branches: %d" % num_failed_branches)
    print("Solutions:")

    for s in solutions:
        print("A = %s, B = %s, C = %s, D = %s, E = %s, F = %s, G = %s, H = %s" % (s[0:1], s[1:2], s[2:3], s[3:4],
                                                                                  s[4:5], s[5:6], s[6:7], s[7:]))

    return 0


"""

Performs a DFS with pruning in searching the space of a CSP. Populates a global variable array with the solutions found
while returning the number of failed branches in its subtree

:param order: the list pertaining to the order in which variables are to be assigned
:param idx: the index in the list "order" determining the variable that is being set next
:param currAssignments: the values of the currently assigned variables, holds 0s in digits of unassigned variables
:param numFails: the accumulated number of failed branches found so far

:returns: the number of failed branches

"""


def dfsPrune(order, idx, currAssignments):

    # First, check if this assignment violates any constraints
    if isViolating(currAssignments):
        # If it does, note its failure and go no further
        return 1

    # If not violating constraints, have all variables been assigned
    elif currAssignments.find("0") == -1:
        # If so, a solution is found,
        solutions.append(currAssignments)

        # Which is definitely not a failing branch
        return 0

    # "Switch statement" on value of order[idx], to determine which variable is being set next
    # For any case, update the proposed value of that variable in its position within the assignment string
    # Start the recursive calls for each possible value 1-4 of this variable being set
    if order[idx] == 'A':
        str1 = "1" + currAssignments[1:]
        str2 = "2" + currAssignments[1:]
        str3 = "3" + currAssignments[1:]
        str4 = "4" + currAssignments[1:]
        return dfsPrune(order, idx + 1, str1) + \
               dfsPrune(order, idx + 1, str2) + \
               dfsPrune(order, idx + 1, str3) + \
               dfsPrune(order, idx + 1, str4)
    elif order[idx] == 'B':
        str1 = currAssignments[0:1] + "1" + currAssignments[2:]
        str2 = currAssignments[0:1] + "2" + currAssignments[2:]
        str3 = currAssignments[0:1] + "3" + currAssignments[2:]
        str4 = currAssignments[0:1] + "4" + currAssignments[2:]
        return dfsPrune(order, idx + 1, str1) + \
               dfsPrune(order, idx + 1, str2) + \
               dfsPrune(order, idx + 1, str3) + \
               dfsPrune(order, idx + 1, str4)
    elif order[idx] == 'C':
        str1 = currAssignments[0:2] + "1" + currAssignments[3:]
        str2 = currAssignments[0:2] + "2" + currAssignments[3:]
        str3 = currAssignments[0:2] + "3" + currAssignments[3:]
        str4 = currAssignments[0:2] + "4" + currAssignments[3:]
        return dfsPrune(order, idx + 1, str1) + \
               dfsPrune(order, idx + 1, str2) + \
               dfsPrune(order, idx + 1, str3) + \
               dfsPrune(order, idx + 1, str4)
    elif order[idx] == 'D':
        str1 = currAssignments[0:3] + "1" + currAssignments[4:]
        str2 = currAssignments[0:3] + "2" + currAssignments[4:]
        str3 = currAssignments[0:3] + "3" + currAssignments[4:]
        str4 = currAssignments[0:3] + "4" + currAssignments[4:]
        return dfsPrune(order, idx + 1, str1) + \
               dfsPrune(order, idx + 1, str2) + \
               dfsPrune(order, idx + 1, str3) + \
               dfsPrune(order, idx + 1, str4)
    elif order[idx] == 'E':
        str1 = currAssignments[0:4] + "1" + currAssignments[5:]
        str2 = currAssignments[0:4] + "2" + currAssignments[5:]
        str3 = currAssignments[0:4] + "3" + currAssignments[5:]
        str4 = currAssignments[0:4] + "4" + currAssignments[5:]
        return dfsPrune(order, idx + 1, str1) + \
               dfsPrune(order, idx + 1, str2) + \
               dfsPrune(order, idx + 1, str3) + \
               dfsPrune(order, idx + 1, str4)
    elif order[idx] == 'F':
        str1 = currAssignments[0:5] + "1" + currAssignments[6:]
        str2 = currAssignments[0:5] + "2" + currAssignments[6:]
        str3 = currAssignments[0:5] + "3" + currAssignments[6:]
        str4 = currAssignments[0:5] + "4" + currAssignments[6:]
        return dfsPrune(order, idx + 1, str1) + \
               dfsPrune(order, idx + 1, str2) + \
               dfsPrune(order, idx + 1, str3) + \
               dfsPrune(order, idx + 1, str4)
    elif order[idx] == 'G':
        str1 = currAssignments[0:6] + "1" + currAssignments[7:]
        str2 = currAssignments[0:6] + "2" + currAssignments[7:]
        str3 = currAssignments[0:6] + "3" + currAssignments[7:]
        str4 = currAssignments[0:6] + "4" + currAssignments[7:]
        return dfsPrune(order, idx + 1, str1) + \
               dfsPrune(order, idx + 1, str2) + \
               dfsPrune(order, idx + 1, str3) + \
               dfsPrune(order, idx + 1, str4)
    elif order[idx] == 'H':
        str1 = currAssignments[0:7] + "1"
        str2 = currAssignments[0:7] + "2"
        str3 = currAssignments[0:7] + "3"
        str4 = currAssignments[0:7] + "4"
        return dfsPrune(order, idx + 1, str1) + \
               dfsPrune(order, idx + 1, str2) + \
               dfsPrune(order, idx + 1, str3) + \
               dfsPrune(order, idx + 1, str4)


"""
:param world: the string corresponding to the value assignments in this world
              the character at position i is 0 when the ith variable is not yet assigned

:returns: boolean; whether or not this possible world violates a constraint
"""
def isViolating(world):
    # Give names to each part of the string
    A = int(world[0:1])
    B = int(world[1:2])
    C = int(world[2:3])
    D = int(world[3:4])
    E = int(world[4:5])
    F = int(world[5:6])
    G = int(world[6:7])
    H = int(world[7:])


    # Test all constraints required by this question
    # Check first whether it is worthwhile to evaluate the condition (both operands non-zero) before actually checking
    if A != 0 and G != 0:
        if not A >= G:
            return True

    if G != 0 and C != 0:
        if not abs(G - C) == 1:
            return True

    if D != 0 and C != 0:
        if not D != C:
            return True

    if G != 0 and F != 0:
        if not G != F:
            return True

    if E != 0 and F != 0:
        if not abs(E - F) % 2 == 1:
            return True

    if A != 0 and H != 0:
        if not A < H:
            return True

    if H != 0 and C != 0:
        if not abs(H - C) % 2 == 0:
            return True

    if E != 0 and C != 0:
        if not E != C:
            return True

    if H != 0 and F != 0:
        if not H != F:
            return True

    if F != 0 and B != 0:
        if not abs(F - B) == 1:
            return True

    if H != 0 and D != 0:
        if not H != D:
            return True

    if E != 0 and D != 0:
        if not E < (D - 1):
            return True

    if C != 0 and F != 0:
        if not C != F:
            return True

    if G != 0 and H != 0:
        if not G < H:
            return True

    if D != 0 and G != 0:
        if not D >= G:
            return True

    if E != 0 and H != 0:
        if not E != (H - 2):
            return True

    if D != 0 and F != 0:
        if not D != F:
            return True

    return False


if __name__ == "__main__":
    main()
