
from tkinter import *
from tkinter.ttk import Combobox

#   CREATE THE FRAME FOR TKINTER
window = Tk()
window.title("Ticket sales")
window.geometry("400x400")
window.config(bg = "green")



#   CREATE A CLASS FOR THE TICKET SALES
class TicketSales:
    #   CREATE A VARIABLE THAT'S GONNA CONTAIN THE result_string
    result_string = StringVar()

    #
    def __init__(self, window):
        #   CREATE ALL THE NECESSARY WIDGETS
        self.cell_label = Label(window, text="Enter cellphone number")
        self.cell_label.place(x=10, y=10)
        self.cell_entry = Entry(window)
        self.cell_entry.place(x=200, y=10)

        self.ticket_category = Label(window, text="Select ticket category")
        self.ticket_category.place(x=10, y=50)
        self.category_combobox = Combobox(window, value=["Soccer", "Movie", "Theatre"])
        self.category_combobox.place(x=200, y=50)

        self.ticket_amount_label = Label(window, text="Number of tickets bought")
        self.ticket_amount_label.place(x=10, y=100)
        self.ticket_amount_entry = Entry(window)
        self.ticket_amount_entry.place(x=200, y=100)

        self.calculate_btn = Button(window, text="Calculate Ticket", command=self.calculate_pre_payment).place(x=10, y=150)
        self.clear_btn = Button(window, text="Clear entries", command=self.clear_entries).place(x=200, y=150)

        self.result_label = Label(window, text="", textvariable=self.result_string).place(x=10, y=200)

    #   FUNCTION WILL CALCULATE THE PAYABLE AMOUNT BY THE USER
    def calculate_pre_payment(self):
        from tkinter import messagebox

        #   GET THE VALUES FROM THE ENTRIES
        cell_number = self.cell_entry.get()
        ticket_amount = self.ticket_amount_entry.get()
        ticket_category = self.category_combobox.get()

        #   HERE, WE WILL DECIDE HOW MUCH THE ticket_price WILL BE BASED ON THE CHOSEN CATEGORY
        if ticket_category.lower() == "soccer":
            ticket_price = 40.00
        elif ticket_category.lower() == "movie":
            ticket_price = 75.00
        elif ticket_category.lower() == "theatre":
            ticket_price = 100.00
        else:
            #   THIS IS ONLY TRIGGERED IF THE ticket_category IS EMPTY OR THE STRING INSIDE DOESNT MATCH THE OPTIONS
            messagebox.showinfo(message="You have chosen an invalid category, please clear entries and try again.")

        #   WE CHECK IF THE ticket_price EXISTS, SO WE DONT CONTINUE WITH THE CALCULATION IF IT DOSN'T
        if ticket_price:
            #   HERE, WE CALCULATE THE amount_payable BEFORE VAT
            amount_payable = float(ticket_amount) * ticket_price
            #   NOW, WE CALCULATE THE VALUE OF THE VAT
            vat = amount_payable * 0.15
            #   NOW, WE ADD THE TWO TOGETHER
            amount_payable = amount_payable + vat

            #   SHOW THE USER THE DETAILS OF THE TRANSACTION
            self.result_string.set("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" + "\n" +
                                   "Amount Payable: R" + str(amount_payable) + "\n" +
                                   "Reservation for: " + str(ticket_category) + " for: " + str(ticket_amount) + " people" + "\n" +
                                   "was done by: " + str(cell_number) + "\n" +
                                   "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    #   FUNCTION CLEARS ALL THE ENTRIES CONTENTS
    def clear_entries(self):
        self.cell_entry.delete(0, END)
        self.ticket_amount_entry.delete(0, END)
        self.category_combobox.delete(0, END)


#   START EVERYTHING UP BY MAKING AN INSTANCE OF THE TicketSales CLASS AND PASSING IN THE TKINTER window OBJECT
ticket_sales = TicketSales(window)
window.mainloop()
