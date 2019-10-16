class Schueler:
    def __init__(self, name, leistungskurs):
        self.name = name
        self.leistungskurs = leistungskurs

    def checkit(self):
        if self.leistungskurs == "Informatik":
            return True
        else:
            return False