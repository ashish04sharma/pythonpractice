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

# 4. Static methods
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.likes_qty = 0

    def like(self):
        self.likes_qty += 1

    @staticmethod
    def format_post(title, content):
        return (
            f"Post title: {title}\n"
            f"Post content: {content}"
        )


formatted_post = Post.format_post("Some post title", "Post contents")
print(formatted_post)

# 5. Class with just static methods
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def mult(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        raise ValueError("Can't divide by zero")


print(Calculator.add(20, 10))
print(Calculator.subtract(20, 10))
print(Calculator.mult(20, 10))
print(Calculator.divide(20, 10))

 6. Class attributes
class User:
    users_qty = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.users_qty += 1


first_user = User('bob234', 'bob@bob.com')
second_user = User('alice356', 'alice@alice.com')
third_user = User('john324', 'john@john.com')

print(second_user.__dict__)
print(User.__dict__)

print(User.users_qty)
print(third_user.users_qty)

third_user.users_qty = 10
print(User.users_qty)  # 3
print(third_user.users_qty)  # 10
print(third_user.__dict__)