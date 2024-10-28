from abc import ABC, abstractmethod

class Ota(ABC):
    @abstractmethod
    def oqigan_kitoblar(self):
        pass

    @abstractmethod
    def tekshir(self, kitob):
        pass

class Birinchi_ogil(Ota):
    def __init__(self, ism, kitoblar):
        self.ism = ism
        self.kitoblar = kitoblar

    def oqigan_kitoblar(self):
        print(f"{self.ism} ning o'qigan kitoblari:")
        for kitob in self.kitoblar:
            print(kitob)

    def tekshir(self, kitob):
        if kitob in self.kitoblar:
            print(f"{kitob} - {self.ism} o'qigan kitob.")
        else:
            print(f"{kitob} - {self.ism} bu kitobni o'qimagan.")

class Ikkinchi_ogil(Ota):
    def __init__(self, ism, kitoblar):
        self.ism = ism
        self.kitoblar = kitoblar

    def oqigan_kitoblar(self):
        print(f"{self.ism} ning o'qigan kitoblari:")
        for kitob in self.kitoblar:
            print(kitob)

    def tekshir(self, kitob):
        if kitob in self.kitoblar:
            print(f"{kitob} - {self.ism} o'qigan kitob.")
        else:
            print(f"{kitob} - {self.ism} bu kitobni o'qimagan.")

bola_1 = Birinchi_ogil("Bola_1", ["Molxona", "Savodgarlar Ustozi", "1984", "Stiv Jobis", "Hamsa"])
bola_2 = Ikkinchi_ogil("Bola_2", ["Yuldizli Tunlar", "Borburnoma", "Graf Monta kristo", "10 ta negir bolasi", "Shiksper"])


kitob_nomi = input("O'qigan kitob nomini kiriting: ")
bola_1.tekshir(kitob_nomi)

kitob_nomi = input("O'qigan kitob nomini kiriting: ")
bola_2.tekshir(kitob_nomi)
