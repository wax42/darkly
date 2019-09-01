# Explication

Nom de la faille:           inspect_recover_password?

Aller sur l'url: `http://IP_DARKLY/?page=recover`


Inspecter le code source de la page.
Changer le champ `value` de la balise `input` ayant pour champ `name`="mail" du formulaire.

Puis cliquer sur le bouton submit.

# Comment profiter de la faille ?


La faille est en réalité inconcevable.

Mais disons qu'elle existe vraiment sur certains sites.

Le hacker peut récupérer très simplement le mot de passe de n'importe quel utilisateur.

# Comment la fixe ?

Le traitement de l'information mot de passe oublié ne doit pas se passer côté client.
