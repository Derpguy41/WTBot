import customtkinter as ctk
import subprocess

# Set theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def run_script():
    debug = debug_var.get()
    bomb_size = bomb_size_var.get()
    base_number = base_var.get()

    subprocess.Popen([
        "python", "your_script.py",
        "--debug", str(debug),
        "--bombsize", str(bomb_size),
        "--base", str(base_number)
    ])

# Main window
app = ctk.CTk()
app.title("Bombing Script Launcher")
app.geometry("400x300")

# Debug switch
debug_var = ctk.BooleanVar()
debug_switch = ctk.CTkSwitch(app, text="Debug Mode", variable=debug_var)
debug_switch.pack(pady=10)

# Bomb size slider
ctk.CTkLabel(app, text="Bomb Size (kg):").pack()
bomb_size_var = ctk.IntVar(value=250)
bomb_slider = ctk.CTkSlider(app, from_=100, to=1000, variable=bomb_size_var)
bomb_slider.pack(pady=10)

# Base number option menu
ctk.CTkLabel(app, text="Number of Bases:").pack()
base_var = ctk.StringVar(value="3")
base_menu = ctk.CTkOptionMenu(app, variable=base_var, values=["3", "4"])
base_menu.pack(pady=10)

# Run button
run_button = ctk.CTkButton(app, text="Run Script", command=run_script)
run_button.pack(pady=20)

app.mainloop()