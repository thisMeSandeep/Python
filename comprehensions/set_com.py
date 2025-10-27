#get unique values and double them

# lst=[1,2,3,4,1,3,4]

# s={x*2 for x in lst}

# print(s)


#complex exmaple
recipes={
    "cake":{
        "flour":500,
        "sugar":200,
        "eggs":1,
    },
    "pancakes":{
        "flour":300,
        "sugar":150,
        "eggs":2,
        "milk":100,
    },
    "oatmeal":{
        "oats":250,
        "water":200,
        "milk":100,
    }
}

#get unique ingredients

ingredients={item for ingredients in recipes.values() for item in ingredients.keys()}
print(ingredients)

