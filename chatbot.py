import random

# -----------------------------
# 1️⃣ Define intents and responses
# -----------------------------
intents = {
    "admission": [
        "Admissions are open from January 10th to March 15th.",
        "You can apply online through our admission portal at college.edu/admissions."
    ],
    "class_time": [
        "Classes are held from 9 AM to 4 PM, Monday to Friday.",
        "Check your timetable on the student portal under 'Schedule'."
    ],
    "fees": [
        "Tuition fees are $1200 per semester.",
        "You can pay fees online or at the accounts office."
    ],
    "hostel": [
        "Hostel facilities are available for both boys and girls.",
        "To apply for hostel accommodation, contact hostel@college.edu."
    ],
    "library": [
        "The library is open from 8 AM to 8 PM on weekdays.",
        "Students can borrow up to 3 books for 15 days."
    ],
    "exam": [
        "Midterm exams are held in March and finals in June.",
        "Exam timetables are published on the student portal."
    ],
    "results": [
        "Results are usually declared two weeks after final exams.",
        "You can check your results in the Examination section of the student portal."
    ],
    "transport": [
        "The college provides bus services from major city routes.",
        "Transport passes are available from the admin office."
    ],
    "holiday": [
        "The college observes all national holidays.",
        "Check the academic calendar for upcoming holidays."
    ],
    "cafeteria": [
        "The cafeteria is open from 8 AM to 6 PM.",
        "We offer vegetarian and non-vegetarian meals at affordable prices."
    ],
    "sports": [
        "Our college has facilities for football, cricket, badminton, and basketball.",
        "The annual sports meet is organized every February."
    ],
    "placement": [
        "The placement cell partners with top companies for internships and jobs.",
        "You can contact placement@college.edu for more information."
    ],
    "contact": [
        "You can reach us at info@college.edu or call +1 234 567 890.",
        "Visit the admin block for in-person assistance."
    ],
    "default": [
        "Sorry, I didn’t understand that. Could you please rephrase?",
        "I'm not sure I got that. Can you try asking differently?"
    ]
}

# -----------------------------
# 2️⃣ Define simple keywords for each intent
# -----------------------------
intent_keywords = {
    "admission": ["admission", "apply", "application", "enroll", "joining"],
    "class_time": ["class", "schedule", "time", "timetable", "lecture"],
    "fees": ["fee", "fees", "payment", "cost", "tuition", "pay"],
    "hostel": ["hostel", "room", "accommodation", "stay", "dorm"],
    "library": ["library", "book", "study", "borrow", "reading"],
    "exam": ["exam", "test", "midterm", "final", "assessment"],
    "results": ["result", "marks", "grade", "score"],
    "transport": ["bus", "transport", "route", "pickup", "drop", "pass"],
    "holiday": ["holiday", "vacation", "break", "leave", "off"],
    "cafeteria": ["cafeteria", "canteen", "food", "meal", "snack"],
    "sports": ["sport", "game", "football", "cricket", "badminton", "basketball"],
    "placement": ["placement", "job", "career", "internship", "recruitment"],
    "contact": ["contact", "email", "phone", "address", "help", "office"]
}

# -----------------------------
# 3️⃣ Intent detection
# -----------------------------
def get_intent(user_input):
    words = user_input.lower().split()  # simple tokenization
    for intent, keywords in intent_keywords.items():
        for word in words:
            if word in keywords:
                return intent
    return "default"

# -----------------------------
# 4️⃣ Chat loop
# -----------------------------
print("🤖 College Chatbot: Hello! How can I help you today?")
print("(Type 'quit' to exit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("🤖 Bot: Goodbye! Have a great day!")
        break

    intent = get_intent(user_input)
    response = random.choice(intents[intent])
    print(f"🤖 Bot: {response}\n")
