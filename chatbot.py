# chat_gpt_bot.py

import openai

# Replace with your actual API key
openai.api_key = "your-api-key-here"

def chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use "gpt-3.5-turbo" if needed
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print("GPT-4 Chatbot (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        reply = chat(user_input)
        print("AI:", reply)
