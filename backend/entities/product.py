class Product:
    def __init__(self, _id: int, name: str, price: float, description: str):
        self.id = _id
        self.name = name
        self.price = price
        self.description = description

    def dictify(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description
        }
