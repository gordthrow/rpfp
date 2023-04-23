import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mb
from PIL import Image, ImageTk
from tkPDFViewer import tkPDFViewer as pdf
from win32api import GetSystemMetrics
import pygame
from pygame import mixer
import json
import sys
import os

from tkPDFViewer import tkPDFViewer as pdf


#the main menu contains all the buttons for traversing through all the options in our program
#all the following menus will be build similarly to this one 
#we create grids and place everything we need there.
#the buttons will be built on a similar formula everytime and if there is a special one we will make sure to 
#say everything important about it in a comment
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        self.configure(background='#4f9ee3')
        Grid.rowconfigure(self, (0,1,2,4,5), weight=1)
        Grid.columnconfigure(self, (0,1,2,3), weight=1)
        
        Label = tk.Label(self, text=" ", bg='#4f9ee3', font=("Arial Bold", 30))
        Label.grid(row=0, column=0, pady=100, sticky="nsew")
        
        Label = tk.Label(self, text=" ", bg='#4f9ee3', font=("Arial Bold", 30))
        Label.grid(row=5, column=3, sticky="nsew", pady=50)

        Label = tk.Label(self, text="Main Menu", bg='#4f9ee3', font=("Arial Bold", 45))
        Label.grid(row=0, column=1, sticky="nsew", padx=100, columnspan=2)#x=300, y=100)

        #takes the user to the info manu
        Button = tk.Button(self, text="Read Information", bg='#ff8e03', font=("Arial", 20), command=lambda: [controller.play_next_btn() ,controller.show_frame(InfoMenu)])
        Button.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)#x=100, y=250)

        #takes the user to the quiz manu
        Button = tk.Button(self, text="Test Your Knowledge", bg='#ff8e03', font=("Arial", 20), command=lambda: [controller.play_next_btn() ,controller.show_frame(Quizmenu)])
        Button.grid(row=2, column=2, sticky="nsew", padx=10, pady=10)#x=420, y=250)
        
        #takes the user to the option manu
        Button = tk.Button(self, text="Options Menu", bg='#ff8e03', font=("Arial", 20), command=lambda: [controller.play_next_btn() , controller.show_frame(OptionsMenu)])
        Button.grid(row=4, column=1, sticky="nsew", padx=10, pady=10,columnspan=2)#x= 250, y=400)

       
class OptionsMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.configure(background='#4f9ee3')
        Grid.rowconfigure(self, (1,8), weight=1)
        Grid.columnconfigure(self, (2), weight=1)
        
        #Label = tk.Label(self, text=" ", bg='#4f9ee3', font=("Arial Bold", 30))
        #Label.grid(row=7, column=0, pady=100, sticky="nsew")
        
        Label = tk.Label(self, text=" ", bg='#4f9ee3', font=("Arial Bold", 30))
        Label.grid(row=8, column=5, pady=10, sticky="nsew")
        
        Label = tk.Label(self, text=" ", bg='#4f9ee3', font=("Arial Bold", 30))
        Label.grid(row=10, column=5, sticky="nsew")
        
        #button to send you back to the main frame
        BackButton = tk.Button(self, text="Back", bg='#ff8e03', font=("Arial", 15), command=lambda: [ controller.play_back_btn() ,controller.show_frame(MainMenu)])
        BackButton.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)#x=15, y=10)
        
        Label = tk.Label(self, text="Options Menu", bg='#4f9ee3', font=("Arial Bold", 30))
        Label.grid(row=2, column=1, sticky="nsew", padx=100, columnspan=3)#x=300, y=100)
        
        Label = tk.Label(self, text="Volume", bg='#4f9ee3', font=("Arial Bold", 20))
        Label.grid(row=3, column=1, sticky="nsew", columnspan=3, padx=100)#x=375, y=200)
        
        #we use that so the user can change the volume of the music or turn it off completely
        Volume_slider = ttk.Scale(self, from_=0, to=1, orient=HORIZONTAL, value=float(lines[2][1]), length=500, command=lambda x: [controller.volume(float(x))])
        Volume_slider.grid(row=4, column=1, sticky="nsew", columnspan=3, padx=100)#x=200, y=250)


        Label = tk.Label(self, text=" ", bg='#4f9ee3', font=("Arial Bold", 20))
        Label.grid(row=5, column=0, sticky="nsew")#x=375, y=200)

        Label = tk.Label(self, text="Resolution\n(restart app to change resolution)", bg='#4f9ee3', font=("Arial Bold", 20))
        Label.grid(row=6, column=1, sticky="nsew", columnspan=3, padx=100)#x=375, y=200)
        
        clicked = StringVar()
        clicked.set(str(lines[0][1]) + "x" + str(lines[1][1]))
        
        max_resolution = str(GetSystemMetrics(0)) + "x" + str(GetSystemMetrics(1))

        #contains the potential resolutions
        DropMenu = OptionMenu(self, clicked, "850x625", max_resolution)
        DropMenu.grid(row=7, column=1, sticky="nsew", columnspan=3, padx=100)
        
        #gets the user selected resolution and manipulates it accordingly
        Button = tk.Button(self, text="Apply resolution\nchanges", bg='#ff8e03', font=("Arial", 15), command=lambda: [ controller.play_back_btn() , controller.resolution(clicked.get()) ,controller.show_frame(MainMenu)])
        Button.grid(row=9, column=3, sticky="nsew", padx=10, pady=30, columnspan=2)#x=15, y=10)
        
       
class InfoMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#4f9ee3')
        Grid.rowconfigure(self, (1,3,4), weight=1)
        Grid.columnconfigure(self, (1,2,3,4,5), weight=1)
        
        Label = tk.Label(self, text=" ", bg='#4f9ee3', font=("Arial Bold", 30))
        Label.grid(row=4, column=5, sticky="nsew", padx=30)#x=250, y=100)
        
        Label = tk.Label(self, text="Information Menu", bg='#4f9ee3', font=("Arial Bold", 30))
        Label.grid(row=1, column=2, columnspan=3, padx=100, sticky="nsew")#x=250, y=100)

        #the next two buttons are used to get the specific information the user wants, 
        #the buttons select the correct file and sends them to the show_info frame
        Button = tk.Button(self, text="Athens", height = 2, width = 16, bg='#ff8e03', font=("Arial", 25), command=lambda: [controller.play_next_btn() ,controller.show_Info(parent, controller, 'newtestr1.pdf')])
        Button.grid(row=2, column=2, sticky="nsew", rowspan=2, padx=10, pady=10)#x=100, y=250)

        Button = tk.Button(self, text="Corfu", height = 2, width = 16, bg='#ff8e03', font=("Arial", 25), command=lambda: [controller.play_next_btn() ,controller.show_Info(parent, controller, 'newtestr2.pdf')])
        Button.grid(row=2, column=4, sticky="nsew", rowspan=2, padx=10, pady=10)#x=420, y=250)
        
        #sends the user back to the previous frame
        BackButton = tk.Button(self, text="Back", bg='#ff8e03', font=("Arial", 15), command=lambda: [ controller.play_back_btn(), controller.show_frame(MainMenu)])
        BackButton.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)#x=15, y=10)


class Infopage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        


    def widget_placement_info(self, parent, controller):
        self.configure(background='#4f9ee3')  
        Grid.rowconfigure(self, (1,2,3), weight=1)
        Grid.columnconfigure(self, (1,2,3), weight=1)
        

        letter_len=int(lines[1][1])
        letter_len=(letter_len / 57)
        
        Label = tk.Label(self, text=" ", bg='#4f9ee3', font=("Arial Bold", 30))
        Label.grid(row=3, column=3, sticky="nsew", padx=10, pady=30)#x=250, y=100)
        
        
        #clears the previous stuff so it does not overlap
        pdf.ShowPdf.img_object_li.clear()

        #we set the v1 as the pdf object and we use the v2 to display it in the screen
        v1 = pdf.ShowPdf()

        v2= v1.pdf_view(self, pdf_location=app.Info_no, bar=False, height=28, width=80)
        v2.grid(row=2, column=2, sticky="nsew", padx=10, pady=10)
        
        
        BackButton = tk.Button(self, text="Back", bg='#ff8e03', font=("Arial", 15), command=lambda: [controller.play_back_btn() ,self.refresh_frame(parent, controller)])
        BackButton.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)#x=15, y=10)


    def refresh_frame(self, parent, controller):
        for widget in self.winfo_children():
            widget.destroy()
        controller.show_frame(InfoMenu)



