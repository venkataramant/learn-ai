import numpy as np
import matplotlib.pyplot as plt
import math

def show_3d_vector(vects,colors):
    
    ax=plt.figure().add_subplot(projection='3d')
    index=0
    for vect in vects:
        index+=1
        ax.scatter(xs=vect[0],ys=vect[1],zs=vect[2],zdir='z',label=f'Vect{index}')
        ax.quiver(0,0,0,vect[0],vect[1],vect[2],color=colors[index-1],arrow_length_ratio=0.1)
    # Origin
    ax.scatter(xs=0,ys=0,zs=0,zdir='z',label='Origin', c='black')

    
    #Make legend, set axes limits and labels
    ax.legend()
    ax.set_xlim(0,150)
    ax.set_ylim(0,150)
    ax.set_zlim(0,150)
    ax.set_xlabel("X")
    ax.set_xlabel("Y")
    ax.set_xlabel("Z")

    # View Angle
    ax.view_init(elev=20.,azim=-35,roll=0)
    plt.show()


def manhattan_distance(vect1,vect2):
    l1=[vect1[i]-vect2[i] for i in range(len(vect1))]
    ans=np.abs(l1).sum()
    print(l1,ans)
    return ans


def l1_distance_manhattan(vect1,vect2):
    ar1=np.array(vect1)
    ar2=np.array(vect2)
    ans= np.linalg.norm((ar1-ar2),ord=1)
    print(ans)
    return ans
def l2_distance_euclidean(vect1,vect2):
    ar1=np.array(vect1)
    ar2=np.array(vect2)
    ans= np.linalg.norm((ar1-ar2),ord=2)
    print(ans)
    return ans

def euclidean_distance(vect1,vect2):
    ed_value=None
    squares=[ (vect1[index]-vect2[index])**2 for index in range(len(vect1))]
    ed_value=np.sqrt(np.array(squares).sum())
    print(squares,ed_value)
    return ed_value


def cosine(vect1,vect2):
    ar1=np.array(vect1)
    ar2=np.array(vect2)
    ans= np.dot(ar1,ar2)/(np.linalg.norm(ar1)*np.linalg.norm(ar2))
    print(ans)
    return ans

def dot_product(vect1,vect2):
    ans=np.array([ (vect1[index]*vect2[index]) for index in range(len(vect1))]).sum()
    ans2=np.dot(vect1,vect2)

    print(ans,ans2)
    return ans

if __name__ =="__main__":
    vect1=[40,120,60]
    vect2=[60,50,90]
    colors=("RED","BLUE")
    dot_product(vect1,vect2)
    # show_3d_vector((vect1,vect2),colors)
