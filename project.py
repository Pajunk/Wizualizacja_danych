import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

V = np.loadtxt("/fme.txt")
x = np.zeros(shape=V.shape[0])
y = np.zeros(shape=V.shape[0])
z = np.zeros(shape=V.shape[0])


for i in range(V.shape[0]):
    x[i] = V[i][0]
for i in range(V.shape[0]):
    y[i] = V[i][1]
for i in range(V.shape[0]):
    z[i] = V[i][2]

X=np.linspace(x.min(),x.max(),1000)
Y=np.linspace(y.min(),y.max(),1000)
Z = griddata((x, y), z, (X[None,:], Y[:,None]), method='cubic')
zmin=z.min()
zmax=z.max()

CS=plt.contourf(X, Y, Z, 15, cmap=plt.cm.rainbow,vmax=zmax,vmin=zmin)
plt.axis('equal')
plt.colorbar()
plt.xlabel('X-oś')
plt.ylabel('Y-oś')
plt.title('2D')
plt.show()
#---------------------------------------------

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

axa=ax.plot_trisurf(x, y, z, cmap='rainbow')
fig.colorbar(axa)
ax.set_xlabel('X-oś')
ax.set_ylabel('Y-oś')
ax.set_zlabel('Z-oś')
ax.set_title('3D')
ax.set_box_aspect([2,1,1])
plt.show()


A=np.zeros(V.shape[0])
B=np.zeros(V.shape[0])
C=np.zeros(V.shape[0])
A[:]=np.reshape(V[:,0],V.shape[0])
B[:]=np.reshape(V[:,1],V.shape[0])
C[:]=np.reshape(V[:,2],V.shape[0])
Ac=[]
Bc=[]
for i in A:
    if(i not in Ac):
        Ac.append(i)
for i in B:
    if(i not in Bc):
        Bc.append(i)
nn=len(Ac)
mm=len(Bc)
Am=np.reshape(A,(mm,nn))
Bm=np.reshape(B,(mm,nn))
Cm=np.reshape(C,(mm,nn))
Bi=np.zeros((len(Bc),int(B.shape[0]/len(Bc))))
for i in range(len(Bc)):
    Tab=[]
    for j in range(C.shape[0]):
        if(B[j]==Bc[i]):
            Tab.append(C[j])
    Bi[i]=np.array(Tab)

C1=np.zeros(Bi.shape[1])
A1=np.zeros(Bi.shape[1])
c=0
for i in range(B.shape[0]):
    if(B[i]==Bc[0]):
        C1[c]=C[i]
        A1[c]=A[i]
        c+=1
A2=np.linspace(min(A1),max(A1),100)
#---------------------------------------------
# Obliczenie średnich wartości F(x, y) dla każdej wartości y
def sr(x):
    srd=0
    for i in x:
        srd=srd+i
    return srd/x.shape[0]
# Wyświetlenie wyników
Q=0
for i in Bi:
    ttp=np.zeros(i.shape[0])
    ttp[:]=i[:]
    print("y = ",Bc[Q],":","średnia F(x, y) = ",sr(ttp))
    Q=Q+1
# Obliczenie mediany wartości F(x, y) dla każdej wartości y
print()
def sort(x):
    for i in range(x.shape[0]):
        for y in range(x.shape[0]-1):
            if(x[y]>x[y+1]):
                ttp=x[y]
                x[y]=x[y+1]
                x[y+1]=ttp

def med(x):
    if(x.shape[0]%2==0):
        return (x[int(x.shape[0]/2)]+x[int((x.shape[0]/2)-1)]/2)
    else:
        return x[int(x.shape[0]/2)]
# Wyświetlenie wyników
Q=0
for i in Bi:
    ttp=np.zeros(i.shape[0])
    ttp[:]=i[:]
    sort(ttp)
    print("y = ",Bc[Q],":","mediana F(x, y) = ",med(ttp))
    Q=Q+1

print()
#############
#Oblicza wariancję
def war(x):
    e=sr(x)
    p=0
    for i in x:
        p=p+(i-e)*(i-e)
    return p/(x.shape[0])

# Wyświetlenie wyników
Q=0
for i in Bi:
    ttp=np.zeros(i.shape[0])
    ttp[:]=i[:]
    print("y = ",Bc[Q],":","odchylenie standardowe F(x, y) = ",np.sqrt(war(ttp)))
    Q=Q+1
