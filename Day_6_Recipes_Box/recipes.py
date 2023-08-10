from pathlib import Path

base = Path.cwd().resolve()
current = Path(base, 'Recipes')

def intro():
    
    print(f"Hello, to find our recipes please visit the following path {current}")
    print(f"In this folder you will find the following categories along with how may recipes are in each!")
    for folder in current.glob('*'):
        txt_files = []
        for file in folder.glob('*.txt'):
            txt_files.append(file)
        print(f"{folder.name}: {len(txt_files)}")
    choice()
    
def choice():
    function_map = {
    '1': choose_category,
    '2': create_recipe,
    '3': create_category,
    '4': delete_recipe,
    '5': delete_category,
    '6': end
    }
    choice = input("""Which option would you like to choose?
        1. Choose a category
        2. Create recipe
        3. Create category
        4. Delete recipe
        5. Delete category
        6. End 
        """)

    selected_choice = function_map.get(choice)
    if selected_choice:
        selected_choice()
    else:
        print("Invalid choice")
        choice()

def choose_category():
    recipe_list = []
    category = input("Which category do you choose? ")
    category_path = Path(current, category)
    for recipe in category_path.glob("*.txt"):
        print(recipe.stem)
        recipe_list.append(recipe.stem)
    recipe = input("Which recipe do you want to read? ")
    if recipe in recipe_list:
        txt = recipe + ".txt"
        read_recipe = Path(category_path, txt)
        selection = read_recipe.read_text()
        print(selection)
        choice()
    else:
        "That recipe does not exist. Please try again"
        choose_category()

def create_recipe():
    recipe_category = input("Which Category does your category belong? ")
    recipe_create = input("What is your recipe called? ")
    recipe_contents = input("Please write the recipe? ")
    recipe_create_txt = recipe_create + ".txt"
    new_file = current / recipe_category / recipe_create_txt
    new_file.touch
    new_file.write_text(recipe_contents)
    print("Recipe has been added")
    choice()

def create_category():
    new_category = input("What is your new category name?")
    category_path = Path(current, new_category)
    category_path.mkdir()
    print("Category has been added!")
    choice()

def delete_recipe():
    recipe_category = input("Which Category does your category belong? ")
    recipe_create = input("What is your recipe called? ")
    recipe_create_txt = recipe_create + ".txt"
    new_file = current / recipe_category / recipe_create_txt
    new_file.unlink()
    print("Recipe has been deleted")
    choice()

def delete_category():
    category = input("What is your category name?")
    category_path = Path(current, category)
    category_path.rmdir()
    print("Category has been deleted!")
    choice()

def end():
    return

intro()