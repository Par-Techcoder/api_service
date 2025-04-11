from rest_framework import serializers
from api_v1.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    gender = serializers.SerializerMethodField(read_only=True)
    raw_gender = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'middle_name',
            'last_name',
            'dob',
            'profile_photo_url',
            'email',
            'phone',
            'raw_gender',      # 🛠️ write only
            'gender',          # 👀 read only
            'address',
            'password',
            'date_joined',
        ]
        read_only_fields = ['id', 'date_joined', 'gender']

    def get_gender(self, obj):
        return obj.get_gender_display() if obj.gender is not None else None

    def validate(self, data):
        # Copy raw_gender to gender so the model can use it
        raw_gender = data.pop('raw_gender', None)
        if raw_gender is not None:
            data['gender'] = raw_gender
        return data
