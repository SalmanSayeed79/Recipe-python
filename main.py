import requests
import json
import webbrowser

#======================================SEARCHING BY NAMES========================================
#doing the json work




    #creating functions for each of the buttons



def Button_1():
    def Ingredients_1():
        empty_label=Label(window_1).grid(column=0,row=1)
        empty_label = Label(window_1).grid(column=0, row=2)
        ingredient_title_label = Label(window_1,text="INGREDIENTS").grid(column=0, row=3)
        empty_label = Label(window_1).grid(column=0, row=4)
        p=5
        print(get_ingredients(id_1))
        for i in ingredients_list:
            ingredient_label_1 = Label(window_1, text=i,padx=50).grid(column=0, row=p, columnspan=1)
            p+=1

    window_1=Toplevel()
    window_1.title('Button 1')
    window_1.geometry('1000x750')
    window_1.configure(bg='red')
    window_1.iconbitmap('1.ico')

    # making the title bar for the window
    title_frame_1 = Frame(window_1, bg='white', width=1000, height=100).grid(row=0, column=0, columnspan=5)

    # making the buttons for the title bar
    ingredients_1 = Button(window_1, text="Ingredients", command=Ingredients_1)
    ingredients_1.grid(column=0, row=0)
    instructions_1 = Button(window_1, text="Instructions")
    instructions_1.grid(column=1, row=0)



def Button_2():
    window_2=Toplevel()
    window_2.title('Button 1')
    window_2.geometry('1000x750')
    window_2.configure(bg='red')
    window_2.iconbitmap('1.ico')

def Button_3():
    window_3=Toplevel()
    window_3.title('Button 1')
    window_3.geometry('1000x750')
    window_3.configure(bg='red')
    window_3.iconbitmap('1.ico')
def Button_4():
    window_4=Toplevel()
    window_4.title('Button 1')
    window_4.geometry('1000x750')
    window_4.configure(bg='red')
    window_4.iconbitmap('1.ico')
def Button_5():
    window_5=Toplevel()
    window_5.title('Button 1')
    window_5.geometry('1000x750')
    window_5.configure(bg='red')
    window_5.iconbitmap('1.ico')
def Button_6():
    window_6=Toplevel()
    window_6.title('Button 1')
    window_6.geometry('1000x750')
    window_6.configure(bg='red')
    window_6.iconbitmap('1.ico')
def Button_7():
    window_7=Toplevel()
    window_7.title('Button 1')
    window_7.geometry('1000x750')
    window_7.configure(bg='red')
    window_7.iconbitmap('1.ico')
def Button_8():
    window_8=Toplevel()
    window_8.title('Button 1')
    window_8.geometry('1000x750')
    window_8.configure(bg='red')
    window_8.iconbitmap('1.ico')
def Button_9():
    window_9=Toplevel()
    window_9.title('Button 9')
    window_9.geometry('1000x750')
    window_9.configure(bg='red')
    window_9.iconbitmap('1.ico')
def Button_10():
    window_10=Toplevel()
    window_10.title('Button 10')
    window_10.geometry('1000x750')
    window_10.configure(bg='red')
    window_10.iconbitmap('1.ico')






def get_id():
#==================================================================================================#
#    |   What we're gonna do in this function:
#    |      1.Request for the title and id according to the item we want to find
#    |      2.Save the titles in a separate global list and the ids in another separate global list
#    |      3.We'll also have to make all the ids global
#==================================================================================================#

    main_url='https://api.spoonacular.com/recipes/search?'

    print("Enter the food you want the recipe for: ")

#defining the parameters
    global INPUT
    global ingredients_list
    INPUT=entry1.get()
    parameters={}
    parameters['apiKey']='0d4dc550de91495482c8dfd2a3a0e27e'
    parameters['number']=10
    parameters['query']=INPUT
    parameters['instructionsRequired']=True

    item_request=requests.get(main_url,params=parameters)
    item_json=item_request.json()


    #getting the url and clicking the url in our desired browser
    p=8
    title_list=[]
    id_list=[]
    for i in item_json['results']:

        title=i['title']
        print(title)
        print('==============================================================================')
        url_recipe=i['sourceUrl']
        id=i['id']
        image=i['image']
        #webbrowser.open_new_tab(url_recipe)

        #creating lists for titles and ids
        title_list.append(title)
        id_list.append(id)


    print(title_list)
    print(id_list)


    #making all the ids global
    global id_1
    global id_2
    global id_3
    global id_4
    global id_5
    global id_6
    global id_7
    global id_8
    global id_9
    global id_10
    id_1=id_list[0]
    id_2=id_list[1]
    id_3=id_list[2]
    id_4=id_list[3]
    id_5=id_list[4]
    id_6=id_list[5]
    id_7=id_list[6]
    id_8=id_list[7]
    id_9=id_list[8]
    id_10=id_list[9]


