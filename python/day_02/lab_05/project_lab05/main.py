class fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class FruitBasket:
    def __init__(self):
        self.Basket = []

    def add_fruit (self, fruit): 
        self.basket.append(fruit)
        print (f"{fruit.name} added to the basket.")
           
    def remove_fruit (self, fruit): 
     
        if fruit in self.basket:
            self.basket.remove(fruit)
            print(f"{fruit.name} removed fruit from the basket.") 

        else:
            print(f"{fruit.name} is not in the basket.")


    def print_basket (self): 
    
       if self.basket:
        print("Fruits in the basket:")
        for fruit in self.basket:
            print(f"-{fruit.name} ({fruit.color})")


        else:
            print("the basket is empty.")

def main():
 
    basket = FruitBasket()
    num_fruits = int(input("How many fruits do you want add to the basket? "))
    for _ in range(num_fruits):
        name = input ("Enter the fruit name: ")
        color = input("Enter the fruit color: ")
        fruit = fruit(name, color ) 
        basket.add_fruit(fruit)

    basket.print_Basket()

main()

    
    