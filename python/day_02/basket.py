from importlib.resources import contents


class Basket:
    def __init__(self, owner, size): 
        self.owner = owner
        self.size = size
        self:content = []

        print("Nova cesta iniciada para o {owner}para ate {size} item!")

    def add_content(self, content):
        self.content.append(content)

    if __name__ =="__main__":
        basket_a = Basket(owner="Diogo", size=10)
        basket_b = Basket(owner="henrique", size=10)