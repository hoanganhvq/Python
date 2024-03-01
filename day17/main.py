class User:
    def __init__(self,user_id,username, password):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0
        self.password = password
    def follow(self, user):
        user.follower +=1
        self.following +=1
user1 = User("001","Huynh Ngoc Vy", "abcde")
user2 = User("002", "Phan Hoang Anh", "anh1507")

# print(user1.id)
# print(user1.username)
# print(user1.password)

user1.follow(user2)
print(user1.following)
print(user1.follower)