from experta import *
from zakah_util import *

class plants_engin(KnowledgeEngine):
    
    @Rule(AS.type<<plants(type='rain raised'), AS.quantity<<plants(count=P(lambda x : x>0)))
    def plants_rain_zakah(self, quantity, type):
        self.declare(Fact(plants_zakah=calculate_plants_zakah(plants(quantity)[0]['count'], plants(type)[0]['type'])))
        return
        
    @Rule(AND(AS.type<<plants(type='self raised'), AS.quantity<<plants(count=P(lambda x : x>0))))
    def plants_water_zakah(self, quantity, type):
        self.declare(Fact(plants_zakah=calculate_plants_zakah(plants(quantity)[0]['count'], plants(type)[0]['type'])))
        return