from tkinter import*
import random,string
root=Tk()
root.geometry("400x280")
root.title("Password Generator")
root.configure(bg="lightgreen")
title=StringVar()
label=Label(root,textvariable=title).pack()
title.set("The strength of password")
def selection():
    selection=choice.get()
choice=IntVar()
R1=Radiobutton(root,text="WEAK",variable=choice,value=1,command=selection).pack(anchor=CENTER ,pady=5)
R2=Radiobutton(root,text="MEDIUM",variable=choice,value=2,command=selection).pack(anchor=CENTER,pady=5)
R3=Radiobutton(root,text="STRONG",variable=choice,value=3,command=selection).pack(anchor=CENTER,pady=5)
labelchoice=Label(root)
labelchoice.pack()
lenlabel=StringVar()
lenlabel.set("Password length")
lentitle=Label(root,textvariable=lenlabel).pack(pady=5)
val=IntVar()
spinlenght=Spinbox(root,from_=8,to_=24,textvariable=val,width=13).pack(pady=5)

def callback():
    Isum.config(text=passgen())
passgenButton=Button(root,text="Generate Password",bd=5,bg="black",fg="white",height=2,command=callback,pady=3)
passgenButton.pack()
password=str(callback)

Isum=Label(root,text="")
Isum.pack(side=BOTTOM)


weak=string.ascii_uppercase+string.ascii_lowercase
medium=string.ascii_uppercase+string.ascii_lowercase+string.digits
symbols="""`!~@#$%^&*;()_-+={}""|?<>,./\:[]"""
strong=weak+medium+symbols

def passgen():
    if choice.get()==1:
        return "".join(random.sample(weak,val.get()))
    elif choice.get()==2:
        return "".join(random.sample(medium,val.get()))
    elif choice.get()==3:
        return "".join(random.sample(strong,val.get()))
root.mainloop()