import numpy as np
import matplotlib.pyplot as plt
import utilis_ODE

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

#es.1
#a)

f=lambda x: x*np.sin(2*np.pi*x)*np.exp(x)
xgrid=np.linspace(-np.pi/4, np.pi/4, 1000)
toll=1e-6

plt.figure()
plt.plot(xgrid, f(xgrid))
plt.plot(xgrid, np.zeros(np.shape(xgrid)))
plt.show()

#dal grafico della funzione e delle sue intersezioni con l'asse y (x=0) emerge che
#l'algoritmo di bisezione può essere impiegato per gli zeri più a sx e a dx, mentre NON 
#può essere usato per lo zero centrale, che ha molteplicità algebrica pari.
#NON esiste un intervallo per questo zero centrale per cui la funzione assuma
#segno opposto agli estremi.

#possibile calcolo degli zeri (con scelta anche dell'intervallo)
#zero più a sx
a0=-0.6
b0=-0.4

xvect0=bisez(f, a0, b0, toll)

print("Numero di iterazioni: %d\n" %len(xvect0))
print("Ultimo valore di x: %f\n" %xvect0[-1])
print("Valore di f: %.e\n" %f(xvect0[-1]))

#zero più a dx
a2=0.4
b2=0.6

xvect2=bisez(f, a2, b2, toll)

print("Numero di iterazioni: %d\n" %len(xvect2))
print("Ultimo valore di x: %f\n" %xvect2[-1])
print("Valore di f: %.e\n" %f(xvect2[-1]))

#zero centrale
a1=-np.pi/4
b1=np.pi/4

xvect1=bisez(f, a1, b1, toll)

print("Numero di iterazioni: %d\n" %len(xvect1))
print("Ultimo valore di x: %f\n" %xvect1[-1])
print("Valore di f: %.e\n" %f(xvect1[-1]))

#b) Metodo di Newton (T+P)
#il metodo di Newton, a differenza di quello di bisezione, è solo localmente convergente
#per cui è necessario scegliere un opportuno valore della guess iniziale x0

df=lambda x: np.sin(2*np.pi*x)*np.exp(x)+x*2*np.pi*np.cos(2*np.pi*x)*np.exp(x)+x*np.sin(2*mp.pi*x)*np.exp(x)

#zero a sx
x0=-0.6
xvect0=newton(f, df, x0, 100, toll,m=1)

#zero a dx
x2=0.6
xvect2=newton(f, df, x2, 100, toll, m=1)

#zero centrale (newton modificato)
x1=0.1
xvect1=newton(f, df, x1, 100, toll, m=2)