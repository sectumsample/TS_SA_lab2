import operator


def main():

    print(str(query(Eurofruit, 'id', operator.ne, 555)) + '\n')

    print(str(query(Human, 'salary', operator.eq, 80000)) + '\n')

    get_thing("Mikhail").print_responds('')

    #getThing("Dmitry").printResponds('')


class Thing(object):
    def __init__(self):
        self.name = ""

        self.fields = [str(f) for f in locals()]

    def __repr__(self):
        return self.name


class Human(Thing):
    def __init__(self, salary, name, latevisit, overwork, birthdate, experience, phone):
        self.salary = salary
        self.name = name
        self.overwork = overwork
        self.birthdate = birthdate
        self.experience = experience
        self.phone = phone

        self.fields = [str(f) for f in locals()]


class Boss(Human):
    def __init__(self, salary, name, latevisit, overwork, birthdate, experience, phone, responsible_for):
        super().__init__(salary, name, latevisit, overwork, birthdate, experience, phone)

        self.responsible_for = responsible_for

        self.fields = [str(f) for f in locals()]
        self.fields.remove('__class__')

    def print_responds(self, spac):
        print(spac + '----------')
        print(spac + 'name:', self.name)
        print(spac + 'occupation:', self.__class__.__name__)
        for f in self.fields:
            v = getattr(self, f, None)
            if v:
                if f == 'responsible_for':
                    print(spac + 'responsible_for:')
                    for o in v:
                        obj = get_thing(o)
                        if obj:
                            obj.print_responds(spac + '   ')
                else:
                    print(spac + f + ':', v)

class Director(Boss):
    def __init__(self, salary, name, latevisit, overwork, birthdate, experience, phone, responsible_for):
        super().__init__(salary, name, latevisit, overwork, birthdate, experience, phone, responsible_for)

class DirectorDiputy(Boss):
    def __init__(self, salary, name, latevisit, overwork, birthdate, experience, phone, responsible_for):
        super().__init__(salary, name, latevisit, overwork, birthdate, experience, phone, responsible_for)

class Accountant(Boss):
    def __init__(self, salary, name, latevisit, overwork, birthdate, experience, phone, responsible_for):
        super().__init__(salary, name, latevisit, overwork, birthdate, experience, phone, responsible_for)

class Foreman(Boss):
    def __init__(self, salary, name, latevisit, overwork, birthdate, experience, phone, responsible_for):
        super().__init__(salary, name, latevisit, overwork, birthdate, experience, phone, responsible_for)


class Worker(Human):
    def __init__(self, salary, name, latevisit, overwork, birthdate, experience, phone):
        super().__init__(salary, name, latevisit, overwork, birthdate, experience, phone)

        self.fields = [str(f) for f in locals()]
        self.fields.remove('__class__')

    def print_responds(self, spac):
        print(spac + '----------')
        print(spac + 'name:', self.name)
        print(spac + 'occupation:', self.__class__.__name__)
        for f in self.fields:
            v = getattr(self, f, None)
            if v:
                print(spac + f + ':', v)

class Cleaner(Worker):
    def __init__(self, salary, name, latevisit, overwork, birthdate, experience, phone):
        super().__init__(salary, name, latevisit, overwork, birthdate, experience, phone)

class Electrician(Worker):
    def __init__(self, salary, name, latevisit, overwork, birthdate, experience, phone):
        super().__init__(salary, name, latevisit, overwork, birthdate, experience, phone)

class Technician(Worker):
    def __init__(self, salary, name, latevisit, overwork, birthdate, experience, phone):
        super().__init__(salary, name, latevisit, overwork, birthdate, experience, phone)

class Packer(Worker):
    def __init__(self, salary, name, latevisit, overwork, birthdate, experience, phone):
        super().__init__(salary, name, latevisit, overwork, birthdate, experience, phone)

class Checker(Worker):
    def __init__(self, salary, name, latevisit, overwork, birthdate, experience, phone):
        super().__init__(salary, name, latevisit, overwork, birthdate, experience, phone)


class Supplier(Thing):
    def __init__(self, id, gatherdate, quantity, name, price):
        self.id = id
        self.gatherdate = gatherdate
        self.quantity = quantity
        self.name = name
        self.price = price

        self.fields = [str(f) for f in locals()]

class Eurofruit(Supplier):
    def __init__(self, id, gatherdate, quantity, name, price):
        super().__init__(id, gatherdate, quantity, name, price)


class Partner(Thing):
    def __init__(self, id, quantity, name, price):
        self.id = id
        self.quantity = quantity
        self.name = name
        self.price = price

        self.fields = [str(f) for f in locals()]

class OgurecInternational(Partner):
    def __init__(self, id, quantity, name, price):
        super().__init__(id, quantity, name, price)

class PomidorHoldings(Partner):
    def __init__(self, id, quantity, name, price):
        super().__init__(id, quantity, name, price)


things = set()


def query(cls, slot, condition, value):
    tmpset = set()
    for obj in things:
        if isinstance(obj, cls):
            v = getattr(obj, slot, None)
            if condition(v, value):
                tmpset.add((obj, v))
    return tmpset


def get_thing(thng):
    for obj in things:
        if obj.name == thng:
            return obj
    return None


things.add(Director(100000, 'Mikhail', '0 times', '60 hours', '02.01.1999', '3 years', '8-916-123-12-23',
                    {'Shmidt', 'Ivan', 'Dmitry'}))

things.add(DirectorDiputy(80000, 'Shmidt', '4 times', '0 hours', '23.11.1998', '3 years', '8-916-123-12-23',
                          {'Ivan', 'Dmitry'}))

things.add(Accountant(80000, 'Ivan', '0 times', '2 hours', '23.11.1997', '2 years', '8-916-123-12-23',
                      {}))

things.add(Foreman(90000, 'Dmitry', '1 times', '1 hours', '23.11.1999', '2 years', '8-916-123-12-23',
                   {'Abdul', 'Innokenty', 'Terumi'}))


things.add(Cleaner(5000, 'Abdul', '0 times', '0 hours', '11.12.1980', '2 years', '8-916-321-23-66'))
things.add(Technician(5000, 'Terumi', '0 times', '0 hours', '11.12.1980', '2 years', '8-916-321-23-66'))
things.add(Technician(5000, 'Innokenty', '0 times', '0 hours', '11.12.1980', '2 years', '8-916-321-23-66'))


things.add(Eurofruit(63424, '12.01.2017', 10, 'Eurofruit', 2670000))

things.add(OgurecInternational(5423334, 20, 'Ogurec International', 200000))
things.add(PomidorHoldings(3423415131, 40, 'Pomidor Holdings', 300000))

main()