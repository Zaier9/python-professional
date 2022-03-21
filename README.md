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