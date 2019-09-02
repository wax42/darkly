# Explication

Nom de la faille: htpasswd

On a regardé le fichier robots.txt du site. Celui-ci est composé de 2 dossiers:

```
    Results:
	User-agent: *
	Disallow: /whatever
	Disallow: /.hidden
```

Apres avoir inspecter le dossier /whatever, on remarque la présence d'un fichier htpasswd.
http://10.11.200.169/whatever/htpasswd

```
    root:8621ffdbc5698829397d97767ac13db3
```

On constate un format de fichier de type login:password.

On decrypte alors le hash avec md5 et on obtient `dragon`.

On se rend sur la page http://10.11.200.169/admin .

```
    Username: root
	Password: dragon
```

On obtient alors le flag `d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff`

# Comment profiter de la faille ?

En devenant administrateur, le hackeur obtient plus de droits. Il peut donc profiter de la faille.

# Comment la fixe ?

En faisant un chmod 640 sur le fichier htpasswd. On perd le droit de lecture.
