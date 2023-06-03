from experta import *
from zakah_util import *
import math


class camel_engin(KnowledgeEngine):
    
    @Rule(AND(camel(count=P(lambda x : x>=5)), camel(count=P(lambda x : x<=9))))
    def first_limit(self):
        self.declare(Fact(camel_zakah='1 sheep'))
        
    @Rule(AND(camel(count=P(lambda x : x>=10)), camel(count=P(lambda x : x<=14))))
    def second_limit(self):
        self.declare(Fact(camel_zakah='2 sheep'))
        
        
    @Rule(AND(camel(count=P(lambda x : x>=15)), camel(count=P(lambda x : x<=19))))
    def third_limit(self):
        self.declare(Fact(camel_zakah='3 sheep'))
        
        
    @Rule(AND(camel(count=P(lambda x : x>=20)), camel(count=P(lambda x : x<=24))))
    def fourth_limit(self):
        self.declare(Fact(camel_zakah='24 sheep'))
        
        
    @Rule(AND(camel(count=P(lambda x : x>=25)), camel(count=P(lambda x : x<=35))))
    def fifth_limit(self):
        self.declare(Fact(camel_zakah='1 makhad female'))
        
        
    @Rule(AND(camel(count=P(lambda x : x>=36)), camel(count=P(lambda x : x<=45))))
    def sixth_limit(self):
        self.declare(Fact(camel_zakah='1 laboon female'))
        
        
    @Rule(AND(camel(count=P(lambda x : x>=46)), camel(count=P(lambda x : x<=60))))
    def seventh_limit(self):
        self.declare(Fact(camel_zakah='1 houkka female'))
    
    @Rule(AND(camel(count=P(lambda x : x>=61)), camel(count=P(lambda x : x<=75))))
    def eighth_limit(self):
        self.declare(Fact(camel_zakah='1 jazaa female'))
        
    @Rule(AND(camel(count=P(lambda x : x>=76)), camel(count=P(lambda x : x<=90))))
    def ninth_limit(self):
        self.declare(Fact(camel_zakah='2 laboon female'))
        
    @Rule(AND(camel(count=P(lambda x : x>=91)), camel(count=P(lambda x : x<=120))))
    def tenth_limit(self):
        self.declare(Fact(camel_zakah='2 houkka female'))
        
    @Rule(AS.count<<camel(count=P(lambda x : x>=121)))
    def final_limit(self, count):
        camel_num = camel(count)[0]['count']
        laboon_num = math.floor(camel_num  / 40)
     
        houkka_num = 0
        if(camel_num % 40 > 10):
            laboon_num -= 1
            houkka_num = 1
        
        if(houkka_num > 0):
            self.declare(Fact(camel_zakah=str(laboon_num) + ' laboon and ' + str(houkka_num) + ' houkka'))
        else:
            self.declare(Fact(camel_zakah=str(laboon_num) + ' laboon '))
        