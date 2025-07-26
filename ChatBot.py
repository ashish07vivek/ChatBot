print("Chatbot: Hi! I'm Vivek.")
print("Chatbot: I can also do basic arithmetic. Try saying: add 4 and 5 or divide 10 by 2.")
print("Type 'bye' to end the conversation.")
while True:
    user_input = input("You: ").lower()

    if "bye" in user_input or "exit" in user_input:
        print("Chatbot: Goodbye! Have a great day!")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello! How can I help you today?")

    elif "how are you" in user_input:
        print("Chatbot: I'm just code, but thanks for asking!")

    elif "name" in user_input:
        print("Chatbot:I'm Vivek. I'm a Python-based chatbot with simple logic!")

    elif "help" in user_input:
        print("Chatbot: You can say things like 'add 5 and 3', 'multiply 4 by 2', or ask my name!")

    # Arithmetic handling
    elif "add" in user_input:
        words = user_input.split()
        numbers = [int(word) for word in words if word.isdigit()]
        if len(numbers) >= 2:
            print(f"Chatbot: The sum is {numbers[0] + numbers[1]}")
        else:
            print("Chatbot: Please provide two numbers to add.")

    elif "subtract" in user_input:
        words = user_input.split()
        numbers = [int(word) for word in words if word.isdigit()]
        if len(numbers) >= 2:
            print(f"Chatbot: The difference is {numbers[0] - numbers[1]}")
        else:
            print("Chatbot: Please provide two numbers to subtract.")

    elif "multiply" in user_input:
        words = user_input.split()
        numbers = [int(word) for word in words if word.isdigit()]
        if len(numbers) >= 2:
            print(f"Chatbot: The product is {numbers[0] * numbers[1]}")
        else:
            print("Chatbot: Please provide two numbers to multiply.")

    elif "divide" in user_input:
        words = user_input.split()
        numbers = [int(word) for word in words if word.isdigit()]
        if len(numbers) >= 2:
            if numbers[1] != 0:
                print(f"Chatbot: The quotient is {numbers[0] / numbers[1]}")
            else:
                print("Chatbot: Division by zero is not allowed.")
        else:
            print("Chatbot: Please provide two numbers to divide.")

    else:
        print("Chatbot: I didn't understand that. Try asking for help.")
