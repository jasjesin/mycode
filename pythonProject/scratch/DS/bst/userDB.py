import users
import time


class UserDB:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def search(self, username):
        [[print(f"Details for searched user, {username}:\n{user}") for user in self.users if user.username == username]]

    def update(self, user):
        target = self.search(user.username)
        target.name, target.email = user.name, user.email

    def list(self):
        return self.users


start_time = time.time()
db = UserDB()
db.insert(bst.jas)
db.insert(bst.biraj)
db.insert(bst.aakash)

db.search('Jas')
print("\n\nList of all users:", *db.list(), sep='\n')
print("\n[] Program Execution Time: \n--- %s ms ---" % ((time.time() - start_time)* 10**3))
