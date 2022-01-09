from werkzeug.security import generate_password_hash, check_password_hash

users = [
    {
        "username": "test",
        "password": generate_password_hash("test", method="pbkdf2:sha512"),
    },
    {
        "username": "admin",
        "password": generate_password_hash("admin", method="pbkdf2:sha512"),
    },
]


def authenticate(username, password):
    user = [user for user in users if user["username"] == username]

    if len(user) > 0:
        if check_password_hash(user[0]["password"], password):
            return user[0]

    return None
