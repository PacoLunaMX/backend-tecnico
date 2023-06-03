from passlib.context import CryptContext

# asigning the algo to hash the passwords
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

# function to hash a password
def hash(password: str):
   return pwd_context.hash(password)