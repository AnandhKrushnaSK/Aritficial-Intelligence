a=8  #Max Capacity of jar1
b=5  #Max Capacity of jar2
c=3  #Max Capacity of jar3
initial= (8,0,0)
parent={}
explored={}
goal=[]

def goal_state(s):
    if(s[0]==4 or s[1]==4):
        #print(s," is goal state")
        return True
    else:
        return False

def next_state(s):
    x=s[0]
    y=s[1]
    z=s[2]
    successor=[]
    if(x>0): #1st jar can be poured
        if(x+y>b): #1st to 2nd Jar, 2nd jar is fulled
            successor.append(((x+y-b),b,z))
        else: #1st to 2nd jar, 1st jar is emptied
            successor.append((0,(x+y),z))
        if(x+z>c): #1st to 3rd jar, 3rd jar is filled
            successor.append(((x+z-c),y,c))
        else: #1st to 3rd jar, 1st jar is emptied
            successor.append((0,y,(x+z)))
    if(y>0): #2nd jar can be poured
        if(y+x>a): #2nd to 1st Jar, 1st jar is fulled
            successor.append((a,(x+y-a),z))
        else: #2nd to 1st jar, 2nd jar is emptied
            successor.append(((x+y),0,z))
        if(y+z>c): #2nd to 3rd jar, 3rd jar is filled
            successor.append((x,(y+z-c),c))
        else: #2nd to 3rd jar, 2nd jar is emptied
            successor.append((x,0,(y+z)))
    if(z>0): #3rd jar can be poured
        if(x+z>a): #3rd to 1st Jar, 1st jar is fulled
            successor.append((a,y,(x+z-a)))
        else: #3rd to 1st jar, 3rd jar is emptied
            successor.append(((x+z),y,0))
        if(y+z>b): #3rd to 2nd jar, 2nd jar is filled
            successor.append((x,b,(y+z-b)))
        else: #3rd to 2nd jar, 3rd jar is emptied
            successor.append((x,(y+z),0))
    return successor


def path(end):
    current=end
    order=[]
    order.append(end)
    while(current!=initial):
        order.append(parent[current])
        current=parent[current]
    #As path is found in reverse order, reverse the path found
    order_reversed=order[::-1]
    return order_reversed


def bfs(initial):
    q=[]
    q.append(initial)
    explored[initial]=1
    parent[initial]=(0,0,0)
    while(len(q)!=0):
        popped=q.pop(0)
        if(goal_state(popped)):
            print("\nGoal State:",popped)
            print("Path is") 
            order=path(popped)
            for i in order:
                print(i)
            goal.append(popped)
            
        successor=next_state(popped)
        for i in successor:
            if i not in explored.keys():
                explored[i]=1
                parent[i]=popped
                q.append(i)
##        for i in explored:
##            print((i,explored[i]))
##        print("break")

def main():
    #print(next_state((5,0,3)))
    print("Initial State:",initial)
    print("Maximum Limit of Jars:",[a,b,c])
    bfs(initial)
    print("\nNumber of states explored:",len(explored))
    print("Explored States are:",[i for i in explored.keys()])
    print("Goal States found are:",goal)
    
    

if __name__=="__main__":
    main()
