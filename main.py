import openai
from dotenv import load_dotenv
import os
import tkinter as tk
from tkinter import scrolledtext

# Load environment variables from .env file
load_dotenv()

# Set up the OpenAI API key from the environment variable
openai.api_key = os.getenv("key")  

def generate_response():
    # Get user input
    user_input = user_input_text.get("1.0", tk.END).strip()
    
    if not user_input:
        output_text.insert(tk.END, "Please enter a prompt.\n")
        return
    
    try:
        # OpenAI API call
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        
        # Get and display the response
        response = completion.choices[0].message["content"]
        output_text.insert(tk.END, f"User: {user_input}\nAssistant: {response}\n\n")
    except Exception as e:
        output_text.insert(tk.END, f"Error: {e}\n\n")

# Create the main window
window = tk.Tk()
window.title("OpenAI Chat GUI")
window.geometry("600x400")

# Create input text box
tk.Label(window, text="Enter your prompt:").pack(pady=5)
user_input_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=5)
user_input_text.pack(padx=10, pady=5)

# Create submit button
submit_button = tk.Button(window, text="Generate Response", command=generate_response)
submit_button.pack(pady=5)

# Create output text box
tk.Label(window, text="Output:").pack(pady=5)
output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=10)
output_text.pack(padx=10, pady=5)

# Run the application
window.mainloop()
