# Extracteur d'information à partir de diapositives

WIP
Titre temporaire
Version : 0.1
Author : Samy Gascoin-Fontaine

Le but de ce projet est de permettre une exploitation plus facile des données textuelles contenues dans une présentation. Le principe est le suivant : traiter le fichier dans son format d'origine (actuellement, il est prévu de gérer .pptx, beamer et odp). On le transforme en un Json intermédiaire que l'on va interroger. 
Ce Json garde les informations de hiérarchie entre slides, et de mise en forme du texte.


## Références : 

Ce code utilise la bibilothèque python-pptx pour parser les doucment pptx

https://github.com/scanny/python-pptx
