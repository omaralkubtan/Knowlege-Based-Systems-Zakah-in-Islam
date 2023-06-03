from experta import *
from zakah_util import *
from anaam_engin import *
from plants_engin import *

HAOUL=12               ## per month 
NESAB_MONY=17_000_000  ## per syrian pound
NESAB_GOLD=85          ## per gram of gold 
NESAB_SILVER=672       ## per gram of silver
NESAB_RIKAZ=NESAB_MONY ## per syrian pound

class zakah(KnowledgeEngine):
       
        
    @Rule(Fact(action='start'), Fact(person='yes'), salience=10)
    def ask_mony(self):
        mony=int(self.window.input('Enter the amount of mony that you have: '))
        if(mony < NESAB_MONY):
            return
        duration_having_mony=int(self.window.input('How many months have you owned that mony without decreasing: '))
        if(duration_having_mony < HAOUL):
            return 
        else:
           self.declare(
                Fact(zakah_mony=calculate_zakah(mony)))   
        
    @Rule(Fact(action='start'), Fact(person='yes'), salience=9)
    def ask_gold(self):
        gold=int(self.window.input('Enter the amount of gold (per gram) that you have, do not include decoration gold: '))
        if(gold < NESAB_GOLD):
            return
        duration_having_gold=int(self.window.input('How many months have you owned this gold without decreasing: '))
        if(duration_having_gold < HAOUL):
            return
        else:
            self.declare(
                Fact(zakah_gold=calculate_zakah(gold)))  
        
    @Rule(Fact(action='start'), Fact(person='yes'), salience=8)
    def ask_silver(self):
        silver=int(self.window.input('Enter the amount of silver (per gram) that you have, do not include decoration silver: '))
        if(silver < NESAB_SILVER):
            return
        duration_having_silver=int(self.window.input('How many months have you owned this silver without decreasing: '))
        if(duration_having_silver < HAOUL):
            return
        else:
            self.declare(
                Fact(zakah_silver=calculate_zakah(silver)))   
            
    @Rule(Fact(action='start'), Fact(person='yes'), salience=7)
    def ask_rikaz(self):
        rikaz=int(self.window.input('Enter the amount of rikaz (any mony or gold or silver that you found it by accident and it has no owner) (per syrian pound): '))
        if(rikaz < NESAB_RIKAZ):
            return
        self.declare(
            Fact(zakah_rikaz=calculate_rikaz_zakah(rikaz)))
        
    @Rule(Fact(action='start'), Fact(person='yes'), salience=6)
    def ask_plants(self):
        plants_num=int(self.window.input('Enter the amount of plants (thant are harvested) (per Kilogram): '))
        type = self.window.radio('What is the type of watering the plants?',[ 'rain raised' , 'self raised'])
        s= plants_engin()
        s.window = self.window
        s.reset()
        s.declare(plants(type=type), plants(count=plants_num))
        s.run()
        for i in range(s.facts.last_index):
            self.declare(s.facts[i])
        return
        
    @Rule(Fact(action='start'), Fact(person='yes'), salience=5)
    def ask_camel(self):
        camel_num=int(self.window.input('Enter the amount of camels you have (do not include camels used for work or camels have been raised by feeding it): '))
        s= anaam_zakah()
        s.window = self.window
        s.reset()
        s.declare(camel(count=camel_num))
        s.run()
        for i in range(s.facts.last_index):
            self.declare(s.facts[i])
        return
        
        
    @Rule(Fact(action='start'), Fact(person='yes'), salience=4)
    def ask_cow(self):
        cow_num=int(self.window.input('Enter the amount of cows you have (do not include cows used for work or cows have been raised by feeding it): '))
        s= anaam_zakah()
        s.window = self.window
        s.reset()
        s.declare(cow(count=cow_num))
        s.run()
        for i in range(s.facts.last_index):
            self.declare(s.facts[i])
        return
        
        
    @Rule(Fact(action='start'), Fact(person='yes'), salience=3)
    def ask_sheep(self):
        sheep_num=int(self.window.input('Enter the amount of sheep you have (do not include sheep used for work or sheep have been raised by feeding it): '))
        s= anaam_zakah()
        s.window = self.window
        s.reset()
        s.declare(sheep(count=sheep_num))
        s.run()
        for i in range(s.facts.last_index):
            self.declare(s.facts[i])
        return
