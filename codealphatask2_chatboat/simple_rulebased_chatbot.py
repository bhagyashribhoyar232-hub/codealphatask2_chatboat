#chatboat
def chatbot_response(user_input): #define a function that takes user input and predefined replys
    # Convert input to lowercase for easier matching
    user_input = user_input.lower()
    
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

# Main loop
print("Chatbot is running... (type 'bye' to exit)")
while True:
    user_message = input("You: ")
    reply = chatbot_response(user_message)
    print("Bot:", reply)
    
    if user_message.lower() == "bye":
        break
