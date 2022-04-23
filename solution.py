# code jam 2021 problem C interactive problem

import sys


#this function return the fisrt tower with the length passed in parameters
def key_from_len(length, towers):

    for k,v in towers.items():
        if len(v) == length:
            return k


#compute the score of a tower from the blocks inside it
def tower_score(tower):

    return "".join(list(map(str, tower))) if tower != [] else '0'

def compute_score(towers):
    sc = 0
    for k,v in towers.items():
        sc += int(tower_score(v))
        
    return sc


#place a block on the highest tower with the length < B-2
#we do it to reserve the top 2 positions for 8s and 9s
def placemin(D, towers, N, started, B):
    tmplen = [len(u) for u in towers.values() if len(u)<B-2]
    if started == 0:
        return 1

    elif len(tmplen) != 0:
        minlength = max(tmplen)
        ind_tower = key_from_len(minlength, towers)
        
        return ind_tower+1
    
    else:
        return place(D, towers, N, B)


#this function place a block on thez highest unfinished tower
# we do it for 8s and 9s digits
def placetall(D, towers, N, started):
    if started == 0:
        return 1
        
    else:
        maxlength = max([len(u) for u in towers.values() if len(u)<B])
        ind_tower = key_from_len(maxlength, towers)
        
        return ind_tower+1

#this function  places a block on the first unfinished tower
def place(D, towers, N, B):

    building = towers.copy()
    for i in range(N):
        if len(towers[i]) < B:
            indice = i
            break
            
    return indice+1




if __name__ == "__main__":
    T, N, B, P = list(map(int, input().split()))

    for t in range(T):
        #we create a dico that will store the state of our towers
        towers = {k:[] for k in range(N)}
        started = 0 #the number of blocks already placed
        cpt = 0
        D = 0
        while cpt < N * B:
            D = int(input())
            if D != -1:
                #index_tower = place(D, towers, N, B)
                index_tower = placemin(D, towers, N, started, B) if D in range(8) else placetall(D, towers, N, started)
                towers[index_tower-1].insert(0,D)
                cpt += 1
                print(index_tower)
                #print(towers)
                sys.stdout.flush()
            else:
                sys.exit()
            started += 1
        
        #print("score : ", compute_score(towers))

    sys.exit()