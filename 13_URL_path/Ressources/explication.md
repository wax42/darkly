# Explication

nom de la faille: URL_path

En testant plusieurs, valeurs différentes sur le paramètre page de l'URL.

On constate que à chaque fois qu'on descend en profondeur dans l'arborescence.

http://10.11.200.169?page=../../../../etc/passwd

Le message d'alert change.

Arrivé à une profondeur de 7 et + .

http://10.11.200.169/?page=../../../../../../../etc/passwd

On obtient le flag: `b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0`

# Comment profiter de la faille ?

Dans les anciennes versions d'Unix, dans le fichier /etc/passwd. Il y avait le mot de passe et le nom des users en clair.
Aujourd'hui en ayant accès à ce fichier, nous pouvons juste lister le nom des users sur le serveur.

# Comment la fix

Afin d'éviter cette faille, une `whitelist` doit être présente dans un fichier de configuration sur le serveur ou sur la base de donnée qui contient la liste que le paramètre page peut accepter.
