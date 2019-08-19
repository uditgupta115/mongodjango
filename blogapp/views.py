
import datetime
import io

from django.http import FileResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas

from .models import Post


# Create your views here.


def index(request):
    posts = Post.objects

    if request.method == 'POST':
        # save new post
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post(title=title)
        post.last_update = datetime.datetime.now()
        post.content = content
        post.save()
        return render(request, 'create.html', {'posts': posts})

    if request.method == 'GET':
        return render(request, 'create.html', {'posts': posts})


def update(request):
    if request.method == 'POST':
        # update post
        ids = request.POST.get('id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post(id=ids)
        post.update(title=title, content=content)
        post.last_update = datetime.datetime.now()
        post.save()

    if request.method == 'GET':
        posts = Post.objects
        return render(request, 'update.html', {'posts': posts})


def delete(request):
    if request.method == 'POST':
        ids = request.POST.get('id')
        post = Post(id=ids)
        post.last_update = datetime.datetime.now()
        post.delete()
        posts = Post.objects
        return render(request, 'delete.html', {'posts': posts})

    if request.method == 'GET':
        posts = Post.objects
        return render(request, 'delete.html', {'posts': posts})


def detail(request, blog_id):
    # blog_id = request.GET.get('id')
    posts = Post.objects
    post = posts.get(id=blog_id)

    return render(request, 'detail.html', {
        'posts': posts,
        'post': post
    })


def pdf_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
