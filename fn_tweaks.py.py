import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time
import threading

class FakeTweakTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Fortnite Performance Tweaks")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.label = tk.Label(root, text="Fortnite CPU & Mouse Tweaks", font=("Arial", 16))
        self.label.pack(pady=20)

        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=20)

        self.status_label = tk.Label(root, text="Press 'Apply Tweaks' to start.", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.apply_button = tk.Button(root, text="Apply Tweaks", command=self.start_tweaks)
        self.apply_button.pack(pady=20)

        # List of fake tweaks to “apply”
        self.tweaks = [
            "Optimizing CPU cores...",
            "Adjusting mouse polling rate...",
            "Reducing background process priority...",
            "Increasing network buffer size...",
            "Enabling low-latency input mode...",
            "Cleaning up temporary files...",
            "Tweaking GPU priority...",
            "Applying Fortnite-specific settings...",
            "Refreshing game cache...",
            "Finalizing tweaks..."
        ]

    def start_tweaks(self):
        self.apply_button.config(state="disabled")
        threading.Thread(target=self.run_tweaks).start()

    def run_tweaks(self):
        total_steps = len(self.tweaks)
        for i, tweak in enumerate(self.tweaks, 1):
            self.status_label.config(text=tweak)
            self.progress['value'] = (i / total_steps) * 100
            time.sleep(1.5)  # Pause to simulate work being done
        self.status_label.config(text="All tweaks applied successfully!")
        messagebox.showinfo("Success", "All Fortnite CPU tweaks applied successfully!")
        self.apply_button.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = FakeTweakTool(root)
    root.mainloop()