print()
#########################
#interpolacja Lagrange'a
def interp_lag(A,B):
    n=A.shape[0]
    O=np.zeros(n)
    for i in range(n):
        mul=1
        for j in range(n):
            if(i!=j):
                mul*=A[i]-A[j]
        O[i]=B[i]/mul
    G=np.zeros(n)
    for h in range(n):
        O0=np.zeros(n)
        O1=np.zeros(n)
        A1=np.concatenate((A[:h],A[h+1:]))
        O0[0]=1
        O1[0]=1
        for i in range(1,n):
            for j in range(1,i+1):
                O0[j]=O1[j]+O1[j-1]*(-A1[i-1])
            for j in range(1,i+1):
                O1[j]=O0[j]
        for g in range(n):
            G[g]+=O0[g]*O[h]
    return G
#############################################################################
def W(x,a):
    n=a.shape[0]
    s=0
    for i in range(n):
        mul=1
        mul*=x**(n-(i+1))
        s+=a[i]*mul
    return s

def divide(Tab):
    New=[]
    E=0
    for i in range(6):
        New.append(np.zeros(4))
        for j in range(4):
            New[i][j]=(Tab[E])
            E+=1
        E-=1
    New.append(np.zeros(3))
    New[6][0]=Tab[E]
    New[6][1]=Tab[E+1]
    New[6][2]=Tab[E+2]
    return New

Adiv=divide(A1)
Cdiv=divide(C1)
Ndiv=len(Adiv)

Alag=[]
for i in range(Ndiv):
    tmp=interp_lag(Adiv[i],Cdiv[i])
    Alag.append(tmp)

plt.plot(A1,C1,'r+')
for i in range(Ndiv):
    xlag=np.linspace(min(Adiv[i]),max(Adiv[i]),100)
    n2=xlag.shape[0]
    ylag=np.zeros(n2)
    for j in range(n2):
        ylag[j]=W(xlag[j],Alag[i])
    plt.plot(xlag,ylag,'b-')
plt.title("interpolacja Lagrange'a")
plt.legend(["Punkty","Fukcja interpolacji"])
plt.xlabel("x")
plt.ylabel("y")
plt.plot(A1,np.zeros(A1.shape[0]),'k-')
plt.show()
###########################################
#Gause
def metoda_el_gaussa(A,B):
    n=A.shape[0]
    m=A.shape[1]
    Ac1=np.zeros((n,m+1))
    Ac2=np.zeros((n,m+1))
    Ac1[:,:m]=A
    Ac1[:,m:]=np.reshape(B,(B.shape[0],1))
    Ac2[:,:]=Ac1
    for s in range(n-1):
        for i in range(s+1,n):
            for j in range(s,n+1):
                Ac2[i][j]=Ac1[i][j]-((Ac1[i][s]/Ac1[s][s])*Ac1[s][j])
        Ac1[:,:]=Ac2
    X=np.zeros((n))
    X[n-1]=Ac1[n-1][n]/Ac1[n-1][n-1]
    for i in range(n-2,-1,-1):
        sum=0
        for s in range(i+1,n):
            sum=sum+Ac1[i][s]*X[s]
        X[i]=(Ac1[i][n]-sum)/Ac1[i][i]
    return X
###########################################
#Aproksymacja
def aproksymacja_f1zm(X,Y):
    n=X.shape[0]
    m=2
    M=np.zeros((m,m))
    P=np.zeros(m)
    x=0
    y=0
    for i in range (m):
        for l in range(n):
            y+=Y[l]*(X[l]**i)
        P[i]=y
        y=0
        for j in range (m):
            if ((i+j)!=0):
                for k in range(n):
                    x+=X[k]**(i+j)
                M[i][j]=x
                x=0
            else:
                M[i][j]=n
    z=metoda_el_gaussa(M,P)#gausa tu wlep
    for i in range(int(z.shape[0]/2)):
        tmp=z[i]
        z[i]=z[z.shape[0]-(i+1)]
        z[z.shape[0]-(i+1)]=tmp
    return z


apro=(aproksymacja_f1zm(A1,C1))
plt.plot(A1,C1,'rx')
B3=np.zeros(A2.shape[0])
for ia in range(A2.shape[0]):
    B3[ia]=W(A2[ia],apro)
plt.plot(A2,B3,'b-')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(A1,np.zeros(A1.shape[0]),'k-')
XN=np.linspace(0,2,7)
plt.title(label="Wykres Aproksymacyjny")
plt.legend(["Aproksymacja liniowa","Punkty"])
plt.show()
#######################################
#pole powierzchni
def odleglosc(x1, y1, f1,x2, y2, f2):
    # Obliczenie odległości między dwoma punktami na podstawie ich współrzędnych
    odleglosc = np.sqrt((x2 - x1)**2 + (y2 - y1)**2+(f2-f1)**2)
    return odleglosc

