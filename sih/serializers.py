from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User,auth
from rest_framework import exceptions
from django.contrib.auth import authenticate


class datasSerializer(serializers.ModelSerializer):
    class Meta:
        model=datas
        fields='__all__'

class registerSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=255,min_length=4)
    password=serializers.CharField(max_length=100)
    first_name=serializers.CharField(max_length=100)
    last_name=serializers.CharField(max_length=100)

    class Meta:
        model=User
        fields='__all__'

    def save(self):
        email=self.validated_data['email']
        username=self.validated_data['username']
        if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'account':'account is already exists'})
        else:
            user=User.objects.create(
                username=self.validated_data['username'],
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name'],
                email=self.validated_data['email'],
            )
            password=self.validated_data['password']
            user.is_active=True
            user.set_password(password)
            user.save() 
            return user



class loginSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=100)

    class Meta:
        model=User
        fields='__all__'

    def save(self):
        username=self.validated_data['username']
        password=self.validated_data['password']

        if username and password:
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    return user
                else:
                    raise serializers.ValidationError({'user':'user is not active'})
            else:
                raise serializers.ValidationError({'user':'please enter valid user credentails'})
        else:
            raise serializers.ValidationError({'error':'username and password not to be blank'})

class resetpasswordSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=100)

    class Meta:
        model=User
        fields='__all__'


    def save(self):
        username=self.validated_data['username']
        password=self.validated_data['password']
        if User.objects.filter(username=username).exists():
            user=User.objects.get(username=username)
            user.set_password(password)
            user.save()
            # for i in user:
            #     ruser=User.objects.get(pk=i.pk)
            #     ruser.set_password(password)
            #user.set_password(password)
            return user
        else:
            return 'no value'
  

