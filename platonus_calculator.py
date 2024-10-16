import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        rk1 = float(entry_rk1.get())
        rk2 = float(entry_rk2.get())
        st = float(entry_st.get())
        exam = float(entry_exam.get())

        result = (rk1 + rk2) / 2.0 * 0.2 + (exam + st) * 0.4
        label_result.config(text=f"Результат: {result:.2f}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа!")

def calculate_exam_needed():
    try:
        rk1 = float(entry_rk1.get())
        rk2 = float(entry_rk2.get())
        st = float(entry_st.get())
        desired_result = float(entry_desired_result.get())

        exam_needed = (desired_result - (rk1 + rk2) / 2.0 * 0.2 - st * 0.4) / 0.4

        if exam_needed < 0:
            label_exam_needed.config(text="Невозможно достигнуть такого результата!")
        else:
            label_exam_needed.config(text=f"Необходимо набрать на экзамене: {exam_needed:.2f}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа!")

root = tk.Tk()
root.title("Platonus Calculator")

label_rk1 = tk.Label(root, text="Первый модуль:")
label_rk1.grid(row=0, column=0, pady = 10)
entry_rk1 = tk.Entry(root)
entry_rk1.grid(row=0, column=1)

label_rk2 = tk.Label(root, text="Второй модуль:")
label_rk2.grid(row=1, column=0)
entry_rk2 = tk.Entry(root)
entry_rk2.grid(row=1, column=1)

label_st = tk.Label(root, text="Сред.ауд:")
label_st.grid(row=2, column=0)
entry_st = tk.Entry(root)
entry_st.grid(row=2, column=1)

label_exam = tk.Label(root, text="Экзамен:")
label_exam.grid(row=3, column=0)
entry_exam = tk.Entry(root)
entry_exam.grid(row=3, column=1)

button_calculate = tk.Button(root, text="Рассчитать результат", command=calculate)
button_calculate.grid(row=4, column=0, columnspan=2)

label_result = tk.Label(root, text="Результат: ")
label_result.grid(row=5, column=0, columnspan=2)

label_desired_result = tk.Label(root, text="Желаемый результат:")
label_desired_result.grid(row=6, column=0)
entry_desired_result = tk.Entry(root)
entry_desired_result.grid(row=6, column=1)

button_calculate_exam = tk.Button(root, text="Рассчитать необходимый балл", command=calculate_exam_needed)
button_calculate_exam.grid(row=7, column=0, columnspan=2)

label_exam_needed = tk.Label(root, text="Необходимо набрать на экзамене: ")
label_exam_needed.grid(row=8, column=0, columnspan=2)

root.mainloop()