from rest_framework import  serializers
from authentication.models import CustomUser, Profile

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email','password','first_name', 'last_name', 'company', 'address', 'phone')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
               username = validated_data['first_name'].lower() + "" + validated_data['last_name'].lower(),
               email = validated_data['email'],
               password = validated_data['password'],
               first_name=validated_data['first_name'],  
               last_name=validated_data['last_name'],
               company = validated_data['company'],
               address = validated_data['address'],
               phone = validated_data['phone'],
               )
        return user
    

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class MembersSerializer(serializers.ModelSerializer):

    #full_name = serializers.SerializerMethodField('get_full_name')
    class Meta:
        model = CustomUser
        fields = ['pk','first_name', 'last_name']

    # def get_full_name(self, CustomUser):
    #     user = CustomUser.objects.all()
    #     first_name = self.user.first_name
    #     last_name = self.user.last_name
    #     return f"{self.first_name} {self.last_name}"

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email','picture']

class UserProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'

class PhotoProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'