
class Athlete:
    def __init__(self,ht,wt,bodyfat):
        self.__ht = ht
        self.__wt = wt
        self.__bf = bodyfat
#height weight and bodyfat are the attributes
    def get_ht(self):
        return self.__ht

    def get_wt(self):
        return self.__wt

    def get_bf(self):
        return self.__bf


#football player si a special type of athlete, inherits fromt he athlete superclass

class Football_Player(Athlete):
#expecting the user to give the same attributes as athlete but have add specific ones for football player

    def __init__(self,ht,wt,bodyfat,position,team):

        Athlete.__init__(self,ht,wt,bodyfat)

        self.__position = position
        self.__team = team


    def get_position(self):
        return self.__position

    def get_team(self):
        return self.__team










    
