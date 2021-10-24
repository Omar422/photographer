from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Portfolio

# Create your views here.

def portfolio(request):

    portfolio = Portfolio.objects.all().order_by('-portfolio_date')

    paginator = Paginator(portfolio, 2) # Show 5 work per page.

    page_number = request.GET.get('page')
    page_number = int(page_number) if page_number else page_number
        
    page_obj = paginator.get_page(page_number)

    
    return render(request, 'portfolio/index.html', {
        'portfolio'     :   page_obj,
        'page_number'   :   page_number})