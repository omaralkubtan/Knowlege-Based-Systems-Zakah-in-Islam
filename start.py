import sys
from experta import *
from zakah import *
from deserve_zakah_engin import *
from threading import Thread
from tkinter import messagebox as mb
from window import window
class start(KnowledgeEngine):
    
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="start")

    @Rule(Fact(action='start'), NOT(Fact(person=W())))
    def ask_islam(self):
        self.declare(
            Fact(person=self.window.radio("Is the person muslim? ",["yes","no"])))
        
    @Rule(Fact(action='start'), Fact(person='no'))
    def kafer_exception(self):
        mb.showerror('', "There is no zakah for kuffars and will not presented to them")
        sys.exit()
         
        
    @Rule(Fact(action='start'), Fact(person='yes'), salience=10)
    def ask_target(self):
        arr = [" 1. calculate zakah for person "," 2. know if person deserve zakah"]
        string = self.window.radio('Choose what do you want:',arr)
        choice = arr.index(string)+1
        if(choice == 1):
            engin = zakah()
            engin.window = self.window
            engin.reset()
            engin.declare(Fact(action='start'), Fact(person='yes'))
            engin.run()
            for fact in engin.facts:
                self.declare(engin.facts[fact])
            have_makhloot_mony = self.window.radio('Does the person have shared mony with others?',['yes','no'])
            if(have_makhloot_mony == 'yes'):  
                engin.reset()
                engin.declare(Fact(action='start'), Fact(person='yes'))
                engin.run()
                out="____this zakah for mixed money____ \n"
                
                for fact in engin.facts:
                    for i in engin.facts[fact]:
                        j = i.split(' ')
                        out+= print_map(j[0], str(engin.facts[fact][i]))+"\n"
                mb.showinfo('',out)
                
            
        else:
            engin = deserve_zakah_engin()
            engin.window = self.window
            engin.reset()
            engin.declare(Fact(person='yes'))
            engin.run()
            out = ""
            for fact in engin.facts:
                for i in engin.facts[fact]:
                    j = i.split(' ')
                    m = print_map(j[0] + str(engin.facts[fact][i]), '')
                    if len(m)>0 :
                        out += m+"\n"
            mb.showinfo('', out)
            sys.exit()

            
        return
    
e = start()
e.window = window()
e.reset()
e.run()  
out="____this zakah for personal money____ \n"
for fact in e.facts:
    for i in e.facts[fact]:
        j = i.split(' ')
        m =  print_map(j[0], str(e.facts[fact][i]))
        if len(m)>0 :
            out+= print_map(j[0], str(e.facts[fact][i]))+"\n"
        
mb.showinfo('', out)
