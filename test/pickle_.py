import pickle

list = ['a', 'b', 'c']

## Save pickle
with open('data.pickle', 'wb') as f:
    pickle.dump(list, f)

## Load pickle
with open("data.pickle","rb") as fr:
    data = pickle.load(fr)
print(data)