a_set = {1, 2, 3}
print('Union: ' + str(a_set))
print('Type: ' + str(type(a_set)))
print('Get union from a list: set(a_list)')
print('Creating new list: set()')
a_set.add(4);
a_set.add(1);
print('Adding elements: .add(element) or .update({1, 2, 3, 4}, {1,2,3})')
a_set.update({1, 2, 5, 6, 7, 8})
print('Attention: {} - creating null dictionary')
print('Union: ' + str(a_set))
print('Deleting elements: .discard(element) or .remove(element)')
print('.remove() removes KeyError if no element in list')
print('Methods pop() и clear()')
print('If belong to..: 1 in a_set')
print('Union: union(new_set)')
print('Intersection: intersection(new_set)')
print('Difference: difference(new_set)')
print('Unique: symmetric_difference(new_set)')
print('a_set.issubset(b_set)')
print('a_set.issuperset(b_set)')