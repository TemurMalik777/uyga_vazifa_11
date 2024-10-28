from abc import ABC, abstractmethod

class Ota(ABC):
    def __init__(self, ism, yosh, varoq_soni):
        self.ism = ism
        self._yosh = yosh
        self.kitoblar = varoq_soni
        self.pul = 25000000
        self.yangi_uy = 0

        self.toboqlar_soni = self.kitoblar // 15
        
        if self.toboqlar_soni > 15:
            self.pul += 13000
            print(f"{self.pul} so'm bolaga berildi.")
        else:
            print("Pul berilmaydi.")

    def kitob_oqish(self, kitob_varoqlari):
        yangi_toboqlar = kitob_varoqlari // 15
        self.toboqlar_soni += yangi_toboqlar

        self.pul += yangi_toboqlar * 1000
        print(f"Yangi pul miqdori: {self.pul} so'm")

    def uy_sovga(self):
        if self.pul >= 50000000:
            uy_narxi = self.toboqlar_soni * 2000
            if uy_narxi <= self.pul:
                self.pul -= uy_narxi
                self.yangi_uy += 1
                print(f"{self.ism} ga bitta yangi uy sovg'a qilindi.")
                print(f"{self.ism} ning pul miqdori: {self.pul} so'm, yangi uy soni: {self.yangi_uy}")
            else:
                print("Yana uy sovg'a qilish uchun etarli pul yo'q.")
        else:
            print("Bola pulini oshirish kerak.")

    @abstractmethod
    def haydash(self):
        pass

class bola_1(Ota):
    def __init__(self, ism, yosh, varoq_soni):
        super().__init__(ism, yosh, varoq_soni)

    def haydash(self):
        print('URA!!!! Otajon haydashga ruxsat oldim')

class bola_2(Ota):
    def __init__(self, ism, yosh, varoq_soni):
        super().__init__(ism, yosh, varoq_soni)

    def haydash(self):
        print('Bola2 haydashga ruxsat oldi')

bola1 = bola_1('Hasan', 15, 300) 
bola1.haydash()

bola2 = bola_2('Berdi', 15, 200)
bola2.haydash()

bola1.kitob_oqish(150)
bola1.kitob_oqish(75)

bola1.pul += 30000000 
bola1.uy_sovga()

bola1.pul += 5000000 
bola1.uy_sovga()
