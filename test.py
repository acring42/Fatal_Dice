from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("360x360")
window.title("Gold River 2.0")

window.config(background="#181818")


#enter weekly earnings
earnings = Entry()
earnings.pack()

# Calculate button's function
def calculate():

    total = float(earnings.get())

    # label which shows value of 'total'
    total_label = Label(window, text=f"${total}  earnt")
    total_label.pack()

    free = int(total) * 0.25

    # label which shows value of 'free'
    free_label = Label(window, text=f"FREE = {free}")
    free_label.pack()

    savings = int(total) * 0.30

    # label which shows value of 'savings'
    savings_label = Label(window, text=f"SAVINGS = {savings} earnt")
    savings_label.pack()

    business = int(total) * 0.15

    # label which shows value of 'business'
    business_label = Label(window, text=f"BUSINESS = {business}")
    business_label.pack()

    investment = int(total) * 0.20

    # label which shows value of 'investment'
    investment_label = Label(window, text=f"INVESTMENTS = {investment}")
    investment_label.pack()

    gifts = int(total) * 0.10

    # label which shows value of 'gifts'
    gifts_label = Label(window, text=f"GIFTS = {gifts}")
    gifts_label.pack()


calculate = Button(window, text="Calculate", command=calculate)
calculate.pack()


window.mainloop() #places window on computer screen