#the quiz menu class is mostly a frame full of buttons to get you to different locations. 
#Its based on previous frames
class Quizmenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self , parent)
        self.configure(background='#4f9ee3')
        Grid.rowconfigure(self, (1,3,4), weight=1)
        Grid.columnconfigure(self, (1,2,3,4,5), weight=1)
        
        Label = tk.Label(self, text=" ", bg='#4f9ee3', font=("Arial Bold", 30))
        Label.grid(row=4, column=5, sticky="nsew", padx=30)#x=250, y=100)
        
        Label = tk.Label(self, text="Quiz Menu", bg='#4f9ee3', font=("Arial Bold", 30))
        Label.grid(row=1, column=2, columnspan=3, padx=100, sticky="nsew")#x=250, y=100)

        #buttons to select the appropriate quiz the user wants
        Button = tk.Button(self, text="Athens Quiz", height = 2, width = 16, bg='#ff8e03', font=("Arial", 20), command=lambda: [controller.play_next_btn() ,controller.show_Quiz(parent, controller, '1')])
        Button.grid(row=2, column=2, sticky="nsew", rowspan=2, padx=10, pady=10)#x=100, y=250)

        Button = tk.Button(self, text="Corfu Quiz", height = 2, width = 16, bg='#ff8e03', font=("Arial", 20), command=lambda: [controller.play_next_btn() ,controller.show_Quiz(parent, controller, '2')])
        Button.grid(row=2, column=4, sticky="nsew", rowspan=2, padx=10, pady=10)#x=420, y=250)
        
        BackButton = tk.Button(self, text="Back", bg='#ff8e03', font=("Arial", 15), command=lambda: [controller.play_back_btn() ,controller.show_frame(MainMenu)])
        BackButton.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)#x=15, y=10)
        
 
