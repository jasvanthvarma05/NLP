def fsa_ends_with_ab(input_string):
    # Initial state
    state = "START"
    
    for char in input_string:
        if state == "START":
            if char == 'a':
                state = "A"
            else:
                state = "START"
        elif state == "A":
            if char == 'b':
                state = "AB"
            elif char == 'a':
                state = "A"
            else:
                state = "START"
        elif state == "AB":
            if char == 'a':
                state = "A"
            else:
                state = "START"
    
    # Accept state
    return state == "AB"

# Testing the automaton
test_string = "cab"
if fsa_ends_with_ab(test_string):
    print(f"The string '{test_string}' ends with 'ab'")
else:
    print(f"The string '{test_string}' does not end with 'ab'")
