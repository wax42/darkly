# Explication

nom de la faille:  html injection

On va sur l'URL http://10.11.200.169/?page=feedback.

Dans le premier input on peut injecter très facilement des balises html (p, script, i, ...).

# Comment profiter de la faille ?

Le hacker peut changer l'apparence du site. Il peut récuperer des données en mettant par exemple de faux formulaires.

Cependant, ce type d'injection est assez rare et comporte un risque relativement faible comparé aux autres injections (JS injection, SQL injection, ...).

# Comment la fix

Ce type d'injection peut être évité en verifiant les inputs et outputs.

Sur tous les inputs, on doit vérifier si la valeur envoyée ne contient pas de balises HTML.
