import datetime

# მიქსინის კლასი TimestampMixin
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

# File კლასი
class File(TimestampMixin):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def rename(self, new_name):
        self.filename = new_name
        self.update_modification_time()

# User კლასი
class User(TimestampMixin):
    def __init__(self, username):
        super().__init__()
        self.username = username

    def change_username(self, new_username):
        self.username = new_username
        self.update_modification_time()

# ობიექტების შექმნა და მათი გამოყენება
file = File("document.txt")
user = User("john_doe")

# შექმნის დროების ჩვენება
print("File creation time:", file.get_creation_time())
print("User creation time:", user.get_creation_time())

# ცვლილებების შეტანა
file.rename("new_document.txt")
user.change_username("jane_doe")

# მოდიფიკაციის დროების ჩვენება
print("\nFile modification time after rename:", file.get_modification_time())
print("User modification time after username change:", user.get_modification_time())