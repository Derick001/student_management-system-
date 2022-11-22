from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User


# Create your views here.
def signup(request):
    if request.method=="POST":
        method=request.POST
        first_name=method['first_name']
        last_name=method['last_name']
        email=method['email']
        username=method['username']
        password=method['password']
        phone=method['phone']
        role=method['role']
        # print(request.POST)
        users= User.objects.filter(username=username)
        if len(users) > 0:
            return render(request, 'db/signup.html', {'error':f'username {username} already exist'})
        else:
            user=User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.save()
            retr_user = User.objects.filter(username=username)
            # print(f"retrieved_user------> {retr_user.values()}")
            
            # [{'id': 14, 'password': '12345', 'last_login': None, 'is_superuser': False, 'username': 'utyboy', 'first_name': 'abasiekeme', 'last_name': 'sylvanus', 'email': 'sylvanusabasiekeme@gmail.com', 'is_staff': False, 'is_active': True, 'date_joined': datetime.datetime(2022, 11, 22, 15, 35, 48, 778472, tzinfo=datetime.timezone.utc)}]
            all_details = User.objects.all().values()
            print(f"this is all details ----> {all_details}")
            retr_val = retr_user.values()
            id = retr_val[0]["id"]
            # print(f"this is id ------> {id}")
            profile = Authentication.objects.create(user_id=id, phone=phone, role=role)
            profile.save()
            return render(request, 'db/signin.html',
             {'message':f'{username} sucessfully signed up'})
    return render(request, 'db\signup.html',)


def signin(request):    
    if request.method=="POST":
        method=request.POST
        username=method["username"]
        password=method["password"]
        users=User.objects.filter(username=username)
        if len(users) > 0:
            first_user = users.first()
            if first_user.password==password:
                request.session['username']= username
                details = User.objects.filter(username=username).values()
                if details:
                    return render(request, 'db/home.html', {"details":details})
                return render(request, 'db/home.html')
            else:
                return render(request, 'db/signin.html', {'display':'wrong password'})
        else:
            return render(request, 'db/signin.html', {'message':'user does not exist'})
    return render(request, 'db/signin.html')


