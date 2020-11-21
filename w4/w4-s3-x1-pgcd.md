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
notebookname: PGCD
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Calculer le PGCD

+++

## Exercice - niveau basique

```{code-cell}
# chargement de l'exercice
from corrections.exo_pgcd import exo_pgcd
```

On vous demande d'écrire une fonction qui calcule le PGCD de deux entiers, en utilisant [l'algorithme d'Euclide](http://fr.wikipedia.org/wiki/Algorithme_d'Euclide).

+++

Les deux paramètres sont supposés être des entiers positifs ou nuls (pas la peine de le vérifier). 

Dans le cas où un des deux paramètres est nul, le PGCD vaut l'autre paramètre. Ainsi par exemple:

```{code-cell}
exo_pgcd.example()
```

**Remarque** on peut tout à fait utiliser une fonction récursive pour implémenter l'algorithme d'Euclide. Par exemple cette version de `pgcd` fonctionne très bien aussi (en supposant a>=b)

```python
def pgcd(a, b):
    "Le PGCD avec une fonction récursive"
    if not b:
        return a
    return pgcd(b, a % b)
```

Cependant, il vous est demandé ici d'utiliser une boucle `while`, qui est le sujet de la séquence, pour implémenter `pgcd`.

```{code-cell}
# à vous de jouer
def pgcd(a, b):
    "<votre code>"
```

```{code-cell}
# pour vérifier votre code
exo_pgcd.correction(pgcd)
```