#this class is responsible for the whole quiz structure
#A big part of the code for the quiz was based on the code from here : https://www.geeksforgeeks.org/python-mcq-quiz-game-using-tkinter/
#We adopted their code and changed it in some major ways so it could fit properly in our project. 
class Quizpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       
 
    #once again this will work with grids to place stuff into since it was the easiest way we could think of
    def widget_placement_quiz(self, parent, controller):
        self.configure(background='#4f9ee3')
        Grid.rowconfigure(self, (1,6,7), weight=5)
        Grid.rowconfigure(self, (2,3,4,5,8), weight=1)
        Grid.columnconfigure(self, (2), weight=5)
        
        Label = tk.Label(self, text=" ", bg='#4f9ee3', font=("Arial Bold", 30))
        Label.grid(row=7, column=4, sticky="nsew", padx=10, pady=10)
        
        Label = tk.Label(self, text=" ", bg='#4f9ee3', font=("Arial Bold", 30))
        Label.grid(row=9, column=4, sticky="nsew", padx=10, pady=10)
        
        # set question number to 0
        self.q_no=0
         
        # assigns ques to the display_question function to update later.
        self.display_title()
        self.display_question()
         
        # opt_selected holds an integer value which is used for
        # selected option in a question.
        self.opt_selected=IntVar()
         
        # displaying radio button for the current question and used to
        # display options for the current question
        self.opts=self.radio_buttons()
         
        # display options for the current question
        self.display_options()
         
        # displays the button for next and exit.
        self.buttons(parent, controller)
         
        # no of questions
        self.data_size=len(app.question)
         
        # keep a counter of correct answers
        self.correct=0
        
    
    # This method is used to Display Title
    def display_title(self):
        
        # The title to be shown
        title = Label(self, text="Test your knowledge", bg='#4f9ee3', font=("ariel", 20, "bold"))
         
        # place of the title
        title.grid(row=0, column=1, sticky="nsew", padx=10, pady=10, columnspan=4)
        
    
    # This method shows the current Question on the screen
    def display_question(self):
         
        # setting the Question properties
        q_no = Label(self, text=app.question[self.q_no], bg='#ff8e03',
        font=( 'ariel' ,20, 'bold' ), anchor= 'w' )
         
        #placing the option on the screen
        q_no.grid(row=1, column=1, sticky="nsew", columnspan=4)
        
        
    # This method shows the radio buttons to select the Question
    # on the screen at the specified position. It also returns a
    # lsit of radio button which are later used to add the options to
    # them.
    def radio_buttons(self):
         
        # initialize the list with an empty list of options
        q_list = []
         
        # position of the first option
        #y_pos = 200
         
        # adding the options to the list
        while len(q_list) < 4:
             
            # setting the radio button properties
            radio_btn = Radiobutton(self,text=" ",variable=self.opt_selected, bg='#4f9ee3',
            value = len(q_list)+1,font = ("ariel",14))
             
            # adding the button to the list
            q_list.append(radio_btn)
             
            # placing the button
            radio_btn.grid(row=(2+len(q_list)), column=1, sticky="wn", padx=10, pady=10)
             
            # incrementing the y-axis position by 40
            #y_pos += 40
         
        # return the radio buttons
        return q_list
    
    
    # This method deselect the radio button on the screen
    # Then it is used to display the options available for the current
    # question which we obtain through the question number and Updates
    # each of the options for the current question of the radio button.
    def display_options(self):
        val=0
         
        # deselecting the options
        self.opt_selected.set(0)
         
        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in app.options[self.q_no]:
            self.opts[val]['text']=option
            val+=1
 
               
    # This method is used to display the result
    # It counts the number of correct and wrong answers
    # and then display them at the end as a message Box
    def display_result(self):
        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
         
        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
         
        # Shows a message box to display the result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
 
    
    # This method checks the Answer after we click on Next.
    def check_ans(self, q_no):
        
        # checks for if the selected option is correct
        if self.opt_selected.get() == app.answer[q_no]:
            # if the option is correct it return true
            return True
 
 
    # This method is used to check the answer of the
    # current question by calling the check_ans and question no.
    # if the question is correct it increases the count by 1
    # and then increase the question number by 1. If it is last
    # question then it calls display result to show the message box.
    # otherwise shows next question.
    def next_btn(self, parent, controller):
         
        # Check if the answer is correct
        if self.check_ans(self.q_no):
             
            # if the answer is correct it increments the correct by 1
            self.correct += 1
         
        # Moves to next Question by incrementing the q_no counter
        self.q_no += 1
         
        # checks if the q_no size is equal to the data size
        if self.q_no==self.data_size:
             
            # if it is correct then it displays the score
            self.display_result()
             
            # destroys the GUI
            self.refresh_quiz(parent, controller)
            
       
        else:
            # shows the next question
            self.display_question()
            self.display_options()
 
 
    # This method shows the two buttons on the screen.
    # The first one is the next_button which moves to next question
    # It has properties like what text it shows the functionality,
    # size, color, and property of text displayed on button. Then it
    # mentions where to place the button on the screen. The second
    # button is the exit button which is used to close the GUI without
    # completing the quiz.
    def buttons(self, parent, controller):
         
        # The first button is the Next button to move to the
        # next Question
        next_button = Button(self, text="Next",command=lambda : [controller.play_next_btn() ,self.next_btn(parent, controller)],
        width=10, bg='#ff8e03',font=("ariel",16,"bold"))
         
        # palcing the button  on the screen
        next_button.grid(row=8, column=4, sticky="nsew", padx=10, pady=10)#x=350,y=380)
         
        # This is the second button which is used to Quit the GUI
        BackButton = tk.Button(self, text="Back", bg='#ff8e03', font=("Arial", 15), command=lambda: [controller.play_back_btn() ,self.refresh_quiz(parent, controller)])
        BackButton.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)#x=15, y=10)
    
    #when the user leaves the quiz or the quiz ends we destroy it so the quiz can be refreshed
    def refresh_quiz(self, parent, controller):
        for widget in self.winfo_children():
            widget.destroy()
        #self.widget_placement_quiz(parent, controller)
        controller.show_frame(Quizmenu)
    
    
    
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #splash_root.destroy
        
        pygame.mixer.init()
        self.backround_music()
        
        #creating a window
        window = tk.Frame(self)
        self.title('Historical Information App')
        self.iconbitmap("acropolis.ico")
        window.grid(row = 0, column = 0, sticky="nsew")

        #setting the grids 
        window.grid_rowconfigure(0, minsize =lines[1][1])############################GetSystemMetrics(1)
        window.grid_columnconfigure(0, minsize =lines[0][1])#########################GetSystemMetrics(0)
        
        
        self.frames = {}
        for F in (MainMenu, OptionsMenu, InfoMenu, Infopage, Quizmenu, Quizpage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")

        self.show_frame(MainMenu)

    #this is to show the appropriate frame
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
      
    #when this method is called it is decided which quiz the user is looking for and it 
    #asks the Quiz_data function to get the data   
    def show_Quiz(self, parent, controller, Q_no):
        self.Quiz_no = Q_no
        self.Quiz_data()
        Quizpage.widget_placement_quiz(self.frames[Quizpage], parent, controller)
        controller.show_frame(Quizpage)
       
    #after this method is called the appropriate data is loaded    
    def Quiz_data(self):  
        self.question = (data['question' + self.Quiz_no])
        self.options = (data['options' + self.Quiz_no])
        self.answer = (data['answer' + self.Quiz_no])
      
    #works similarly to the show_quiz method. when it is called we get which city's information the user wants to read   
    def show_Info(self, parent, controller, I_no):
        self.Info_no =  I_no
        Infopage.widget_placement_info(self.frames[Infopage], parent, controller)
        controller.show_frame(Infopage)
        
    #we set a specific sound when the "Next" button is pressed
    def play_next_btn(self):
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(lines[4][1]),  maxtime = 600)
        pygame.mixer.Channel(0).set_volume(float(lines[2][1]))
        
    #we set a specific sound when the "Back" button is pressed    
    def play_back_btn(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(lines[5][1]), maxtime = 600)
        pygame.mixer.Channel(1).set_volume(float(lines[2][1]))
        
    #this sets a specific background music and loops it a lot of times so it can keep playing for a long time    
    def backround_music(self):
        mixer.music.load(lines[3][1])
        mixer.music.set_volume(float(lines[2][1]))
        mixer.music.play(loops=1000)   
        #Music by <a href="/users/lesfm-22579021/?tab=audio&amp;utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=audio&amp;utm_content=11157">Lesfm</a> from <a href="https://pixabay.com/music/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=11157">Pixabay</a>

    
    def volume(self, x):
        pygame.mixer.music.set_volume(x)  
        pygame.mixer.Channel(0).set_volume(x)
        pygame.mixer.Channel(1).set_volume(x)
        lines[2][1] = str(x)
        with open("options.txt", 'w') as fp:
            for i in range(len(lines)):   
                line_to_write = lines[i][0] + "=" + lines[i][1] 
                print (line_to_write)
                fp.write('%s\n' % line_to_write)
