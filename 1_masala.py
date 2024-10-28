from abc import ABC, abstractmethod

class Ota(ABC):
    @abstractmethod
    def haydash(self):
        pass

class Birinchi_ogil(Ota):
    def __init__(self, ism):
        self.ism = ism

    def haydash(self):
        print(f"{self.ism} - Haydash huqiqiga ega")
class Ikkinchi_ogil(Ota):
    pass

bola_1 = Birinchi_ogil("Bola_1")
bola_1.haydash()

try:
    bola2 = Ikkinchi_ogil("Bola2")
    bola2.haydash()
except:
    print("Ruxsat yo'q")
