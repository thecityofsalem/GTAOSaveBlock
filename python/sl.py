import subprocess
import tkinter as tk
from tkinter import messagebox

rule_name = "GTAOSAVEBLOCK"

def firewall():
    check = subprocess.run(["netsh", "advfirewall", "firewall", "show", "rule", f"name={rule_name}"], capture_output=True, text=True)
    if "No rules match" in check.stdout:
        subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule", f"name={rule_name}", "dir=out", "action=block", "remoteip=192.81.241.170-192.81.241.171", "enable=yes"], creationflags=subprocess.CREATE_NO_WINDOW)
        messagebox.showwarning("Enabled", "GTAOSB On")
    else:
        subprocess.run(["netsh", "advfirewall", "firewall", "delete", "rule", f"name={rule_name}"], creationflags=subprocess.CREATE_NO_WINDOW)
        messagebox.showinfo("Disabled", "GTAOSB Off")

root = tk.Tk()
root.title("cityofsalem")
btn = tk.Button(root, text="toggle nosave", command=firewall, bg="red", fg="white", font=("Arial", 12))
btn.pack(padx=20, pady=20)
root.mainloop()