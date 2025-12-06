# IDEAS GENERALES

La idea del programa es representar la sopa de letras como una matriz $n \times n$, cuyo dominio que llamaremos **Posiciones** son los pares ordenados $(x,y)$ pertenecientes al conjunto $[|0, n - 1|] \times [|0, n - 1|]$ (ej. $(4,5)$).

Los $x$ cumplen el rol de fila de la sopa de letras y los $y$ el rol de columna.

Y el codominio $(\{'a','b','c',...,'y','z'\} \times [|1, p|]) \cup \{('-',0)\}$, donde $p$ es la cantidad de palabras contenidas en la sopa de letras (ej. $('a', 3)$).

El par (String, entero) indica una letra y en segundo plano la cantidad de palabras que relacionadas con el elemento del dominio.

El elemento $('-', 0)$ del codominio cumple el rol de "nulo", es decir, no hay ninguna (letra, contador) asignada al elemento del dominio.

Para esta representación utilizaremos un diccionario **Posiciones**, donde cada clave del diccionario representa una tupla $(x,y)$ y es mapeada con una tupla (letra, contador). Ej. $\{(0,0) : ('g', 1)\}$.

Una **Palabra** (String) es representada como vector dentro de la matriz, ya que esta tienen módulo (Longitud del String), dirección (pares ordenados alineados) y sentido:
*   **ID**: palabras escritas de izquierda a derecha ('hola')
*   **DI**: palabras escritas de derecha a izquierda ('aloh')

La Longitud y el sentido están dados por el String y la dirección está dada por un subconjunto del dominio de la matriz que cumplen con las siguientes condiciones:

Sea $k$ la longitud de alguna palabra y $(i,j)$ el origen de su vector asociado:
*   **Dirección horizontal H**: $\{(i,j),(i, j+1), ... , (i, j+(k-1))\}$, con $0 \le j+(k-1) \le n-1$
*   **Dirección vertical V**: $\{(i,j),(i+1,j),...,(i+(k-1),j)\}$, con $0 \le i+(k-1) \le n-1$
*   **Dirección Diagonal de esquina sup. izq a Esquina inf der Dsi**: $\{(i,j),(i+1,j+1),...,(i+(k-1),j+(k-1))\}$, con $0 \le i+(k-1) \le n-1$ y $0 \le j+(k-1) \le n-1$
*   **Dirección Diagonal de esquina sup. der a Esquina inf izq Dsd**: $\{(i,j),(i+1,j-1),...,(i+(k-1),j-(k-1))\}$, con $0 \le i+(k-1) \le n-1$ y $0 \le j-(k-1) \le n-1$

## Complejidad

La Complejidad de la sopa de letras nos ponen ciertas condiciones extras a los vectores:

*   **Facil**: Vectores de tipo H o V sentido ID tales que sus respectivas posiciones sean disjuntas (no comparten posición, por lo tanto, las palabras no se cruzan).
*   **Medio**: Vectores de tipo H, V o Dsi con sentido ID tales que sus respectivas posiciones sean disjuntas.
*   **Dificil**: Vectores de todo tipo, tales que sus respectivas posiciones sean disjuntas.
*   **Muy dificil**: Vectores de todo tipo, tales que sus respectivas posiciones sean disjuntas o cada elemento de su intersección este mapeado a la misma letra.

## Candidatos

Como no toda combinación de vectores es válida, y la elección de un vector condiciona la elección de otros vectores, llamaremos **Candidatos** al conjunto de vectores que cumplen con las condiciones dadas por el tipo de complejidad y los candidatos elegidos previamente.

La idea es elegir un candidato por palabra y armar los candidatos para la próxima palabra en función de los candidatos ya elegidos.

Si al generar los candidatos para una palabra el resultado es el conjunto vacío, se vuelve la palabra anterior y se prueba con otro candidato.

El proceso termina cuando se obtiene un candidato por palabra (se puede generar la sopa de letras) o cuando el conjunto de candidatos es vacío para todas las palabras, lo cual implica que no es posible generar una sopa de letras con las palabras dadas y la complejidad.

Para poder generar Candidatos en función de las palabras ya elegidas se utiliza el diccionario `MatrizSopa` para guardar información de los vectores ya elegidos y en paralelo un diccionario `infoPalabras`, que guarda información de los candidatos en cada una de las palabras.

Una vez terminado el proceso de elección de Candidatos de forma satisfactoria, se completan las posiciones mapeadas al elemento nulo con una letra al azar de forma que no se generen palabras repetidas y se obtiene una sopa de letras válidas para el enunciado.
