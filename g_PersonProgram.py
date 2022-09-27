import g_PersonClass as pc

def main():
    name="John"
    address= '123 main st'
    telephone= '123-456-7890'
    number= '33'
    mailing = False

    person1= p.Person(name, address, telephone)

    customer1= p.Customer(name, address, telephone, number, mailing)
    

    person1.print_person()

    print()
    print()
    print()

    customer1.print_person()

    
main()