import csv

link0 = []
link1 = []
link2 = []
def nova():
    with open('parsing\second\link_pars.csv', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        results = []
        for row in enumerate(reader):
            results.append(row)


        link0.append(results[0][1]['Ссылка на продукт'])
        print(link0[0])


        link1.append(results[1][1]['Ссылка на продукт'])
        print(link1[0])

        link2.append(results[2][1]['Ссылка на продукт'])
        print(link2[0])

nova()