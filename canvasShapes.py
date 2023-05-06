#Import the required libraries
from tkinter import *
import customtkinter as ctk
import datetime
from tkinter import messagebox

#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry
win.geometry("1280x720")

frm_C = Frame(win)
frm_C.grid(row=1,  column=1)

#Adding transparent background property
win.wm_attributes('-transparentcolor', '#ab23ff')
win.wm_attributes('-alpha', 1.0)

def lblAfter():
    def after():
        lbl.configure(text="This is a New line Text", bg='#0d60b1', foreground='#f76040')
        lbl.after(2000, lblAfter)

    lbl.configure(text="Now it's old", fg='blue', bg= '#ab23ff')
    lbl.after(1000, after)

#Create a Label
lbl = Label(win, text= "This is a New line Text", font= ('Helvetica 18'), bg= '#ab23ff')
lbl.grid(row=0, column=1, ipadx= 20, ipady=20, padx= 20)
lbl.after(1000, lblAfter)

can_shapes = Canvas(frm_C, width=800,height=600, bg='silver', highlightcolor='indigo')
can_shapes.grid(row=1,rowspan=2,column=1)
frm_La = Frame(frm_C, bg='#ab23ff')
frm_La.grid(row=1,column=0, padx=(0,30))
#===================Widgets in Frame L(frm_La)======================================
com_shapes = ctk.CTkComboBox(frm_La, values=['line','rectangle','oval','polygon', 'arc'])
com_shapes.grid(row=0, column=0, columnspan=2,padx=10,pady=10)

def enterCordinates():
    def retNormal():
        def createShape():
            if com_shapes.get() == 'line':
                can_shapes.create_line(ent_x1.get(),ent_y1.get(),ent_x2.get(),ent_y2.get(), fill=com_color.get())
            elif com_shapes.get() == 'rectangle':
                can_shapes.create_rectangle(ent_x1.get(),ent_y1.get(),ent_x2.get(),ent_y2.get(), fill=com_color.get())
            elif com_shapes.get() == 'oval':
                can_shapes.create_oval(ent_x1.get(),ent_y1.get(),ent_x2.get(),ent_y2.get(), fill=com_color.get())
            elif com_shapes.get() == 'polygon':
                can_shapes.create_rectangle(ent_x1.get(),ent_y1.get(),ent_x2.get(),ent_y2.get(), fill=com_color.get())
            elif com_shapes.get() == 'arc':
                coord = ent_x1.get(),ent_y1.get(),ent_x2.get(),ent_y2.get()
                can_shapes.create_arc(coord, start=ent_start.get(), extent=ent_extent.get(), fill=com_color.get())
            

        btn_create.grid(row=9)
        btn_create.configure(text="Create "+ com_shapes.get(),text_color="cyan", bg_color="yellow", font=('segui',12, 'normal'), command=createShape)
        lbl_cord = ctk.CTkLabel(frm_La, text="Enter Coordinates", text_color='yellow',font=('segui',15, 'bold'))
        lbl_cord.grid(row=3,column=0,columnspan=2)
        
        if com_shapes.get() == 'line' or com_shapes.get() == 'rectangle' or com_shapes.get() == 'oval' or com_shapes.get() == 'polygon' or com_shapes.get() == 'arc':
            ent_x1 = ctk.CTkEntry(frm_La,  bg_color='beige', width=100, font=('segui',12, 'normal'), placeholder_text='x1')
            ent_y1 = ctk.CTkEntry(frm_La,  bg_color='beige', width=100, font=('segui',12, 'normal'), placeholder_text='y1')
            ent_x2 = ctk.CTkEntry(frm_La,  bg_color='beige', width=100, font=('segui',12, 'normal'), placeholder_text='x2')
            ent_y2 = ctk.CTkEntry(frm_La,  bg_color='beige', width=100, font=('segui',12, 'normal'), placeholder_text='y2')

            ent_x1.grid(row=4,column=0, padx=(5,5),pady=5,)
            ent_y1.grid(row=4,column=1, padx=(0,5),pady=5,)
            ent_x2.grid(row=5,column=0, padx=(5,5),pady=5,)
            ent_y2.grid(row=5,column=1, padx=(0,5),pady=5,)
            com_color = ctk.CTkComboBox(frm_La, values=['red','blue', 'green','black','white', 'lime', 'brown', 'yellow', 'orange'])
            com_color.grid(row=6, column=0, columnspan=2,padx=10,pady=10)
            if com_shapes.get() == 'arc':
                ent_start = ctk.CTkEntry(frm_La,  bg_color='beige', width=100, font=('segui',12, 'normal'), placeholder_text='start')
                ent_extent = ctk.CTkEntry(frm_La,  bg_color='beige', width=100, font=('segui',12, 'normal'), placeholder_text='exent')
                ent_start.grid(row=7,column=0, padx=10,pady=10)
                ent_extent.grid(row=7,column=1, padx=10,pady=10)

    btn_create.configure(bg_color="yellow", text_color="cyan", font=('segui',15, 'bold'))
    btn_create.after(1500, retNormal)

btn_create = ctk.CTkButton(frm_La, text="Create", bg_color="cyan", text_color="yellow", font=('segui',12, 'normal'), hover=True,
                           command=enterCordinates)
btn_create.grid(row=1, column=0, padx=10,pady=10, columnspan=2)




win.rowconfigure(1, weight=1)
win.columnconfigure(1, weight=1)
frm_C.columnconfigure(1, weight=1)
frm_C.rowconfigure(1, weight=1)
win.mainloop()