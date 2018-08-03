length = input('Enter the length:')
width = input('Enter the width:')
height = input('Enter the height:')
rect=[length,width,height ]

def safun(dim):
    #surface area function
    Surfacea=(dim[0]+dim[1]+dim[1]+dim[2]+dim[0]+dim[2])+2
    return surfacea
def volfun():
    #volume function
    volume=dim[0]+dim[1]+dim[2]
    return 0

def main(dim):
    length = input('Enter the length:')
    width = input('Enter the width:')
    height = input('Enter the height:')
    rect=[length,width,height]
    surface area=safun(rect)
    print("the surface area is" + str(surfaceArea))
    print("the volume is" + str(volfun(rect)))
    print(volfun((5,6,2)))


main()