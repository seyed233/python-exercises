"""ماشین‌حساب ساده با رابط گرافیکی Tkinter."""

import ast
import tkinter as tk


def evaluate_expression(node):
    """عبارت ریاضی را فقط با عملگرهای مجاز محاسبه می‌کند."""
    if isinstance(node, ast.Expression):
        return evaluate_expression(node.body)

    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value

    if isinstance(node, ast.BinOp):
        left = evaluate_expression(node.left)
        right = evaluate_expression(node.right)

        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return left / right

    if isinstance(node, ast.UnaryOp):
        value = evaluate_expression(node.operand)
        if isinstance(node.op, ast.UAdd):
            return value
        if isinstance(node.op, ast.USub):
            return -value

    raise ValueError("عبارت شامل عملگر پشتیبانی‌نشده است.")


def calculate(expression):
    """عبارت واردشده را بدون اجرای کد دلخواه محاسبه می‌کند."""
    syntax_tree = ast.parse(expression, mode="eval")
    return evaluate_expression(syntax_tree)


def main():
    """پنجره و دکمه‌های ماشین‌حساب را می‌سازد."""
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("320x400")
    root.resizable(False, False)

    expression = tk.StringVar()
    display = tk.Entry(
        root,
        textvariable=expression,
        font=("Arial", 24),
        justify="right",
        state="readonly",
        readonlybackground="white",
        relief="solid",
        bd=2,
    )
    display.grid(row=0, column=0, columnspan=4, padx=12, pady=12, sticky="nsew")

    def append_to_expression(value):
        expression.set(expression.get() + value)

    def clear_expression():
        expression.set("")

    def remove_last_character():
        expression.set(expression.get()[:-1])

    def show_result():
        try:
            result = calculate(expression.get())
        except (SyntaxError, ValueError, ZeroDivisionError):
            expression.set("Invalid expression")
            return

        expression.set(str(result))

    button_layout = (
        ("7", "8", "9", "/"),
        ("4", "5", "6", "*"),
        ("1", "2", "3", "-"),
        ("00", "0", ".", "+"),
        ("C", "⌫", "="),
    )

    for row_index, row in enumerate(button_layout, start=1):
        column_index = 0
        for button_text in row:
            if button_text == "C":
                command = clear_expression
            elif button_text == "⌫":
                command = remove_last_character
            elif button_text == "=":
                command = show_result
            else:
                command = lambda value=button_text: append_to_expression(value)

            column_span = 2 if button_text == "=" else 1
            button = tk.Button(
                root,
                text=button_text,
                font=("Arial", 16),
                command=command,
                relief="groove",
                bd=2,
            )
            button.grid(
                row=row_index,
                column=column_index,
                columnspan=column_span,
                padx=4,
                pady=4,
                sticky="nsew",
            )
            column_index += column_span

    for column_index in range(4):
        root.grid_columnconfigure(column_index, weight=1)
    for row_index in range(1, len(button_layout) + 1):
        root.grid_rowconfigure(row_index, weight=1)

    root.mainloop()


if __name__ == "__main__":
    main()
