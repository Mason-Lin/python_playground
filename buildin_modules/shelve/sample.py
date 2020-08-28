import shelve

shelf = shelve.open("fruit.db")
print(shelf["apple"])

shelf["apple"] = (1, 2, 3)
shelf.sync()
shelf.close()
