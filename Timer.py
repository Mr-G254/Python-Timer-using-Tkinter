import tkinter as tk
from tkinter import*
import time
from pygame import mixer


win=Tk()
win.title("Timer")
win.geometry("330x160+0+0")
win.resizable(False,False)

def number1(event):
    try:
        x=int(entryb.get())
    except:
        u=len(entryb.get())-1
        
        entryb.delete(u)
    
    try:
        x1=entryb.get()
        if x1[0]=="0":
            entryb.delete(0)
    except:
        entryb.insert("0",0)
        entryb.insert("0",0)
    
    if len(str(entryb.get()))==1:
        entryb.insert("0",0)

    if len(str(entryb.get()))==3:
        entryb.delete(0)

    if entryb.get():
        pass
    else:
        entryb.insert("0",0)
        entryb.insert("1",0)


def number2(event):
    try:
        v=int(entrye.get())
    except:
        w=len(entrye.get())-1
        
        entrye.delete(w)
    
    try:
        v1=entrye.get()
        if v1[0]=="0":
            entrye.delete(0)
    except:
        entrye.insert("0",0)
        entrye.insert("0",0)
    
    if len(str(entrye.get()))==1:
        entrye.insert("0",0)

    if len(str(entrye.get()))==3:
        entrye.delete(0)
    
    try:
        if int(entrye.get()) > 59:
            entrye.delete(0,END)
            entrye.insert("0",0)
            entrye.insert("0",0)
    except:
        pass

    if entrye.get():
        pass
    else:
        entrye.insert("0",0)
        entrye.insert("1",0)

def number3(event):
    try:
        a=int(entryh.get())
    except:
        b=len(entryh.get())-1
        
        entryh.delete(b)
    
    try:
        a1=entryh.get()
        if a1[0]=="0":
            entryh.delete(0)
    except:
        entryh.insert("0",0)
        entryh.insert("0",0)
    
    if len(str(entryh.get()))==1:
        entryh.insert("0",0)

    if len(str(entryh.get()))==3:
        entryh.delete(0)

    try:
        if int(entryh.get()) > 59:
            entryh.delete(0,END)
            entryh.insert("0",0)
            entryh.insert("0",0)
    except:
        pass

    if entryh.get():
        pass
    else:
        entryh.insert("0",0)
        entryh.insert("1",0)

def pg2():
    def back():
        frame2.destroy()

    def sec(x):
        for i in reversed(range(x)):
            win.update()
            time.sleep(1)
            if i < 10:
                y=str(0)+str(i)
                labelc.configure(text=y)
            else:
                labelc.configure(text=i)

            A=labela.cget("text")
            B=labelb.cget("text")   
            C=int(labelc.cget("text"))
            
            if A=="00" and B=="00" and C < 6:
                labela.configure(fg="red")
                labelb.configure(fg="red")
                labelc.configure(fg="red")

                mixer.init()
                mixer.music.load("beep-sound.mp3")
                mixer.music.set_volume(1.0)
                mixer.music.play(2)
            else:
                pass
    
    def min(y):
        for i in reversed(range(y+1)):
            labelc.configure(text="59")
            
            z=59
            sec(z)
            e=i-1
        
            if e < 10 and e > -1:
                u=str(0)+str(e)
                labelb.configure(text=u)
            elif e > 10:
                labelb.configure(text=e)
            else:
                pass

    def hr(x):
        for v in reversed(range(x+1)):
            labelb.configure(text="59")
            min(59)
            
            y=v-1
            if y < 10 and y > -1:
                q=str(0)+str(y)
                labela.configure(text=q)
            elif y > 10:
                labela.configure(text=y)
            else:
                pass
        

    global frame2
    frame2=Frame(win,bg="#003060",height=160,width=330)
    frame2.place(x=0,y=0)

    txt=Label(frame2,bg="#003060",text="Hr          Min          Sec",font=("Timesbold,30"))
    txt.place(x=85,y=40)

    labela=Label(frame2,bg="#003060",font=("Times,40"),bd=0,justify=CENTER)
    labela.place(x=80,y=71,height=40,width=30)

    col3=Label(frame2,bg="#003060",text="|")
    col3.place(x=121,y=71,height=40,width=10)

    labelb=Label(frame2,bg="#003060",font=("Times,40"),bd=0,justify=CENTER)
    labelb.place(x=142,y=71,height=40,width=30)

    col4=Label(frame2,bg="#003060",text="|")
    col4.place(x=183,y=71,height=40,width=10)

    labelc=Label(frame2,bg="#003060",font=("Times,40"),bd=0,justify=CENTER)
    labelc.place(x=204,y=71,height=40,width=30)

    photo=tk.PhotoImage(file="Back.png")
    backbtn=Button(frame2,bg="#003B73",text="Back",font=("Times,30"),bd=0,command=back)
    backbtn.place(x=248,y=128,height=30,width=80)

    labela.configure(text=entryb.get())
    labelb.configure(text=entrye.get())
    labelc.configure(text=entryh.get())

    H=int(labela.cget("text")) 
    M=int(labelb.cget("text")) 
    S=int(labelc.cget("text"))

    if H==0 and M==0:
        sec(S)

    elif H==0 and M > 0:
        if S > 0:
            sec(S)
            win.update()
            time.sleep(1)
            M=M-1
            if M < 10:
                v=str(0)+str(M)
                labelb.configure(text=v)
            else:
                labelb.configure(text=M)

        else:
            M=M-1
            if M < 10:
                q=str(0)+str(M)
                labelb.configure(text=q)
            else:
                labelb.configure(text=M)

        min(M)
 
    elif H > 0:
        if S==0 and M > 0:
            M=M-1
            if M < 10:
                q=str(0)+str(M)
                labelb.configure(text=q)
            else:
                labelb.configure(text=M)

            min(M)

            H=H-1
            if H < 10 and H > -1:
                l=str(0)+str(H)
                labela.configure(text=l)
            else:
                labela.configure(text=H)
            

        elif S > 0 and M==0:
            sec(S)

            H=H-1
            if H < 10 and H > -1:
                l=str(0)+str(H)
                labela.configure(text=l)
            else:
                labela.configure(text=H)

        elif S > 0 and M > 0:
            sec(S)

            M=M-1
            if M < 10:
                q=str(0)+str(M)
                labelb.configure(text=q)
            else:
                labelb.configure(text=M)

            min(M)
            
            H=H-1
            if H < 10 and H > -1:
                l=str(0)+str(H)
                labela.configure(text=l)
            else:
                labela.configure(text=H)
            
            labelb.configure(text="59")
        
        elif S==0 and M==0:
            H=H-1
            if H < 10 and H > -1:
                l=str(0)+str(H)
                labela.configure(text=l)
            else:
                labela.configure(text=H)

        hr(H)
    

