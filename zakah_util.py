from email import message
from experta import *

class camel(Fact):
    pass 

class cow(Fact):
    pass 

class sheep(Fact):
    pass 

class plants(Fact):
    pass 

def calculate_zakah(mony_gold_silver_metal):
    return (mony_gold_silver_metal * 2.5) / 100

def calculate_rikaz_zakah(rikaz):
    return (rikaz * 5) / 100


def calculate_plants_zakah(quantity, type):
    
    if(type == 'rain raised'):
        return int(quantity) / 10
    else:
        return int(quantity) / 20       
    
    
messages = {
    'moustahkyes': 'This person deserve the zakah',
    'moustahkno' : 'This person does not deserve the zakah',
    'zakah_mony' : 'zakah of mony = ',
    'zakah_gold' : 'zakah of gold = '  ,
    'zakah_silver' : 'zakah of silver = ',
    'zakah_rikaz' : 'zakah of rikaz = ',
    'plants_zakah' : 'zakah of plants = ' ,
    'camel_zakah' : 'zakah of camels = ',
    'cwo_zakah' : 'zakah of cows = ',
    'sheep_zakah' : 'zakah of sheep = '
    
    
}    
    
def print_map(key, value):
    try:
        letter = messages[key]
        letter += value
        return letter
    except:
        return ''
