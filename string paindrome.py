s = input('enter a string:')
c = ''
for i in range(len(s),0,-1):

    ch = s[i-1]
    c= c+ch

print(c)
if c == s :
    print(s,'is a plindrome')



# def strRev(str):
#     revStr = ''
#     for i in range (len(str),0,-1):
#         ch = str[i-1]
#         revStr = revStr + ch

#     return revStr

# if __name__ == "__main__":
#     str = input('enter aa string:')
#     rs = strRev(str)
#     print('revers of ',str,' is ',rs)

#     if rs == str :
#         print("its a palindrome!")



