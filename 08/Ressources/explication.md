# Explication

En inspectant le code source, on observe dans le footer un `BornToSec`.
En cliquant sur celui-ci, nous sommes redirigés vers :

http://10.11.200.169/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c

En inspectant le code source de cette page on observe un commentaire avec 2 indices:
    - "Let's use this browser : "ft_bornToSec". It will help you a lot."
    - "You must cumming from : "https://www.nsa.gov/" to go to the next step"
  
On modifie la requête en changeant les champs :
```
    Referer https://www.nsa.gov/ 
	User-Agent: ft_bornToSec
```

Le flag `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188` s'affiche.

# Comment profiter de la faille ?

Par exemple, considérons une page "réinitialiser le mot de passe" avec un lien de média social dans un pied de page. Si le lien a été suivi, en fonction de la manière dont les informations ont été partagées, le site  peut recevoir l'URL de réinitialisation de mot de passe et peut toujours utiliser les informations partagées, ce qui peut compromettre la sécurité de l'utilisateur.

# Comment la fixe ?

Afin de limiter ce risque, la plus simple et qu'on préfère, c'est de ne pas de pas permettre le tracking. Pour se faire, on peut mettre dans le header de la requête:
```
    Referrer-Policy: no-referrer
```