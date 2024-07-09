import numpy as np
import matplotlib.pyplot as plt
import random as rd
import math
from scipy.stats import norm, expon
import sys

#############################################################################################


def sturges (N_events) : 
  return int(np.ceil (1 + 3.322 * np.log (N_events)))


def check_ratio (numerator, denominator):
  return (numerator % denominator) == 0
  
def add_element (input_list) :
    input_list.append (input_list[-1])
    
def read_file (filename, arrayname):
  with open(filename, 'r') as input_file:
    arrayname = [float(x) for x in input_file.readlines()]
      


def on_file (filename, floats):
   with open(filename, 'w') as output_file:
     output_file.writelines([f"{number}\n" for number in floats])

    
def fattoriale (n):
    '''
    Funzione che calcola il fattoriale
    '''
    if (n == 0): return 1;
    return (n * fattoriale (n-1))
    
    


#PLOTTARE FUNZIONI
'import numpy as np'
'import matplotlib.pyplot as plt'

'x = np.linspace(min, max, 10000)'
'y = f(x)'
'fig, ax = plt.subplots(nrows = 1, ncols = 1)'
'ax.plot(x, y, label = '', color = '')'
'plt.axhline(y = 2, ...)'
'plt.axvline(x = 2, color = '', linestyle = '', linewidth = 2)'
'plt.set_ylim(min, max)' #allargo o avvicino il grafico su y
'ax.set_yalbel('')' 
'ax.set_xlabel('')'
'ax.set_xscale(log)'  
'ax.legend()'

#PLOTTARE ISTOGRAMMI

'N_bins = sturges(N_evts)'
'bin_edges = np.linspace(min, max, N_bins)'
'ax.hist(events, bins = bin_edges, color = '', histtype = '')' 

#PLOTTARE ERRORBARS

'ax.errorbar(dati1, dati2, yerr = sigma, marker = "o")'

#GENERAZIONE CASUALE DI DATI O ERRORI

'from random import uniform'
'from random import normal'

'generazione uniforme'
'generazione try and catch'      #genero uniforme ma prendo solo ciò che sta sotto f(x)
'generazione gaussiana con TLC'  #ho una funzione, calcolo la media di n valori (circa 30) della funzione. se li rigenero tot volte, avrò tot medie. 
                                 #se aumento di molto il valore tot, le medie si distribuiranno gaussianamente
                                 #ex. samples = np.random.normal(mean, stdv, size = (tot, x))    means = np.mean(samples, axis = 1)
                                 #anche se valori non distribuiti gaussianamente, lo sono sempre le medie (basta che seguano stessa distribuzione)
              
'generazione esponenziale'
'generazione poisson'            


#COORDINATE CON FUNZIONE + ERRORI

#ho una funzione f(x, a, b), e ogni evento che trovo è distribuito co coordinata f + errore generato gaussiano'
#come li metto assieme?'
'gli eventi sono N'
'y_coord = list(map(lambda k:sum(k), zip(f(x,a,b), genera_errore(min, max, N))))'
'y_coord = list(map(lambda k:sum(k), zip(f(x,a,b), genera_errore(min, max) for i in range (N)))'

#FIT SU DATI E MODELLI

'from iminuit import Minuit'
'from iminuit.cost import LeastSquares'
'x_coord.sort()' #riordino valori su asse x per eseguire il fit
'least_squares = LeastSquares(dati1, dati2, sigma, modello)' #inserisco dati, errori e il modello con cui voglio fittare
'fit = Minuit(least_squares, cost1 = 0, cost2 = 0...)' #le costanti vanno inizializzate con un valore iniziale di pova
'fit.migrad()' #fa la minimizzazione
'fit.hesse()'  #calcola matrice hessiana
'print(fit.fval)' #minimo della funzione
'fit.values["parametro"]' #restituisce la stima del parametro
'fit.errors["parametro"]' #ne restituisce l'incertezza
'print(fit.ndof)' #restituisce i gradi di libertà


#SIMULAZIONI TOY

'servono per simulare più prese dati'
#ex. N_toy = 20   valore_serve = []   for i in range (N_toy): ... valore_serve.append(valore trovato)


#INTEGRAZIONE

'hit or miss' #tipo try and catch, genero numeri, vedo quando cadono sotto funzione. A è l'area del rettangono in cui sono generati gli estremi, 
              #ma mandato tendente a infinito. per eseguirlo mi serve il valore più alto di y np.max(y). 
'crude MC'    #sfrutto il valore di aspettazione della funzione

#Tramite integrazione posso normalizzare l'area delle pdf (le moltiplico per 1/A)

#CHI QUADRO E P-VALUE

'fare toy della distribuzione del chi2'
'Q2 = []'
'for i in range (N_toys):'
'''... fit ...'''
'''Q2.append(fit.fval)'''


'from scipy.stats import chi2'

'p_value_finale = 0'
'valore_fit_best = 0'
'modelli = []'

'for mod in modelli: '
'''p_value = 1- chi2.cdf(mod.fval, df = mod.ndov)'''
'''if p_value > p_value_finale:'''
'''''p_value_finale = p_value'''''
'''''valore_fit_best = mod.values[parametro che voglio]'''''
'''''count += 1'''''
  


    
    
    
    
