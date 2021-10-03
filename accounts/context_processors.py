from .models import Profile

def profile_slug(request):
    if request.user.is_authenticated:
        user_profile = Profile.objects.get(user = request.user)
        return {'profile_slug':user_profile.user_slug}
    return {}