from tkinter import *
from tkinter import messagebox

# **************** Functions ****************


def calculate():
    number = int(total_calorie_e.get())
    total_protein = int(total_protein_e.get())
    protein_cal = total_protein * 4
    last_protein = protein_cal * 0.25
    sub_total = number - last_protein
    calculated_result.configure(text=sub_total)


def reset():
    calculated_result.configure(text='0000')
    total_protein_e.delete(0, 4)    # Only bug is that when reset is pressed I am left with a 0, can't find out why
    total_calorie_e.delete(0, 3)


def info_pop():
    # messagebox.showinfo("App Information", "This app takes your total protein grams and calculates the thermic effort "
    #                                        "of it and subtracts it from your total calorie intake")
    question_window = Tk()
    question_window.configure(bg='black')
    question_window.title("Question")
    question_window.iconbitmap('Burn.ico')
    question_window.geometry("470x55")
    question = "This app takes your total protein grams \nand calculates the thermic effort of \nit and subtracts it from " \
               "your total calorie intake "
    question_frame = Frame(question_window)
    question_frame.pack()
    question_label = Label(question_frame, text=question, bg='black', fg='white', font='Times, 12')
    question_label.pack()

    question_window.mainloop()


# **************** Main Window ****************
mainWindow = Tk()
mainWindow.title("Calorie Cutting App")
mainWindow.iconbitmap("Burn.ico")
mainWindow.geometry("345x500")
mainWindow.configure(bg='black')

# **************** Main Frame ****************
mainFrame = Frame(mainWindow, width=350, height=550, bg='black')
mainFrame.pack()

# **************** Calorie Label ****************
my_label = Label(mainFrame, text="Calorie Calculator For Cutting", fg='white', bg='black', font=("Arial", 18))
my_label.grid(row=1, column=0, padx=10, pady=10)


# **************** Version Label ****************
version_label = Label(mainFrame, text='Version 2.1', fg='red', bg='black', font=('Arial', 8))
version_label.grid(row=12, column=0, sticky='ws', pady=9)

# **************** Calculate Button ****************
buttonOne = Button(mainFrame, text='CALCULATE', bg='black', fg='cyan', font='Arial, 14', borderwidth=5,
                   command=calculate)
buttonOne.grid(row=6, column=0, pady=20)

reset_button = Button(mainFrame, text='RESET', bg='black', fg='cyan', font='Arial, 10', borderwidth=5, command=reset)
reset_button.grid(row=7, column=0, sticky=N)

info_button = Button(mainFrame, text='?', bg='black', fg='white', font='Arial, 8', width=2, command=info_pop)
info_button.grid(row=11, column=0, sticky=E)

# **************** Main Entries ****************
total_cal_label = Label(mainFrame, text="Total Calories:", fg='cyan', bg='black', font=('Arial', 14))
total_cal_label.grid(row=2, column=0)

total_calorie_e = Entry(mainFrame, font=('Arial', 16))  # Total Calorie .get()
total_calorie_e.grid(row=3, column=0, pady=5)

total_protein_label = Label(mainFrame, text='Total Protein Grams:', fg='cyan', bg='black',
                            font=('Arial', 14))
total_protein_label.grid(row=4, column=0, pady=10)

total_protein_e = Entry(mainFrame, font=('Arial', 16))  # Total Protein .get()
total_protein_e.grid(row=5, column=0)

# **************** Result Entries ****************
result_label = Label(mainFrame, text='Total Calories:', fg='cyan', bg='black', font=('Arial', 16))
result_label.grid(row=8, column=0, pady=30)

calculated_result = Label(mainFrame, text="0000", fg='white', bg='black', font=('Arial', 26))
calculated_result.grid(row=10, column=0)

mainWindow.mainloop()
