from models import User


class EmailAuth(object):
    def authenticate(self, email=None, password=None):
        # Get an instance of user using the supplied email and check its password

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        # Used by django auth system to retreive an instance of user

        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None