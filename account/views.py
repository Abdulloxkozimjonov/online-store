from django.shortcuts import render
from main.models import User
from main.serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout
from rest_framework.permissions import IsAuthenticated


""" Start accaunt view """
@api_view(['POST'])
def singin_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        usr = authenticate(username = username, password = password)
        try:
            if usr is not None:
                login(request, usr)
                status = 200
                data = {
                    'status' : status,
                    'usrname' : username,
                }
            else:
                status = 403
                message = " Invali Password or Username! "
                data = {
                    'status' : status,
                    'message' : message
                }
        except User.DoesNoteExit:
            status = 404
            message = 'This User is not defined '
            data = {
                'status' : status,
                'message' : message
            }
        return Response(data)
    except Exception as err:
        return Response(f'{err}')


@api_view(['POST'])
def singup_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    phone_number = request.POST.get('phone_number')
    new = User.objects.create_user(
        username = username,
        password = password,
        phone_number = phone_number
    )
    ser = UserSerializer(new)
    return Response(ser.data)


@api_view(['POST'])
def edit_user(request, pk ):
    try:
        user = User.objects.get(pk=pk)
        try:
            username = request.POST['username']
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('cofirm_password')
            user.username = username
            if first_name is not None:
                user.first_name=first_name
            if last_name is not None:
                user.last_name=last_name
            if email is not None:
                user.email =email
            if bio is not None:
                user.bio=bio
            if phone_number is not None:
                user.phone_number = phone_number
            if password is not None:
                if password == confirm_password:
                    user.set_password(password)
            user.save()
        except:
            status: 404
            message = "Page not found"
            data = {
                'status ': status,
                'message': message
            }
    except:
        status = 403
        message = ' Invalid Again Password '
        data = {
            'status': status,
            'message': message
        }
        ser = UserSerializer(user)
    return Response(ser.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logoout(request):
    logout(request)
    return Response({'data':'sucses'})

""" End accound view """
