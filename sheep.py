from experta import *
from zakah_util import *
import math


class sheep_engin(KnowledgeEngine):
    
    @Rule(AND(sheep(count=P(lambda x : x>=40)), sheep(count=P(lambda x : x<=120))))
    def first_limit(self):
        self.declare(Fact(sheep_zakah='1 shaah (shaah is 1 daen or 1 maez)'))
        
    @Rule(AND(sheep(count=P(lambda x : x>=121)), sheep(count=P(lambda x : x<=200))))
    def second_limit(self):
        self.declare(Fact(sheep_zakah='2 shaah (shaah is 1 daen or 1 maez)'))
        
    @Rule(AND(sheep(count=P(lambda x : x>=201)), sheep(count=P(lambda x : x<=300))))
    def third_limit(self):
        self.declare(Fact(sheep_zakah='3 shaah (shaah is 1 daen or 1 maez)'))
        
    @Rule(AS.count<<sheep(count=P(lambda x : x>=301)))
    def final_limit(self, count):
        shaah = math.floor(sheep(count)[0]['count'] / 100) 
        self.declare(Fact(sheep_zakah= str(shaah) + ' shaah (shaah is 1 daen or 1 maez)'))
        