# Python Professional

## Modulo mypy

El modulo **mypy** se complementa con el modulo typing ya que permitira motrar mostrar los errores de tipado debil en Python.
Para revisar si algun archivo contiene errores de tipado, ejecutamos en la linea de comandos lo siguiente:

**mypy archivo.py --check-untyped-defs**

Como resultado nos mostrara si existe algun error de compatibilidad de tipos.


## Scope

El scope es el alcance que tienen las variables. Depende de donde declares o inicialices una variable para saber si tienes acceso. Regla de oro:

*Una variable solo esta disponible dentro de la region donde fue creada*

### Local Scope

Es la región que corresponde el ámbito de una función, donde podremos tener una o mas variables, las variables van a ser accesibles únicamente en esta region y no serán visibles para otras regiones

### Global Scope

Al escribir una o mas variables en esta region, estas podrán ser accesibles desde cualquier parte del código.


## Closures

### Reglas para encontrar un closure:

* Debemos tener una nested function.
* La nested function debe referenciar un valor de un scope superior.
* La funcion que envuelve a la nested function debe retornarla tambien.


## Decorators

Funcion que recibe como parametro otra funcion, le añade cosas, y retorna una funcion diferente.


## Generators

### Los Generadores son iteradores con Sugar Syntax.

**Yield** es una palabra clave que se usa para retornar de una función sin destruir los estados de las variables locales y cuando se llama a la función, la ejecución comienza desde el último yield declarado. Toda función que contenga la palabra clave yield es denominada como un generador.



## Sets

*Conjuntos: Una colección desordenada de elementos únicos e inmutables.*

**Características:**

Un set al ser impreso puede presentar diferente orden al definido pues Python los ordena a modo de optimizar/ahorrar memoria: un set es una colección desordenada.
En caso de existir elementos repetidos, los elimina, pues: un set es una lista de elementos únicos.
En caso de indicar una lista, por ejemplo, en un set este nos arroja un error, dado que: un set es inmutable.
Al set no se puede acceder con un índice.

Para declarar un set, el grupo de elementos debe ir entre llaves. Se diferencia de los diccionarios ya que no contienen el símbolo “:”, por lo que automáticamente Python lo entiende como un set de datos.

En caso de desear declarar un set vacío no es posible usar llaves ya que al no contener datos entre las llaves las interpreta como un diccionario. En este caso la declaración de un set debe ser explicita mediante el comando set()

**Casting con Sets**

Para convertir una estructura de datos a un set se utiliza el comando set()

Si se castea una lista a un set como resultado tenemos un set de elementos únicos ya que elimina los elementos repetidos. Los elementos mutables, en caso de existir, este comando los eliminará.

**Agregando elementos a un Set**

Para agregar un solo elemento se utiliza el método .add de los sets, en cambio, para agregar múltiples elementos se utiliza el método .update. En ambos se eliminan todos los elementos que fuesen repetido en el set o mutables.

**Eliminando elementos de un Set**

Existen 4 métodos:

* discard() = Se indica como parámetro el elemento a eliminar, en caso de no exisitir el elemento no realiza ninguna operación y continúa con la ejecución.
* remove() = También se indica como parámetro el elemento a eliminar, pero en este caso si no exististe el elemento arroja un error (KeyError) y detiene la ejecución.
* pop() = Elimina un elemento del set de manera aleatoria.
* clear() = Limpia el set completo.