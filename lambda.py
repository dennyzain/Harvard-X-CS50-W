# define a lambda

people=[
    {"name":"harry","house":"gryffindor"},
    {"name":"mail","house":"bojong"},
    {"name":"atong","house":"babakan"},
    {"name":"alex","house":"sempu"}
]
# def f(person): # must be define a parameter for specific field 
#    return person['house']

# people.sort(key=f) # if you using sort method for sorting dictionary you need a key

# ! you can using code in above for sorting a dict
# ! but if you using a lambda its make you easier

people.sort(key=lambda person: person['name']) # ? we using a lambda function

print(people)
