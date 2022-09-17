from django.shortcuts import render

posts = [
  {
    'author': 'AdrianM',
    "title": "Blog Post 1",
    "content": "First post",
    "date_posted": "17.07.22"
  },
    {
    'author': 'MM',
    "title": "Blog Post 2",
    "content": "Second post",
    "date_posted": "17.09.22"
  }
]

# Create your views here.
def home(request):
  context = {
    "posts": posts
  }
  return render(request, "blog/home.html", context)

def about(request):
  return render(request, "blog/about.html", {"title": "About"})