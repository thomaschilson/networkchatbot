import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Network Stats Chatbot")
root.geometry("400x400")


def open_window(old_window):
    old_window.destroy()



def get_response():
    user_input = question_var.get()  # Get the selected question
    if user_input == "Select an option":
        response = "Please select a valid option."
    elif user_input == "Network Utilization Percentage":
        root.destroy()
        response = "Network utilization measures the percentage of network capacity currently being used."
        new_window = tk.Tk()
        new_window.grab_set()
        #new_window = tk.Toplevel(root)
        new_window.geometry("400x400")
        new_window.title("Network Util")

        # Add content to the new window here
        response = "Network utilization measures the percentage of network capacity currently being used."
        label = tk.Label(new_window, text="Input a percentage to query.", bg="lightgray", fg="black")
        label.pack(pady=10)
        entry = tk.Entry(new_window, selectbackground="lightblue", selectforeground="black")

        entry.pack()
        #root.destroy()
        response_button = tk.Button(new_window, text="Get Info", command=open_window)
        response_button.pack()
        new_window.mainloop()

        # Destroy the old window



    elif user_input == "What is Latency?":
        response = "Latency is the time it takes for data to travel from source to destination across the network."
    elif user_input == "What is Packet Loss?":
        response = "Packet loss occurs when packets of data fail to reach their destination."
    elif user_input == "What is Bandwidth?":
        response = "Bandwidth is the maximum rate at which data can be transferred over a network path."
    else:
        response = "No information available for the selected option."

    # Display response in the chat history
    chat_history.config(state=tk.NORMAL)
    #chat_history.insert(tk.END, "You: " + user_input + "\n")
    chat_history.insert(tk.END, "Bot: " + response + "\n\n")
    chat_history.config(state=tk.DISABLED)
    chat_history.see(tk.END)

# Chat history display
chat_history = tk.Text(root, wrap="word", state=tk.DISABLED, width=50, height=15)
chat_history.pack(pady=10)

# Dropdown menu for preset questions
question_var = tk.StringVar(value="Select an option")
questions_layer_1 = [
    "Select an option",
    "Network Utilization Percentage",
    "What is Latency?",
    "What is Packet Loss?",
    "What is Bandwidth?"
]
question_menu = ttk.Combobox(root, textvariable=question_var, values=questions_layer_1, state="readonly")
question_menu.pack(pady=10)

# Button to get response
response_button = tk.Button(root, text="Get Info", command=get_response)
response_button.pack(pady=10)

# Run the main loop
root.mainloop()
