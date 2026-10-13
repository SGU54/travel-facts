# Astra review — pins : système et design, 2026-09-18

## Verdict en cinq lignes

Le format vertical et les trois familles constituent une base exploitable, mais pas encore un système de production fiable.
La hiérarchie rend les titres visibles et les informations qui les qualifient presque microscopiques.
Le comparateur peut transformer deux nombres exacts en une comparaison trompeuse ; la destination imposée aux listes peut également rompre la promesse.
Deux protections annoncées comme acquises sont défectueuses : les miniatures de contrôle et l’ancrage du bandeau B.
Il faut conserver une grammaire commune, puis spécifier les contrats de contenu, les variantes de densité et les conditions d’export.

## Périmètre et méthode

J’ai lu les **cinq fichiers** de `pins.skill`, soit environ 756 lignes : doctrine, copy, templates, exemple Rome et moteur Python. Le dossier fourni ne contient pas de pins livrés. Ce n’est donc **pas** l’expérience comparative à trois marques du dossier : je ne prétends pas observer des défauts partagés par trois productions indépendantes.

J’ai rendu les **12 entrées de `references/pins_rome_example.py`**, sans modifier le moteur, avec Playwright/Chromium installé localement, sur le canevas prescrit de **1000 × 1500 CSS px, DPR 2**, soit **2000 × 3000 pixels**. Pour comparer la composition sans dépendre des photos, les huit A/B utilisent volontairement le mode placeholder. Les polices Google nécessaires au rendu normal ont chargé. Les illustrations ici sont des **reproductions de l’exemple**, pas des publications réelles.

La [planche des 12 rendus](review-evidence/contact.png) juxtapose des réductions indépendantes à **236 × 354 px**, obtenues à partir des PNG effectivement produits. Les preuves natives du moteur sont examinées séparément en B1. Les [mesures DOM](review-evidence/metrics.json), [contrôles ciblés](review-evidence/checks.json), scripts de reproduction et empreinte SHA-256 de l’archive sont conservés dans `review-evidence/`.

Pour reproduire les mesures depuis le dossier `pins/`, avec Playwright, son Chromium et Pillow installés :

```sh
python3 -m zipfile -e pins.skill /tmp/astra-pins-review
python3 review-evidence/probe.py
python3 review-evidence/checks.py
```

Ces scripts écrivent dans `/tmp/astra-pins-review` et utilisent les polices distantes de l’exemple ; ils ne publient rien.

Les chemins de code ci-dessous sont internes à l’archive, sous `pins/`. Le **rang de coût** est global : 1 = conséquence la plus grave. `CERTAIN` désigne un mécanisme ou résultat directement vérifiable ; `LIKELY`, une conséquence d’usage plausible mais non testée auprès de lecteurs. Les tailles proposées sont des points de départ à éprouver, pas des normes officielles Pinterest.

## A. Défauts du système

### A1. Le comparateur donne une équivalence visuelle à des quantités différentes [CERTAIN]

**Coût lecteur :** rang 1 — décider à partir d’une comparaison faussée par sa présentation. **Coût de réalisation :** modéré.

**Où :** `references/templates.md`, « C — diagram » ; `scripts/make_pins.py`, `tpl_c()`, lignes 159–208 ; `references/pins_rome_example.py`, entrées `roma-pass` et `rome-airport-train`. Preuve : [Roma Pass à 236 px](review-evidence/roma-pass-actual236.png).

**Observation :** « The two big values ARE the pin at grid size; everything else rewards the tap. » Roma Pass oppose **€1.50** à **€58.50**, à 120 CSS px, avec un VS central et un gagnant encadré. Les précisions « per metro/bus ride » et « 2 sites + transit included » sont à 26px. À 236px de large, cela devient respectivement **28,3px** et **6,1px**. Le premier nombre concerne un trajet ; l’autre un forfait de 72 heures avec visites. Le comparateur aéroport oppose également deux prix sans champ obligatoire indiquant la base par personne ou par véhicule.

**Pourquoi c’est un défaut :** Le problème n’exige pas de déterminer si les tarifs sont encore actuels. Même exacts, ces nombres ne désignent pas le même panier. La symétrie graphique promet une comparabilité que le contenu ne fournit pas. La réserve ne peut être reléguée au tap lorsqu’elle change le sens de ce qui est déjà visible.

