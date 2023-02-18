all_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {2, 4, 6, 8, 10}
# intersection is used to check if theres something common in both variables, it can be used in database
print(all_numbers.intersection(even_numbers))

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item8', 'item2'}
checking_super = st1.isdisjoint(st2)  # True
print(checking_super)
