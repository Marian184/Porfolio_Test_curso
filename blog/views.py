from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.
def allblogs(request):
    blog = Blog.objects.all
    return render(request, 'blog/allblogs.html',{'blogs' :blog})

def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id) #pk es primary key
    return render(request, 'blog/detail.html', {'blog':detail_blog})