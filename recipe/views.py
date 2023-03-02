from django.shortcuts import render,redirect
from .models import Recipe
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.
def home(request):
    recipes=Recipe.objects.filter().order_by('-id')
    return render(request,'app/home.html',{"recipes":recipes})

def recipe_detail(request,id):
    recipe=Recipe.objects.get(id=id)
    isSameUser=recipe.author==request.user
    return render(request,'app/recipe_detail_view.html',{"recipe":recipe,'isSameUser':isSameUser})

def create_recipe(request):
    try:
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            ingredients = request.POST.get('ingredients')
            steps = request.POST.get('steps')
            image = request.FILES.get('image')
            Recipe.objects.create(title=title,author=request.user,description=description,ingredients=ingredients,steps_to_make=steps,image=image)
            messages.success(request,"Successfully Posted!!!")
            return redirect('/')
        else:
            return render(request,'app/recipe_create.html')
    except Exception as e:
        messages.error(request,"Something went wrong!!!")
        return redirect('/')
    
def edit_recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id,author=request.user)
        if request.method == 'POST':
            # Update the recipe with the new data
            recipe.title = request.POST.get('title')
            recipe.description = request.POST.get('description')
            recipe.ingredients = request.POST.get('ingredients')
            recipe.steps_to_make = request.POST.get('steps')
            if 'image' in request.FILES:
                recipe.image = request.FILES.get('image')
            recipe.save()
            # Redirect the user back to the recipe detail page
            return redirect('recipe_detail', id=recipe_id)
        else:
            return render(request,'app/edit_recipe.html',{"recipe":recipe})
    except Exception as e:
        messages.error(request,"Something went wrong!!!")
        return redirect('/')
    
def search(request):
    query = request.GET.get('search')
    if query:
        recipes = Recipe.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(ingredients__icontains=query))
    else:
        recipes = Recipe.objects.all()

    context = {
        'query': query,
        'recipes': recipes,
    }

    return render(request, 'app/search_results.html', context)