from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class widget_list:  # Note that parens are optional if not inheriting from another class
  def __init__(self, description, quanity):
    self.description = description
    self.quanity = quanity

# Define the home view
def about(request):
  return render(request,'about.html')