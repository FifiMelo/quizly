

result = 0
exec("d = {'a': 1, 'b': 2, 'c': 3}\nd['d'] = d.pop('a') + d.get('b', 0) + d.pop('c') \nresult = d")
print(result)