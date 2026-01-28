# Projet McFlow - Justifications Techniques

## 1) Décisions Mobile First
**Priorité au-dessus de la ligne de flottaison :**
J'ai choisi d'afficher uniquement le **H1 (Problème)**, la **Promesse**, le **CTA** et le **Graphique (LCP)**.
*Pourquoi :* Sur mobile, l'utilisateur est pressé. Il doit comprendre la valeur ajoutée (l'anticipation du rush) en moins de 3 secondes sans avoir à scroller. C'est la zone la plus accessible au pouce ("Thumb Zone").

**Éléments masqués/différés sur mobile :**
* Le menu de navigation complet (`nav ul { display: none }`).
* Le bloc secondaire de téléchargement PDF (`aside { display: none }`).
*Pourquoi :* Le menu prendrait trop de hauteur verticale. L'aside est un objectif secondaire qui ne doit pas distraire de l'objectif principal (l'inscription).

## 2) Responsive Desktop
**Breakpoint choisi :**
`900px` (`@media (min-width: 900px)`).
*Pourquoi :* C'est une largeur standard où les tablettes en mode paysage et les petits ordinateurs portables ont assez de place pour afficher des colonnes côte à côte confortablement.

**Enrichissements Desktop :**
* **Header :** Passage en `sticky` avec menu visible et bouton "Connexion" stylisé.
* **Hero :** Centrage du contenu pour un look plus "éditorial".
* **Grilles :** Passage des Fonctionnalités en 3 colonnes et des Avis en 2 colonnes via `display: grid`.
* **Aside :** Réapparition du bloc PDF en bas de page pour capter les utilisateurs non convertis.

## 3) Performance
**LCP identifié (Largest Contentful Paint) :**
L'élément est l'image du graphique dans la section Hero : `<img src="courbe.webp" ...>`.

**Deux actions d'optimisation décidées :**
1.  **Format moderne :** Conversion de l'image PNG en **WebP** (réduction de poids de ~40% pour un chargement plus rapide).
2.  **Stabilité (CLS) :** Ajout des attributs `width="600"` et `height="300"` dans le HTML.
*Pourquoi :* Cela permet au navigateur de réserver l'espace de l'image avant son chargement, évitant que le texte ne saute (Layout Shift) pendant l'affichage.