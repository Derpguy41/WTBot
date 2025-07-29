import customtkinter as ctk
import subprocess

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def run_script():
    debug = debug_var.get()
    bomb_size = bomb_size_var.get()
    base_number = base_var.get()

    # Validate bomb size input
    try:
        bomb_size = int(bomb_size)
        if bomb_size < 0.75 or bomb_size > 12000 or bomb_size == "":
            bomb_size_entry.configure(border_color="red")
            return

    except ValueError:
        bomb_size_entry.configure(border_color="red")
        return

    bomb_size_entry.configure(border_color="gray")

    subprocess.Popen([
        "python", "./Main/main.py",
        "--debug", str(debug),
        "--bombsize", str(bomb_size),
        "--base", str(base_number)
    ])

app = ctk.CTk()
app.title("WTBot")
app.geometry("400x250")

# Debug switch
debug_var = ctk.BooleanVar()
debug_switch = ctk.CTkSwitch(app, text="Debug Mode", variable=debug_var)
debug_switch.pack(pady=10)

# Bomb size text box
ctk.CTkLabel(app, text="Bomb Size (TNT kg):").pack()
bomb_size_var = ctk.StringVar(value="250")
bomb_size_entry = ctk.CTkEntry(app, textvariable=bomb_size_var, width=100)
bomb_size_entry.pack(pady=5)

# Base number dropdown
ctk.CTkLabel(app, text="Number of Bases:").pack()
base_var = ctk.StringVar(value="3")
base_menu = ctk.CTkOptionMenu(app, variable=base_var, values=["3", "4"])
base_menu.pack(pady=10)

# Run button
run_button = ctk.CTkButton(app, text="Run Script", command=run_script)
run_button.pack(pady=20)

app.mainloop()