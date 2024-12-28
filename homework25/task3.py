import datetime

class TimestampMixin:
    def __init__(self):
        self._creation_time = datetime.datetime.now()
        self._modification_time = self._creation_time

    def get_creation_time(self):
        return self._creation_time

    def get_modification_time(self):
        return self._modification_time

    def update_modification_time(self):
        self._modification_time = datetime.datetime.now()

class File(TimestampMixin):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def rename(self, new_name):
        self.filename = new_name
        self.update_modification_time()

class User(TimestampMixin):
    def __init__(self, username):
        super().__init__()
        self.username = username

    def change_username(self, new_username):
        self.username = new_username
        self.update_modification_time()
def main():
    file = File("document.txt")
    user = User("john_doe")

    print("File creation time:", file.get_creation_time())
    print("User creation time:", user.get_creation_time())

    file.rename("new_document.txt")
    user.change_username("jane_doe")

    print("\nFile modification time after rename:", file.get_modification_time())
    print("User modification time after username change:", user.get_modification_time())
if __name__ == '__main__':
    main()