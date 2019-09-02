# Explication


Nom de la faille:  data_validation

Aller sur l'url: `http://10.11.200.169/index.php?page=survey#`


Inspecter le code source de la page.
Changer le champ `value` d'une balise `option` à 11, des `select` du formulaire.
Puis cliquer sur la balise `option` qui a été modifiée.


# Comment profiter de la faille ?

Le hacker peut transmettre des valeurs, qui ne sont pas prises en compte dans le backend.

Ce qui peut provoquer tout sorte de Hack.

Par exemple:

Le hacker peut injecter du code dans la valeur. Si cette valeur n'est pas vérifiée et directement envoyée en tant que requête SQL. Celà peut conduire à une faille d'injection SQl.

Le hacker peut faire des "overflow" et faire crash le serveur en mettant des INT_MAX

# Comment la fixe ?


En sécurisant les valeurs reçues de la part du client.
C'est à dire: L'interval des valeurs, le type des valeurs.
La sécurité peut se faire du côté client et serveur.

De base,  il ne faut pas faire confiance aux informations qui viennent du client.

