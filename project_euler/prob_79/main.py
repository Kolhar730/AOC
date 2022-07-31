from collections import defaultdict

attempts = [line.strip() for line in open('keylog').readlines()]
appearances = defaultdict(list)
for attempt in attempts:
    for i, n in enumerate(attempt):
        appearances[n].append(i)

average_positions = {}
for k,v in list(appearances.items()):
    average_positions[k] = float(sum(v))/float(len(v))

a = [k for k,v in sorted(list(average_positions.items()), key=lambda a: a[1])]
print(''.join(str(x) for x in a))
