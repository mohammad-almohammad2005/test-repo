def au_marché(type, saison):
    if type=='fruits' and saison=='hiver':
        print("orange,mandarineetkiwi")
    
    elif type=='fruits' and saison=='ete':
        print("poire,fraiseetcassis")
    
    elif type=='légume' and saison=='hiver':
        print("carotte,topinambour,endive")
    
    elif type=='légume' and saison=='ete':
        print("artichaut,aubergine,navet")
    else:
       
        print("erreur")

au_marché("fruits","ete")

print(au_marché)