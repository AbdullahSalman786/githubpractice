import tkinter as tk
from tkinter import ttk, messagebox
import math
import cmath
import statistics
import random
import re

import sympy as sp
import numpy as np


# ============================================================
# SCIENTIFIC CALCULATOR
# ============================================================

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Scientific Calculator")
        self.root.geometry("1200x760")
        self.root.minsize(1000, 650)

        self.dark = True
        self.angle_mode = "DEG"
        self.ans = 0
        self.memory = 0
        self.history = []

        self.configure_style()
        self.create_menu()
        self.create_main_interface()

    # ========================================================
    # STYLE
    # ========================================================

    def configure_style(self):
        self.bg = "#171717"
        self.panel = "#222222"
        self.button = "#303030"
        self.function = "#444444"
        self.orange = "#ff9500"
        self.blue = "#1677ff"
        self.red = "#b83232"
        self.text = "#ffffff"
        self.secondary = "#aaaaaa"

        self.root.configure(bg=self.bg)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TNotebook",
            background=self.bg,
            borderwidth=0
        )

        style.configure(
            "TNotebook.Tab",
            background=self.panel,
            foreground=self.text,
            padding=[15, 8]
        )

        style.map(
            "TNotebook.Tab",
            background=[("selected", self.blue)]
        )

    # ========================================================
    # MENU
    # ========================================================

    def create_menu(self):
        menu = tk.Menu(self.root)

        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(
            label="Clear History",
            command=self.clear_history
        )
        file_menu.add_separator()
        file_menu.add_command(
            label="Exit",
            command=self.root.destroy
        )

        view_menu = tk.Menu(menu, tearoff=0)
        view_menu.add_command(
            label="Dark Mode",
            command=lambda: self.set_theme(True)
        )
        view_menu.add_command(
            label="Light Mode",
            command=lambda: self.set_theme(False)
        )

        menu.add_cascade(label="File", menu=file_menu)
        menu.add_cascade(label="View", menu=view_menu)

        self.root.config(menu=menu)

    # ========================================================
    # MAIN INTERFACE
    # ========================================================

    def create_main_interface(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=8, pady=8)

        calculator_tab = tk.Frame(
            notebook,
            bg=self.bg
        )

        algebra_tab = tk.Frame(
            notebook,
            bg=self.bg
        )

        statistics_tab = tk.Frame(
            notebook,
            bg=self.bg
        )

        matrix_tab = tk.Frame(
            notebook,
            bg=self.bg
        )

        conversion_tab = tk.Frame(
            notebook,
            bg=self.bg
        )

        number_tab = tk.Frame(
            notebook,
            bg=self.bg
        )

        notebook.add(
            calculator_tab,
            text="Calculator"
        )

        notebook.add(
            algebra_tab,
            text="Algebra"
        )

        notebook.add(
            statistics_tab,
            text="Statistics"
        )

        notebook.add(
            matrix_tab,
            text="Matrices"
        )

        notebook.add(
            conversion_tab,
            text="Conversions"
        )

        notebook.add(
            number_tab,
            text="Number Systems"
        )

        self.create_calculator(calculator_tab)
        self.create_algebra(algebra_tab)
        self.create_statistics(statistics_tab)
        self.create_matrix(matrix_tab)
        self.create_conversions(conversion_tab)
        self.create_number_systems(number_tab)

    # ========================================================
    # CALCULATOR
    # ========================================================

    def create_calculator(self, parent):

        top = tk.Frame(
            parent,
            bg=self.bg
        )
        top.pack(fill="x", padx=15, pady=10)

        self.mode_label = tk.Label(
            top,
            text="Angle: DEG",
            bg=self.bg,
            fg=self.secondary,
            font=("Arial", 12)
        )
        self.mode_label.pack(side="left")

        tk.Button(
            top,
            text="DEG",
            command=lambda: self.set_angle("DEG"),
            bg=self.function,
            fg=self.text,
            bd=0,
            padx=12,
            pady=5
        ).pack(side="right", padx=2)

        tk.Button(
            top,
            text="RAD",
            command=lambda: self.set_angle("RAD"),
            bg=self.function,
            fg=self.text,
            bd=0,
            padx=12,
            pady=5
        ).pack(side="right", padx=2)

        tk.Button(
            top,
            text="GRAD",
            command=lambda: self.set_angle("GRAD"),
            bg=self.function,
            fg=self.text,
            bd=0,
            padx=12,
            pady=5
        ).pack(side="right", padx=2)

        self.display = tk.Entry(
            parent,
            font=("Arial", 28),
            bg="#252525",
            fg=self.text,
            insertbackground=self.text,
            justify="right",
            bd=0
        )

        self.display.pack(
            fill="x",
            padx=15,
            pady=(0, 15),
            ipady=15
        )

        self.display.bind(
            "<Return>",
            lambda event: self.calculate()
        )

        self.create_calculator_buttons(parent)

    # ========================================================
    # CALCULATOR BUTTONS
    # ========================================================

    def create_calculator_buttons(self, parent):

        buttons = [

            ["MC", "MR", "M+", "M-", "Ans", "C", "⌫"],

            [
                "sin", "cos", "tan",
                "asin", "acos", "atan",
                "sinh"
            ],

            [
                "cosh", "tanh", "ln",
                "log", "log2", "10^x",
                "e^x"
            ],

            [
                "√", "∛", "x²",
                "x³", "xʸ", "1/x",
                "!"
            ],

            [
                "(", ")", "π",
                "e", "abs", "floor",
                "ceil"
            ],

            [
                "7", "8", "9",
                "÷", "%", "mod",
                "±"
            ],

            [
                "4", "5", "6",
                "×", "nPr", "nCr",
                "GCD"
            ],

            [
                "1", "2", "3",
                "−", "LCM", "random",
                "i"
            ],

            [
                "0", ".", ",",
                "+", "=", "HIST",
                "COPY"
            ]
        ]

        container = tk.Frame(
            parent,
            bg=self.bg
        )
        container.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        for r, row in enumerate(buttons):

            container.rowconfigure(
                r,
                weight=1
            )

            for c in range(len(row)):
                container.columnconfigure(
                    c,
                    weight=1
                )

            for c, text in enumerate(row):

                if text == "=":
                    color = self.blue
                elif text in ["+", "−", "×", "÷", "=", "%", "mod"]:
                    color = self.orange
                elif text in ["C", "⌫"]:
                    color = self.red
                elif text in [
                    "sin", "cos", "tan",
                    "asin", "acos", "atan",
                    "sinh", "cosh", "tanh",
                    "ln", "log", "log2",
                    "√", "∛", "x²", "x³",
                    "xʸ", "1/x", "nPr",
                    "nCr", "GCD", "LCM"
                ]:
                    color = self.function
                else:
                    color = self.button

                tk.Button(
                    container,
                    text=text,
                    font=("Arial", 12, "bold"),
                    bg=color,
                    fg=self.text,
                    activebackground="#666666",
                    activeforeground="white",
                    bd=0,
                    command=lambda x=text: self.calculator_button(x)
                ).grid(
                    row=r,
                    column=c,
                    sticky="nsew",
                    padx=3,
                    pady=3
                )

    # ========================================================
    # CALCULATOR LOGIC
    # ========================================================

    def calculator_button(self, value):

        if value == "C":
            self.display.delete(0, tk.END)

        elif value == "⌫":
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current[:-1])

        elif value == "=":
            self.calculate()

        elif value == "HIST":
            self.show_history()

        elif value == "COPY":
            self.copy_result()

        elif value == "MC":
            self.memory = 0

        elif value == "MR":
            self.insert_text(str(self.memory))

        elif value == "M+":
            try:
                self.memory += float(self.evaluate_expression())
            except:
                pass

        elif value == "M-":
            try:
                self.memory -= float(self.evaluate_expression())
            except:
                pass

        elif value == "Ans":
            self.insert_text(str(self.ans))

        elif value == "π":
            self.insert_text("pi")

        elif value == "e":
            self.insert_text("E")

        elif value == "i":
            self.insert_text("I")

        elif value == "sin":
            self.insert_text("sin(")

        elif value == "cos":
            self.insert_text("cos(")

        elif value == "tan":
            self.insert_text("tan(")

        elif value == "asin":
            self.insert_text("asin(")

        elif value == "acos":
            self.insert_text("acos(")

        elif value == "atan":
            self.insert_text("atan(")

        elif value == "sinh":
            self.insert_text("sinh(")

        elif value == "cosh":
            self.insert_text("cosh(")

        elif value == "tanh":
            self.insert_text("tanh(")

        elif value == "ln":
            self.insert_text("ln(")

        elif value == "log":
            self.insert_text("log10(")

        elif value == "log2":
            self.insert_text("log2(")

        elif value == "√":
            self.insert_text("sqrt(")

        elif value == "∛":
            self.insert_text("root(")

        elif value == "x²":
            self.insert_text("^2")

        elif value == "x³":
            self.insert_text("^3")

        elif value == "xʸ":
            self.insert_text("^")

        elif value == "10^x":
            self.insert_text("10^(")

        elif value == "e^x":
            self.insert_text("exp(")

        elif value == "1/x":
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, f"1/({current})")

        elif value == "!":
            self.insert_text("!")

        elif value == "abs":
            self.insert_text("abs(")

        elif value == "floor":
            self.insert_text("floor(")

        elif value == "ceil":
            self.insert_text("ceil(")

        elif value == "nPr":
            self.insert_text("P(")

        elif value == "nCr":
            self.insert_text("C(")

        elif value == "GCD":
            self.insert_text("gcd(")

        elif value == "LCM":
            self.insert_text("lcm(")

        elif value == "random":
            self.insert_text(str(random.random()))

        elif value == "±":
            current = self.display.get()

            if current:
                self.display.delete(0, tk.END)
                self.display.insert(0, f"-({current})")

        else:
            self.insert_text(value)

    # ========================================================
    # EXPRESSION HELPERS
    # ========================================================

    def insert_text(self, text):
        self.display.insert(tk.INSERT, text)

    def set_angle(self, mode):
        self.angle_mode = mode
        self.mode_label.config(
            text=f"Angle: {mode}"
        )

    def trig_value(self, function, x):

        if self.angle_mode == "DEG":
            x = math.radians(x)

        elif self.angle_mode == "GRAD":
            x = x * math.pi / 200

        return function(x)

    def evaluate_expression(self):

        expression = self.display.get()

        expression = expression.replace(
            "×", "*"
        ).replace(
            "÷", "/"
        ).replace(
            "^", "**"
        ).replace(
            "mod", "%"
        )

        expression = expression.replace(
            "P(", "perm("
        )

        expression = expression.replace(
            "C(", "comb("
        )

        expression = re.sub(
            r"(\d+)!",
            r"factorial(\1)",
            expression
        )

        local_dict = {
            "pi": math.pi,
            "E": math.e,
            "I": sp.I,

            "sin": lambda x: self.trig_value(math.sin, x),
            "cos": lambda x: self.trig_value(math.cos, x),
            "tan": lambda x: self.trig_value(math.tan, x),

            "asin": lambda x: math.degrees(math.asin(x)),
            "acos": lambda x: math.degrees(math.acos(x)),
            "atan": lambda x: math.degrees(math.atan(x)),

            "sinh": math.sinh,
            "cosh": math.cosh,
            "tanh": math.tanh,

            "ln": math.log,
            "log10": math.log10,
            "log2": math.log2,

            "sqrt": math.sqrt,
            "root": lambda x, n=3: x ** (1 / n),

            "exp": math.exp,

            "factorial": math.factorial,

            "abs": abs,
            "floor": math.floor,
            "ceil": math.ceil,

            "perm": math.perm,
            "comb": math.comb,

            "gcd": math.gcd,
            "lcm": math.lcm
        }

        return eval(
            expression,
            {"__builtins__": {}},
            local_dict
        )

    def calculate(self):

        try:
            expression = self.display.get()

            result = self.evaluate_expression()

            self.ans = result

            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 12)

            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))

            self.history.append(
                f"{expression} = {result}"
            )

        except Exception as error:
            messagebox.showerror(
                "Calculation Error",
                f"Invalid expression.\n\n{error}"
            )

    # ========================================================
    # HISTORY
    # ========================================================

    def show_history(self):

        window = tk.Toplevel(self.root)
        window.title("Calculation History")
        window.geometry("500x500")
        window.configure(bg=self.bg)

        listbox = tk.Listbox(
            window,
            bg=self.panel,
            fg=self.text,
            font=("Consolas", 12)
        )

        listbox.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        for item in self.history:
            listbox.insert(tk.END, item)

    def clear_history(self):
        self.history.clear()

    def copy_result(self):

        value = self.display.get()

        self.root.clipboard_clear()
        self.root.clipboard_append(value)

    # ========================================================
    # ALGEBRA
    # ========================================================

    def create_algebra(self, parent):

        title = tk.Label(
            parent,
            text="Algebra & Equation Solver",
            bg=self.bg,
            fg=self.text,
            font=("Arial", 22, "bold")
        )
        title.pack(pady=20)

        self.algebra_entry = tk.Entry(
            parent,
            font=("Arial", 18),
            bg=self.panel,
            fg=self.text,
            insertbackground=self.text
        )

        self.algebra_entry.pack(
            fill="x",
            padx=30,
            pady=10,
            ipady=10
        )

        examples = tk.Label(
            parent,
            text="Examples: x^2 - 5*x + 6 = 0    |    x^2 + 2*x + 1",
            bg=self.bg,
            fg=self.secondary
        )

        examples.pack()

        tk.Button(
            parent,
            text="Solve / Simplify",
            command=self.solve_algebra,
            bg=self.blue,
            fg="white",
            bd=0,
            font=("Arial", 14, "bold"),
            padx=20,
            pady=10
        ).pack(pady=15)

        self.algebra_result = tk.Text(
            parent,
            bg=self.panel,
            fg=self.text,
            font=("Consolas", 14)
        )

        self.algebra_result.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

    def solve_algebra(self):

        try:
            expression = self.algebra_entry.get()

            x = sp.symbols("x")

            if "=" in expression:
                left, right = expression.split("=")

                equation = sp.Eq(
                    sp.sympify(left),
                    sp.sympify(right)
                )

                result = sp.solve(equation, x)

            else:
                expression = sp.sympify(expression)

                result = sp.simplify(expression)

                factor = sp.factor(expression)
                expand = sp.expand(expression)

                result = (
                    f"Simplified:\n{result}\n\n"
                    f"Factored:\n{factor}\n\n"
                    f"Expanded:\n{expand}"
                )

            self.algebra_result.delete(
                "1.0",
                tk.END
            )

            self.algebra_result.insert(
                tk.END,
                str(result)
            )

        except Exception as error:
            messagebox.showerror(
                "Algebra Error",
                str(error)
            )

    # ========================================================
    # STATISTICS
    # ========================================================

    def create_statistics(self, parent):

        title = tk.Label(
            parent,
            text="Statistics Calculator",
            bg=self.bg,
            fg=self.text,
            font=("Arial", 22, "bold")
        )
        title.pack(pady=20)

        tk.Label(
            parent,
            text="Enter numbers separated by commas:",
            bg=self.bg,
            fg=self.text,
            font=("Arial", 13)
        ).pack()

        self.stats_entry = tk.Entry(
            parent,
            font=("Arial", 18),
            bg=self.panel,
            fg=self.text,
            insertbackground=self.text
        )

        self.stats_entry.pack(
            fill="x",
            padx=30,
            pady=15,
            ipady=10
        )

        tk.Button(
            parent,
            text="Calculate Statistics",
            command=self.calculate_statistics,
            bg=self.blue,
            fg="white",
            bd=0,
            font=("Arial", 14, "bold"),
            padx=20,
            pady=10
        ).pack()

        self.stats_result = tk.Text(
            parent,
            bg=self.panel,
            fg=self.text,
            font=("Consolas", 14)
        )

        self.stats_result.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

    def calculate_statistics(self):

        try:
            values = [
                float(x.strip())
                for x in self.stats_entry.get().split(",")
            ]

            mean = statistics.mean(values)
            median = statistics.median(values)

            try:
                mode = statistics.mode(values)
            except:
                mode = "No unique mode"

            variance_population = statistics.pvariance(
                values
            )

            variance_sample = (
                statistics.variance(values)
                if len(values) > 1
                else 0
            )

            std_population = math.sqrt(
                variance_population
            )

            std_sample = math.sqrt(
                variance_sample
            )

            values_sorted = sorted(values)

            result = f"""
COUNT          = {len(values)}
SUM            = {sum(values)}
MEAN           = {mean}
MEDIAN         = {median}
MODE           = {mode}

MINIMUM        = {min(values)}
MAXIMUM        = {max(values)}
RANGE          = {max(values) - min(values)}

POP VARIANCE   = {variance_population}
SAMPLE VARIANCE= {variance_sample}

POP STD DEV    = {std_population}
SAMPLE STD DEV = {std_sample}

Q1             = {np.percentile(values, 25)}
Q2             = {np.percentile(values, 50)}
Q3             = {np.percentile(values, 75)}

SORTED:
{values_sorted}
"""

            self.stats_result.delete(
                "1.0",
                tk.END
            )

            self.stats_result.insert(
                tk.END,
                result
            )

        except Exception as error:
            messagebox.showerror(
                "Statistics Error",
                str(error)
            )

    # ========================================================
    # MATRICES
    # ========================================================

    def create_matrix(self, parent):

        title = tk.Label(
            parent,
            text="Matrix Calculator",
            bg=self.bg,
            fg=self.text,
            font=("Arial", 22, "bold")
        )

        title.pack(pady=20)

        tk.Label(
            parent,
            text="Matrix A (rows separated by ; and values by spaces)",
            bg=self.bg,
            fg=self.text
        ).pack()

        self.matrix_a = tk.Entry(
            parent,
            font=("Arial", 16),
            bg=self.panel,
            fg=self.text,
            insertbackground=self.text
        )

        self.matrix_a.pack(
            fill="x",
            padx=30,
            pady=10,
            ipady=8
        )

        tk.Label(
            parent,
            text="Matrix B",
            bg=self.bg,
            fg=self.text
        ).pack()

        self.matrix_b = tk.Entry(
            parent,
            font=("Arial", 16),
            bg=self.panel,
            fg=self.text,
            insertbackground=self.text
        )

        self.matrix_b.pack(
            fill="x",
            padx=30,
            pady=10,
            ipady=8
        )

        example = tk.Label(
            parent,
            text="Example: 1 2; 3 4",
            bg=self.bg,
            fg=self.secondary
        )

        example.pack()

        buttons = tk.Frame(
            parent,
            bg=self.bg
        )

        buttons.pack(pady=15)

        operations = [
            ("A + B", "add"),
            ("A - B", "sub"),
            ("A × B", "mul"),
            ("det(A)", "det"),
            ("A⁻¹", "inv"),
            ("Aᵀ", "transpose")
        ]

        for text, operation in operations:

            tk.Button(
                buttons,
                text=text,
                command=lambda op=operation:
                self.matrix_operation(op),
                bg=self.function,
                fg=self.text,
                bd=0,
                padx=15,
                pady=8
            ).pack(
                side="left",
                padx=4
            )

        self.matrix_result = tk.Text(
            parent,
            bg=self.panel,
            fg=self.text,
            font=("Consolas", 14)
        )

        self.matrix_result.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

    def parse_matrix(self, text):

        rows = text.split(";")

        return np.array([
            [
                float(x)
                for x in row.split()
            ]
            for row in rows
        ])

    def matrix_operation(self, operation):

        try:

            A = self.parse_matrix(
                self.matrix_a.get()
            )

            result = None

            if operation == "det":
                result = np.linalg.det(A)

            elif operation == "inv":
                result = np.linalg.inv(A)

            elif operation == "transpose":
                result = A.T

            else:

                B = self.parse_matrix(
                    self.matrix_b.get()
                )

                if operation == "add":
                    result = A + B

                elif operation == "sub":
                    result = A - B

                elif operation == "mul":
                    result = A @ B

            self.matrix_result.delete(
                "1.0",
                tk.END
            )

            self.matrix_result.insert(
                tk.END,
                str(result)
            )

        except Exception as error:
            messagebox.showerror(
                "Matrix Error",
                str(error)
            )

    # ========================================================
    # UNIT CONVERSIONS
    # ========================================================

    def create_conversions(self, parent):

        title = tk.Label(
            parent,
            text="Unit Converter",
            bg=self.bg,
            fg=self.text,
            font=("Arial", 22, "bold")
        )

        title.pack(pady=20)

        frame = tk.Frame(
            parent,
            bg=self.bg
        )

        frame.pack(pady=20)

        tk.Label(
            frame,
            text="Value:",
            bg=self.bg,
            fg=self.text
        ).grid(row=0, column=0, padx=5)

        self.convert_value = tk.Entry(
            frame,
            font=("Arial", 16),
            bg=self.panel,
            fg=self.text
        )

        self.convert_value.grid(
            row=0,
            column=1,
            padx=5
        )

        tk.Label(
            frame,
            text="Type:",
            bg=self.bg,
            fg=self.text
        ).grid(row=1, column=0, padx=5, pady=10)

        self.convert_type = ttk.Combobox(
            frame,
            values=[
                "Length",
                "Temperature",
                "Mass",
                "Time",
                "Speed",
                "Area"
            ],
            state="readonly"
        )

        self.convert_type.current(0)

        self.convert_type.grid(
            row=1,
            column=1
        )

        tk.Label(
            frame,
            text="From:",
            bg=self.bg,
            fg=self.text
        ).grid(row=2, column=0)

        self.convert_from = ttk.Entry(
            frame
        )

        self.convert_from.grid(
            row=2,
            column=1,
            pady=5
        )

        tk.Label(
            frame,
            text="To:",
            bg=self.bg,
            fg=self.text
        ).grid(row=3, column=0)

        self.convert_to = ttk.Entry(
            frame
        )

        self.convert_to.grid(
            row=3,
            column=1
        )

        tk.Button(
            parent,
            text="Convert",
            command=self.convert,
            bg=self.blue,
            fg="white",
            bd=0,
            padx=30,
            pady=10
        ).pack(pady=15)

        self.convert_result = tk.Label(
            parent,
            text="Result:",
            bg=self.bg,
            fg=self.text,
            font=("Arial", 18)
        )

        self.convert_result.pack(pady=20)

    def convert(self):

        try:

            value = float(
                self.convert_value.get()
            )

            conversion_type = (
                self.convert_type.get()
            )

            source = (
                self.convert_from.get()
                .lower()
                .strip()
            )

            target = (
                self.convert_to.get()
                .lower()
                .strip()
            )

            # LENGTH
            length = {
                "m": 1,
                "km": 1000,
                "cm": 0.01,
                "mm": 0.001,
                "mile": 1609.344,
                "ft": 0.3048,
                "in": 0.0254,
                "yard": 0.9144
            }

            # MASS
            mass = {
                "kg": 1,
                "g": 0.001,
                "mg": 0.000001,
                "lb": 0.45359237,
                "oz": 0.0283495
            }

            # TIME
            time_units = {
                "s": 1,
                "min": 60,
                "h": 3600,
                "day": 86400
            }

            # SPEED
            speed = {
                "m/s": 1,
                "km/h": 1 / 3.6,
                "mph": 0.44704,
                "ft/s": 0.3048
            }

            if conversion_type == "Length":

                result = (
                    value *
                    length[source] /
                    length[target]
                )

            elif conversion_type == "Mass":

                result = (
                    value *
                    mass[source] /
                    mass[target]
                )

            elif conversion_type == "Time":

                result = (
                    value *
                    time_units[source] /
                    time_units[target]
                )

            elif conversion_type == "Speed":

                result = (
                    value *
                    speed[source] /
                    speed[target]
                )

            elif conversion_type == "Temperature":

                if source == "c":
                    celsius = value

                elif source == "f":
                    celsius = (value - 32) * 5 / 9

                elif source == "k":
                    celsius = value - 273.15

                else:
                    raise ValueError(
                        "Use C, F, or K"
                    )

                if target == "c":
                    result = celsius

                elif target == "f":
                    result = celsius * 9 / 5 + 32

                elif target == "k":
                    result = celsius + 273.15

                else:
                    raise ValueError(
                        "Use C, F, or K"
                    )

            elif conversion_type == "Area":

                units = {
                    "m2": 1,
                    "km2": 1_000_000,
                    "cm2": 0.0001,
                    "ft2": 0.092903
                }

                result = (
                    value *
                    units[source] /
                    units[target]
                )

            self.convert_result.config(
                text=f"Result: {result}"
            )

        except Exception as error:
            messagebox.showerror(
                "Conversion Error",
                str(error)
            )

    # ========================================================
    # NUMBER SYSTEMS
    # ========================================================

    def create_number_systems(self, parent):

        title = tk.Label(
            parent,
            text="Number System Converter",
            bg=self.bg,
            fg=self.text,
            font=("Arial", 22, "bold")
        )

        title.pack(pady=20)

        frame = tk.Frame(
            parent,
            bg=self.bg
        )

        frame.pack(pady=20)

        tk.Label(
            frame,
            text="Number:",
            bg=self.bg,
            fg=self.text
        ).grid(row=0, column=0)

        self.number_input = tk.Entry(
            frame,
            font=("Arial", 18),
            bg=self.panel,
            fg=self.text
        )

        self.number_input.grid(
            row=0,
            column=1,
            padx=10
        )

        tk.Label(
            frame,
            text="Base:",
            bg=self.bg,
            fg=self.text
        ).grid(row=1, column=0, pady=10)

        self.number_base = ttk.Combobox(
            frame,
            values=[
                "2",
                "8",
                "10",
                "16"
            ],
            state="readonly"
        )

        self.number_base.set("10")

        self.number_base.grid(
            row=1,
            column=1
        )

        tk.Button(
            parent,
            text="Convert",
            command=self.convert_number,
            bg=self.blue,
            fg="white",
            bd=0,
            padx=30,
            pady=10
        ).pack()

        self.number_result = tk.Text(
            parent,
            bg=self.panel,
            fg=self.text,
            font=("Consolas", 16)
        )

        self.number_result.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

    def convert_number(self):

        try:

            number = self.number_input.get()

            base = int(
                self.number_base.get()
            )

            decimal = int(
                number,
                base
            )

            result = f"""
DECIMAL      : {decimal}
BINARY       : {bin(decimal)}
OCTAL        : {oct(decimal)}
HEXADECIMAL  : {hex(decimal)}

HEX VALUE    : {format(decimal, 'X')}
BINARY VALUE : {format(decimal, 'b')}
"""

            self.number_result.delete(
                "1.0",
                tk.END
            )

            self.number_result.insert(
                tk.END,
                result
            )

        except Exception as error:
            messagebox.showerror(
                "Number System Error",
                str(error)
            )

    # ========================================================
    # THEME
    # ========================================================

    def set_theme(self, dark):

        if dark:
            self.bg = "#171717"
            self.panel = "#222222"
            self.text = "#ffffff"

        else:
            self.bg = "#eeeeee"
            self.panel = "#ffffff"
            self.text = "#111111"

        self.root.configure(
            bg=self.bg
        )


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = ScientificCalculator(root)

    root.mainloop()