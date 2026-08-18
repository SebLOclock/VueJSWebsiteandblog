---
title: "Coder avec l'IA sans finir avec du plat de spaghettis : trois méthodes que j'ai testées"
slug: "trois-methodes-coder-avec-lia"
date: "2026-08-19"
author: "Sebastien LEMOINE"
excerpt: "Le vibe coding, ça marche très bien pendant vingt minutes. Et puis ça part en vrille. Trois méthodes tentent de mettre un peu de structure là-dedans, et elles n'ont vraiment rien à voir les unes avec les autres."
image: "/images/blog/methodes-coder-ia.webp"
---

Depuis quelques mois, ou quelques années pour les plus anticipateurs, vous chantez un nouveau refrain dans votre façon de travailler. Vous ouvrez votre meilleur agent IA, vous tapez une phrase, et en l'espace de quelques secondes à peine, vous vous retrouvez avec un truc fonctionnel. Magique !

Deux heures après, vous demandez une modif toute bête. L'agent réécrit la moitié de ce qu'il vous avait généré juste avant, casse une partie du code, oublie de reprendre le bon ton dans un paragraphe, modifie la couleur de fond d'une image sans que vous lui ayez demandé, bref il pète tout ! Et vous vous retrouvez à lui redonner une tonne d'instructions ou à retravailler, vous-même, sur un texte, un code, une image que vous voyez réellement pour la première fois. Bienvenue dans le vibe coding ! Vos échanges informels avec la machine qui crée des trucs bluffants au début et finit par vous servir un plat de spaghetti tiède ensuite.

Le caillou dans la chaussure, c'est pas l'IA mais plutôt l'absence même de structure autour. En fin de compte, le vibe coding souffre du même problème que le code. Une appli codée à l'arrache peu importe où et par qui mais qui n'a pas été conçue, réfléchie, prouvée en amont a de bonnes chances de se retrouver complètement buggée dès son lancement. Souvent par manque d'envie, de temps ou même par philosophie. « Bof, tester c'est douter ! » se répétait l'équipe commerciale de Cyberpunk 2077 pour économiser quelques dollars. Du coup, des gens plutôt malins et qui avaient sans doute fait le parallèle entre les difficultés rencontrées dans le vibe coding et les projets moins bien structurés avant l'apparition de l'IA, ont creusé le sujet histoire de mettre un peu d'ordre dans ce joyeux bordel. J'en ai testé trois très opposées dans leur approche et voici ce que je peux en dire aujourd'hui.

## BMAD : l'IA rejoue toute une équipe projet

BMAD, ça veut dire Breakthrough Method for Agile AI-Driven Development. Bon BMAD c'est bien au final. L'idée derrière ce nom à rallonge est assez simple : plutôt que de demander à un seul agent d'endosser l'ensemble des rôles nécessaires à la bonne conduite du projet, on répartit les rôles sur différents agents, chacun avec sa casquette précise. Un analyste qui va explorer le besoin, un product manager qui rédige les specs fonctionnelles, un architecte qui pose la structure technique, un dev qui implémente, un QA qui teste. Bref une vraie équipe de spécialistes qui ont leurs propres définitions, leur propre périmètre et leurs propres responsabilités.

Ce qui me plaît dans cette méthode, c'est qu'on passe par des étapes qu'on aurait d'instinct mis de côté dans un projet solo. Soyons honnête cinq minutes, quand on a une idée, un besoin, on veut le résultat le plus vite possible. Dopamine power ! Ici, chaque décision, chaque changement est documenté avant même de passer à l'implémentation. Et, quand vous ou un agent revenez dessus deux jours plus tard, le contexte est déjà là posé noir sur blanc et pas uniquement du code à relire pour essayer de se souvenir où on en était.

La limite, c'est que ça reste un processus de planification. BMAD structure très bien l'amont. Il vérifie moins bien si le résultat final est réellement bon.

## Gauntlet Loop : le bruteforce du vibe coding

