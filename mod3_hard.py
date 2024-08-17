def calculate_structure_sum(*data_):
    cal = 0
    for i in data_:
        if isinstance(i, (int, float)):
            cal += i
        elif isinstance(i, str):
            cal += len(i)
        elif isinstance(i, dict):
            cal += calculate_structure_sum(*i.items())
        elif isinstance(i, (list, tuple, set)):
            cal += calculate_structure_sum(*i)
    return cal

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