**Changement :** Ajouter au schéma `compare` des champs obligatoires `basis`, `unit`, `scope` et, pour un gagnant conditionnel, `winner_condition`. N’utiliser deux grands prix opposés que pour **un scénario commun** : mêmes voyageurs, même durée, mêmes prestations et mêmes limites de trajet. Si le corpus ne permet pas ce calcul, conserver un comparatif de couverture — « Un trajet » / « Transport + visites » — sans vainqueur de prix. Placer l’unité immédiatement sous la valeur, à **42px minimum sur le canevas**, et vérifier qu’elle reste lisible avec le nombre. Le moteur peut imposer la présence des champs ; leur comparabilité exige une validation éditoriale. Aucun montant supplémentaire ne doit être inventé pour remplir le modèle.

### A2. La lisibilité est contrôlée sur le titre, pas sur l’utilité du pin [CERTAIN]

**Coût lecteur :** rang 2 — voir le sujet sans pouvoir récupérer la ressource promise. **Coût de réalisation :** modéré.

**Où :** `SKILL.md`, étape 5 ; `references/templates.md`, B, C et adaptation n°4 ; `scripts/make_pins.py`, styles `.it b`, `.it em`, `.lab`, `.s`, `.verdict`. Exemples : `rome-scams-list`, `rome-3-days-list`, `rome-airport-train` dans la [planche](review-evidence/contact.png).

**Observation :** Le contrôle demande un titre lisible et « the one key figure legible ». Dans B, les affirmations sont à **31px**, les explications à **25px** ; dans C, les libellés sont à **23px**, les détails à **26px**, le verdict à **33px**. À 236px de large, ces tailles deviennent **7,3 / 5,9 / 5,4 / 6,1 / 7,8px**. La liste de trois jours garde les mêmes petits caractères que la liste de sept arnaques. Le C aéroport conserve environ **489 CSS px** entre la fin du verdict et le haut du footer : la petitesse n’est pas imposée par un manque de place.

**Pourquoi c’est un défaut :** Il est légitime que certains détails récompensent l’ouverture. Mais une liste conçue pour être sauvegardée doit au moins exposer ses actions ; un comparatif doit montrer les unités qui rendent ses nombres interprétables. Le système réserve de la place à l’habillage alors que son contenu utile ne passe pas son propre contexte de lecture.

**Changement :** Définir, pour chaque pin, les éléments **indispensables à sa compréhension en miniature**, puis les tester ensemble. Point de départ : items B à **44px/1.15**, précisions indispensables à **42px/1.2** ; libellés et unités C à **42px**, verdict bref à **44px**. Conserver un détail plus petit seulement s’il n’inverse pas la lecture. Dans B, créer une variante **3–4 éléments** lisibles et scinder les listes plus longues lorsque nécessaire ; « sept éléments maximum » n’est pas un budget typographique. Exploiter d’abord l’espace disponible, puis raccourcir ou répartir le contenu. Ne pas résoudre le problème en diminuant encore le titre.

### A3. La destination dépend de la silhouette, pas de la promesse [LIKELY]

**Coût lecteur :** rang 5 — cliquer sur une ressource et arriver dans un parcours qui peut répondre à une autre question. **Coût de réalisation :** modéré.

**Où :** `SKILL.md`, étape 4 ; `references/copy.md`, « Destinations » ; `references/pins_rome_example.py`, `MAGNET`, `rome-scams-list`, `rome-neighborhoods-list`, `rome-kids-list`.

**Observation :** « Template B (list) → the lead-magnet page. » Les listes sur les arnaques, les quartiers et les enfants pointent toutes vers `/#free-guide`, avec le même PDF « Rome in 3 Days ». L’exemple contient bien un commentaire demandant d’ajuster cette destination ; cela ne corrige pas la règle générale. La cohérence effective du PDF avec chaque promesse n’est pas démontrée par l’archive.

**Pourquoi c’est un défaut :** Une liste n’est pas nécessairement une intention de télécharger un itinéraire. Le dessin détermine ici le parcours commercial avant que le système ait vérifié la réponse attendue. L’arrivée réellement décevante reste à confirmer sur le site ; l’absence de contrat de correspondance est vérifiable.

