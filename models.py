"""class for making cupcakes"""

class Cupcake():
    def __init__(self, id, flavor='vanilla', size='small', rating=0, image=''):
        self.id = id
        self.flavor = flavor
        self.size = size
        self.rating = rating
        self.image = image

    def get_json (self):
        cake = {
            '_id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }
        return cake



c1 = Cupcake(
    id=1,
    flavor="cherry",
    size="large",
    rating=5,
    image='https://www.cookingclassy.com/wp-content/uploads/2014/01/cherry-almond-cupcakes-edit+srgb+text..jpg'
)

c2 = Cupcake(
    id=2,
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)
