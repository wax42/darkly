# Explication

nom de la faille: hidden_file

On a regardé le fichier robots.txt du site. Celui-ci est composé de 2 dossiers:

```
    Results:
	User-agent: *
	Disallow: /whatever
	Disallow: /.hidden
```

En inspectant le dossier .hidden, on constante toute une arborescence qui se termine à chaque fois par un README.

On a donc fait un scraper python afin de parcourir recursivement ce dossier.

Le but de ce script est d'ouvrir tous les README afin de trouver le flag.

# Comment profiter de la faille ?

En soit, ceci n'est pas vraiment une faille. Il y a peu d'intérêt de créer une telle arborescence afin de cacher des données sensibles.
