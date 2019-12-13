from matplotlib import pyplot as plt

f = open('articles.txt')
theCounter = 0
aCounter = 0
anCounter = 0


def countThe():
    global theCounter
    lst = line.split()
    var = theCounter

    for s in lst:
        if s == 'the':
            var += theCounter + 1

    return var


def countA():
    global aCounter
    lst = line.split()
    var = aCounter

    for s in lst:
        if s == 'a':
            var += aCounter + 1

    return var


def countAn():
    global anCounter
    lst = line.split()
    var = anCounter

    for s in lst:
        if s == 'an':
            var += anCounter + 1

    return var


for line in f:
    theCounter = countThe()
    aCounter = countA()
    anCounter = countAn()


articles = ["the", "a", "an"]
countArticles = [theCounter, aCounter, anCounter]

xs = [i + 0.1 for i, _ in enumerate(articles)]

plt.bar(xs, countArticles)

plt.ylabel('Количество артиклей в тексте')

plt.xticks([i + 0.5 for i, _ in enumerate(articles)], articles)
plt.show()
