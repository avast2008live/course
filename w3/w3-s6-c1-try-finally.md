---
jupytext:
  cell_metadata_filter: all
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: try..else..finally
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# `try` … `else` … `finally`

+++

## Complément - niveau intermédiaire

+++

L'instruction `try` est généralement assortie d'une une ou plusieurs clauses `except`, comme on l'a vu dans la vidéo.

Sachez que l'on peut aussi utiliser - après toutes les clauses `except` :

* une clause `else`, qui va être exécutée si aucune exception n'est attrapée ;
* et/ou une clause `finally` qui sera alors exécutée quoi qu'il arrive.

+++

Voyons cela sur des exemples.

+++

### `finally`

+++

C'est sans doute `finally` qui est la plus utile de ces deux clauses, car elle permet de faire un nettoyage **dans tous les cas de figure** - de ce point de vue, cela rappelle un peu les *context managers*.

Et par exemple, comme avec les *context managers*, une fonction peut faire des choses même après un `return`.

```{code-cell}
# une fonction qui fait des choses après un return
def return_with_finally(number):
    try:
        return 1/number
    except ZeroDivisionError as e:
        print(f"OOPS, {type(e)}, {e}")
        return("zero-divide")
    finally:
        print("on passe ici même si on a vu un return")
```

```{code-cell}
# sans exception
return_with_finally(1)
```

```{code-cell}
# avec exception
return_with_finally(0)
```

### `else`

+++

La logique ici est assez similaire, sauf que le code du `else` n'est exécuté que dans le cas où aucune exception n'est attrapée.

+++

En première approximation, on pourrait penser que c'est équivalent de mettre du code dans la clause `else` ou à la fin de la clause `try`. En fait il y a une différence subtile :

> *The use of the `else` clause is better than adding additional code to the `try` clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the `try` … `except` statement.*

Dit autrement, si le code dans la clause `else` lève une exception, celle-ci ne **sera pas attrapée** par le `try` courant, et sera donc propagée.

+++

Voici un exemple rapide, en pratique on rencontre assez peu souvent une clause `else` dans un `try` :

```{code-cell}
# pour montrer la clause else dans un usage banal
def function_with_else(number):
    try:
        x = 1/number
    except ZeroDivisionError as e:
        print(f"OOPS, {type(e)}, {e}")
    else:
        print("on passe ici seulement avec un nombre non nul")
    return 'something else'
```

```{code-cell}
# sans exception
function_with_else(1)
```

```{code-cell}
# avec exception
function_with_else(0)
```

Remarquez que `else` ne présente pas cette particularité de "traverser" le `return`, que l'on a vue avec `finally` :

```{code-cell}
# la clause else ne traverse pas les return
def return_with_else(number):
    try:
        return 1/number
    except ZeroDivisionError as e:
        print(f"OOPS, {type(e)}, {e}")
        return("zero-divide")
    else:
        print("on ne passe jamais ici à cause des return")
```

```{code-cell}
# sans exception
return_with_else(1)
```

```{code-cell}
# avec exception
return_with_else(0)
```

### Pour en savoir plus

+++

Voyez [le tutorial sur les exceptions](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) dans la documentation officielle.