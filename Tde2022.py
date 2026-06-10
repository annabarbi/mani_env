import numpy as np
import matplotlib as plt
#tde luglio 2022

#es1 (sistema lineare con A=matrice di Hilbert nxn)
import scipy
import scipy.linalg

def fwsub(A,b):
  """
  Algoritmo di sostituzione in avanti - forward substitution 
  Input:
  A: matrice quadrata triangolare inferiore (è la L della teoria!!!!)
  b: termine noto
  Output:
  x: soluzione del sistema lineare = b
  """
  #dimensione di b o A
  n=b.shape[0] #restituisce 20, ossia le righe(posizione 0) del vettore b

  #verifichiamo che la matrice A sia quadrata, triangolare inferiore e non singolare
  if A.shape[0]!=A.shape[1]:
    raise RuntimeError("Errore: matrice no quadrata")
  
  if(A!=np.tril(A)).any(): #np.tril(A) -> matrice triangolare inferiore
    raise RuntimeError("Errore: matrice A non triangolare inferiore") 
  
  #A è triangolare inferiore -> ha gli autovalori sulla diagonale, quindi per controllare che sia non singolare
  #devo valutare il prodotto degli elementi sulla diagonale
  if np.prod(np.diag(A))==0:
    raise RuntimeError("Errore: matrice singolare")
  
  #inizializzo la soluzione (x=vettore di zeri di dimensione n)
  x=np.zeros(n)
  x[0]=b[0]/A[0,0]
  for i in range(1,n): #l'ultimo estremo è escluso --> va da 1 a n o da 0 a n-1
    x[i] = (b[i] - A[i, 0:i]@x[0:i]) / A[i, i] 
    #A[i, 0:i]@x[0:i] significa fare la sommatoria per j da 0 a i-1 degli aij*xj, con i fissato dal ciclo for; @->prodotto riga per colonna,
    #quindi sostanzialmente si sta facendo la sommatoria tra gli elementi moltiplicati

    #oppure si può realizzare con altri cicli che scorrono gli elmenti delle colonne e creano la sommatoria
  return x

def bksub(A,b):
  """
  Algoritmo di sostituzione all'indietro - backward substitution
  Input:
  A: matrice quadrata triangolare superiore
  b: termine noto
  Output:
  x: soluzione del sistema lineare = b
  """
  n=b.shape[0]
  #eventuali verifiche (vedi sopra: A quadrata, triangolare superiore -> comando np.triu(A), non singolare)

  if A.shape[0]!=A.shape[1]:
    raise RuntimeError ("ERRORE: la matrice A non è quadrata")

  if (A!=np.triu(A)).any():
    raise RuntimeError ("ERRORE: la matrice A non è triangolare superiore")
  
  if np.prod(np.diag((A))==0):
    raise RuntimeError ("ERRORE: la matrice A non è non singolare")

  
  x=np.zeros(n)
  x[-1]=b[-1]/A[-1,-1] #nell'algoritmo di sostituzione all'indietro parto dall'ultimo elmento
  
  for i in range(n-2,-1,-1): #vado da n-1 a 0 con passo -1 (comando centrale), ossia si cicla in modo discreto andando all'indietro
    x[i]=(b[i]-A[i, i+1:n]@x[i+1:n])/A[i,i]

  return x

from utilis_ODE import *

#a) soluzione del problema con LU, metodi di sost avanti e indietro; errore e condizionamento 
err=[]
condA=[]
n_val=[5, 10, 20]

for n in n_val:
    A=scipy.linalg.hilbert(n)
    x_ex=np.ones(n)
    b=A @ x_ex

    P,L,U=scipy.linalg.lu(A)
    y=fwsub(L, P.T@b)
    x=bksub(U, y)
    err.append(np.linalg.norm(x-x_ex))
    condA.append(np.linalg.cond(A))
print(f"err= {np.array(err)}")
print(f"condA= {np.array(condA)}")

#b) teoria (concetto di condizionamento di una matrice e sua importanza sulla
#stabilità della risoluzione di un sistema lineare con metodo di eliminazione di Gauss)

#c) Punto precedente usando metodo del gradiente coniugato (da fare)






