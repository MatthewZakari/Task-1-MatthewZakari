def main():
    print("Chatbot: Hello! I'm Zakari. Type 'exit' or 'quit' to leave.")
    
    try:
        while True:
            try:
                user_input = input("You: ").lower().strip()
            except EOFError:
                print("\nChatbot: Goodbye! (EOF)")
                break
            
            if user_input in ["exit", "quit"]:
                print("Chatbot: Goodbye! Have a great day!")
                break
            elif user_input in ["hello", "hi", "hey"]:
                print("Chatbot: Hello there! How can I help you today?")
            elif user_input == "how are you":
                print("Chatbot: I'm just a program, but I'm functioning perfectly. How about you?")
            elif user_input == "what is your name":
                print("Chatbot: I'm Zakari, the DecodeLabs Chatbot.")

            elif user_input == "help":
                print("Chatbot: You can say hello, ask my name, or say 'exit' to quit.")
            else:
                print("Chatbot: I'm sorry, I don't understand that. Type 'help' for available commands.")
    except KeyboardInterrupt:
        print("\nChatbot: Goodbye! (Interrupted)")

if __name__ == "__main__":
    main()