**Changement :** Remplacer « B → magnet » par « toute destination livre la promesse principale du pin ». Séparer `template` de `destination_type` et ajouter `promise` / `destination_answer`. B peut mener à l’article exact ; un magnet convient s’il traite explicitement la question et si le CTA l’annonce. Exiger le contenu correspondant avant d’accepter « Free PDF » comme destination. `/#free-guide` peut être une ancre pertinente : ne pas la refuser seulement parce qu’elle appartient à l’accueil, mais ne pas la présumer pertinente non plus.

## B. Défauts d’exécution reproduits

### B1. La preuve miniature est une image cassée [CERTAIN]

**Coût lecteur :** rang 3 — le contrôle qui doit empêcher la livraison d’un mauvais visuel n’examine pas ce visuel. **Coût de réalisation :** trivial.

**Où :** `scripts/make_pins.py`, `render()`, lignes 236–244 ; `SKILL.md`, « Render and gate ». Preuve : [sortie native pour Rome en trois jours](review-evidence/native-proof-rome-3-days-list.png), comparée à la [réduction réelle](review-evidence/rome-3-days-list-actual236.png).

**Observation :** Le moteur crée une nouvelle page avec `set_content()`, puis charge un `<img src="file://…">`. Dans l’environnement testé, Chromium signale **« Not allowed to load local resource »**. L’image est `complete: true` mais `naturalWidth: 0`. Le PNG de preuve est blanc avec une icône d’image cassée. Le moteur annonce néanmoins la production réussie des fichiers.

**Pourquoi c’est un défaut :** Un fichier de bonnes dimensions n’est pas une preuve de rendu. Le délai fixe de 150ms ne vérifie ni le chargement ni le contenu. Ce constat est reproduit dans ce Chromium ; je ne prétends pas qu’aucune configuration permissive ne pourrait charger cette URL.

**Changement :** Produire la preuve directement à partir du PNG final, sans seconde page ni accès `file://` :

```python
from PIL import Image
with Image.open(f) as image:
    image.convert("RGB").resize(
        (236, 354), Image.Resampling.LANCZOS
    ).save(proofs / f"{p['slug']}_236.png")
```

Ajouter Pillow aux dépendances. Vérifier aussi que le PNG source mesure bien 2000 × 3000. Ce chemin a été utilisé pour les preuves indépendantes de cette revue. Une preuve correctement produite reste à inspecter : elle ne constitue pas, à elle seule, un verdict de lisibilité.

### B2. Le mode de secours est aussi un mode de livraison [CERTAIN]

**Coût lecteur :** rang 6 — recevoir un visuel dont la photo, l’identité ou le texte alternatif ne correspondent pas à ce qui a été préparé. **Coût de réalisation :** modéré.

**Où :** `SKILL.md`, « Doctrine » — « a render never fails » ; `scripts/make_pins.py`, `ONERROR`, `render()` lignes 225–235 et `write_csv()` ; exemple `colosseum-tickets`.

**Observation :** Un `TODO` devient un fond hachuré. Une erreur d’image applique `nophoto`. Les erreurs de polices sont tolérées et le CSV n’exclut pas ces sorties. Test réseau bloqué : aucune face web déclarée, mais un PNG complet est produit avec les polices de remplacement ; voir [le Colisée hors ligne](review-evidence/offline-colosseum-236.png). Le texte alternatif de l’exemple annonce pourtant une photo du Colisée, absente du placeholder. Les TODO de l’exemple sont évidemment volontaires ; le défaut est que le moteur ne distingue pas leur export de celui d’une image prête.

**Pourquoi c’est un défaut :** Une dégradation élégante est utile pour travailler. Elle n’est pas une validation de l’objet à publier. Le système assimile « PNG techniquement créé » à « pin conforme » et peut conserver une description accessible désormais fausse.

**Changement :** Introduire `draft` et `release`. En draft, placeholders et polices de secours restent autorisés, mais la sortie porte un statut explicite. En release : photos requises décodées avec `naturalWidth > 0`, aucune photo TODO, faces nécessaires chargées, débordements contrôlés, preuve validée. Une absence de photo doit être une composition explicitement choisie, pas une panne dissimulée. `write_csv()` ne reçoit que les pins validés de ce rendu. Réviser l’alt après choix de l’image finale. Aucune publication automatique n’est à ajouter.

