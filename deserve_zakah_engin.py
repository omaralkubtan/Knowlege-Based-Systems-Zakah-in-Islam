from ast import Not
from multiprocessing import managers
from experta import * 


class deserve_zakah_engin(KnowledgeEngine):
    
    @DefFacts()
    def _initial_action(self):
        yield Fact(moustahk='no')
        
        
    @Rule(Fact(person='yes'), salience=10)
    def ask_al_albet(self):
        mansoub=self.window.radio('is the person mansoub to prophet mouhammad? ',["yes","no"])
        self.declare(Fact(mansoub=mansoub))
        
        
    @Rule(AND(Fact(person='yes'), Fact(mansoub='no')), salience=9)
    def ask_poor(self):
        poor=self.window.radio('is the person poor and need financial help?',["yes","no"])
        self.declare(Fact(poor=poor))
        
        
    @Rule(AND(Fact(person='yes'), Fact(mansoub='no'), NOT(Fact(poor='yes'))), salience=8)
    def ask_new_muslim(self):
        new_week_muslim=self.window.radio('have the person entered islam recently and might be insure completely about islam? ',["yes","no"])
        self.declare(Fact(new_week_muslim=new_week_muslim))
        
        
    @Rule(AND(Fact(person='yes'), Fact(mansoub='no'), NOT(Fact(poor='yes')), NOT(Fact(new_week_muslim='yes'))), salience=7)
    def ask_slave(self):
        slave=self.window.radio('is the person muslim slave?',["yes","no"])
        self.declare(Fact(slave=slave))
        
        
    @Rule(AND(Fact(person='yes'), Fact(mansoub='no'), NOT(Fact(poor='yes')), NOT(Fact(new_week_muslim='yes')),
             NOT(Fact(slave='yes'))), salience=6)
    def ask_soldier(self):
        soldier=self.window.radio('is the person soldier protecting the country? ',["yes","no"])
        self.declare(Fact(soldier=soldier))
        
        
    @Rule(AND(Fact(person='yes'), Fact(mansoub='no'), NOT(Fact(poor='yes')), NOT(Fact(new_week_muslim='yes')),
             NOT(Fact(slave='yes')), NOT(Fact(soldier='yes'))), salience=5)
    def ask_lender(self):
        lender=self.window.radio('have the person lend mony for good purpose and its hard for him to return the mony back? ',["yes","no"])
        self.declare(Fact(lender=lender))
        
        
    @Rule(AND(Fact(person='yes'), Fact(mansoub='no'), NOT(Fact(poor='yes')), NOT(Fact(new_week_muslim='yes')),
             NOT(Fact(slave='yes')), NOT(Fact(soldier='yes')), NOT(Fact(lender='yes'))), salience=4)
    def ask_son_of_sabeel(self):
        son_of_sabeel=self.window.radio('is the person foreign and need financial aid to return his home?',["yes","no"])
        self.declare(Fact(son_of_sabeel=son_of_sabeel))
        
        
        
    @Rule (AS.mo << Fact(moustahk='no'), OR(Fact(poor='yes'), Fact(new_week_muslim='yes'),Fact(slave='yes'), Fact(soldier='yes'), Fact(lender='yes')), salience=3)
    def set_moustahk(self, mo):
        self.modify(mo, moustahk='yes')
    