r = input('enter a string:')
c = ''
for i in range(len(str),0,-1):

    ch = str[i-1]
    c= c+ch

print(c)
if c == str :
    print(str,'is a plindrome')
