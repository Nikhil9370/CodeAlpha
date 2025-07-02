'''
   Task 3 :
        Goal: Build a simple rule-based chatbot. 
'''

def get_bot_reply(user_input):
    # Convert input to lowercase for easy matching
    user_input = user_input.lower()

    # Rule-based replies
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what's your name":
        return "I'm ChatBot 1.0!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

# Chat loop
print("ChatBot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ")
    reply = get_bot_reply(user)
    print("ChatBot:", reply)

    if user.lower() == "bye":
        break
