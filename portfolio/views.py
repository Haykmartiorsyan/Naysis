from django.shortcuts import render
from django.views import generic
from project.models import PortfolioItems, PortfolioCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def listing(request):
        items_count = 6
        items = PortfolioItems.objects.filter(is_active=True).order_by('-created')
        paginator = Paginator(items, items_count)

        page = request.GET.get('page', 1)
        try:
            protfolio_page = paginator.page(page)
        except PageNotAnInteger:
            protfolio_page = paginator.page(1)
        except EmptyPage:
            protfolio_page = paginator.page(paginator.num_pages)

        categoryes = PortfolioCategory.objects.all()

        return render(request, 'portfolio/index.html', {'protfolio_page': protfolio_page, 'categoryes': categoryes})