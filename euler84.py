#/usr/bin/python


from random import choice,shuffle
def tirage(nbre=2,faces=4):
    des=[]
    for i in range(nbre):
        des.append(choice(range(faces))+1)
    return des

if __name__=='__main__':
    caisse=range(16)
    chance=range(16)
    

    shuffle(caisse)
    shuffle(chance)

    print caisse,chance

    max=1000000
    tour=0
    case_courante=0
    doubles=0
    visites=[0]*40
    print len(visites)
    C_CHANCE=(7,22,36)
    C_COMM=(2,17,33)
    while tour < max:
        tour += 1
        des=tirage(2,20)
        if des[0]==des[1]: doubles += 1
        else: doubles=0
        
        if doubles==3:
            case_courante=10

        depl=des[0]+des[1]

        tmp=(case_courante+depl)%40
        if tmp in C_CHANCE:
            ## print "Tirage CHANCE"
            c_c=chance[0]
            chance=chance[1:]
            chance.append(c_c)
            if c_c==1:       ## case depart
                case_courante=0
            elif c_c==2: ## allez en prison
                case_courante=10
            elif c_c==3: ## ## bd de la villette
                case_courante=11
            elif c_c==4: ## Matignon
                case_courante=24
            elif c_c==5: ## rue de la paix
                case_courante=39
            elif c_c==6: ## gare st lazare
                case_courante=5
            elif c_c==7 or c_c==8:
                if tmp == 36: case_courante=5
                elif tmp==22: case_courante=25
                else: case_courante=15
            elif c_c==9:
                if tmp == 36: case_courante=12
                elif tmp==22: case_courante=28
                else: case_courante=12
            elif c_c==10:
                if tmp == 36:
                    if caisse[0]==0:
                        case_courante=0
                    elif caisse[0]==1:
                        case_courante=10
                    caisse.append(caisse[0])
                    caisse = caisse[1:]

                elif tmp==22: case_courante=19
                else: case_courante=4
            else:
                case_courante=tmp
                    
            ###print "tirage CHANCE"
        elif tmp in C_COMM:
            if caisse[0]==0:
                case_courante=0
            elif caisse[0]==1:
                case_courante=10
            else:
                case_courante=tmp
            caisse.append(caisse[0])
            caisse = caisse[1:]
            ##print 'tirage COMM'
        elif tmp==30:
            case_courante=10
        else:
            case_courante=tmp

        visites[case_courante]+=1
        #print case_courante,visites[case_courante]
    print visites
    ## je sort les trois plus grande valeur
    un,deux,trois=0,0,0
    for i in range(len(visites)):
        if visites[i]>un:
            
            trois=deux
            deux=un
            un=visites[i]
            continue
        if visites[i]>deux:
            trois=deux
            deux=visites[i]
            continue
        if visites[i]> trois:
            trois=visites[i]

    print visites.index(un),un,visites.index(deux),deux,visites.index(trois),trois