Alors lui, il est tout neuf. Mon expérience avec cette méthode est un peu en construction mais elle apporte vraiment quelque chose. Ici on change complètement de logique. Le Gauntlet Loop, popularisé par Matt Shumer, ne part pas du principe qu'il faut mieux planifier, mais plutôt de celui qu'il faut mieux vérifier.

Le fonctionnement : un agent principal découpe l'objectif en sous-parties. Chaque sous-partie est ensuite confiée à un sous-agent Builder. Surtout, chacun de ces sous-agents est associé à un autre sous-agent critique, dans un contexte complètement vide, qui compare le produit à une référence concrète, un produit existant et dont la légitimité ne fait pas débat. Tant que le critique ne valide pas, le builder recommence.

Je suis en train d'expérimenter quelques trucs autour de cette méthode et, ce qui me frappe, c'est la brutalité assumée du dispositif. Le critique n'a aucune idée de ce que le builder a essayé de faire ni même pourquoi. Il ne fait que comparer, à l'aveugle, le résultat à la barre fixée. Aucune complaisance, le builder subit sans pouvoir se justifier.

## Spec-Driven Development : le cahier des charges devient la seule vérité

Encore une nouvelle approche. Le Spec-Driven Development, porté notamment par GitHub Spec Kit et AWS Kiro, part d'un postulat un peu provoc pour les devs. Le code n'est plus vraiment ce qu'on édite, c'est la spec qui compte.

Concrètement, l'idée est de rédiger un cahier des charges très précis, avec des critères d'acceptation, parfois même avec une notation formelle du style :

> « QUAND telle condition, LE SYSTÈME DOIT tel comportement »

Le code est ensuite généré à partir de cette spec, un peu comme un fichier source compilé en binaire. Si le besoin change, on modifie pas le code à la main, on modifie la spec et on régénère derrière.

L'avantage, un peu comme pour BMAD, c'est la traçabilité. On sait pourquoi telle ou telle feature existe en suivant le cahier des charges qui est la source de vérité, contrairement au code qui est presque jetable.

## Trois outils, trois usages, pas de méthode universelle

Aucune de ces méthodes ne règle tout, et c'est très bien comme ça.

On va plutôt définir des cas d'usage de ces méthodes, des contextes où elles seraient à privilégier sans pour autant mettre de côté leurs limites :

BMAD, je l'utiliserais sur des projets ambitieux avec plusieurs modules différents. C'est celle qui cadrera le mieux le projet en amont, notamment si votre idée de départ tient en une phrase.

Gauntlet Loop, c'est une méthode qui a un prérequis de départ. Avoir une référence clairement identifiée qu'on veut égaler voire dépasser. « Je veux refaire cette app mais en mieux ! »

Et enfin, le Spec-Driven Development va nécessiter un cahier des charges de départ très précis, mais va vous garantir la traçabilité et surtout de ne jamais sortir du périmètre défini par vos specs.

Et pour un proto tout bête un dimanche matin ? Si l'idée c'est juste de prouver un concept ou combler un besoin rapide, ne vous prenez pas plus la tête qu'un vibe coding classique. Dans ce cas, vous recherchez surtout le résultat rapide et ces méthodes ont un coût en temps et en tokens non négligeable.

## Ce que ça dit du rapport qu'on construit avec l'IA

Ce qui me frappe le plus en creusant ces différentes approches, c'est qu'elles répondent toutes au même constat de base : livré à lui-même, l'agent va produire un travail plausible mais pas un travail vérifié. Leur différence tient surtout à où elles situent le garde-fou. Là où BMAD va faire la vérification en amont du développement, Gauntlet Loop vérifiera tout au long de l'implémentation. Et, SDD va quant à lui cadrer directement dans le contrat de départ.

Je faisais déjà ce constat il y a quelques semaines : une réponse plausible, même bien présentée, n'est pas forcément juste. Force est de constater que ça se vérifie aussi en vibe coding. Ces méthodes tentent aujourd'hui de recréer artificiellement ce que la vérification humaine faisait naturellement avant qu'on délègue une partie du boulot à une machine qui, elle, ne doute jamais d'elle-même.