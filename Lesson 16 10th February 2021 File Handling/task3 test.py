text_file = open("Text//Task5_Price.txt", 'r')
text = text_file.read()
words = text.split()
words = [word.strip('£') for word in words]
prices = []
for word in words:
    if word not in prices:
        prices.append(word)

prices.sort()
prices = prices[1:6]
res = [int(i) for i in prices]
res.sort()
res = res[0:4]
for x in res:
    print(x, end="\n")

text_file.close()

