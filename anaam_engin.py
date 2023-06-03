from experta import *
from cow import cow_engin
from camel import camel_engin
from sheep import sheep_engin
from zakah_util import *

NESAB_CAMEL=5          ## per 1 camel
NESAB_COW=30           ## per 1 cow
NESAB_SHEEP=40         ## per 1 sheep


class anaam_zakah(KnowledgeEngine):
    @Rule(AS.camel_num<<camel(count=P(lambda x : x>=NESAB_CAMEL)))
    def detect_camel(self, camel_num):
        s= camel_engin()
        s.reset()
        s.declare(camel(count=camel(camel_num)[0]['count']))
        s.run()
        for i in range(s.facts.last_index):
            self.declare(s.facts[i])
    
    @Rule(AS.sheep_num<<sheep(count=P(lambda x : x>=NESAB_SHEEP)))
    def detect_sheep(self, sheep_num):
        s= sheep_engin()
        s.reset()
        s.declare(sheep(count=sheep(sheep_num)[0]['count']))
        s.run()
        for i in range(s.facts.last_index):
            self.declare(s.facts[i])
        
    @Rule(AS.cow_num<<cow(count=P(lambda x : x>=NESAB_COW)))
    def detect_cow(self, cow_num):
        s= cow_engin()
        s.reset()
        s.declare(cow(count=cow(cow_num)[0]['count']))
        s.run()
        for i in range(s.facts.last_index):
            self.declare(s.facts[i])
        