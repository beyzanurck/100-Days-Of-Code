class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0

user1 = User("123","Beyza")
user1.follower = 1
print(user1.follower)