import json, csv

with open('indian_banks.csv') as fil:

    a = csv.reader(fil, delimiter=',')
    f = []
    d = next(a)
    l = 0
    for i in a:
        # print(i)
        c = {
            'model': 'app.banks',
            'pk': l,
            'fields': { d[k]:i[k] for k in range(len(i)) }
        }
        f.append(c)
        l = l + 1

    with open('indian_banks.json', 'w') as lo:
        lo.write(json.dumps(f))