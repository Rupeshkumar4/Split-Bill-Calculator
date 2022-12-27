from tkinter import *
from tkinter import messagebox
sp=Tk()
sp.title(" BILL SPLIT!! ")
sp.geometry("500x500")
sp.config(bg="lightyellow")
sp.minsize(500,500)
sp.maxsize(500,500)




## Taking th input for total bill
lab=Label(sp,text="Total Bill",font=("Time New Roman",20,"bold",),bg="yellow",fg="black", anchor="w")
lab.place(x=40,y=50, width = 250) ## this is label
# now input 
total_bill = Entry(font=20, text = 'total bill', borderwidth=2)
total_bill.place(x=40, y = 90, height=25, width=250)


## Taking tip percent as input
lab=Label(sp,text="TIPS PERCENT",font=("Time New Roman",20,"bold",),bg="yellow",fg="black", anchor="w")
lab.place(x=40,y=130, width  = 250)
## input of tips
tips = Entry(font=20)
tips.place(x = 40, y = 170, height = 25)


## Now with no of person
lab=Label(sp,text="NO OF PERSON",font=("Time New Roman",20,"bold",),bg="yellow",fg="black", anchor="w")
lab.place(x=40,y=210, width = 250)
# taking input for no of person
no_person = Entry(font=20)
no_person.place(x = 40, y = 250, height = 25)

answer_label = Label(sp, text="Split bill is : ", font=("Time New Roman",22,"bold",),bg="cyan",fg="blue")
answer_label.place(x = 100, y = 330, width = 300)


def calculate():
    try:
        t_bill = float(total_bill.get())
        t_perc = float(tips.get())
        n_pers = int(no_person.get())

        calculate = (t_bill*(1 + t_perc/100))/n_pers
        answer_label.config(text = "Split bill is {:.2f}".format(calculate))
    except:
        messagebox.showwarning("Warning", "Enter correct details.")


button=Button(sp,text="CALCULATE",font=("Time New Roman",30,"bold"),relief="raised",fg="green",command=calculate)
button.place(x=100,y=400)

sp.mainloop()