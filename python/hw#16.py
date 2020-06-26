s1 = "abeeecdabec"
s2 = "abc"
def fine(s1,s2):
    out = s1
    tmp = s2
    t2 = ""
    mode = 0
    num = 0
    for c in s2:
        num += s1.count(c)
    for n in range(num):
        for c in range(len(s1)):
            if s2.count(s1[c]) > 0:
                n -= 1
            if n == -1:
                cur = s1[c:]
                break
        for i in cur:
            if tmp.count(i) > 0:
                mode = 1
                tmp = tmp.replace(i,'')
            if mode:
                t2 += i
            if not tmp:
                out = t2 if len(t2) < len(out) else out
                t2 = ""
                break
        tmp = s2
    return out
print(fine(s1,s2))
