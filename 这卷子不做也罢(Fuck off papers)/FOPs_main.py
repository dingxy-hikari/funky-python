import random as rd

listing = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', ]
outputing = ''
ct = 0
# times = int(input('times'))

while True:
    for i in range(0, 15):
        if ct == 5:
            outputing += ' '
            ct = 0
        selected = rd.randint(1, len(listing)) - 1
        t = listing[selected]
        del (listing[selected])
        outputing += t
        ct += 1
        i += 1

    selected = 0
    ct = 0
    print(outputing)
    outputing = ''
    listing = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', ]
    input('再生成')