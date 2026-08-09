import tkinter as tk
import math


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("520x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#181818")

        self.expression = ""

        # ---------------- DISPLAY ----------------
        self.display = tk.Entry(
            root,
            font=("Arial", 28),
            bg="#252525",
            fg="white",
            insertbackground="white",
            justify="right",
            bd=0
        )
        self.display.pack(
            padx=15,
            pady=20,
            fill="x",
            ipady=15
        )

        # ---------------- BUTTONS ----------------
        buttons = [
            ["sin", "cos", "tan", "log", "ln"],
            ["(", ")", "π", "e", "⌫"],
            ["7", "8", "9", "÷", "√"],
            ["4", "5", "6", "×", "x²"],
            ["1", "2", "3", "−", "xʸ"],
            ["0", ".", "%", "+", "="],
            ["C", "sin⁻¹", "cos⁻¹", "tan⁻¹", "n!"]
        ]

        for row in buttons:
            frame = tk.Frame(root, bg="#181818")
            frame.pack(expand=True, fill="both")

            for button in row:

                if button == "=":
                    color = "#0078D7"
                elif button in ["+", "−", "×", "÷", "x²", "xʸ"]:
                    color = "#FF9500"
                elif button in ["C", "⌫"]:
                    color = "#B83232"
                elif button in [
                    "sin", "cos", "tan", "log", "ln",
                    "√", "π", "e", "sin⁻¹",
                    "cos⁻¹", "tan⁻¹", "n!"
                ]:
                    color = "#444444"
                else:
                    color = "#303030"

                tk.Button(
                    frame,
                    text=button,
                    font=("Arial", 15, "bold"),
                    fg="white",
                    bg=color,
                    activebackground="#666666",
                    activeforeground="white",
                    bd=0,
                    command=lambda b=button: self.press(b)
                ).pack(
                    side="left",
                    expand=True,
                    fill="both",
                    padx=3,
                    pady=3
                )

    # ---------------- BUTTON LOGIC ----------------
    def press(self, button):

        if button == "C":
            self.expression = ""
            self.display.delete(0, tk.END)

        elif button == "⌫":
            self.expression = self.expression[:-1]
            self.update_display()

        elif button == "=":
            self.calculate()

        elif button == "π":
            self.expression += "pi"
            self.update_display()

        elif button == "e":
            self.expression += "e"
            self.update_display()

        elif button == "sin":
            self.expression += "sin("
            self.update_display()

        elif button == "cos":
            self.expression += "cos("
            self.update_display()

        elif button == "tan":
            self.expression += "tan("
            self.update_display()

        elif button == "sin⁻¹":
            self.expression += "asin("
            self.update_display()

        elif button == "cos⁻¹":
            self.expression += "acos("
            self.update_display()

        elif button == "tan⁻¹":
            self.expression += "atan("
            self.update_display()

        elif button == "log":
            self.expression += "log10("
            self.update_display()

        elif button == "ln":
            self.expression += "log("
            self.update_display()

        elif button == "√":
            self.expression += "sqrt("
            self.update_display()

        elif button == "x²":
            self.expression += "**2"
            self.update_display()

        elif button == "xʸ":
            self.expression += "**"
            self.update_display()

        elif button == "n!":
            self.expression += "factorial("
            self.update_display()

        elif button == "×":
            self.expression += "*"
            self.update_display()

        elif button == "÷":
            self.expression += "/"
            self.update_display()

        elif button == "−":
            self.expression += "-"
            self.update_display()

        elif button == "%":
            self.expression += "/100"
            self.update_display()

        else:
            self.expression += button
            self.update_display()

    # ---------------- DISPLAY ----------------
    def update_display(self):
        self.display.delete(0, tk.END)

        shown = self.expression

        shown = shown.replace("**", "^")
        shown = shown.replace("*", "×")
        shown = shown.replace("/", "÷")
        shown = shown.replace("sqrt", "√")

        self.display.insert(0, shown)

    # ---------------- CALCULATION ----------------
    def calculate(self):

        try:
            result = eval(
                self.expression,
                {
                    "__builtins__": {},
                    "sin": lambda x: math.sin(math.radians(x)),
                    "cos": lambda x: math.cos(math.radians(x)),
                    "tan": lambda x: math.tan(math.radians(x)),
                    "asin": lambda x: math.degrees(math.asin(x)),
                    "acos": lambda x: math.degrees(math.acos(x)),
                    "atan": lambda x: math.degrees(math.atan(x)),
                    "sqrt": math.sqrt,
                    "log10": math.log10,
                    "log": math.log,
                    "factorial": math.factorial,
                    "pi": math.pi,
                    "e": math.e
                }
            )

            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 10)

            self.expression = str(result)

            self.display.delete(0, tk.END)
            self.display.insert(0, result)

        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.expression = ""


# ---------------- START PROGRAM ----------------
root = tk.Tk()
app = ScientificCalculator(root)
root.mainloop()