from tkinter import Tk, Label, Entry

root = Tk()
root.geometry("500x600")
root.title("Love Calculator")
root.config(bg='#6e1423')

heading = Label(root, text="Love Calculator", font=('Times new roman', 40, 'bold'),
                bg="#85182a", fg='#fdf0d5', border=2, relief='solid')
heading.place(x=20, y=20, height=100, width=460)

your_name = Label(root, text="Enter Your Name", font=('Arial', 15),
                  bg="#6e1423", fg='black', )
your_name.place(x=20, y=170, height=30, width=460)


partner_name = Label(root, text="Enter Your Partner's Name", font=('Arial', 15),
                     bg="#6e1423", fg='black', )
partner_name.place(x=20, y=350, height=30, width=460)


root.mainloop()
