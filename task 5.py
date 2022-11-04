import random

def generate_pwd(n) -> str:
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.sample(list(set(alphabet)), n))

def get_random_password() -> str:
    return generate_pwd(8)

print(get_random_password())
