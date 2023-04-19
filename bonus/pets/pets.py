class PetError(ValueError):
    pass


class Pet(object):
    def __init__(self, species=None, name=""):
        if species.lower() in [
            "dog",
            "cat",
            "horse",
            "gerbil",
            "hamster",
            "ferret",
        ]:
            self.species_str = species.title()
            self.name_str = name.title()

        else:
            raise PetError()

    def __str__(self):
        if self.name_str:
            result_str = "Species of {:s}, named {:s}".format(
                self.species_str, self.name_str
            )
        else:
            result_str = "Species of {:s}, unnamed".format(self.species_str)
        return result_str


class Dog(Pet):
    def __init__(self, name="", chases="Cats"):
        Pet.__init__(self, "Dog", name)
        self.chases = chases.title()
    
    def __str__(self):
        if self.name_str:
            result_str = "Species of {:s}, named {:s}, chases {:s}".format(
                self.species_str, self.name_str, self.chases
            )
        else:
            result_str = "Species of {:s}, unnamed, chases {:s}".format(
                self.species_str, self.chases
            )
        return result_str


class Cat(Pet):
    def __init__(self, name="", hates="Dogs"):
        Pet.__init__(self, "Cat", name)
        self.hates = hates

    def __str__(self):
        if self.name_str:
            result_str = "Species of {:s}, named {:s}, hates {:s}".format(
                self.species_str, self.name_str, self.hates
            )
        else:
            result_str = "Species of {:s}, unnamed, hates {:s}".format(
                self.species_str, self.hates
            )
        return result_str
