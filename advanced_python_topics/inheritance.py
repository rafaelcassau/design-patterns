
class Pet:
    """ Base class for all pets """
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def __str__(self):
        return '{} is a {}'.format(self.name, self.species)


class Dog(Pet):

    def __init__(self, name, chases_cats):
        """
            This is a overloading
            Same method with custom parameters
        """
        super().__init__(name, 'Dog')
        self.chases_cats = chases_cats

    def chases_cats(self):
        return self.chases_cats

    def __str__(self):
        """
            This is a override
            Same method and same attributes
        """
        additional_info = ''
        if self.chases_cats:
            additional_info = ' who chases cats'
        return super().__str__() + additional_info


p = Pet('Polly', 'Parrot')
p.__str__()
Pet.__subclasses__()

d = Dog('Fred', True)
d.__str__()
Dog.__bases__