# Simple AI Chatbot
# By: Imtiaz Ali - PIAIC Batch 86

print("=== AI Chatbot ===")
print("Type 'exit' to quit")
print()

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Bot: Khuda Hafiz!")
        break
    elif "naam" in user_input.lower():
        print("Bot: Mera naam PIAIC Bot he!")
    elif "hello" in user_input.lower():
        print("Bot: Assalam o Alaikum!")
    elif "piaic" in user_input.lower():
        print("Bot: PIAIC Pakistan ka best AI course he!")
    else:
        print("Bot: Mujhe samajh nahi aaya, dobara poochein!")