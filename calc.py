import tkinter as tk

def calculate_result(expression):
    result = str(eval(expression))
    entry.delete(0, tk.END)
    entry.insert(0, result)

def on_button_click(button_text): 
    if button_text == "=":
        current = entry.get()
        calculate_result(current)
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "Exit":
        exit()
    else:
        entry.insert(tk.END, button_text)

def create_button(text, row, col):
    button = tk.Button(window, text=text, width=5, height=2, font=('Arial', 14), command=lambda: on_button_click(text))
    button.grid(row=row, column=col, padx=5, pady=5)

def setup_calculator():
    global entry
    entry = tk.Entry(window, font=('Arial', 20), borderwidth=2, relief="solid", justify='right')
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Buttons
    buttons = [ '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', 'C', '+', '=', '**', 'Exit' ]

    row, col = 1, 0
    for text in buttons:
        create_button(text, row, col)
        col += 1
        if col > 3:
            col = 0
            row += 1
            
window = tk.Tk()
window.title("Calculator")
setup_calculator()
window.mainloop()
