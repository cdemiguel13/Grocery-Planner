from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    print("hello john")
    return render(request, 'index.html')

# <---Register and Login ---->
# sends to success page with wall
def success(request):
    if 'user' not in request.session:
        return redirect('/')
    context = {
        'wall_messages': Wall_Message.objects.all(),
        'grocery_list': Grocery_List.objects.all(),
        'current_user': User.objects.get(id=request.session['id'])
    }
    return render(request, 'dashboard.html', context)

def logout(request):
    print(request.session)
    request.session.flush()
    print(request.session)
    return redirect('/')
# sends to success page
def register(request):
    print(request.POST)
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    new_user = User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'], password=request.POST['password'])
    request.session['user'] = new_user.first_name
    request.session['id'] = new_user.id
    return redirect('/success')

def login(request):
    print(request.POST)
    logged_user = User.objects.filter(email=request.POST.get('email'))
    print(logged_user)
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if logged_user.password == request.POST['password']:
            request.session['user'] = logged_user.first_name
            request.session['id'] = logged_user.id
            return redirect('/success')
    return redirect('/')

# ------added these render methods, needs functionality
def my_profile(request):
    context = {
        'user': User.objects.get(id=request.session['id'])
    }
    return render(request, 'edit_my_profile.html', context)

def meal_plan(request):
    #needs to pass user's list of recipes
    return render(request, 'meal_plan.html')

def add_recipe(request):
    return render(request, 'add_recipe.html')

def render_edit_recipe(request, recipe_id):
    context = {
        'recipe': Recipe.objects.get(id=recipe_id),
    }
    return render(request, 'edit_recipe.html', context)

# ------------------------------------------

# <---Updating User Information---->
def update_profile(request):
    # needs functionality for updating user info
    return redirect('/update_user_info')

# <---Processing Recipes/Ingredients/MealPlan---->
# these need functionality
def create_ingredient(request):
    return redirect('/add_recipe')

def process_add_recipe(request):
    return redirect('/add_recipe')

def update_recipe(request, recipe_id):
    recipe_to_update = Recipe.objects.get(id=recipe_id)
    # needs updating functionality
    return redirect('/add_recipe')

def remove_ingredient(request, ingredient_id):
    #needs functionality
    return redirect('/add_recipe')

def add_to_meal_plan(request):
    #needs to add to meal database
    return redirect('/meal_plan')


# <---Wall and comments---->
def post_mess(request):
    Wall_Message.objects.create(message=request.POST.get('comment'), poster=User.objects.get(id=request.session['id']))
    return redirect('/success')

def post_comment(request, id):
    poster = User.objects.get(id=request.session['id'])
    message = Wall_Message.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], poster=poster, wall_message=message)
    return redirect('/success')

def profile(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'profile.html', context)

def add_like(request, id):
    liked_message = Wall_Message.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['id'])
    liked_message.user_likes.add(user_liking)
    return redirect('/success')

def destroy(request, id):
    deleted_post = Wall_Message.objects.get(id=id)
    deleted_post.delete()
    return redirect('/success')

def edit_page(request, id):
    context = {
        'edit_mess': Wall_Message.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

def process_edit(request, id):
    mess_edit = Wall_Message.objects.get(id=id)
    mess_edit.message = request.POST['message']
    mess_edit.save()
    return redirect('/success')


# <---- Grocery List --->
def add_item(request):
    Grocery_List.objects.create(item=request.POST['item'], creator=User.objects.get(id=request.session['id']))
    return redirect('/grocery_list')

def remove_item(request,id):
    delete_item = Grocery_List.objects.get(id=id)
    delete_item.delete()
    return redirect('/success')

def grocery_list(request):
    if 'user' not in request.session:
        return redirect('/')
    context = {
        'grocery_list': Grocery_List.objects.all(),
    }
    return render(request, 'grocery.html', context)