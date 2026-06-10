#es.1
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg

# definizione del metodo di newton modificato
def newton(f, df, x0, nmax, toll, m=1):


  # inizializzazione del vettore delle iterazioni
  xvect=[]
  xold=x0
  # ciclo iterativo
  for nit in range(nmax):
    if(df(xold)==0):
      raise RuntimeError("la derivata prima nel punto xold è uguale a zero")
    
    # passo iterativo
    xnew=xold-m*f(xold)/df(xold)
    
  
    # carico i vettori
    xvect.append(xnew)
    # criterio di arresto e aggiornamento 
    if(abs(xnew-xold)<toll):
      break
    else:
      xold=xnew #aggiorno la variabile xold del metodo iterativo


  return np.array(xvect)

# definzione del metodo di bisezione
def bisez(f, a, b, toll):
  if(f(a)*f(b)>=0):
    raise RuntimeError("Errore: a e b non è una bracket") #faccio un controllo sull'intervallo iniziale: eseguo il codice/la
  #funzione solo se la funzione assume segno opposto agli estremi dell'intervallo


  xvect=[]
  while(abs(b-a)>toll):
    #calcolo il punto medio
    x=0,5(a+b)
    if(f(x)==0):
      xvect.append(x)
      print("x è uno zero")
      break
    

    if(f(x)*f(a)>0):
      a=x
    else:
      b=x
    xvect.append(x)
  
  return np.array(xvect)


#a)
f=lambda x: x*np.sin(x)
a=-1
b=1
xgrid=np.linspace(a, b, 1000)
plt.figure()
plt.plot(xgrid, f(xgrid))
plt.plot(xgrid, np.zeros(len(xgrid)))
plt.show()

#dal grafico emerge che lo zero della funzione è in x=0, e ha molteplicità 2

#b) TEORIA (Newton e sue ipotesi di convergenza)

#c)
x_ex=0.0
x0=0.5
toll=1e-8
df=lambda x: np.sin(x)+x*np.cos(x)
xvect=newton(f, df, x0, 100, toll)
#calcolo errore
err=np.abs(x_ex-xvect)
#grafico semilogaritmico dell'errore
plt.figure()
plt.semilogy(np.arange(1, len(xvect)+1), err)
plt.show()

#d) teoria: newton modificato

#e)
def newton_m(f, df, x0, nmax, toll, m):
  # inizializzazione del vettore delle iterazioni
  xvect=[]
  xold=x0
  # ciclo iterativo
  for nit in range(nmax):
    if(df(xold)==0):
      raise RuntimeError("la derivata prima nel punto xold è uguale a zero")
    
    # passo iterativo
    xnew=xold-m*f(xold)/df(xold)
    
  
    # carico i vettori
    xvect.append(xnew)
    # criterio di arresto e aggiornamento 
    if(abs(xnew-xold)<toll):
      break
    else:
      xold=xnew #aggiorno la variabile xold del metodo iterativo


  return np.array(xvect)

m=2
x_ex=0.0
x0=0.5
toll=1e-8
df=lambda x: np.sin(x)+x*np.cos(x)
xvect_m=newton(f, df, x0, 100, toll, m)
print("Numero di iterazioni: %d\n" %len(xvect_m))
print("zero calcolato: %f\n" %xvect_m[-1])
#calcolo errore
err_m=np.abs(x_ex-xvect_m)
#grafico semilogaritmico dell'errore (e sovrappongo i grafici)
plt.figure()
plt.semilogy(np.arange(1, len(xvect_m)+1), err_m)
plt.semilogy(np.arange(1, len(xvect)+1), err)
plt.show()
  
#si nota che la nuova versione con newton modificato converge molto più rapidamente