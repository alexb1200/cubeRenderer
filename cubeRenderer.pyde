import matrix
from p4 import p4
from p5 import p5

projection= [[1,0,0],[0,1,0]]


def connect (offset,i,j,points):
    a=points[i+offset]
    b=points[j+offset]
    strokeWeight(2)
    #stroke(255)
    #line(a.x,a.y,a.z, b.x,b.y,b.z)
    noStroke()
    textureMode(NORMAL)
    beginShape()
    texture(img)
    vertex(a.x,a.y,a.z,0,0)
   
    
    vertex(a.x+30,a.y+30,a.z,0,1)
    
    vertex(b.x+30,b.y+30,b.z,1,1)
    vertex(b.x,b.y,b.z,1,0)
    endShape()
    
    
    
def setup():
    global angle
    global angle1
    angle1=0
    angle = 0
    print(cos(angle))
    size(1000,1000,P3D)
    #fullScreen(P3D)
    global points
    points=[]
    points.append(p5(-1,-1,-1,1,1))
    points.append(p5(1,-1,-1,1,1))
    points.append(p5(1,1,-1,1,1))
    points.append(p5(-1,1,-1,1,1))
    points.append(p5(-1,-1,1,1,1))
    points.append(p5(1,-1,1,1,1))
    points.append(p5(1,1,1,1,1))
    points.append(p5(-1,1,1,1,1))
    
    points.append(p5(-1,-1,-1,-1,1))
    points.append(p5(1,-1,-1,-1,1))
    points.append(p5(1,1,-1,-1,1))
    points.append(p5(-1,1,-1,-1,1))
    points.append(p5(-1,-1,1,-1,1))
    points.append(p5(1,-1,1,-1,1))
    points.append(p5(1,1,1,-1,1))
    points.append(p5(-1,1,1,-1,1))
    
    
    points.append(p5(-1,-1,-1,1,-1))
    points.append(p5(1,-1,-1,1,-1))
    points.append(p5(1,1,-1,1,-1))
    points.append(p5(-1,1,-1,1,-1))
    points.append(p5(-1,-1,1,1,-1))
    points.append(p5(1,-1,1,1,-1))
    points.append(p5(1,1,1,1,-1))
    points.append(p5(-1,1,1,1,-1))
    
    points.append(p5(-1,-1,-1,-1,-1))
    points.append(p5(1,-1,-1,-1,-1))
    points.append(p5(1,1,-1,-1,-1))
    points.append(p5(-1,1,-1,-1,-1))
    points.append(p5(-1,-1,1,-1,-1))
    points.append(p5(1,-1,1,-1,-1))
    points.append(p5(1,1,1,-1,-1))
    points.append(p5(-1,1,1,-1,-1))
    print(points[0].x)
    global img
    img=loadImage("LOOKATME.png")
    #print( matrix.matMatMul(points,points)[0][0])
        
    
        
