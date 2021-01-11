def SwapFiles():
    i=input("File1: ")
    o=input("File2: ")
    data1=open(i)
    a=data1.read()
   

    data2=open(o)
    b=data2.read()
    

    w1=open(i,"w")
    w2=open(o,"w")
    w1.write(b)
    w2.write(a)
    
SwapFiles()