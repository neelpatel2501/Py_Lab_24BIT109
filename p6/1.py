def q1():
    l=[('Neel','Sasank'),('Kush',),'Vishwen']
    boys=0
    girls=0
    for i in l:
        if type(i)==tuple:
            if len(i)>1:
                for j in i:
                    boys=boys+1
            else:
                boys=boys+1
        else:
            girls=girls+1
    print(girls,boys)
q1()
