from p4 import p4
from p5 import p5

def vec4ToMat(v):
    m=[[0 for i in range(1)] for j in range(4)]
    m[0][0]=v.x
    m[1][0]=v.y
    m[2][0]=v.z
    m[3][0]=v.w
    return m
def vec5ToMat(v):
    m=[[0 for i in range(1)] for j in range(5)]
    m[0][0]=v.x
    m[1][0]=v.y
    m[2][0]=v.z
    m[3][0]=v.w
    m[4][0]=v.m
    return m
def vecToMat(v):
    m=[[0 for i in range(1)] for j in range(3)]
    m[0][0]=v.x
    m[1][0]=v.y
    m[2][0]=v.z
    return m

def matToVec(m):
    v=PVector()
    v.x=m[0][0]
    v.y=m[1][0]
    if len(m) > 2:
        v.z=m[2][0]
        if len(m) >3:
            v.w=[3][0]
            if len(m)>4:
                v.m[4][0]
    return v

def matToV4(m):
    v= p4(0,0,0,0)
    v.x=m[0][0]
    v.y=m[1][0]
    v.z=m[2][0]
    v.w=m[3][0]
    return v
def matToV5(m):
    v= p5(0,0,0,0,0)
    v.x=m[0][0]
    v.y=m[1][0]
    v.z=m[2][0]
    v.w=m[3][0]
    v.m=m[4][0]
    return v

def matP4Mul(a,b):
    m=vec4ToMat(b)
    return matToV4(matMatMul(a,m))

def matP5Mul(a,b):
    m=vec5ToMat(b)
    return matToV5(matMatMul(a,m))
def matP5proj(a,b):
    m=vec5ToMat(b)
    return matToV4(matMatMul(a,m))
    
def matVecMul(a,b):
    m=vec4ToMat(b)
    return matToVec(matMatMul(a,m))

def matMatMul(a,b):
    colsA=len(a[0])
    rowsA=len(a)
    colsB=len(b[0])
    rowsB=len(b)
    
    if(colsA != rowsB):
        print ("cols dont match")
        return None
    
    result = [[0 for i in range(colsB)] for j in range(rowsA)]
    
    for i in range(rowsA):
        for j in range(colsB):
            sum=0
            for k in range(colsA):
                sum+= a[i][k] *b[k][j]
            result[i][j]=sum
    
    return result
