from django.shortcuts import render



def starting_page(request):
    return render(request, "blog/home_page.html")



def posts(request):
    return render(request, "blog/post_list.html")



def post_detail(request):
    return render(request, "blog/post_detail.html")


