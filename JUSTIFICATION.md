# McFlow - Gestion de rush par IA

## 1) Décisions Mobile First
- **Priorité au-dessus de la ligne de flottaison :**
  J'ai choisi d'afficher uniquement l'essentiel immédiat : le Titre H1 (le problème), la promesse (la solution), le bouton CTA (l'action) et l'image du graphique (la preuve visuelle).
- **Éléments masqués/différés sur mobile :**
  - Le menu de navigation complet (`nav ul { display: none; }`).
  - Le bloc latéral "Aside" proposant le PDF (`aside { display: none; }`).
- **Pourquoi :**
  Sur mobile, l'espace écran est limité et l'attention de l'utilisateur est courte. Le menu et le téléchargement PDF sont des distractions qui éloignent de l'objectif principal (cliquer sur "Démarrer l'essai"). La navigation verticale doit rester fluide sans pollution visuelle.

## 2) Responsive desktop
- **Breakpoint(s) choisi(s) :**
  `900px` (`@media (min-width: 900px)`).
- **Enrichissements desktop :**
  - **Header Premium :** Le menu devient visible à l'horizontale, le header devient "Sticky" (fixe) avec un effet de flou (Glassmorphism) et le bouton Connexion est mis en valeur.
  - **Layout Grille :** Passage d'une pile verticale à des grilles (`display: grid`) : 3 colonnes pour les fonctionnalités et 2 colonnes pour les avis.
  - **Réintégration :** Le bloc Aside (Guide PDF) réapparaît en bas de page pour capter les utilisateurs indécis.
- **Pourquoi :**
  Ce breakpoint correspond aux tablettes en mode paysage et aux petits ordinateurs portables. La largeur disponible permet d'afficher du contenu côte à côte (colonnes) pour réduire la hauteur de page et donner un aspect plus "logiciel professionnel" sans nuire à la lisibilité.

## 3) Performance
- **LCP identifié (élément + section HTML) :**
  L'élément LCP (Largest Contentful Paint) est l'image du graphique dans la première section Hero : `<img src="images/courbe.webp" ...>`.
- **Deux actions max décidées :**
  1. **Optimisation du format :** Conversion de l'image originale `.png` vers le format `.webp` (réduction de poids d'environ 40%).
  2. **Stabilité visuelle (CLS) :** Ajout explicite des attributs `width="600"` et `height="300"` dans la balise HTML.
- **Pourquoi :**
  L'image est l'élément le plus lourd visible au chargement. Le passage en WebP accélère l'affichage sur les réseaux mobiles. Fixer les dimensions permet au navigateur de réserver l'espace avant le chargement de l'image, empêchant le texte de sauter (Cumulative Layout Shift) et améliorant l'expérience utilisateur.