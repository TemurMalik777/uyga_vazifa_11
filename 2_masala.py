from abc import ABC, abstractmethod
class Ota(ABC):
    def __init__(self, ism, yosh):
        self.ism = ism
        self._yosh = yosh

        if self._yosh<18:
            self.pul = 120000000000
            print(f'{self.pul} dan puldan foydalnish mumkin')
        else:
            print('Afsus puldan foydalanish mumkin emas')

    @abstractmethod
    def haydash(self):
        print(self.ism,' haydash mumkin')

class bola_1(Ota):
    def __init__(self,ism, yosh):
        super().__init__(ism, yosh)
        self.yosh = yosh

    def haydash(self):
        print('URA!!!! Otajon haydashga ruxsat oldim')

class bola_2(Ota):
    pass

bola1 = bola_1('Bola1',15)
bola1.haydash()

try:
    bola2 = bola_2('Bola2',16)
    bola2.haydash()
except:
    print('Bola2 ga ruxsat yo`q')    