### B3. B annule exactement le correctif qu’il annonce protéger [CERTAIN]

**Coût lecteur :** rang 7 — fin de composition instable, espace résiduel et CTA qui remonte avec la longueur de liste. **Coût de réalisation :** trivial.

**Où :** `SKILL.md`, « Doctrine » ; `references/templates.md`, B ; `scripts/make_pins.py`, `.foot` dans `base_css()` puis ligne 142 dans `tpl_b()`. Exemple : [Rome en trois jours](review-evidence/rome-3-days-list-actual236.png).

**Observation :** La documentation dit que le bandeau est maintenu en bas par `margin-top:auto`. Le style partagé le définit effectivement. Mais B le remplace ensuite par **`margin:0 -62px -58px`**, donc par une marge supérieure nulle. Pour trois items, le bandeau occupe **y=954,3 à 1052,3** sur un canevas haut de 1500. Pour sept items, il se déplace à **y=1279,5–1377,5**.

**Pourquoi c’est un défaut :** C’est une régression de cascade, pas une préférence concernant les blancs. La position du bandeau dépend du nombre d’items alors que le modèle promet le contraire.

**Changement :** Remplacer la déclaration B par :

```css
.foot { margin: auto -62px -58px; }
```

Testé avec les mêmes polices et le même contenu : le bandeau de trois jours passe à **y=1402–1500**, exactement en bas. Voir [le rendu corrigé](review-evidence/footer-fixed-236.png). Ajouter une assertion géométrique sur son bord inférieur. Cette réparation n’agrandit pas les items : le grand blanc restant confirme A2 et doit être traité par la variante de densité, pas par le retour du bandeau au milieu.

## C. Améliorations aujourd’hui interdites ou insuffisamment prévues

### C1. Préserver la photo fixe sans figer la priorité du message [LIKELY]

**Coût lecteur :** rang 4 — découvrir tardivement ce qui distingue le pin dans la grille. **Coût de réalisation :** modéré.

**Où :** `references/templates.md`, A ; `scripts/make_pins.py`, `tpl_a()` ; les quatre exemples A de la première rangée de la [planche](review-evidence/contact.png).

**Observation :** La photo occupe **780px**, soit 52% de la hauteur totale. Après la photo viennent marge, kicker et keyline ; les quatre titres commencent à **y=966**, soit **64,4% de la hauteur**, ou 228px dans la miniature. La règle propose de diminuer `title_px` si le titre dépasse trois lignes. Les quatre exemples normaux tiennent actuellement en trois lignes : je ne leur attribue pas un débordement inexistant.

**Pourquoi c’est un défaut :** Pour un conseil sur le pourboire ou un avertissement hôtelier, l’image peut être moins discriminante que l’information. Le contrat accorde pourtant toujours la première place et plus de la moitié du canevas à la photo, puis fait supporter au titre tout dépassement. L’effet sur les clics reste à tester ; l’ordre de lecture imposé est certain. Les placeholders ne permettent pas de juger l’efficacité des photos finales.

**Changement :** Conserver des hauteurs fixes, mais autoriser deux compositions nommées : `photo_first` et `message_first`. Pour la seconde : kicker court → titre → photo fixe de **560px** → éventuel complément → footer. Pour la première, proposer un préréglage photo **640px** lorsque le titre a besoin de place. Séparer `image_headline`, court et composé pour l’image, de `seo.title`, déjà distinct dans les données. Point de départ : titre **96px/1.04**, deux ou trois lignes, plancher explicite avant réécriture ; ne pas autoriser une réduction sans limite. Mesurer le budget complet avant capture. Cela conserve le correctif contre `flex:1` sur la photo, sans transformer 780px en dogme.

### C2. L’adaptation de marque doit pouvoir changer la forme [CERTAIN]

**Coût lecteur :** rang 8 — distinction de marque limitée à la palette et aux polices ; bénéfice surtout identitaire, pas gain de conversion démontré. **Coût de réalisation :** structurel.

**Où :** `SKILL.md`, étape 2 ; `references/templates.md`, « Per-site adaptation rules » et « SITE dict fields » ; `scripts/make_pins.py`, `base_css()`, `.num` et `.vs`.