def draw():
    global angle
    global angle1
    global points
    background(0)
    translate(width/2,height/2)
    rotateX(-PI/2)
    dist =1.6
   # print(cos(angle))
    #rotZ=[ [cos(angle),-sin(angle),0],[sin(angle), cos(angle),0], [0,0,1]]
   # rotX=[ [1,0,0],[0,cos(angle),-sin(angle)],[0,sin(angle),cos(angle)]]
   # rotY=[ [cos(angle),0,sin(angle)],[0,1,0],[-sin(angle),0,cos(angle)]]
    
    
    
    projected3d= [PVector() for i in range(32)]
    
    for i in range(len(points)):
        
        n= points[i]
        rotZY= [ [1,0,0,0,0],
                   [0,cos(angle),-sin(angle),0,0],
                  [0,sin(angle),cos(angle),0,0],
                [0,0,0,1,0],
                [0,0, 0,0,1]]
        rotXZ= [ [cos(angle),0, -sin(angle), 0,0],
                 [0,1,0,0,0],
                 [sin(angle),0,cos(angle),0,0],
                [0,0,0,1,0],
                [0,0,0,0,1 ]]
       
        rotXM= [ [cos(angle),0,0,0,-sin(angle)],
                 [0,1,0,0,0],
                 [0,0,1,0,0],
                [0,0,0,1,0],
                [sin(angle),0,0,0,cos(angle) ]]
        rotXW= [ [cos(angle),0,0,-sin(angle),0],
                 [0,1,0,0,0],
                 [0,0,1,0,0],
                [0,0,0,1,0],
                [sin(angle),0,0,cos(angle),0 ]]
        rotated5d=matrix.matP5Mul(rotXZ,n)
        rotated5d=matrix.matP5Mul(rotXM,rotated5d)
        rotated5d=matrix.matP5Mul(rotXZ,rotated5d)
        rotated5d=matrix.matP5Mul(rotXW,rotated5d)
       
        m=1/(1.7*dist-rotated5d.m)
        project4d =  [ [m,0,0,0,0], 
                 [0,m,0,0,0], 
                 [0,0,m,0,0],
                 [0,0,0,m,0] ]
        p4d=matrix.matP5proj(project4d,rotated5d)
        
        
        
        
        
        v=p4d
        
        # rotXY= [ [cos(angle), -sin(angle), 0,0],
        #  [sin(angle),cos(angle),0,0],
        #          [0,0,1,0],
        #         [0,0,0,1] ]
        # # rotZW = [ [1,0,0,0],
        # #          [0,1,0,0],
        # #         [0,0,cos(angle),-sin(angle)],
        # #          [0,0,sin(angle), cos(angle)] ]
        # rotYZ = [ [cos(angle),0,-sin(angle),0],
        #              [0,1,0,0],
        #              [sin(angle),0,cos(angle),0],
        #         [0,0,0,1] ]
        # rotXW= [ [cos(angle),0,0, -sin(angle)],
        #        [0,1,0,0],# [sin(angle),cos(angle),0,0],
        #       [0,0,1,0],
        #         [sin(angle), cos(angle),0,0]  ]
        
        # rotated= matrix.matP4Mul(rotXY,v)
        # rotated= matrix.matP4Mul(rotXW, rotated)
        # rotated= matrix.matP4Mul(rotYZ, rotated)
        
        w= 1/ (1.9*dist-v.w)
        project =  [ [w,0,0,0], 
                 [0,w,0,0], 
                 [0,0,w,0] ]
        
        proj = matrix.matVecMul(project,v)
        proj.mult(width/2)
        projected3d[i]=proj
       
        stroke(255, 250)
        strokeWeight(20)
        noFill()
        
        point(proj.x,proj.y,proj.z)
        
    for i in range(4):
        connect(0,i,(i+1)%4, projected3d)
        connect(0, i+4, ((i+1)%4)+4, projected3d)
        connect(0,i, i+4, projected3d)
        
    for i in range(4):
        connect(8,i,(i+1)%4, projected3d)
        connect(8, i+4, ((i+1)%4)+4, projected3d)
        connect(8,i, i+4, projected3d)
        
    for i in range(4):
        connect(16,i,(i+1)%4, projected3d)
        connect(16, i+4, ((i+1)%4)+4, projected3d)
        connect(16,i, i+4, projected3d)
    for i in range(4):
        connect(24,i,(i+1)%4, projected3d)
        connect(24, i+4, ((i+1)%4)+4, projected3d)
        connect(24,i, i+4, projected3d)
        
    
        
    for i in range(8):
        connect(0,i,i+8, projected3d)
        
    for i in range(8):
        connect(8,i,i+8, projected3d)
    for i in range(8):
        connect(16,i,i+8, projected3d)
        
    for i in range(16):
        connect(0,i,i+16, projected3d)
   
    
    
    angle+=.01 #if you want it to rotate on its own
   # angle = map(mouseX,0,width,0,TWO_PI)
    angle1 = map(mouseY,0,height,0,TWO_PI)
    
    
    #for 3d to 2d
    #index=0
    # for vec in points:
    #     rot=matrix.matVecMul(rotY,vec)
    #     rot=matrix.matVecMul(rotX,rot)
    #     rot=matrix.matVecMul(rotZ,rot)
    #     proj2d = matrix.matVecMul(projection,rot)
    #     proj2d.mult(200)
    #     projected[index]=proj2d
    #     index+=1
        
    # for v in projected:
    #     stroke(0)
    #     strokeWeight(16)
    #     noFill()
    #     point(v.x,v.y)
    
    # for i in range(4):
    #     connect(i,(i+1)%4, projected)
    #     connect(i+4, ((i+1)%4)+4, projected)
    #     connect(i,i+4,projected)
    
    # angle+=.03
    

        
        
