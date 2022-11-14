import numpy as matrix #numpy es una libreria para manejo de matrices
import plotly.express as px #plotly es una libreria para graficar

paises = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay",
             "Peru", "Suriname", "Uruguay", "Venezuela"]

colores = ["blue", "green", "red", "yellow"] #colores disponibles para colorear el mapa

def esPosible(paisVecino, color):
   
    for i in range(13): #comprueba cada arista
        for j in range(i + 1, 13):
            if (paisVecino[i][j] and color[j] == color[i]):
                return False
    return True

def colorearMapa(paisVecino, m, i, color):

    if (i == 13): 
        if (esPosible(paisVecino, color)): 
            mapaColoreado(color)  # imprime el mapa coloreado
            return True
        return False
  
    
    for j in range(1, m + 1): # asigna el color actual a la posicion actual
        color[i] = j
        if (colorearMapa(paisVecino, m, i + 1, color)):
            return True
        color[i] = 0
    return False

    
     

def mapaColoreado(color): #imprime los colores con los que se coloreo el mapa
    
    for i in range(13):
        if color[i]==1:
            color[i]=colores[0]
        elif color[i]==2 :
            color[i]=colores[1]
        elif color[i]==3:    
            color[i]=colores[2]
        elif color[i]==4:
            color[i]=colores[3]
        elif color[i]==0 :  
            color[i]="white"
     
               
    plot_choropleth(color)  #Funcion predefinida para graficar el mapa, no es parte del algoritmo

  
def plot_choropleth(colormap): #Funcion predefinida para graficar el mapa, no es parte del algoritmo
  fig=px.choropleth(locationmode="country names",
                  locations=paises,
                  color=paises,
                  color_discrete_sequence=colormap,
                  scope="south america")
  fig.show()    
  
if __name__ == "__main__":

    paisVecino = [ # matriz de adyacencia de cada pais con sus vecinos
                    # 1 si son vecinos, 0 si no lo son

        [ 0, 1, 1, 1 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0], # Argentina
        [ 1, 0, 1, 1 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,0], # Bolivia
        [ 1, 1, 0, 0 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1], # Brazil
        [ 1, 1, 0, 0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0], # Chile
        [ 0, 0, 1, 0 ,0 ,1, 0, 0, 0, 1, 0, 0 ,1], # Colombia
        [ 0, 0, 0, 0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0], # Ecuador
        [ 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0], # Islas Malvinas
        [ 0, 0, 1, 0 ,0 ,0, 0 ,0 ,0 ,0 ,1 ,0 ,1], # Guyana
        [ 1, 1, 1, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0], # Paraguay
        [ 0, 1, 1, 1 ,1 ,1, 0 ,0 ,0 ,0 ,0 ,0 ,0], # Peru
        [ 0, 0, 1, 0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0], # Suriname
        [ 0, 0, 1, 0 ,0 ,0, 0, 1, 0 ,0 ,0 ,0 ,0], # Uruguay
        [ 0, 0, 1, 0 ,1 ,0, 0, 1, 0, 0, 0, 0 ,0], # Venezuela
    ]
    c = 4 # numero de colores disponibles para colorear el mapa
   
    color = [0 for i in range(13)]
    print("\n" + "\033[;31m" + " Hola, este es un programa para colorear mapas" + "\033[0m" + "\n") 
    print("\033[;31m" + "*-~--~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~--~*" + "\033[0m") 
    print("\033[;31m" + "* Por favor espera unos segundos, tu mapa está siendo coloreado con solo 4 colores *" + "\033[0m") 
    print("\033[;31m" + "*-~--~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~--~*" + "\033[0m" + "\n") 
    print("\033[36mEl proceso ha terminado, disfruta tu mapa coloreado\033[0m") 
    print("\033[36mGracias por usar el programa :'D \033[0m" + "\n")      
  
    if (not colorearMapa(paisVecino, c, 0, color)): 
        print ("No se puede colorear el mapa con los colores dados" + "\n")

    colormap_test = {"Argentina": "blue", "Bolivia": "red", "Brazil": "yellow", "Chile": "yellow", "Colombia": "red",
                     "Ecuador": "yellow", "Falkland Islands": "yellow", "Guyana": "red", "Paraguay": "green",
                     "Peru": "green", "Suriname": "green", "Uruguay": "red", "Venezuela": "green"}  #colores de prueba
    
    color_discrete_sequence=[colormap_test[c] for c in paises]   # (no es parte del algoritmo, es parte de la funcion plot_choropleth)
    if (not esPosible(paisVecino,color_discrete_sequence)):  
        print ("\n No se puede colorear el mapa con los colores dados")
    else:    
        mapaColoreado(color_discrete_sequence) #imprime el mapa coloreado
