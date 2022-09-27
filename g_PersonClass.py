class Person:

    def __init__(self, name, address, telephone):
        self.__name= name
        self.__address= address
        self.__telephone= telephone

    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_telephone(self):
        return self.__telephone

class Customer(Person):
    def _init__(self, name, address, telephone, number, mailing):
        Person.__init__(self, name, address, telephone)

        self.__number= number
        self.__mailing=mailing
    '''  
    def get_number(self):
        return self.__number
    
    def get_mailing(self):
        return self.__mailing
    '''
    


    def print_person(self):
        print('method 1')
        print('Name: ', Person.get_name(self))
        print('Add:', Person.get_address(self))
        print('Phone:', Person.get_telephone(self))

        print()
        print()

        print('method 1')
        Person.print_person(self)

        print('')

    Person.print_person(self)




