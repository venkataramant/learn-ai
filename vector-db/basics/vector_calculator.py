import math
def get_euclidean_distance_old(vect1,vect2):
    ed_value=None
    if len(vect1)!=len(vect2):
        return ed_value
    sum_value=0
    for index in range(len(vect1)):
        sum_value=sum_value+math.pow((vect1[index]-vect2[index]),2)
    print(sum_value)
    ed_value=math.sqrt(sum_value)

    return ed_value

def get_euclidean_distance(vect1,vect2):
    ed_value=None
    squares=[ math.pow((vect1[index]-vect2[index]),2) for index in range(len(vect1))]
    print(squares)
    ed_value=math.sqrt(sum(squares))

    return ed_value

if __name__=="__main__":
    vect1=[40,120,60]
    vect2=[60,50,90]
    ed=get_euclidean_distance(vect1,vect2)
    print("ed is {}".format(ed))
    print("Test")