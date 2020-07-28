import requests
import json
import webbrowser

main_url='https://api.spoonacular.com/recipes/findByIngredients?'

print("Enter the food you want the recipe for: ")

#defining the parameters
parameters={}
parameters['apiKey']='20da25c69ae5442cab091cba87b91f0a'
parameters['number']=5
parameters['ingredients']=input()


file=requests.get(main_url,params=parameters)
file=file.json()
#print(file.url)
#print(file.json())
p=0
#getting the url and clicking the url in our desired browser

for i in file:

    print(file[p]['title'])
    print('==========================================================================================')
    id=file[p]['id']
    #url_recipe=file[p]['sourceUrl']
    #webbrowser.open_new_tab(url_recipe)
    p += 1




    # defining the parameters

    ###============================Ingredients
    print('=====INGREDIENTS=====')
    main_url='https://api.spoonacular.com/recipes/{}/information?apiKey=20da25c69ae5442cab091cba87b91f0a&includeNutrition=true'.format(id)
    ingredient_request=requests.get(main_url)
    ingredient_json=ingredient_request.json()
    ingredients=ingredient_json['nutrition']['ingredients']
    for i in ingredients:
        print(i['name']+'  '+str(i['amount'])+' '+str(i['unit']))
    print('-------------------------------------------------------------------------------------')
