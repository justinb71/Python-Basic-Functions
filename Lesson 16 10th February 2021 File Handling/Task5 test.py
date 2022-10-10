from tabulate import tabulate

outputList = dictOfOutputs.items()
table = outputList
print (tabulate.table)

with open('filename.txt', 'w') as outputfile:
    outputfile.write(tabulate(table))
