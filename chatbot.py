def chatbot_response(user_input):
    # Convert user input to lowercase for easier matching
    user_input = user_input.lower()

    # Define responses based on user input
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a computer program, but thanks for asking! How can I help you?"
    elif "what is your name" in user_input:
        return "I am a simple rule-based chatbot. You can call me ChatBot!"
    elif "help" in user_input:
        return "Sure! What do you need help with?"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    elif "your favorite color" in user_input:
        return "I don't have feelings, but I've heard blue is a nice color!"
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"

def main():
    print("Welcome to the ChatBot! Type 'bye' or 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("ChatBot:", response)
        
        # Exit the loop if the user says goodbye
        if response.startswith("Goodbye"):
            break

if __name__ == "__main__":
    main()