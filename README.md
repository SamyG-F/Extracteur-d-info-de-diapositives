# Extracteur d'information à partir de diapositives

WIP

Titre temporaire

Version : 0.1

Author : Samy Gascoin-Fontaine

Le but de ce projet est de permettre une exploitation plus facile des données textuelles contenues dans une présentation. Le principe est le suivant : traiter le fichier dans son format d'origine (actuellement, il est prévu de gérer .pptx, beamer et odp). On le transforme en un Json intermédiaire que l'on va interroger. 

Ce Json garde les informations de hiérarchie entre slides (deepness), et de mise en forme du texte.

## Description des fichiers :

fichier utilisé lors des tests : data/CM1_React.pptx

### /pptx : Transformation de .pptx en Json

1ère version : pptx_to_Json.py avec le test associé test.txt

version actuelle : pptx_to_Json_Samy.py avec le test associé test_Samy.txt

## Spécification du Json :

La spécification du Json est dans 'spec_Json.txt'	        

Un exemple de sortie Json suivant cette spécification se trouve dans pptx/test_Samy.txt


## TODOS :

Interrogation du Json à mettre en place

## Références : 

Ce code utilise la bibilothèque python-pptx pour parser les documents pptx

https://github.com/scanny/python-pptx
