from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile, Project, Rate

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/registration_form.html',{'form':form})

def profile(request):
    projects = Profile.projects.all()
    #user_profile = get_object_or_404(User, pk=pk)
   
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
           user_form.save() 
           profile_form.save()
           messages.success(request, f'Profile info updated successfully!')
           return redirect('profile' )

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    params = {
        'images':projects,
        'user_form':user_form,
        'profile_form':profile_form,
        
       
    }
   
    return render(request, 'profile.html', params)

def search_results(request):
    if request.method == 'GET':
        title = request.GET.get("query")
        results = Post.objects.filter(title__icontains=title).all()
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'search.html', {'message': message})

def detail(request,project_id):
   
    project = Project.objects.get(id=project_id)
    params = {
        'project': project,
       
        }

    return render(request,"project_detail.html", params)
