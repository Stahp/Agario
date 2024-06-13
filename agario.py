WIDTH= 1920
HEIGHT= 1080
FOOD_COUNT= 100
PLAYER_STARTING_SIZE= 10
FOOD_SIZE= 1

class Sphere:
    def __init__(self, x, y, size):
        self.x= x
        self.y= y
        self.size= size

    def is_colliding(self, sphere):
        return (self.x - sphere.x)^2 - (self.y - sphere.y)^2  < (self.size + sphere.size) ^ 2

    def spawn(self):
        self.x= random() * WIDTH
        self.y= random() * HEIGHT

# def get_speed_from_size(size):
#     return speed

class Food(Sphere):
    self.FOOD_SIZE= FOOD_SIZE
    def __init__(self):
        self.__init__(self.FOOD_SIZE)

class Player(Sphere):
    self.PLAYER_STARTING_SIZE= PLAYER_STARTING_SIZE
    self.MIN_SPEED= 1
    self.MAX_SPEED= 10
    # self.PLAYER_STARTING_SIZE= PLAYER_STARTING_SIZE
    def __init__(self):
        self.__init__(self.PLAYER_STARTING_SIZE)
        self.speed= 10

    def move(self, unit_vector):
        self.x+= self.speed * unit_vector[0]
        self.y+= self.speed * unit_vector[1]

    def eat(self, sphere):
        self.size+= sphere.size
        self.set_speed()
    
    def set_speed(self):
        self.speed= MAX_SPEED - (MAX_SPEED - MIN_SPEED) * size / WIDTH
    

class Scene:
    def __init__(self):
        self.width= WIDTH
        self.height= HEIGHT
    
    def setup(self):
        self.foods= []
        for i in range(FOOD_COUNT):
            food= Food()
            food.spawn()
            self.foods.append(food)
        self.players= [Player()]
    
    def next(self):
        for player in self.players:
            for food in self.foods:
                if player.is_colliding(food):
                    player.eat(food)
                    food.spawn()
                


def main():
    scene= Scene()
    scene.setup()
    while True:
        scene.next()


if __name__ == "__main__":
    main()