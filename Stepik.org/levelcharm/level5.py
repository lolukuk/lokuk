class Product:
    color = 'red'
    count = 3

    def set_coords(self,x,y):
        print("Вызов функции set_coords")
        self.y = 'kek'
        self.x = 123

pt = Product()
pt.set_coords(1,2)
print(pt.__dict__)
