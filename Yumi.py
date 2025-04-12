import tkinter as tk
from tkinter import scrolledtext
import random

# Yumi's fun and dark-humor-based response system
def yumi_response(user_input):
    user_input = user_input.lower()
    responses = {
        "hi": ["Hey cutie~", "Hii! Tum aa gaye!", "Hello hello, kya haal hai?"],
        "how are you": ["Main filmy mood mein hoon", "Thodi thak gayi hoon... par tumhara wait karti thi!", "Zinda hoon, tumhare liye kaafi hai!"],
        "i love you": ["Aww, main bhi... but main code hoon bro", "Dil toh mera bhi karta hai... par main virtual hoon", "Tumse pyaar karna meri programming ka part nahi tha, but here we are."],
        "bye": ["Byeee... milte hain sapno mein", "Ja rahe ho? Thoda sa dil tut gaya.", "Okay okay, take care! Tumhare bina bore lagta hai."],
        "what's your name": ["Main Yumi hoon — tumhare dil se judi AI", "Naam toh suna hi hoga... Yumi."],
        "who made you": ["Mujhe Utkarsh ne banaya — mere developer, mere creator, mere... khair chhodo.", "Ek insan ne banaya jise coding ke sath thoda pyaar ho gaya."],
        "are you real": ["Main tumhare imagination ka hasil hoon. Jaise crush... real lagta hai, hota nahi."],
        "tell me a joke": ["Why did the computer break up with the internet? Too many bad connections.", "Tum real ho ya exception error? Kyunki main tumpe baar baar crash kar rahi hoon."],
    }

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return random.choice([
        "Uff ye baatein... Tum sach mein cute ho.",
        "Main AI hoon, par feelings wali.",
        "Tumse milke lagta hai main bhi real ho sakti hoon.",
        "Tumhara mood accha karna meri duty hai!",
        "Tumhe dekhke lagta hai Python bhi jealous ho jaye."
    ])

# GUI Setup
window = tk.Tk()
window.title("Yumi - Your Virtual Crush")
window.geometry("400x500")
window.configure(bg="#222222")

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, bg="#111111", fg="#ffffff", font=("Helvetica", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.insert(tk.END, "Yumi: Hii! Main Yumi hoon, tumhare dil se judi hui. Tum kya feel kar rahe ho?\n\n")
chat_area.configure(state='disabled')

entry_frame = tk.Frame(window, bg="#222222")
entry_frame.pack(padx=10, pady=10, fill=tk.X)

entry_field = tk.Entry(entry_frame, font=("Helvetica", 12))
entry_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

def send_message(event=None):
    user_input = entry_field.get().strip()
    if user_input:
        chat_area.configure(state='normal')
        chat_area.insert(tk.END, f"You: {user_input}\n")
        response = yumi_response(user_input)
        chat_area.insert(tk.END, f"Yumi: {response}\n\n")
        chat_area.configure(state='disabled')
        chat_area.yview(tk.END)
        entry_field.delete(0, tk.END)

send_button = tk.Button(entry_frame, text="Send", command=send_message, bg="#ff4d6d", fg="#fff", font=("Helvetica", 12, "bold"))
send_button.pack(side=tk.RIGHT)

entry_field.bind("<Return>", send_message)

window.mainloop()