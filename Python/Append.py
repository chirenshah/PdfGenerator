import os
def append(receipe):
    f=open("/home/chiren/Downloads/Python/%s.txt"%receipe,"r")
    if f.mode == 'r':
        a=f.read()
    f.close()
    f=open("/home/chiren/Downloads/Python/Diet.txt","a+")
    f.write(a)
    f.close()

def test():
    append("Mango-Chutney")

def test2():
    append("Brown rice Biryani")
    
