from experta import *
from zakah_util import *
import math


class cow_engin(KnowledgeEngine):
    
    @Rule(AND(cow(count=P(lambda x : x>=30)), cow(count=P(lambda x : x<=39))))
    def first_limit(self):
        self.declare(Fact(cwo_zakah='1 tabeea male or 1 tabeea female'))
    
    @Rule(AND(cow(count=P(lambda x : x>=40)), cow(count=P(lambda x : x<=59))))
    def second_limit(self):
        self.declare(Fact(cwo_zakah='1 mousinna female'))
    
    @Rule(AND(cow(count=P(lambda x : x>=60)), cow(count=P(lambda x : x<=69))))
    def third_limit(self):
        self.declare(Fact(cwo_zakah='2 tabeea'))
        
    @Rule(AND(cow(count=P(lambda x : x>=70)), cow(count=P(lambda x : x<=79))))
    def fourth_limit(self):
        self.declare(Fact(cwo_zakah='1 mousinna and 1 tabeea'))
        
    @Rule(AND(cow(count=P(lambda x : x>=80)), cow(count=P(lambda x : x<=89))))
    def fifth_limit(self):
        self.declare(Fact(cwo_zakah='2 mousinna'))
        
    @Rule(AND(cow(count=P(lambda x : x>=90)), cow(count=P(lambda x : x<=99))))
    def sixth_limit(self):
        self.declare(Fact(cwo_zakah='3 tabeea'))    
        
    @Rule(AND(cow(count=P(lambda x : x>=100)), cow(count=P(lambda x : x<=109))))
    def seventh_limit(self):
        self.declare(Fact(cwo_zakah='1 mousinna and 2 tabeea'))    
        
    @Rule(AND(cow(count=P(lambda x : x>=110)), cow(count=P(lambda x : x<=119))))
    def eighth_limit(self):
        self.declare(Fact(cwo_zakah='2 mousinna and 1 tabeea'))    
        
    @Rule(AS.count<<cow(count=P(lambda x : x>=120)))
    def final_limit(self, count):
        cow_num = cow(count)[0]['count']
        tabeea = math.floor(cow_num  / 30)
        mousinnna = 0
        if(cow_num  % 30 > 10):
            tabeea -= 1
            mousinnna = 1
        
        if(mousinnna > 0):
            self.declare(Fact(cwo_zakah=str(tabeea) + ' tabeea and ' + str(mousinnna) + ' mousinna'))
        else:
            self.declare(Fact(cwo_zakah=str(tabeea) + ' tabeea '))
                