from collections import namedtuple
n=5
table=namedtuple('table','MARKS CLASS NAME ID')
entries = [
    table(97, 7, 'Calum', 1),
    table(50, 4, 'Scott', 2),
    table(91, 9, 'Jason', 3),
    table(72, 5, 'Glenn', 4),
    table(80, 6, 'Fergus', 5)
]
avg = sum(i.MARKS for i in entries) / n
print(f"{avg:.2f}")