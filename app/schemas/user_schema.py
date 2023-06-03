from app.utils import hash

def user_serializer(user) -> dict:
    return {
        '_id':str(user["_id"]),
        'phone': int(user["phone"]),
        "email": str(user["email"]),
        'first_name': str(user["first_name"]),
        'last_name': str(user["last_name"]),
        'password': str(user["password"])
    }


def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]