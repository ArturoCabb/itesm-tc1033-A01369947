with open("datos_vuelos.csv","r") as f:
    lines=f.readlines()
    dmp={}
    dmp1={}
    
    for l in lines:
        string=l.split(",")
        pais=string[0][:5]
        mes=string[1][3:5]
        if mes not in dmp:
            dmp[mes]=1
        else:
            dmp[mes]+=1
        if mes not in dmp1:
            dmp1[mes]={}
        elif pais not in dmp1[mes]:
            dmp1[mes][pais]=1
        else:
            dmp1[mes][pais]+=1
print(dmp)
print(dmp1)
d_average={}
file=open("Tarea1.csv","w+")
file.write("Mes,Pais,Porcentaje\n")
for mes in dmp1:
    for pais in dmp1[mes]:
        average=dmp1[mes][pais]/dmp[mes]
        average=average*100
        #add a value in the last key
        if average>=20:
            average=str(average)
            file.write(mes+","+pais+","+average+"\n")
file.close()






        
        
