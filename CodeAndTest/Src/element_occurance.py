def delete_nth(order, max_e):
    new_order = []
    for i in order:
        if new_order.count(i) != max_e:
            new_order.append(i)
    return new_order

print delete_nth([20,37,20,21], 1)
print delete_nth([1,1,3,3,7,2,2,2,2], 3)
print delete_nth([1,1,1,1],2)