#this is the method we are using to change the resolution of the window, we are getting the option of the user 
#and we manipulate it accordingly         
    def resolution(self, resolution_option):
        w, h = str(resolution_option).split("x", 1)
        lines[0][1]= w 
        lines[1][1]= h
        with open("options.txt", 'w') as fp:
            for i in range(len(lines)):   
                line_to_write = lines[i][0] + "=" + lines[i][1] 
                print (line_to_write)
                fp.write('%s\n' % line_to_write)
        os.execl(sys.executable, sys.executable, *sys.argv)
    
    
    
#we open the file that contains the questions and answers for the quiz   
with open('data.json') as f:
    data = json.load(f)

with open("options.txt", 'r+') as fp:
    lines = []
    for i, line in enumerate(fp):
        lines.append(line.strip())
        lines[i] = lines[i].split('=')
#Compare the system metrics from the file to the one of the users monitor
#GetSystemMetrics 0 gets us the width of the primary monitor and with GetSystemMetrics 1 we get the height. 
#When compared it takes the appropriate action.  
    if (int(lines[0][1]) > GetSystemMetrics(1)):
        lines[0][1] = GetSystemMetrics(0)
        
    if (int(lines[1][1]) > GetSystemMetrics(0)):
        lines[1][1] = GetSystemMetrics(1)

app= Application()
#we set the minimum and maximum window size based on the current size of the window so the user cant 
#resize it without going into to options menu
app.minsize(height=lines[1][1], width=lines[0][1])
app.maxsize(height=lines[1][1], width=lines[0][1])
app.mainloop()

