book = {
    "name" : "SGK",
    "seller":"Nha nc"
}
# book["content"] = "education"
print (book)
input_key = input("Key:")
input_value = input("Value:")
book[input_key] = input_value
print ("Keys :",*book.keys())
print ("Values :",*book.values())