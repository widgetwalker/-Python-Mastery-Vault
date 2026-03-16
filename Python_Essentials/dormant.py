import pickle as sam
dot={"terence":"flipkart","witcher":"dungeons and dragons","carter":"magician's manual"}
dot1=["duration","accuracy","speed","skill","mastery"]
dormant=open("dor.dat","wb+")
sam.dump(dot,dormant)
sam.dump(dot1,dormant) 
dormant.seek(0)
scream=sam.load(dormant)
s1=sam.load(dormant)
dormant.close()
print(scream,"\n ",s1)
