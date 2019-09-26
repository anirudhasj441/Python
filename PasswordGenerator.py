import random

class PasswordGenerator:

    def __init__(self,len):
        self.len = len

    def geneate(self):

        global password
        smCh = ['a','b','c','d','e','f','i','j','k','l','m','n','o','p','q','q','r','s','t','u','v','w','x','y','z']
        capCh = []
        for x in smCh:
            capCh.append(x.upper())

        sy = ['!','@','#','$','%','&']

        li = [x for x in smCh]
        for i in capCh:
            li.append(i)
        for i in sy:
            li.append(i)
        # print(li)

        pas_li = random.sample(li,self.len)
        passWord = ''
        for i in pas_li:
            passWord += i 
        # print(pas_li)
        return passWord

if __name__ == "__main__":
    obj = PasswordGenerator(8)
    print(obj.geneate())
    

