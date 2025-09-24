# TASK: Check if a string contains only unique characters
def analyze_string_uniqueness(input_string):
    char_counts = {}
    
    input_string = input_string.replace(" ", "")
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    unique_chars = set()
    repeated_chars = set()

    for char, count in char_counts.items():
        if count == 1:
            unique_chars.add(char)
        else:
            repeated_chars.add(char)

    is_unique = not bool(repeated_chars)

    return is_unique, unique_chars, repeated_chars

if __name__ == "__main__":
    user_input = input("Enter a string: ")

    is_unique, unique_chars, repeated_chars = analyze_string_uniqueness(user_input)

    if is_unique:
        print("The string contains only unique characters.")
    else:
        print("The string does not contain only unique characters.")
        print(f"Non-unique characters found: {', '.join(sorted(list(repeated_chars)))}")

    if unique_chars:
        print(f"Unique characters found: {', '.join(sorted(list(unique_chars)))}")
    else:
        print("No unique characters were found in the string.")