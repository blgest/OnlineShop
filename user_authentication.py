from werkzeug.security import generate_password_hash, check_password_hash

class UserAuthentication:
    def hash_password(self, password):
        return generate_password_hash(password, method='sha256')

    def verify_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
