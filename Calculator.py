import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.current_input = tk.StringVar()
        self.current_input.set("")
        
        self.result = tk.StringVar()
        self.result.set("")
        
        self.create_widgets()

    def create_widgets(self):
        
        input_display = tk.Entry(self.root, textvariable=self.current_input, font=("Helvetica", 16), justify="right")
        input_display.grid(row=0, column=0, columnspan=4)
        
        
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]
        
        row_idx = 1
        col_idx = 0
        
        for button_text in buttons:
            tk.Button(self.root, text=button_text, padx=20, pady=20, font=("Helvetica", 14),
                      command=lambda b=button_text: self.button_click(b)).grid(row=row_idx, column=col_idx)
            col_idx += 1
            if col_idx > 3:
                col_idx = 0
                row_idx += 1

    def button_click(self, button_text):
        if button_text == "C":
            self.current_input.set("")
            self.result.set("")
        elif button_text == "=":
            try:
                expression = self.current_input.get()
                result = str(eval(expression))
                self.result.set(result)
                self.current_input.set(result)
            except:
                self.result.set("Error")
        else:
            current_value = self.current_input.get()
            if button_text == "←":
                self.current_input.set(current_value[:-1])
            else:
                self.current_input.set(current_value + button_text)

if __name__ == "__main__":
    root = tk.Tk()
    
    calculator = Calculator(root)
    root.mainloop()
