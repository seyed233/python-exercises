"""بررسی گذرواژه و تأیید دوباره‌ی آن با رابط گرافیکی Tkinter."""

import tkinter as tk
from tkinter import messagebox


def validate_password(password, confirmation):
    """در صورت نامعتبر بودن گذرواژه، پیام مناسب را برمی‌گرداند."""
    if not password or not confirmation:
        return "Please fill in both password fields."

    if not 8 <= len(password) <= 12:
        return "Password must contain between 8 and 12 characters."

    # گذرواژه باید دست‌کم یک حرف داشته باشد؛ عدد و نویسه‌ی ویژه نیز مجازند.
    if not any(character.isalpha() for character in password):
        return "Password must contain at least one letter."

    if password != confirmation:
        return "The passwords do not match."

    return None


def main():
    """پنجره‌ی بررسی گذرواژه را می‌سازد و اجرا می‌کند."""
    root = tk.Tk()
    root.title("Password Validator")
    root.geometry("420x300")
    root.resizable(False, False)
    root.configure(padx=20, pady=16)

    tk.Label(root, text="Enter your password:", anchor="w").pack(fill="x", pady=(0, 5))
    password_entry = tk.Entry(root, show="*", relief="groove", bd=2)
    password_entry.pack(fill="x", pady=(0, 14))

    tk.Label(root, text="Confirm your password:", anchor="w").pack(fill="x", pady=(0, 5))
    confirmation_entry = tk.Entry(root, show="*", relief="groove", bd=2)
    confirmation_entry.pack(fill="x", pady=(0, 14))

    status_label = tk.Label(root, text="", wraplength=370, justify="left")
    status_label.pack(fill="x", pady=5)

    def check_password():
        error_message = validate_password(
            password_entry.get(),
            confirmation_entry.get(),
        )
        if error_message:
            status_label.config(text=error_message, fg="red")
            return

        status_label.config(text="Password is valid.", fg="green")
        messagebox.showinfo("Success", "The password has been validated.")

    tk.Label(
        root,
        text="Use 8–12 characters and include at least one letter.",
        fg="blue",
        wraplength=370,
    ).pack(fill="x", pady=(8, 14))

    tk.Button(root, text="Check password", command=check_password).pack()

    root.mainloop()


if __name__ == "__main__":
    main()






