from django.db import transaction
from django.core.exceptions import ValidationError
from account.models import User
from account.serializers import RegisterSerializer

class AccountServices:
    @staticmethod
    def register_user(data) :
        with transaction.atomic():
            name = data.get('name')
            email = data.get('email')
            phone = data.get('phone')
            role = data.get('role')
            password = data.get('password')
            if not phone :
                raise ValidationError("Phone number is required")
            if not email :
                raise ValidationError("Email is required")
            user = User.objects.filter(email=email, phone=phone).first();
            if user:
                raise ValidationError("User with this email or phone already exists")
            
            user = User.objects.create_user(
                email=email,
                name=name,
                phone=phone,
                role=role,
                password=password
            )

            serialized_user = RegisterSerializer(user).data
            return {'message': 'User Created Successfully', 'user': serialized_user}