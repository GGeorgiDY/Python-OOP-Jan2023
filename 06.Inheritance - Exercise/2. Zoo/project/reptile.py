from project.animal import Animal


class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)

    # тук нещата могат и да работят ако имаме написан просто един pass. Това е така защото като се извиква този клас,
    # ще и ако не се намери name, ще продължи да се търси в парента на този клас докато го намери.


