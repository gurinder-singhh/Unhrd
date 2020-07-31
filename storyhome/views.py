from storyhome.models import Profile,Friends
from django.shortcuts import redirect, render
from .forms import ProfileUpdateForm,FriendsListForm
from django.contrib.auth.models import User
# Create your views here.

def landingpage(request):
    return render(request,'storyhome/landingpage.html')

def userhomepage(request):
    return render(request,'storyhome/userhomepage.html')

def profileupdate(request):
    if request.method == 'POST':
        print(request.POST)
        form = ProfileUpdateForm(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    form = ProfileUpdateForm(instance = request.user)
    context = {'form':form,'caller':'profileupdate'}
    return render(request,'storyhome/profile.html',context)

def friendslist(request):
    try:
        friend = Friends.objects.get(current_user = request.user)
        friends = friend.users.all()
    except Friends.DoesNotExist:
        friends = None
    # form = FriendsListForm(request.POST,instance = request.user)
    context = {'friends':friends, 'caller':'friendslist'}
    return render(request,'storyhome/profile.html',context)

def addfriends(request,**kwargs):
    new_friend = User.objects.get(id = kwargs['userid'])
    try:
        friend = Friends.objects.get(current_user = request.user)
    except Exception as e:
        friend = Friends(current_user = request.user)
        friend.save()
    if new_friend == request.user:
        print("NOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        friend.users.add(new_friend)
    return redirect('home:friendslist')

def getallusers(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request,'storyhome/allusers.html',context)

def deletefriends(request,**kwargs):
    x_friend = User.objects.get(id = kwargs['userid'])
    friend = Friends.objects.get(current_user = request.user)
    friend.users.remove(x_friend)
    return redirect('home:friendslist')

# if request.method == 'POST':
#         print(request.POST)
#         form = FriendsListForm(request.POST,instance = request.user)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # active_list = Friends.objects.get(id = request.user.id)
#             active_list.delete()
#             # print(f.friends.get(id = request.POST.dict()['friends']))
#         else:
#             print(form.errors)

#     form = FriendsListForm(instance = request.user)
#     context = {'form':form, 'caller':'friendslist'}
#     return render(request,'storyhome/profile.html',context)


