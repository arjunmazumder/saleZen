from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','first_name', 'last_name', 'email', 'password', 'address', 'phone_number', 'designation', 'blood_group']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name = 'CustomUser'
        fields = ['id','first_name', 'last_name', 'email', 'address', 'phone_number', 'designation', 'blood_group']
        read_only_fields = ['is_staff']