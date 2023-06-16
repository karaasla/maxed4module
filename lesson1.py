'''
def strcounter(s):
    for i in set(s):
        c = 0
        for ss in s:
            if ss == i:
                c += 1
        print(i, '-', c)
strcounter('aasdfgddffgghhg')'''

def superc(s):
    sc = {}
    for i in s:
        sc[i] = sc.get(i, 0) + 1
    for i, c in sc.items():
        print(i, '-', c)

superc('addddsffggggfddssas')