**Observation :** Le skill demande de porter l’élément signature de chaque site. Mais le moteur impose à tous le double cadre, les badges carrés tournés à 45°, leur rayon et leurs dimensions. `SITE` expose des couleurs, fonds et polices, pas la forme des badges ni le cadre. Changer les signatures comme demandé oblige donc à modifier le moteur générique. Autre limite du même contrat : `dark_accent + '55'` et `+ '12'` supposent une couleur hexadécimale longue. Un test avec `rgb(201,169,74)` conserve la bordure directe du gagnant mais perd son fond teinté, devenu transparent.

**Pourquoi c’est un défaut :** Le point d’extension annoncé n’est pas réellement celui qui existe. Cela ne prouve pas que plusieurs marques se ressemblent trop — leurs pins ne sont pas fournis — mais cela prouve qu’une adaptation conforme nécessite du code supplémentaire non spécifié.

**Changement :** Ajouter un contrat fermé : `frame_style: double|single|none`, `badge_shape: diamond|circle|square`, dimensions et rayons, plus `display_weight`, `display_tracking` et `display_line_height`. Générer des classes de variante, sans copier tout `tpl_b()` pour chaque site. Ajouter des couleurs explicites `dark_border` et `dark_tint`, ou parser la couleur avant d’y appliquer un alpha ; ne pas concaténer des suffixes sur un token CSS arbitraire. Vérifier les variantes avec leurs polices, sans graisse synthétique interdite. Le but est d’autoriser une vraie signature là où elle existe, pas de créer un catalogue décoratif.

### C3. Le pipeline photo ne suit pas la résolution qu’il promet [CERTAIN]

**Coût lecteur :** rang 9 — netteté inutilement perdue à l’ouverture, invisible dans le seul contrôle miniature. **Coût de réalisation :** trivial à modéré.

**Où :** `scripts/make_pins.py`, `cloudinary()`, appels dans `tpl_a()` et `tpl_b()`, `device_scale_factor=2` dans `render()` ; `references/templates.md`, introduction.

**Observation :** A demande à Cloudinary une image de **900 × 780**, B de **900 × 330**. Ces images sont placées dans un canevas capturé à DPR 2 : la surface raster affichée approche **1750 × 1560** pour A et **1750 × 660** pour B, selon les bordures. Le texte bénéficie bien du rendu 2× ; la photo issue de ces URLs est agrandie presque deux fois par axe. Les URLs complètes, laissées intactes par `cloudinary()`, ne sont pas couvertes par ce constat.

**Pourquoi c’est un défaut :** Le PNG de 2000px ne donne pas rétroactivement cette définition à la photo. Le défaut de dimensionnement est certain ; la dégradation perceptible d’une photo donnée ne peut pas être affirmée à partir de placeholders.

**Changement :** Demander à Cloudinary les dimensions de la zone image **multipliées par le DPR**, arrondies, en conservant le ratio exact de cette zone. Prévoir `crop_position` ou un point focal par pin lorsque `g_auto` ne choisit pas le bon sujet, sans double recadrage contradictoire. Vérifier à la fois le cadrage miniature et la netteté à l’ouverture. Ne pas agrandir artificiellement une source insuffisante : la signaler ou choisir une source adaptée.

## D. L’idée directrice et les contrôles

### Garder trois familles, retirer leurs effets supposés du contrat

