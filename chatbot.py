import nltk
from nltk.chat.util import Chat, reflections

# Download required data
nltk.download('punkt')

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"what is your name ?",
        ["I am a simple NLP chatbot."]
    ],
    [
        r"how are you ?",
        ["I am fine. How about you?"]
    ],
]

chatbot = Chat(pairs, reflections)

print("Hello! Type 'quit' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break

    response = chatbot.respond(user_input)

    if response:
        print("Chatbot:", response)
    else:
        print("Chatbot: I don't understand.")
