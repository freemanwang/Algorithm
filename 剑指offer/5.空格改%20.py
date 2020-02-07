str = 'We are happy.'
def sp2Num(str):
    st = ''
    for ch in str:
        if ch ==' ':
            ch ='%20'
        st+= ch
    return st

print(sp2Num(str))  #We%20are%20happy.