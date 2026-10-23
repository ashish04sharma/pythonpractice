# 1. Methods are inherited by the instances of the class
class Car:
    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car stopped")


my_car = Car()
print(type(my_car))
print(isinstance(my_car, Car))
print(isinstance(my_car, object))
print(dir(my_car))
print(my_car.__dict__)

my_car.move()
my_car.stop()


#  2. Magic __init__ method
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def info(self):
        print(f"User {self.username} has email {self.email}")


first_user = User('bogdan123', 'bogdan@bogdan.com')
first_user.info()
print(first_user.username)
print(first_user.email)

other_user = User('alice3245', 'alice@alice.com')
other_user.info()
print(other_user.username)
print(other_user.email)
print(other_user.__dict__)

other_user.username = 'a6363'
print(other_user.username)


#  3. Methods
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.likes_qty = 0

    def like(self):
        self.likes_qty += 1


my_post = Post("My first post", "Some post content", "Bogdan")
print(my_post)
print(my_post.title)
print(my_post.likes_qty)

my_post.like()  # recommended
my_post.like()
print(my_post.likes_qty)

Post.like(my_post)  # not recommended
print(my_post.likes_qty)


# Post class doesn't have such attributes!
# Post.likes_qty
# Post.title