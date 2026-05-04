class Ota:
    def __init__(self, fullname):
        self.fullname = fullname
        self.__money = 23

    def pul_solish(self, toza_pul):
        self.__money += toza_pul
        print(f"Toza pul: {self.__money}")

    def info(self):
        print(f"Egasi: {self.fullname}")
        print(f"Puli: {self.__money}")


o1 = Ota("Aliyev Vali")
o1.info()
o1.pul_solish(20)