`SKILL.md`, introduction et étape 4, ainsi que `references/copy.md`, introduction, affirment que titre, description et board décident de l’affichage, tandis que « the image only decides the click ». Cette séparation est trop absolue : Pinterest Engineering décrit notamment des légendes générées depuis l’image et des représentations visuelles parmi les caractéristiques de son système de pertinence. Cela suffit à réfuter « only » ; cela ne permet pas de déduire la pondération actuelle de chaque signal. Voir [Pinterest Engineering, *Improving Pinterest Search Relevance Using Large Language Models*, 4 avril 2025](https://medium.com/pinterest-engineering/improving-pinterest-search-relevance-using-large-language-models-4cd938d4e892), « Pin Text Representations » et « Model Architecture » du modèle servi.

**A → clics, B → sauvegardes, C → repartages** sont des hypothèses de conception, pas des fonctions garanties par la silhouette. Les exemples reproduits n’apportent aucune mesure de ces résultats. La phrase « saves outweigh clicks » n’a ici ni source ni condition d’application ; elle ne doit pas décider à elle seule d’un modèle ou d’une destination. Réécrire : « Choisir la forme qui rend la promesse compréhensible ; enregistrer l’objectif visé séparément ; mesurer le résultat. » Ne pas imposer « corpus × 3 templates » lorsque l’article ne contient aucune comparaison honnête à dessiner. Cela met aussi cette règle en accord avec le refus explicite de forcer C dans `templates.md`.

### Remplacer le contrôle unique par une courte chaîne vérifiable

Le moteur réalise des captures, pas un audit automatique de lisibilité. Le contrôle humain demandé par le skill peut trouver les défauts ; le code ne l’exige pas avant export. La correction de B1 est donc prioritaire, puis :

1. **Contrat de contenu :** promesse, destination, unités, conditions et sources présentes ; aucun gagnant obtenu seulement par un style `win`.
2. **Actifs et typographie :** état réel des images et faces utilisées, distinction draft/release, texte alternatif correspondant au rendu final.
3. **Géométrie :** bornes de chaque bloc, nombre de lignes du titre, absence de chevauchement et de contenu masqué par `html,body {overflow:hidden}`. Vérifier les rectangles de texte et les débordements horizontaux, pas seulement la taille du conteneur.
4. **Échelles de lecture :** réduction 236px comme référence interne, test complémentaire à 180px et à une largeur d’ouverture, par exemple 600px. Le 236px n’est pas à traiter comme une largeur universelle et immuable de toute interface Pinterest. À petite taille : sujet, promesse, nombre **et unité**, action principale. À grande taille : détails et photo.
5. **Livraison :** manifeste limité aux fichiers effectivement rendus et validés. Le code actuel filtre `pins` avec `--only`, puis appelle encore `write_csv(mod.PINS, ...)` aux lignes 275–281 : un rendu partiel peut donc produire le CSV du lot entier. Transmettre la liste validée issue du rendu, et vérifier l’existence de chaque fichier référencé.

Le seuil « trait du titre ≥2px » n’indique pas quels traits mesurer, comment traiter l’anticrénelage ni comment cela prédit la lecture d’un mot. Conserver une inspection de mots réels à taille réelle ; ne pas épaissir automatiquement toutes les fontes pour satisfaire un pseudo-score. Le PNG haute résolution ne compense ni les petits caractères de sa réduction ni un sens incomplet.

## E. Ce que je ne peux pas juger

- **Résultats Pinterest :** aucune donnée d’impression, de clic, de sauvegarde, de repartage ou de conversion fournie. Je n’attribue donc aucun effet commercial mesuré aux changements. Les règles de cadence et de délai de démarrage sortent de cette revue de système/design.
- **Comparaison entre marques :** une seule configuration d’exemple. Il faudrait au moins des lots A/B/C de deux autres marques, leurs tokens et leurs polices pour distinguer effectivement un défaut commun d’une divergence d’adaptation.
- **Photos finales :** les reproductions utilisent volontairement les placeholders. Leurs surfaces et budgets sont mesurables ; leur pouvoir d’attraction, leur sujet et leur recadrage final ne le sont pas. C3 établit le problème de dimensionnement dans le code, pas un jugement sur une photo absente.
- **Promesses et tarifs :** les prix sont cités comme contenu de l’exemple, pas comme conseils de voyage actuels. Vérifier les faits demanderait les articles sources et leurs dates. A1 reste valable indépendamment de cette vérification. La concordance des magnets avec chaque pin demanderait les pages et PDF effectivement destinataires.
- **Environnement de production :** B1 et les mesures ont été reproduits dans le Chromium Playwright local. Un autre moteur ou des politiques d’accès différentes peuvent changer certains résultats. Les corrections proposées utilisent du CSS ordinaire, Pillow et des assertions Playwright ; elles ne dépendent pas de Paged.js, absent de ce skill.
- **Correctifs réellement vérifiés :** réduction des PNG en preuves lisibles et rétablissement du footer B ont été testés. Les nouvelles tailles, variantes et contrats sont des propositions à implémenter puis à rendre ; ils ne constituent pas un lot de remplacement déjà validé. L’archive `pins.skill` originale n’a pas été modifiée.
