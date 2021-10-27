import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
from tkinter.ttk import Combobox, Style
import os


gpad=tk.Tk()
gpad.geometry("1000x600")
gpad.title("Gpad Text Editor")
gpad.resizable(0,0)




mnu=tk.Menu()

New=tk.PhotoImage(file='Image/New.png')
ope=tk.PhotoImage(file='Image/ope.png')

save=tk.PhotoImage(file='Image/save.png')
sav=tk.PhotoImage(file='Image/sav.png')
exi=tk.PhotoImage(file='Image/exi.png')

File=tk.Menu(mnu, tearoff=False)
#edit menu Gpad

copy=tk.PhotoImage(file='Image/copy.png')
paste=tk.PhotoImage(file='Image/paste.png')
cut=tk.PhotoImage(file='Image/cut.png')
clear=tk.PhotoImage(file='Image/clear.png')
find=tk.PhotoImage(file='Image/find.png')



Edit=tk.Menu(mnu, tearoff=False)


##view Menu Gpad
Toolbar=tk.PhotoImage(file='Image/Toolbar.png')
status=tk.PhotoImage(file='Image/status.png')

View=tk.Menu(mnu, tearoff=False)
##color Menu Gpad

Default=tk.PhotoImage(file='Image/Default.png')
light=tk.PhotoImage(file='Image/light.png')
Dark=tk.PhotoImage(file='Image/Dark.png')
Red=tk.PhotoImage(file='Image/Red.png')
Monokoi=tk.PhotoImage(file='Image/Monokoi.png')
Blue=tk.PhotoImage(file='Image/Blue.png')

Colors=tk.Menu(mnu, tearoff=False)

theme_choice= tk.StringVar()


color_icons=(Default,light,Dark,Red,Monokoi,Blue)

color_dict={
                 'Deafault' :('#000000','#ffffff'),
                 'light'    :('#474747','#e0e0e0'),
                 'Dark'     :('#c4c4c4','#2d2d2d'),
                 'Red'      :('#2d2d2d','#ffe8e8'),
                 'Monokoi'  :('#d3b774','#474747'),
                 'Blue'     :('#ededed','#6b9dc2')
         }
count=0

    

# cascade MenuBar
mnu.add_cascade(label='File' ,menu=File)
mnu.add_cascade(label='Edit' ,menu=Edit)
mnu.add_cascade(label='View' ,menu=View)
mnu.add_cascade(label='Colors' ,menu=Colors)
mnu.add_cascade(label='Wen View',menu=Colors )


###Tool barr..
tool_bar=ttk.Label(gpad)
tool_bar.pack(side=tk.TOP,fill=tk.X)















#font box
ft=tk.font.families()
font_family=tk.StringVar()



font_box= ttk.Combobox(tool_bar , width=30, textvariable=font_family, state='readonly')

