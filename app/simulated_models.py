users_db = []

class UserNotFoundException(Exception):
    pass


class NullUserError(Exception):
    pass


class RecipeNotFoundError(Exception):
    pass

    
class Users():
    def __init__(self):
        self.users = users_db

    def add_user(self, user):
        if user:
            if len(self.users) == 0:
                self.users.append(user.user_details)
            else:
                for u in self.users:
                    if u["email"] == user.email:
                        raise NullUserError("user already exists") 
                    else:
                        self.users.append(user.user_details) 
        else:
            raise NullUserError("Cannot add empty user")

    def get_all_users(self):
        return self.users


class User():
    def __init__(self, id, firstname, lastname, email, mobilenumber, password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.mobilenumber = mobilenumber
        self.password = password

    @property
    def user_details(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "mobilenumber": self.mobilenumber,
            "password": self.password
        }

    def __repr__(self):
        return "<User {} {}>".format(self.firstname, self.lastname)
