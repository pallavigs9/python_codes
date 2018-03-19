from collections import OrderedDict

ItemList = OrderedDict()
nooflines = int(raw_input(''))

for i in range(nooflines):
    line = raw_input().split()
    item, price = ' '.join(line[:-1]), int(line[-1])
    price2 = int(price)
    if item not in ItemList:
        ItemList.update({item : int(price)})
    else:
        #print item, ItemList.get(item)
        ItemList.update({item: ItemList.get(item) + price2})

for k, v in ItemList.items():
    print k, v


