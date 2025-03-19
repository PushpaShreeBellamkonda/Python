from collections import OrderedDict
ordered_dict= OrderedDict()
N=9
ordered_dict['BANANA FRIES']=12
ordered_dict['POTATO CHIPS']=ordered_dict.get('POTATO CHIPS',0)+30
ordered_dict['APPLE JUICE']=ordered_dict.get('APPLE JUICE',0)+10
ordered_dict['CANDY']=ordered_dict.get('CANDY',0)+5
ordered_dict['APPLE JUICE']=ordered_dict.get('APPLE JUICE',0)+10
ordered_dict['CANDY']=ordered_dict.get('CANDY',0)+5
ordered_dict['CANDY']=ordered_dict.get('CANDY',0)+5
ordered_dict['CANDY']=ordered_dict.get('CANDY',0)+5
ordered_dict['POTATO CHIPS']=ordered_dict.get('POTATO CHIPS',0)+30
for item, price in ordered_dict.items():
    print(item, price)


# METHOD-2


from collections import OrderedDict

ordered_dict = OrderedDict()
N = 9  # Number of items

# List of items (simulating input)
items = [
    ('BANANA FRIES', 12),
    ('POTATO CHIPS', 30),
    ('APPLE JUICE', 10),
    ('CANDY', 5),
    ('APPLE JUICE', 10),
    ('CANDY', 5),
    ('CANDY', 5),
    ('CANDY', 5),
    ('POTATO CHIPS', 30),
]

# Populating the OrderedDict and accumulating values
for item, price in items:
    ordered_dict[item] = ordered_dict.get(item, 0) + price

# Printing the output in the expected format
for item, price in ordered_dict.items():
    print(item, price)
