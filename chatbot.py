import random
from datetime import datetime
import wikipedia

# Predefined data
greetings = ["Hello! 👋", "Hey there! 😊", "Hi! 🙌", "Namaste! 🙏", "Yo! ✌️"]
goodbyes = ["Goodbye! 👋", "Take care! 😊", "See you later! 👋", "Bye-bye! ✌️"]

# Jokes
jokes = [
    "Why don't programmers like nature? It has too many bugs! 😂",
    "Ek Aadmi ne bola: Mujhe acting ka bada shauk hai! Usne shaadi kar li... ab har din acting karni padti hai! 😂",
    "Why did the smartphone break up with the charger? It found a better connection. 😂",
    "Pappu: Bhai tu idhar kyun khada hai? 😂 Ramesh: Padhai karne aaya tha, lekin library band thi... toh socha dharna de du 😂",
    "Why did the bicycle fall over? Because it was two-tired! 🚲😂",
    "Teacher: Tum class me kyun nahi aaye? 🤨 Student: Sir, soch raha tha ki aaj ke class me kal ki tayyari kar leta hoon! 😂",
    "What do you call fake spaghetti? An impasta! 🍝😂",
    "Biwi ne pati se kaha: Tum mujhe kabhi gifts nahi dete! Pati: Tumhi toh ho meri sabse badi gift! 🎁😜"
]

# Quotes
quotes = [
    "💡 'Success is not final, failure is not fatal: It is the courage to continue that counts.' – Winston Churchill",
    "💡 'Zindagi jeene ke do hi tareeke hote hain, ek jo ho raha hai hone do, ya zimmedari uthao use badalne ki.' – Ranveer Singh",
    "💡 'Believe you can and you're halfway there.' – Theodore Roosevelt",
    "💡 'Opportunities don't happen. You create them.' – Chris Grosser",
    "💡 'Great things never came from comfort zones.' – Anonymous",
    "💡 'Jindagi ek rangmanch hai, har koi apna kirdaar nibha raha hai.' – Gulzar",
    "💡 'Stay hungry, stay foolish.' – Steve Jobs",
    "💡 'Mehnat karo, safalta jhakk maar kar peeche bhagegi.' – Anonymous"
]

# Fun Facts
facts = [
    "🧠 The human brain can hold about 2.5 petabytes of information – equivalent to 3 million hours of TV shows! 🤯",
    "🌌 A day on Venus is longer than its year! 🌠",
    "🐢 Turtles can breathe through their butts. 😂",
    "🚀 There are more stars in the universe than grains of sand on Earth. 🌌",
    "🐘 Elephants can 'hear' with their feet by detecting seismic signals. 🐾",
    "🔥 Kya tum jaante ho? Insaan apni zindagi ka 1/3 hissa so kar bita deta hai! 😴",
    "🎧 Music sunne se dimaag me dopamine release hota hai, jo hume khush karta hai! 🎵",
    "🐦 Kabootar apna raasta yaad rakhne me mahir hote hain. 🕊️"
]

# Time and date functions
def get_time():
    return f"⏰ Current time: {datetime.now().strftime('%H:%M:%S')}"

def get_date():
    return f"📅 Today's date: {datetime.today().strftime('%Y-%m-%d')}"

# Wikipedia Search
def wiki_search(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return f"🌍 {summary}"
    except:
        return "❌ No matching page found!"

# Math Operations
def math_operations(expression):
    try:
        return f"✅ Result: {eval(expression)}"
    except:
        return "❌ Invalid math expression!"

# Basic logic
def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey", "hii","hiii","hlw","namaste"]:
        return random.choice(greetings)

    elif user_input in ["bye", "goodbye", "exit"]:
        return random.choice(goodbyes)

    elif "fact" in user_input:
        return random.choice(facts)

    elif "joke" in user_input:
        return random.choice(jokes)

    elif "quote" in user_input:
        return random.choice(quotes)

    elif "time" in user_input:
        return get_time()

    elif "date" in user_input:
        return get_date()

    elif "wiki" in user_input:
        topic = user_input.replace("wiki", "").strip()
        return wiki_search(topic)

    elif any(op in user_input for op in ['+', '-', '*', '/']):
        return math_operations(user_input)

    else:
        return "🤖 Sorry, I didn't understand that. Try again!"

# Chat loop
print("Chatbot 🤖: Hello! Ask me something or type 'bye' to exit.")
while True:
    user_input = input("You: ")

    if user_input.lower() in ["bye", "exit"]:
        print("Chatbot 🤖:", random.choice(goodbyes))
        break
    
    response = chatbot_response(user_input)
    print("Chatbot 🤖:", response)