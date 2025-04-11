from api_v1.models import User

def get_all_user():
    """Get all users from the database."""
    return User.objects.filter(is_active=True, is_superuser=False).all()


def user_create(validated_data):
    password = validated_data.pop('password')
    user = User(**validated_data)
    user.set_password(password)  # ✅ Hash password
    user.save()
    return user
