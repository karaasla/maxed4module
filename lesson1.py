'''
def strcounter(s):
    for i in set(s):
        c = 0
        for ss in s:
            if ss == i:
                c += 1
        print(i, '-', c)
strcounter('aasdfgddffgghhg')'''

'''def superc(s):
    sc = {}
    for i in s:
        sc[i] = sc.get(i, 0) + 1
    for i, c in sc.items():
        print(i, '-', c)

superc('addddsffggggfddssas' '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')'''



def palind(s):
    c = 0
    for i in range(len(s)//2):
        if s[i] == s[-(i+1)]:
            c += 1
    if c == len(s)//2:
        return True
    else:
        return False


print(palind('лепсспел'))