import random

def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ["hi", "hello"]
    bye = ["bye", ]
    thanks = ["thank you"]

    question = {
        "what is ai": "AI stands for Artificial Intelligence. It means machines that can think and learn like humans .",
        "who is the father of computer": "Charles Babbage is known as the father of the computer .",
        "what is python": "Python is a high-level programming language, simple and powerful .",
        "what is your name": "im chatbot.",
        "what is machine learning": "Machine Learning is a subset of AI where systems learn from data and improve automatically .",
        "who are you": "I’m your chatbot assistant, created to talk and help you!"
    }

    if any(word in user_input for word in greetings):
        return random.choice([
            "Hi ,What’s up?"
        ])

    elif any(word in user_input for word in bye):
        return random.choice([
            "Bye",
          
        ])

    elif any(word in user_input for word in thanks):
        return random.choice([
            "You're most welcome! ",
           
        ])

    elif user_input in question:
        return question[user_input]

    elif "how are you" in user_input:
        return random.choice([
            "I’m fine  What about you?"
        ])

    else:
        return random.choice([
            "Great! "
        ])

print("Chatbot: Hi! I’m your friendly AI chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot:", random.choice(["Bye! Take care ", "Goodbye! Stay safe "]))
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