frame=Frame(win,bg="#003060",height=160,width=330)
frame.place(x=0,y=0)

txt=Label(frame,bg="#003060",text="Hr          Min          Sec",font=("Timesbold,30"))
txt.place(x=85,y=40)

global entryb
entryb=Entry(frame,bg="#003B73",font=("Times,40"),bd=0,justify=CENTER)
entryb.bind('<KeyRelease>',number1)
entryb.place(x=80,y=71,height=40,width=30)

col1=Label(frame,bg="#003060",text="|")
col1.place(x=121,y=71,height=40,width=10)

global entrye
entrye=Entry(frame,bg="#003B73",font=("Times,40"),bd=0,justify=CENTER)
entrye.bind('<KeyRelease>',number2)
entrye.place(x=142,y=71,height=40,width=30)

col2=Label(frame,bg="#003060",text="|")
col2.place(x=183,y=71,height=40,width=10)

global entryh
entryh=Entry(frame,bg="#003B73",font=("Times,40"),bd=0,justify=CENTER)
entryh.bind('<KeyRelease>',number3)
entryh.place(x=204,y=71,height=40,width=30)

entryb.insert("0",0)
entrye.insert("0",0)
entryh.insert("0",0)

entryb.insert("1",0)
entrye.insert("1",0)
entryh.insert("1",0)

startbtn=Button(frame,bg="#003B73",text="start",font=("Times,30"),bd=0,command=pg2)
startbtn.place(x=248,y=128,height=30,width=80)

mainloop()


# Art by:

#     ...     ..      ..                                      ....        .   
#   x*8888x.:*8888: -"888:                                 .x88" `^x~  xH(`   
#  X   48888X `8888H  8888             .u    .            X888   x8 ` 8888h   
# X8x.  8888X  8888X  !888>          .d88B :@8c          88888  888.  %8888   
# X8888 X8888  88888   "*8%-        ="8888f8888r        <8888X X8888   X8?    
# '*888!X8888> X8888  xH8>            4888>'88"         X8888> 488888>"8888x  
#   `?8 `8888  X888X X888>            4888> '           X8888>  888888 '8888L 
#   -^  '888"  X888  8888>            4888>             ?8888X   ?8888>'8888X 
#    dx '88~x. !88~  8888>      .    .d888L .+      .    8888X h  8888 '8888~ 
#  .8888Xf.888x:!    X888X.:  .@8c   ^"8888*"     .@8c    ?888  -:8*"  <888"  
# :""888":~"888"     `888*"  '%888"     "Y"      '%888"    `*88.      :88%    
#     "~'    "~        ""      ^*                  ^*         ^"~====""`      
                                                                            
                                                                            
                                                                            
