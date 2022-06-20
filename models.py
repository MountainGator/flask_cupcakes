"""class for making cuypcakes"""

class Cupcake():
    def __init__(self, id, flavor, size, rating, image):
        self.id = id
        self.flavor = flavor
        self.size = size
        self.rating = rating
        self.image = image

c1 = Cupcake(
    id=1,
    flavor="cherry",
    size="large",
    rating=5,
    image=''
)

c2 = Cupcake(
    id=2,
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)
