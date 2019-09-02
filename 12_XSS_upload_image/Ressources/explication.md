# Explication

Nom de la faille: XSS_upload_image

En allant sur l'URl: http://10.11.200.169/\?page\=upload

On remarque qu'on peut upload une photo, en se renseignant sur la facon dont la photo s'upload on constate que ça recharge la page. En modifiant la requete `POST`, et en mettant dans le corps de la requête les élements du formulaires.

On obtient la commande `curl` suivante:

```
curl -F "uploaded=@test.php; type= image/jpeg" -F "Upload=Upload" http://10.11.200.169/\?page\=upload
```

Ce qu'on fait est une injection de PHP en mentant sur le type du fichier envoyé afin que le serveur l'accepte.

# Comment profiter de la faille ?

On peut profiter de la faille, en injectant du code qui peut avoir différentes actions.

Par exemple: - Un script qui va envoyé toutes les données passant par le serveur au serveur du hacker. - Un script qui permet de prendre le contrôle du serveur.( web-shell ) - Un script qui créer de fausses pages. ( Phishing )

# Comment la fixe ?

Uttiliser une blacklist ou une whitelist pour les extensions de fichier.
Limiter la taille du fichier.
Enrengistrer les fichiers dans un répertoire qui n'a pas les droits d'exécution.