font_box['values']=ft
font_box.current(ft.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

#size box

size_var= tk.IntVar()
cb=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
cb['values']=tuple(range(0,81))
cb.current(4)
cb.grid(row=0,column=1,padx=5)           

##bold button





bold=tk.PhotoImage(file='Image/bold.png')
bold_btn=ttk.Button(tool_bar,image=bold)
bold_btn.grid(row=0,column=2,padx=5)


#italic




italic=tk.PhotoImage(file='Image/italic.png')
italic_btn=ttk.Button(tool_bar,image=italic)
italic_btn.grid(row=0,column=3,padx=5)


                          
##underline
under=tk.PhotoImage(file='Image/under.png')
under_btn=ttk.Button(tool_bar,image=under)
under_btn.grid(row=0,column=4,padx=5)
## color icon

fcl=tk.PhotoImage(file='Image/fcl.png')
fcl_btn=ttk.Button(tool_bar,image=fcl)
fcl_btn.grid(row=0,column=5,padx=5)


##align

left=tk.PhotoImage(file='Image/left.png')
left_btn=tk.Button(tool_bar,image=left)
left_btn.grid(row=0,column=6,padx=5)

right=tk.PhotoImage(file='Image/right.png')
right_btn=tk.Button(tool_bar,image=right)
right_btn.grid(row=0,column=7,padx=5)

center=tk.PhotoImage(file='Image/center.png')
center_btn=tk.Button(tool_bar,image=center)
center_btn.grid(row=0,column=8,padx=5)

##gpad text editor
text_editor=tk.Text(gpad)
text_editor.config(wrap='word',relief=tk.FLAT)
                          
scroll_bar=tk.Scrollbar(gpad)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#font family

current_font_family='Arial'
current_font_size=12

def change_font(gpad):
        global current_font_family
        current_font_family= font_family.get()
        text_editor.config(font=(current_font_family,current_font_size))

def change_fontsize(gpad):
        global current_font_family
        current_cb= size_var.get()
        text_editor.configure(font=(current_font_family,current_cb))
        
font_box.bind("<<ComboboxSelected>>",change_font)
cb.bind("<<ComboboxSelected>>",change_fontsize)



#bold Button Functionality

'''def bold():
    text_property= tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_cb, 'bold'))

    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_cb, 'normal'))

bold_btn.configure(command=bold)


#italic button
def italc():
    text_property= tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_cb, 'italic'))

    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_cb, 'normal'))



italic_btn.configure(command=italc)


#underline

def unln():
    text_property= tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']== 0:
        text_editor.configure(font=(current_font_family,current_cb, 'underline'))

    if text_property.actual()['underline']== 1:
        text_editor.configure(font=(current_font_family,current_cb, 'normal'))



under_btn.configure(command=unln)'''


####Clor choosr

def color():
        color_var= tk.colorchooser.askcolor()
        text_editor.configure(fg=color_var[1])

fcl_btn.configure(command=color)

##align func

def leftal():
        text_content= text_editor.get(1.0, 'end')
        text_editor.tag_config('left',justify=tk.LEFT)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(tk.INSERT, text_content, 'left')                            

left_btn.configure(command=leftal)                          

#right
                                     
def rihtal():
        text_content= text_editor.get(1.0, 'end')
        text_editor.tag_config('right',justify=tk.RIGHT)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(tk.INSERT, text_content, 'right')                            

right_btn.configure(command=rihtal)

#center
def centeral():
        text_content= text_editor.get(1.0, 'end')
        text_editor.tag_config('center',justify=tk.CENTER)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(tk.INSERT, text_content, 'center')                            

center_btn.configure(command=centeral)



text_editor.configure(font=('Arial',12))

##status bar
status_bar=ttk.Label(gpad,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)


text_changed=False
def changed(event=None):
        if text_editor.edit_modified():
                text_changed= True
                words= len(text_editor.get(1.0, 'end-1c').split())
                characters =len(text_editor.get(1.0, 'end-1c'))#replace(' ', '')
                status_bar.config(text=f'Characters: {characters} Words: {words}')
        text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',changed)
                

#menu func
#new
url=''


def New_file(event=None):
        global url
        url= ''
        text_editor.delete(1.0, tk.END)






##files


File.add_command(label='   New' ,image=New, compound=tk.LEFT, accelerator='Ctlr+N',command=New_file)
##file open
def open_file(event=None):
        global url
        url = filedialog.askopenfilename(initialdir=os.getcwd(), title="Selete File", filetypes=(('Text File', '*.txt'),('All files', '*.*')))
        try:
                                         
                with open(url, 'r') as fr:
                        text_editor.delete(1.0, tk.END)
                        text_editor.insert(1.0, fr.read())
                                         
        except FileNotFoundError:
                return
        except:
                return
        gpad.title(os.path.basename(url))


File.add_command(label='   Open',   image=ope, compound=tk.LEFT, accelerator='Ctlr+O',command=open_file)
##save Mn function
def saved(event=None):
        global url
        try:
                if url:
                        content= str(text_editor.get(1.0, tk.END))
                        with open(url, 'w', encoding='utf-8') as fw:
                                fw.write(content)
                else:
                        url = filedialog.asksaveasfile(mode='w',defaultextension='.txt', filetypes=(('Text File', '*.txt'),('All files', '*.*')))
                        content2 = text_editor.get(1.0, tk.END)
                        url.write(content2)
                        url.close()
        except:
                        return

                
File.add_command(label='   Save',image=save, compound=tk.LEFT, accelerator='Ctlr+S',command=saved)
        ###save as func
def saves(event=None):
        global url
        try:
                content = text_editor.get(1.0, tk.END)
                url = filedialog.asksaveasfile(mode='w',defaultextension='.txt', filetypes=(('Text File', '*.txt'),('All files', '*.*')))
                url.write(content)
                url.close()
        except:
                return


File.add_command(label='   Save As' ,image=sav, compound=tk.LEFT, accelerator='Ctlr+Alt+s',command=saves)

def exitt(event=None):
         global url,text_changed
         try:
                if text_changed:
                        mbox= messageBox.askyesnocancel('Warning', 'Do you want to exit?')
                        if mbox is True:
                                if url:
                                        content = text_editor.get(1.0, tk.END)
                                        with open(url, 'w', encoding='utf-8')as fw:            
                                         fw.write(content)
                                         gpad.destroy()      
                                                       
                                else:
                                        content2= str (text_editor.get(1.0, tk.END))
                                        url = filedialog.asksaveasfile(mode='w',defaultextension='.txt', filetypes=(('Text File', '*.txt'),('All files', '*.*')))
                                        url.write(content2)
                                        url.close()
                                        gpad.destroy()
                                                
                                         
                                       
                        elif mbox is False:
                                gpad.destroy()
                                                                            

                else:
                          gpad.destroy()
                          
                     
         except:
                return
                                        
        
File.add_command(label='   Exit' ,image=exi, compound=tk.LEFT, accelerator='Ctlr+Q',command=exitt)

##Find fun

def finds(evnt=None):

        def find():
                word = find_input.get()
                text_editor.tag_remove('match', '1.0', tk.END)
                matches=0
                if word:
                        start_pos = '1.0'
                       
                        while True:
                                start_pos = text_editor.search(word, start_pos ,stopindex==tk.END)
                                if not start_pos:
                                        break
                                end_pos = f'{start_pos}+ {len(word)}c'
                                text_editor.tag_add('match', start_pos, end_pos)
                                matches += 1
                                start_pos= end_pos
                                text_editor.tag_config('match', foreground='red',background='Yellow')
        
                
                


        def rep():
                #global replace_text
                word = find_input.get()
                replace_text = replace_input.get()
                content = text_editor.get(1.0, tk.END)
                new_content = content.replace(word, replace_text)
                text_editor.delete(1.0, tk.END)
                text_editor.insert(1.0, new_content)
                
                
              
        




        
        find_dialogue= tk.Toplevel()
        find_dialogue.geometry("450x250+500+200")
        find_dialogue.title('Find')
        find_dialogue.resizable(0,0)

        ##frm
        find_frame= tk.LabelFrame(find_dialogue, text='Find/Replace')
        find_frame.pack(pady=20)

        text_find_label = ttk.Label(find_dialogue, text='Find')
        text_replace_label =ttk.Label(find_dialogue,text='Replace')

        find_input = ttk.Entry(find_dialogue, width=30)
        replace_input = ttk.Entry(find_dialogue, width=30)

        find_btn = ttk.Button(find_dialogue, text="Find",command=find)
        replace_btn = ttk.Button(find_dialogue, text="Relace",command=rep)

        text_find_label.place(x=50,y=70)        #grid(row=0, column=0, padx=4, pady=4)
        text_replace_label.place(x=50,y=120)   #grid(row=1, column=0, padx=4, pady=4)

        find_input.place(x=130,y=70)            #grid(row=0, column=1, padx=4, pady=4)
        replace_input.place(x=130,y=120)         #grid(row=1, column=1, padx=4, pady=4)

        find_btn.place(x=80,y=180)               #grid(row=2, column=0, padx=8, pady=4)
        replace_btn.place(x=230,y=180)             #grid(row=2, column=1, padx=8, pady=4)

        find_dialogue.mainloop()
         



        
        

    
## Edit Menu
Edit.add_command(label='   Copy' ,image=copy, compound=tk.LEFT, accelerator='Ctlr+c', command=lambda:text_editor.event_generate("<Control c>"))
Edit.add_command(label='   Paste',   image=paste, compound=tk.LEFT, accelerator='Ctlr+v', command=lambda:text_editor.event_generate("<Control v>"))
Edit.add_command(label='   Cut',image=cut, compound=tk.LEFT, accelerator='Ctlr+x', command=lambda:text_editor.event_generate("<Control x>"))
Edit.add_command(label='   Clear' ,image=clear, compound=tk.LEFT, accelerator='Ctlr+Alt+x', command=lambda:text_editor.delete(1.0, tk.END))
Edit.add_command(label='   Find' , image=find , compound=tk.LEFT, accelerator='Ctlr+F',command=finds)

##view
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar= tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
        global show_toolbar
        if show_toolbar:
                tool_bar.pack_forget()
                show_toolbar= False
        else:
                text_edior.pack_forget()
                status_bar.pack_forget()
                tool_bar.pack(side=tk.TOP, fill=tk.X)
                text_editor.pack(fil=t.BOTH, expand=True)
                status_bar.pack(side=k.BOTTOM)
                show_toolbar = True

def hide_statusbar():
        global show_statusbar
        if  show_statusbar:
                 show_statusbar.pack_forget()
                 show_statusbar = False
        else:
                statusbar.pack(side=tk.BOTTOM)
                show_statusbar= True
                
                 
        
        


View.add_checkbutton(label=" Tool Bar",onvalue=True,offvalue=0,variable= show_toolbar,image=Toolbar,compound=tk.LEFT,command=hide_toolbar)
View.add_checkbutton(label="  Status Bar",onvalue=1,offvalue=False,variable=show_statusbar,image=status,compound=tk.LEFT,command=hide_statusbar)


#Colors

def ct():
        chosen_theme= theme_choice.get()
        color_tuple= color_dict.get(chosen_theme)
        fg_color, bg_color= color_tuple[0], color_tuple[1]
        text_editor.config(background=bg_color, fg=fg_color)



for i in color_dict:
        Colors.add_radiobutton(label = i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=ct)
        count +=1
        



gpad.config(menu=mnu)

###shorcut keys
gpad.bind("<Control-n>",New_file)
gpad.bind("<Control-o>",open_file)
gpad.bind("<Control-s>",saved)
gpad.bind("<Control-Alt-s>",saves)
gpad.bind("<Control-q>",exitt)

gpad.mainloop()
 