def Pole(A,B,C):
    #Obliczanie pola trójkąta
    Obw=((A+B+C)/2)
    Pole=np.sqrt(Obw*(Obw-A)*(Obw-B)*(Obw-C))
    return Pole

def liczenie_powierzchni(x,y,z):
    Polecal=0
    q=x.shape[1]
    qq=y.shape[0]
    for i in range(qq-1):
        for j in range(q):
            if(j!=q-1):
                A=odleglosc(x[i][j],y[i][j],z[i][j],x[i][j+1],y[i][j+1],z[i][j+1])
                B=odleglosc(x[i][j],y[i][j],z[i][j],x[i+1][j],y[i+1][j],z[i+1][j])
                C=odleglosc(x[i][j+1],y[i][j+1],z[i][j+1],x[i+1][j],y[i+1][j],z[i+1][j])
                Polecal+=Pole(A,B,C)
            if(j!=0):
                A=odleglosc(x[i][j],y[i][j],z[i][j],x[i+1][j-1],y[i+1][j-1],z[i+1][j-1])
                B=odleglosc(x[i][j],y[i][j],z[i][j],x[i+1][j],y[i+1][j],z[i+1][j])
                C=odleglosc(x[i+1][j-1],y[i+1][j-1],z[i+1][j-1],x[i+1][j],y[i+1][j],z[i+1][j])
                Polecal+=Pole(A,B,C)
    return Polecal

print("Pole powierzchni funkcji:", liczenie_powierzchni(Am,Bm,Cm))
###############################################
#Całki
def metoda_trap(x1,x2,y1,y2):
    trap=((y1+y2)/2)*abs(x1-x2)
    return trap
def calkPr(x,a):
    n=x.shape[0]
    y=np.zeros(n)
    for i in range(n):
        y[i]=W(x[i],a)
    plt.plot(x,y,'b-')
    wy=0
    for i in range(n-1):
        wy=wy+metoda_trap(x[i+1],x[i],y[i],y[i+1])
        plt.plot([x[i],x[i]],[y[i],0],'g-')
        plt.plot([x[i+1],x[i+1]],[y[i+1],0],'g-')
        plt.plot([x[i],x[i+1]],[0,0],'g-')
    return wy
S=0
plt.plot(A1,C1,'r+')
for i in range(Ndiv):
    xlag=np.linspace(min(Adiv[i]),max(Adiv[i]),25)
    S+=calkPr(xlag,Alag[i])
plt.title("Calka interpolacji Lagrange'a")
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(["Punkty","Funkcja interpolcaji","Calka"])
plt.plot(A1,np.zeros(A1.shape[0]),'k-')
print("\nCalka funkcji interpolacyjnej Lagrange'a: "+str(S))
plt.show()
######################
#wyświetlanie całki aproksymacji
plt.plot(A1,C1,'r+')
plt.title("Calka aproksymacji liniowej")
plt.xlabel('X')
plt.ylabel('Y')
SS=calkPr(A2,apro)
plt.legend(["Punkty","Funkcja aproksymacji liniowej","Calka"])
plt.plot(A1,np.zeros(A1.shape[0]),'k-')
print("\nCalka funkcji aproksymacji liniowej: "+str(SS))
plt.show()
#################
#czastkowa pochodna
def poch_licz(x1,x2,y1,y2):
    wynik=(x1-x2)/(y1-y2)
    return wynik
def poch(b,d):
    n=b.shape[0]
    poc=np.zeros(n)
    poc[0]=poch_licz(d[0],d[1],b[0],b[1])
    poc[n-1]=poch_licz(d[n-1],d[n-2],b[n-1],b[n-2])
    for i in range(1,n-1):
        poc[i]=poch_licz(d[i-1],d[i+1],b[i-1],b[i+1])
    return poc

pochh=poch(A1,C1)
plt.plot(A1,pochh,'rs')
plt.plot(A1,pochh,'b-')
plt.plot(A1,np.zeros(A1.shape[0]),'k-')
plt.title("Pochodna czesciowa")
plt.legend(["Punkty","Pochodna czesciowa"])
plt.show()
print()
###############################
#Monotonicznosc
dudu=[]
Ujd=[]
for i in range(pochh.shape[0]):
    if(pochh[i]>0):
        dudu.append(A1[i])
    else:
        Ujd.append(A1[i])
print("Pochodna czesciowa jest dodatnia w punktach:",dudu,"i ujemna w punktach:",Ujd)
plt.plot(A1,np.sign(pochh),'c+')
plt.plot(A1,np.zeros(A1.shape[0]),'m-')
plt.plot(A1,np.sign(pochh),'y-')
plt.title("Znak pochodnej")
plt.legend(["Punkty pochodnej","Pochodna czesciowa"])
plt.show()
