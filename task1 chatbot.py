# CodeAlpha Internship - AI Task 1: FAQ Chatbot
print("--- CodeAlpha FAQ Chatbot ---")
print("Type: what is ai, what is python, what is codealpha (type 'exit' to stop)")

faqs = {
    "what is ai": "AI is Artificial Intelligence, machines that learn like humans.",
    "what is python": "Python is a simple language used for AI and data science.",
    "what is codealpha": "CodeAlpha gives real-world internships to students."
}

while True:
    user = input("\nYou: ").lower()
    if user == "exit":
        print("Bot: Bye! Task 1 Done!")
        break
    
    found = False
    for key in faqs:
        if key in user:
            print(f"Bot: {faqs[key]}")
            found = True
            break
    
    if not found:
        print("Bot: Sorry, try asking 'what is ai / python / codealpha'")