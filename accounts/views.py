from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import SignupForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login


def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save(commit=True)
            # authenticate => make sure that user is exist
            user_name = signup_form.cleaned_data['username']
            user_pass = signup_form.cleaned_data['password1']
            user = authenticate(username=user_name, password=user_pass)
            login(request, user)
            user_profile = Profile.objects.get(user=request.user)
            return redirect('/accounts/profile/'+user_profile.user_slug)

    else:
        signup_form = SignupForm()

    return render(request, 'registration/signup.html', {'signup_form':signup_form})

@login_required(login_url='/accounts/login')
def profile(request, userURL):
    user_profile = Profile.objects.get(user_slug = userURL)
# def profile(request, userURL):
#     user_profile = Profile.objects.get(id = request.user.id, user_slug = userURL)
    return render(request, 'profile/profile.html', {'user_profile':user_profile})

@login_required(login_url='/accounts/login')
def profile_edit(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            # should sign it to the same user, so commit it false to add the user
            profile_form.save(commit=False)
            profile_form.user = request.user
            profile_form.save()
            return redirect('/accounts/profile/'+profile.user_slug)
    
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    # user_profile = 
    return render(request, 'profile/profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })