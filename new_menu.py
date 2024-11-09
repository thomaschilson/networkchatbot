import tkinter as tk
from tkinter import ttk

def create_main_window():
    """Sets up and runs the main application window."""
    root = tk.Tk()
    root.title("Network Stats Chatbot")
    root.geometry("400x400")

    # Chat history display
    chat_history = tk.Text(root, wrap="word", state=tk.DISABLED, width=50, height=15)
    chat_history.pack(pady=10)

    # Dropdown menu for preset questions
    question_var = tk.StringVar(value="Select an option")
    questions_layer_1 = [
        "Select an option",
        "Utilization percentage",
        "Top Volume (Bytes)",
        "Top Flows today"
    ]
    question_menu = ttk.Combobox(root, textvariable=question_var, values=questions_layer_1, state="readonly")
    question_menu.pack(pady=10)

    # Button to get response
    response_button = tk.Button(root, text="Get Info",
                                command=lambda: handle_user_input(question_var, chat_history, root))
    response_button.pack(pady=10)

    root.mainloop()

def handle_user_input(question_var, chat_history, root):
    """Processes the selected question and opens a new window with information as needed."""
    user_input = question_var.get()
    if user_input == "Select an option":
        response = "Please select a valid option."
        display_response(user_input, response, chat_history)
    elif user_input == "Utilization percentage":
        open_utilization_threshold_window(root)
    elif user_input == "Top Volume (Bytes)":
        open_top_volume_input_window(root)
    elif user_input == "Top Flows today":
        open_top_flows_input_window(root)

def display_response(user_input, response, chat_history):
    """Displays the user input and chatbot response in the chat history."""
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"You: {user_input}\nBot: {response}\n\n")
    chat_history.config(state=tk.DISABLED)
    chat_history.see(tk.END)

def open_utilization_threshold_window(root):
    """Opens a new window for entering a utilization threshold."""
    new_window = tk.Toplevel(root)
    new_window.geometry("400x400")
    new_window.title("Utilization Threshold")

    label = tk.Label(new_window, text="Enter a utilization percentage threshold:", wraplength=350)
    label.pack(pady=10)

    threshold_entry = tk.Entry(new_window)
    threshold_entry.pack(pady=10)

    submit_button = tk.Button(new_window, text="Submit",
                              command=lambda: display_utilization_over_threshold(new_window, threshold_entry))
    submit_button.pack(pady=10)

def display_utilization_over_threshold(window, threshold_entry):
    """Displays networks over the entered utilization threshold."""
    threshold = float(threshold_entry.get())
    window.destroy()

    result_window = tk.Toplevel()
    result_window.geometry("400x400")
    result_window.title("Networks Over Utilization Threshold")

    # Placeholder list of networks with utilization percentages
    networks_over_threshold = [
        ("Network A", 85), ("Network B", 90), ("Network C", 95)  # Sample data
    ]
    filtered_networks = [net for net in networks_over_threshold if net[1] > threshold]

    label = tk.Label(result_window, text=f"Networks with utilization over {threshold}%:", wraplength=350)
    label.pack(pady=10)

    for network, utilization in filtered_networks:
        network_label = tk.Label(result_window, text=f"{network}: {utilization}%")
        network_label.pack()

    close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
    close_button.pack(pady=10)

def open_top_volume_input_window(root):
    """Opens a new window for entering the number of top volumes to display."""
    new_window = tk.Toplevel(root)
    new_window.geometry("400x400")
    new_window.title("Top Volume (Bytes)")

    label = tk.Label(new_window, text="Enter the number of top volumes to display:", wraplength=350)
    label.pack(pady=10)

    volume_entry = tk.Entry(new_window)
    volume_entry.pack(pady=10)

    submit_button = tk.Button(new_window, text="Submit",
                              command=lambda: display_top_volume(new_window, volume_entry))
    submit_button.pack(pady=10)

def display_top_volume(window, volume_entry):
    """Displays the top N volumes based on user input."""
    top_n = int(volume_entry.get())
    window.destroy()

    result_window = tk.Toplevel()
    result_window.geometry("400x400")
    result_window.title("Top Volume Networks")

    # Placeholder list of networks with volume data
    top_volumes = [
        ("Network A", "500 MB"), ("Network B", "450 MB"), ("Network C", "400 MB")  # Sample data
    ]
    top_volumes = top_volumes[:top_n]

    label = tk.Label(result_window, text=f"Top {top_n} networks by volume (Bytes):", wraplength=350)
    label.pack(pady=10)

    for network, volume in top_volumes:
        volume_label = tk.Label(result_window, text=f"{network}: {volume}")
        volume_label.pack()

    close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
    close_button.pack(pady=10)

def open_top_flows_input_window(root):
    """Opens a new window for entering the number of top flows to display."""
    new_window = tk.Toplevel(root)
    new_window.geometry("400x400")
    new_window.title("Top Flows Today")

    label = tk.Label(new_window, text="Enter the number of top flows to display:", wraplength=350)
    label.pack(pady=10)

    flows_entry = tk.Entry(new_window)
    flows_entry.pack(pady=10)

    submit_button = tk.Button(new_window, text="Submit",
                              command=lambda: display_top_flows(new_window, flows_entry))
    submit_button.pack(pady=10)

def display_top_flows(window, flows_entry):
    """Displays the top N flows based on user input."""
    top_n = int(flows_entry.get())
    window.destroy()

    result_window = tk.Toplevel()
    result_window.geometry("400x400")
    result_window.title("Top Flows Networks")

    # Placeholder list of networks with flow data
    top_flows = [
        ("Network A", "1200 Flows"), ("Network B", "1100 Flows"), ("Network C", "1050 Flows")  # Sample data
    ]
    top_flows = top_flows[:top_n]

    label = tk.Label(result_window, text=f"Top {top_n} networks by flows:", wraplength=350)
    label.pack(pady=10)

    for network, flows in top_flows:
        flows_label = tk.Label(result_window, text=f"{network}: {flows}")
        flows_label.pack()

    close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
    close_button.pack(pady=10)

# Run the main window
create_main_window()
