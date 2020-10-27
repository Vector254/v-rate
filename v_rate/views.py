from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile, Project, Rate
from .forms import UserRegistrationForm, ProjectPostForm, UserUpdateForm, ProfileUpdateForm, RatingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html',{"projects":projects})

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
    projects = Profile.objects.all()
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
        results = Project.objects.filter(title__icontains=title).all()
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

def detail(request,pk):
   
    project = Project.objects.get(id=pk)
    ratings = Rate.objects.filter(user=request.user, project=project).first()
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = project
            rate.save()
            project_rating = Rate.objects.filter(project=project)
            design = sum([design.design for design in project_rating])/len([design.design for design in project_rating])
            usability = sum([use.usability for use in project_rating])/len([use.usability for use in project_rating])
            content = sum([content.content for content in project_rating])/len([content.content for content in project_rating])

            score =(design + usability + content) / 3
            rate.score = round(score, 2)
            print(rate.score)
            rate.save()
            
            
    else:
        form = RatingForm()
    
    params = {
        'project': project,
        'form':form,
       
            }

    return render(request,"project_detail.html", params)

@login_required
def create_post(request):
    current_user = request.user
    form = ProjectPostForm()
    if request.method == 'POST':
        form = ProjectPostForm(request.POST, request.FILES or None)
        if form.is_valid():
            add=form.save(commit=False)
            add.user = request.user
            add.save()
            return redirect('index')
    

    context = {'form':form}
    return render(request,'create_post.html',context)
