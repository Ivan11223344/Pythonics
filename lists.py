bagpack = ["woter","giroskuter","gun","food"]
vopros = input("лешить еды?")
if vopros == "да" or vopros == "ДА":
    bagpack.pop(1)
print(bagpack)
if vopros == "нет"  or vopros ==  "НЕТ":
    bagpack.pop(0)
    print(bagpack)
bagpack.insert(0,1)
minibagpag = []
bagpack.append(minibagpag)