#creating the buttons
    button_1=Button(root,text=title_list[0],font="Cambria",command=Button_1,width=75).grid(column=1,row=8)
    button_2 = Button(root, text=title_list[1], font="Cambria",command=Button_2,width=75).grid(column=1, row=9)
    button_3 = Button(root, text=title_list[2], font="Cambria",command=Button_3,width=75).grid(column=1, row=10)
    button_4 = Button(root, text=title_list[3], font="Cambria",command=Button_4,width=75).grid(column=1, row=11)
    button_5 = Button(root, text=title_list[4], font="Cambria",command=Button_5,width=75).grid(column=1, row=12)
    button_6 = Button(root, text=title_list[5], font="Cambria",command=Button_6,width=75).grid(column=1, row=13)
    button_7 = Button(root, text=title_list[6], font="Cambria",command=Button_7,width=75).grid(column=1, row=14)
    button_8 = Button(root, text=title_list[7], font="Cambria",command=Button_8,width=75).grid(column=1, row=15)
    button_9 = Button(root, text=title_list[8], font="Cambria",command=Button_9,width=75).grid(column=1, row=16)
    button_10 = Button(root, text=title_list[9], font="Cambria",command=Button_10,width=75).grid(column=1, row=17)
def get_ingredients(id):
# ==================================================================================================#
#    |   What we're gonna do in this function:
#    |      1.Take the respective ids as an arguement and get the ingredients of that recipe
#    |      2.Print the ingredients in an intuitive manner
# ==================================================================================================#


    ###============================Ingredients
    # when we press the button of an item, make another window pop-up
    # This window will have two buttons
    print('=====INGREDIENTS=====')
    main_url = 'https://api.spoonacular.com/recipes/{}/information?apiKey=20da25c69ae5442cab091cba87b91f0a&includeNutrition=true'.format(
        id)
    ingredient_request = requests.get(main_url)
    ingredient_json = ingredient_request.json()
    ingredients = ingredient_json['nutrition']['ingredients']

    ingredients_list = []
    for i in ingredients:
        item = i['name'] + '  ' + str(i['amount']) + ' ' + str(i['unit'])
        print(i['name'] + '  ' + str(i['amount']) + ' ' + str(i['unit']))
        ingredients_list.append(item)
    print('-------------------------------------------------------------------------------------')

    # we need to create a list for each items in the ingredients list
    print(ingredients_list)
    #we're gonna use this list to print out the stuff in it
def get_instructions(id):
    # ==============================Instruction===========
    main_url = 'https://api.spoonacular.com/recipes/{}/information?apiKey=20da25c69ae5442cab091cba87b91f0a&nutritionWidget.json'.format(id)
    # print(main_url)
    full_json = requests.get(main_url).json()
    # print(full_json)
    instructions = full_json['instructions']
    splitted_instructions=instructions.split('.')
    for i in splitted_instructions:
        print(i)
    print(
        '======================================================================================================================================================================')
    print(instructions)


















#================================Building the gui======================================================
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Recipo")
root.iconbitmap('1.ico')
root.geometry('1000x750')
root.resizable(False,False)
root.configure(bg='#DBAAC6')

#creating the header part
frame1=Frame(root,width=1000,height=100,bg='white').grid(column=0,row=0,columnspan=5)
label1=Label(root,text='Recipe',bg='white',font=("Cambria",25)).grid(row=0,column=0)
empty_label=Label(root,bg='#DBAAC6').grid(column=1,row=1)
empty_label=Label(root,bg='#DBAAC6').grid(column=1,row=2)

#creating the entry label
label_entry1=Label(root,bg='#DBAAC6',text="Enter the type of food you want: ",font=("Cambria",11)).grid(row=3,column=0)
entry1=Entry(root,width=120)
entry1.grid(row=3,column=1)
empty_label=Label(root,bg='#DBAAC6').grid(column=1,row=4)

#creating the button
button1=Button(root,text="GO!!",bg='#DBAAC6',padx=20,pady=15,font=("Cambria",10),command=get_id).grid(column=1,row=5)
empty_label=Label(root,bg='#DBAAC6').grid(column=1,row=6)
empty_label=Label(root,bg='#DBAAC6').grid(column=1,row=7)
#enter the 10 buttons for each of the options



root.mainloop()


