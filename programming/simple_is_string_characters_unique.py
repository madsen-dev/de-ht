# TASK: Check if a string contains only unique characters

def is_string_unique(input_string):
    return len(input_string) == len(set(input_string))

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    
    if is_string_unique(user_input):
        print("The string only contains unique characters.")
    else:
        print("The string does not contain unique characters.")