# Explication

Nom de la faille:   cookies

Aller sur l'url: `http://IP_DARKLY/`

En inspectant le header de la requête. On peut voir qu'il y a un cookie.

```
i_am_admin: 68934a3e9455fa72420237eb05902327
```

En decryptant, avec md5 on obtient la valeur `true`.

On a donc testé d'encrypter la valeur `false` avec md5.

```
false --> b326b5062b2f0e69046810717534cb09
```


Puis nous avons renvoyer la requête en remplaçant le cookie i_am_admin par le hash trouvé ci-dessus.


# Comment profiter de la faille ?

En devenant administrateur, le hackeur obtient plus de droits. Il peut donc profiter de la faille.


# Comment la fixe ?

Il est fortement déconseillé de stocker des mots de passes dans les cookies. Il est préférable de passer par un protocole de sécurité telle que OAuth, JWt ou autres.


De plus, l'algorithme de cryptage md5 n'est plus recommandé aujourd'hui car il existe de très grosses bases de données qui permettent de décrypter le hash.