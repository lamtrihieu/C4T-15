book = {
    "name": "Comic",
    "re_year": "20xx",
    "characters":["boy","girl","mom"],
}
# print(book)
book["publisher"] = "FOW studio"
# for k ,v in book.items():
#     print(k,"-",v)

book["characters"] = ["boy","monkey","mc"]
book["characters"].append("tiger")
book["characters"].pop(0)

# print(book)
# print(*book["characters"],sep="\n")
for k,v in book.items():
    print(k,"-",v)








