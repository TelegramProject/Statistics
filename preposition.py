from matplotlib import pyplot as plt

f = open('articles.txt')

inC = 0
on = 0
to = 0
at = 0
of = 0
forC = 0
by = 0
prepositions = ['in', 'on', 'to', 'at', 'of', 'for',  'by']


def findPreposition(line):
    global inC
    global on
    global to
    global at
    global of
    global forC
    global by
    lst = line.split()

    for s in lst:
        if s == 'in':
            inC += inC + 1
        elif s == 'on':
            on += on + 1
        elif s == 'to':
            to += to + 1
        elif s == 'at':
            at += at + 1
        elif s == 'of':
            of += of + 1
        elif s == 'for':
            forC += forC + 1
        elif s == 'by':
            by += by + 1


for line in f:
    findPreposition(line)

countPreposition = [inC, on, to, at, of, forC, by]
xs = [i + 0.1 for i, _ in enumerate(prepositions)]

plt.bar(xs, countPreposition)

plt.ylabel('Количество предлогов в тексте')

plt.xticks([i + 0.5 for i, _ in enumerate(prepositions)], prepositions)
plt.show()
