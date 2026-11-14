def main():
    print("Welcome to LaTeX formatter.")
   
    while True:
        user_input: str = input("Please enter your text\n> ")
        fixed_text: str = replace_latex(user_input)
        print(fixed_text)

        user_choice = input("Would you like to enter more text? (Y/N)\n> ")
        if user_choice.lower() == "y":
            print()
            continue
        else:
            break

def replace_latex(text: str):
    counter: int = 1
    new_text: list[str] = []
    for char in text:
        # counter is odd, so we are on our first '$'
        if char == "$" and ((counter % 2) == 1):
            new_text.append("\\(")
            counter += 1

        # counter is odd, so we are on our second '$' 
        elif char == "$" and ((counter % 2) == 0):
            new_text.append("\\)")
            counter += 1

        else:
            new_text.append(char)
    return ''.join(new_text)


main()
