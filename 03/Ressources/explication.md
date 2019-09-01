# Explication

Nom de la faille: redirect

En inspectant le code source, nous pouvans constater que dans le `footer` se trouve un lien dans une balise `href` qui contient une redirection.

En copiant le lien et modifiant le site de la redirection. Nous tombons sur le flag.

Aller sur l'url: `http://IP_DARKLY/index.php?page=redirect&site=`

# Comment profiter de la faille ?

Le hacker peut profiter de la faille en mettant un autre site dans la redirection.

Il peut ainsi rediriger le client vers des faux sites. ( `Phishing`)
Ou bien le rediriger vers un site qui va télecharger des virus.

# Comment la fixe ?

Afin d'éviter cette faille, une `whitelist` doit être présente dans un fichier de configuration sur le serveur ou sur la base de donnée qui contient la liste des domaines pouvant être uttilisée afin de filtrer les redirections.

Pour sécuriser encore plus les redirections, celles-ci ne doivent pas prendre en parametre l'URL de la redirection mais son index dans la `whitelist`.
