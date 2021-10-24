from accounts.models import Profile
from service.models import Category

def base_processors(request):
    
    categories = Category.objects.all()

    if request.user.is_authenticated:
        
        user_profile = Profile.objects.get(user = request.user).user_slug

    else:
        user_profile = {}

    return {
        'profile_slug':user_profile,
        'categories':categories,
    }

