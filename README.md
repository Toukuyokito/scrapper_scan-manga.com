# scrapper_scan-manga.com
Scrapper du site scan-manga.com, développé avec python.

## Un scrapper ?
Un scrapper est un programme d'extraction de contenu de sites web.

## Origine du projet
Ce projet à pour origine l'envie de dévelloper mes compétences en python / web.

## Composition du projet

### Objectif du projet
L'objectif du projet est de centraliser la recherche des nouveaux épisodes de mes séries sur le site [scan-manga.com](https://www.scan-manga.com).
Dans un usage normal, il faut aller sur la page de toutes les séries une par une, puis vérifier si un épisode est sorti.
Grâce à cet outil, il est possible en un seul clique de réaliser cette action.

### Partie frontEnd
La partie frondEnd est développée en JavaScript pur, HTML5 et CSS.
Elle est décomposée en deux parties : la page de scan et la page d'administration.

#### Page de scan
La page de scan est composée d'un bouton appelé **scan** pour lancer la recherche, d'un lien vers la page d'administration et d'un tableau permettant le bon affichage des données obtenues lors du scan.
![scan](https://user-images.githubusercontent.com/67798835/128612690-4abc32bb-24a9-4738-b798-4fcd9034b71c.png)

#### Page d'aministration
La page d'administration sert à rajouter et à supprimer des séries à notre scanner. Elle est composée d'un lien menant vers la page de scan et de deux formulaires un pour ajouter une série, l'autre pour supprimer des séries.
![admin](https://user-images.githubusercontent.com/67798835/128612803-50e929a0-5a2d-4ebd-b67a-f88c20d72bfb.png)

### Partie backEnd
La partie backEnd est développée avec python grâce au framework Flask. Elle permet le stockage des séries et la cohérence du site web (accès aux différentes pages). La réponse à une requête émise depuis la partie frontEnd sera toujours au format JSON.

## Démonstration
https://user-images.githubusercontent.com/67798835/128612187-feb37626-902b-4f6f-9622-687f40f9656b.mov

