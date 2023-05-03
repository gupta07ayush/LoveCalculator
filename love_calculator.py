from tkinter import Tk, Label, Entry, Button

root = Tk()
root.geometry("500x670")
root.title("Love Calculator")
root.config(bg='#6e1423')

heading = Label(root, text="Love Calculator", font=('Times new roman', 40, 'bold'),
                bg="#161a1d", fg='#fdf0d5', border=3, relief='solid')
heading.place(x=20, y=20, height=100, width=460)

your_name = Label(root, text="Enter Your Name", font=('Arial', 15),
                  bg="#6e1423", fg='black', )
your_name.place(x=20, y=170, height=30, width=460)

your_name_entry = Entry(root, text="Enter Your Name", font=('Arial', 15),
                        bg="#590d22", fg='#fdf0d5', border=10)
your_name_entry.place(x=70, y=200, height=50, width=360)


partner_name = Label(root, text="Enter Your Partner's Name", font=('Arial', 15),
                     bg="#6e1423", fg='black', )
partner_name.place(x=20, y=320, height=30, width=460)

partner_name_entry = Entry(root, text="", font=('Arial', 15),
                           bg="#590d22", fg='#fdf0d5', border=10)
partner_name_entry.place(x=70, y=350, height=50, width=360)

calculate_button = Button(root, text="Result", font=('Arial', 15, 'bold'),
                          bg="#6e1423", fg='#fdf0d5', border=5)
calculate_button.place(x=150, y=460, height=50, width=200)

result = Label(root, text="", font=('Arial', 15),
               bg="#6e1423", fg='#fdf0d5', border=2, relief='solid')
result.place(x=50, y=550, height=70, width=400)


root.mainloop()
