"""
Quiz Algorithmique pour Codebog.
"""

ALGO_CHALLENGES = [
# Jour 2 — ALGO
('ALGO', 'Big O — O(1) vs O(n)', 'Laquelle de ces fonctions est O(1) ?', 'function a(arr) { return arr[0]; }\nfunction b(arr) {\n  let s = 0;\n  for (let x of arr) s += x;\n  return s;\n}', ['a() et b()', 'Seulement a()', 'Seulement b()', "Ni l'une ni l'autre"], 1, 'Seulement a()', "a() accède directement à l'index 0 → temps constant O(1).\nb() parcourt tout le tableau → O(n) : le temps grandit\navec la taille du tableau.", '// O(1) = temps constant quelle que soit la taille'),

# Jour 4 — ALGO
('ALGO', 'Two Sum', 'Trouve les 2 indices dont la somme vaut target.', 'function twoSum(nums, target) {\n  // ???\n  // Input:  [2, 7, 11, 15], target=9\n  // Output: [0, 1]\n}', ['Boucle double O(n²)', 'HashMap O(n)', 'Sort + two pointers', 'Récursion'], 1, 'HashMap O(n)', 'La solution optimale utilise un HashMap.\nPour chaque nb, on cherche (target - nb) dans la map.\nSi trouvé → on a notre paire. Sinon on stocke nb.', 'map.set(nums[i], i) // complément → index'),

# Jour 6 — ALGO
('ALGO', 'Palindrome', 'Est-ce que cette fonction détecte un palindrome ?', 'function isPalin(s) {\n  return s === s.split("").reverse().join("")\n}\nconsole.log(isPalin("racecar"))', ['false', 'true', 'Error', '"racecar"'], 1, 'true', '"racecar" inversé = "racecar" → c\'est bien un palindrome.\nCette solution est correcte mais O(n) en mémoire.\nLa solution optimale utilise deux pointeurs O(1) mémoire.', 'let l=0, r=s.length-1; // two pointers'),

# Jour 8 — ALGO
('ALGO', 'Anagramme', 'Ces deux strings sont-elles des anagrammes ?', 'function isAnagram(s, t) {\n  return s.split("").sort().join("") ===\n         t.split("").sort().join("")\n}\nconsole.log(isAnagram("listen", "silent"))', ['false', 'true', 'Error', '"listen"'], 1, 'true', '"listen" triée = "eilnst"\n"silent" triée = "eilnst"\nMême résultat → anagrammes ✅\nSolution O(n log n). La version HashMap est O(n).', '// HashMap : compter les fréquences de chaque lettre'),

# Jour 10 — ALGO
('ALGO', 'Binary Search', "Combien d'étapes pour trouver 7 dans ce tableau trié ?", 'const arr = [1, 3, 5, 7, 9, 11, 13]', ['7 étapes', '4 étapes', '1 étape', '3 étapes'], 2, '1 étape', 'Le tableau a 7 éléments. mid = index 3 = valeur 7.\nOn trouve directement → 1 seule étape !\nBinary search : O(log n) au lieu de O(n) pour la search linéaire.', '// log2(7) ≈ 2.8 → max 3 étapes dans le pire cas'),

# Jour 12 — ALGO
('ALGO', 'Bubble Sort', 'Quelle est la complexité de Bubble Sort ?', 'function bubbleSort(arr) {\n  for (let i = 0; i < arr.length; i++) {\n    for (let j = 0; j < arr.length - i - 1; j++) {\n      if (arr[j] > arr[j+1])\n        [arr[j], arr[j+1]] = [arr[j+1], arr[j]]\n    }\n  }\n  return arr\n}', ['O(n)', 'O(n log n)', 'O(n²)', 'O(log n)'], 2, 'O(n²)', "Deux boucles imbriquées sur n éléments = O(n²).\nC'est le pire des algos de tri pour les grandes données.\nPréférer merge sort O(n log n) ou quick sort O(n log n).", '// Bubble sort : simple à comprendre, lent en pratique'),

# Jour 14 — ALGO
('ALGO', 'Linked List — reverse', 'Comment inverser une linked list en O(n) O(1) mémoire ?', 'function reverse(head) {\n  let prev = null, curr = head\n  while (curr) {\n    let next = curr.next  // sauvegarder\n    curr.next = prev      // inverser\n    prev = curr           // avancer prev\n    curr = next           // avancer curr\n  }\n  return prev\n}', ['Utiliser un tableau', 'Récursion', '3 pointeurs', 'Impossible en O(1)'], 2, '3 pointeurs', "La technique des 3 pointeurs (prev, curr, next) permet\nd'inverser en un seul passage O(n) sans mémoire extra.\nC'est un classique des entretiens GAFAM.", '// prev=null → curr → next : on réoriente un à un'),

# Jour 16 — ALGO
('ALGO', 'Stack — valid parentheses', 'Comment valider des parenthèses avec une Stack ?', 'function isValid(s) {\n  const stack = []\n  const map = { ")":"(", "}":"{", "]":"[" }\n  for (let c of s) {\n    if ("([{".includes(c)) stack.push(c)\n    else if (stack.pop() !== map[c]) return false\n  }\n  return stack.length === 0\n}\nconsole.log(isValid("({[]})"))', ['false', 'true', 'Error', '"({[]})"'], 1, 'true', "On pousse les ouvrants sur la stack.\nPour chaque fermant, on vérifie que le top\nde la stack est l'ouvrant correspondant.", '// Stack LIFO = parfait pour matcher des paires'),

# Jour 18 — ALGO
('ALGO', 'Fibonacci — complexité', 'Quelle est la complexité de la version récursive naïve ?', 'function fib(n) {\n  if (n <= 1) return n\n  return fib(n-1) + fib(n-2)\n}\n// Analyse l\'arbre des appels récursifs', ['O(n)', 'O(n log n)', 'O(2ⁿ)', 'O(n²)'], 2, 'O(2ⁿ)', "Chaque appel crée 2 sous-appels → arbre binaire.\nL'arbre a une profondeur n → 2ⁿ appels au total.\nAvec mémoisation (cache) on passe à O(n) !", '// memo = {} → if(memo[n]) return memo[n]'),

# Jour 20 — ALGO
('ALGO', 'Two pointers — sum pair', 'Trouve une paire dont la somme = 9 dans ce tableau trié.', 'const arr = [1, 2, 4, 6, 8, 10]\n// Trouver une paire [i, j] tel que arr[i] + arr[j] === 9', ['[0, 4]', '[1, 2]', '[2, 5]', '[0, 5]'], 0, '[0, 4]', 'Avec deux pointeurs (gauche et droite) :\n- Si sum < target → avancer gauche\n- Si sum > target → reculer droite\nO(n) au lieu de O(n²) avec la boucle double.', '// Two pointers : always sur tableaux TRIÉS'),

# Jour 22 — ALGO
('ALGO', 'Sliding Window — max sum', 'Trouve la sous-liste de longueur 3 avec la somme maximale.', 'const arr = [2, 1, 5, 1, 3, 2]\nconst k = 3\n\n// Quelle est la somme maximale\n// d\'une fenêtre de taille k ?', ['8', '7', '9', '10'], 2, '9', 'Sliding window : on maintient une "fenêtre" de taille k.\nOn glisse d\'un pas à la fois, en ajoutant le nouvel\nélément et retirant l\'ancien. O(n) au lieu de O(n·k).', '// sum += arr[i] - arr[i-k] à chaque slide'),

# Jour 24 — ALGO
('ALGO', 'HashMap — frequency count', 'Comment compter les occurrences de chaque lettre ?', 'function charCount(s) {\n  const map = {}\n  for (let c of s) {\n    map[c] = (map[c] || 0) + 1\n  }\n  return map\n}\nconsole.log(charCount("hello"))', ['{ h:1,e:1,l:1,o:1 }', '{ h:1,e:1,l:2,o:1 }', '5', 'Error'], 1, '{ h:1,e:1,l:2,o:1 }', '"hello" contient 2x "l" → l:2.\nLa technique HashMap/freq-count est fondamentale :\nanagrammes, doublons, top-K... tout s\'appuie dessus.', '// map[c] = (map[c] || 0) + 1 : pattern classique'),

# Jour 26 — ALGO
('ALGO', 'Recursion — factorial', 'Que retourne factorial(5) ?', 'function factorial(n) {\n  if (n <= 1) return 1\n  return n * factorial(n - 1)\n}\nconsole.log(factorial(5))', ['25', '120', '60', 'Infinity'], 1, '120', '5! = 5 × 4 × 3 × 2 × 1 = 120\nLa récursion appelle la fonction avec n-1 à chaque fois.\nCas de base : n <= 1 → retourne 1 pour stopper.', '// Toujours définir un cas de base !'),

# Jour 28 — ALGO
('ALGO', 'Merge Sort', 'Quelle est la complexité de Merge Sort ?', 'function mergeSort(arr) {\n  if (arr.length <= 1) return arr\n  const mid = Math.floor(arr.length / 2)\n  const left = mergeSort(arr.slice(0, mid))\n  const right = mergeSort(arr.slice(mid))\n  return merge(left, right)\n}', ['O(n²)', 'O(n)', 'O(n log n)', 'O(log n)'], 2, 'O(n log n)', 'Merge sort divise en 2 à chaque niveau → log n niveaux.\nÀ chaque niveau, on fait O(n) opérations pour merge.\nTotal : O(n log n) — optimal pour un tri par comparaison.', '// Stable, prévisible, idéal pour les grandes listes'),

# Jour 30 — ALGO
('ALGO', 'Quick Sort — pivot', 'Quelle est la complexité moyenne de Quick Sort ?', 'function quickSort(arr) {\n  if (arr.length <= 1) return arr\n  const pivot = arr[arr.length - 1]\n  const left  = arr.slice(0,-1).filter(x => x <= pivot)\n  const right = arr.slice(0,-1).filter(x => x > pivot)\n  return [...quickSort(left), pivot, ...quickSort(right)]\n}', ['O(n²)', 'O(n)', 'O(n log n)', 'O(log n)'], 2, 'O(n log n)', 'En moyenne, le pivot sépare bien → log n niveaux.\nPire cas (pivot = min ou max) → O(n²).\nEn pratique très rapide en mémoire (in-place possible).', '// Pivot aléatoire = meilleure protection O(n²)'),

# Jour 32 — ALGO
('ALGO', 'Valid parentheses — complexité', 'Complexité de la solution avec Stack pour les parenthèses ?', 'function isValid(s) {\n  const stack = []\n  const map = { ")":"(", "}":"{", "]":"[" }\n  for (let c of s) {\n    if ("([{".includes(c)) stack.push(c)\n    else if (stack.pop() !== map[c]) return false\n  }\n  return stack.length === 0\n}', ['O(n²) temps, O(n) espace', 'O(n) temps, O(n) espace', 'O(n) temps, O(1) espace', 'O(log n) temps, O(1) espace'], 1, 'O(n) temps, O(n) espace', "On parcourt la string une seule fois → O(n) temps.\nLa stack peut contenir au max n éléments → O(n) espace.\nPas d'algo O(1) espace possible ici car on doit tracer les ouvrants.", '// Stack size = moitié max de la string en pire cas'),

# Jour 34 — ALGO
('ALGO', 'Binary Tree — BFS', 'BFS sur un arbre binaire utilise quelle structure ?', 'function bfs(root) {\n  const queue = [root]\n  while (queue.length) {\n    const node = queue.shift()\n    console.log(node.val)\n    if (node.left)  queue.push(node.left)\n    if (node.right) queue.push(node.right)\n  }\n}', ['Stack (LIFO)', 'Queue (FIFO)', 'HashMap', 'Array trié'], 1, 'Queue (FIFO)', "BFS (Breadth-First Search) explore niveau par niveau.\nOn utilise une Queue FIFO : on traite les nœuds dans l'ordre d'insertion.\nDFS utilise une Stack (ou la récursion).", '// BFS = Queue | DFS = Stack/recursion'),

# Jour 36 — ALGO
('ALGO', 'Reverse string', 'Quelle méthode est la plus concise pour inverser ?', 'const s = "codebog"\n// Option A:\nconst a = s.split("").reverse().join("")\n// Option B (two pointers):\nconst arr = s.split("")\nlet l = 0, r = arr.length - 1\nwhile (l < r) {\n  [arr[l], arr[r]] = [arr[r], arr[l]]\n  l++; r--\n}\nconst b = arr.join("")', ['A et B donnent "gobedoc"', 'A donne "gobedoc", B différent', 'A = "gobedoc" = B', 'B est incorrect'], 2, 'A = "gobedoc" = B', 'Les deux donnent "gobedoc" mais avec des trade-offs :\nA : concis, O(n) mémoire (3 arrays créés).\nB : verbeux, O(1) mémoire (in-place, idéal en entretien).', '// Two pointers in-place = meilleure réponse entretien'),

# Jour 38 — ALGO
('ALGO', 'FizzBuzz', 'Quelle est la sortie pour i = 15 ?', 'for (let i = 1; i <= 20; i++) {\n  if (i % 15 === 0) console.log("FizzBuzz")\n  else if (i % 3 === 0) console.log("Fizz")\n  else if (i % 5 === 0) console.log("Buzz")\n  else console.log(i)\n}', ['"Fizz"', '"Buzz"', '"FizzBuzz"', '"15"'], 2, '"FizzBuzz"', '15 est divisible par 3 ET par 5 (15 % 15 === 0).\nL\'ordre des conditions est crucial :\nVérifier d\'abord % 15, sinon on tomberait sur "Fizz".', '// FizzBuzz : classique des entretiens débutants'),

# Jour 40 — ALGO
('ALGO', 'Is Prime?', 'Ce code détecte-t-il correctement les nombres premiers ?', 'function isPrime(n) {\n  if (n < 2) return false\n  for (let i = 2; i <= Math.sqrt(n); i++) {\n    if (n % i === 0) return false\n  }\n  return true\n}\nconsole.log(isPrime(17))', ['false — bug', 'true ✅', 'Error', '"premier"'], 1, 'true ✅', "17 est bien premier. La boucle va jusqu'à √17 ≈ 4.\nOn teste : 17%2, 17%3, 17%4 → aucun diviseur → premier.\nAller jusqu'à √n suffit : si diviseur > √n, l'autre est < √n.", '// O(√n) au lieu de O(n) — optimisation clé'),

# Jour 42 — ALGO
('ALGO', 'Merge intervals', 'Quel est le résultat du merge de ces intervalles ?', 'const intervals = [[1,3],[2,6],[8,10],[15,18]]\n// Après merge :\n// [1,3] et [2,6] se chevauchent → [1,6]\n// [8,10] seul\n// [15,18] seul', ['[[1,3],[2,6],[8,10],[15,18]]', '[[1,6],[8,10],[15,18]]', '[[1,10],[15,18]]', '[[1,18]]'], 1, '[[1,6],[8,10],[15,18]]', "On trie d'abord par le début, puis on merge :\nSi current.start <= last.end → on étend last.\nSinon on pousse current tel quel.", '// Toujours trier avant de merger les intervalles'),

# Jour 44 — ALGO
('ALGO', 'Max subarray — Kadane', 'Trouve la sous-liste avec la somme maximale.', 'const arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]\n// Algorithme de Kadane\n// Réponse : [4,-1,2,1] → somme = 6\nfunction maxSubArray(nums) {\n  let maxSum = nums[0], curr = nums[0]\n  for (let i = 1; i < nums.length; i++) {\n    curr = Math.max(nums[i], curr + nums[i])\n    maxSum = Math.max(maxSum, curr)\n  }\n  return maxSum\n}', ['4', '5', '6', '7'], 2, '6', "Kadane's algorithm en O(n) :\nÀ chaque position, on décide : continuer la sous-liste\nou recommencer depuis ici. maxSum garde le meilleur.", '// Kadane : DP classique, O(n) temps O(1) espace'),

# Jour 46 — ALGO
('ALGO', 'Contains duplicate', 'Complexité optimale pour détecter les doublons ?', 'function hasDuplicate(nums) {\n  const seen = new Set()\n  for (let n of nums) {\n    if (seen.has(n)) return true\n    seen.add(n)\n  }\n  return false\n}\n// Input: [1, 2, 3, 1] → ???', ['false', 'true', 'Error', '[1]'], 1, 'true', "[1,2,3,1] contient 1 en double → true.\nSolution Set : O(n) temps, O(n) espace.\nAlternative : trier d'abord O(n log n) O(1) espace.", '// Set.has() → O(1) en moyenne'),

# Jour 48 — ALGO
('ALGO', 'Climbing stairs — DP', "Combien de façons d'atteindre la marche 4 (1 ou 2 pas) ?", 'function climbStairs(n) {\n  if (n <= 2) return n\n  let a = 1, b = 2\n  for (let i = 3; i <= n; i++) {\n    [a, b] = [b, a + b]\n  }\n  return b\n}\n// n=1:1, n=2:2, n=3:3, n=4:???', ['4', '5', '6', '7'], 1, '5', "C'est la séquence de Fibonacci !\n4 marches : (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), (2+2)\n= 5 façons.\nDP bottom-up O(n) temps, O(1) espace.", '// Climbing stairs = Fibonacci déguisé'),

# Jour 50 — ALGO
('ALGO', 'House Robber — DP', 'Montant max sans voler 2 maisons adjacentes ?', 'const houses = [2, 7, 9, 3, 1]\n// On ne peut pas voler 2 maisons consécutives\n// Option 1: 2+9+1 = 12\n// Option 2: 7+3  = 10\n// Option 3: 2+9  = 11\n// Option 4: 7+9  ✗ adjacentes', ['10', '11', '12', '13'], 2, '12', "DP : à chaque maison, on choisit le max entre :\n- Voler ici + meilleur des 2 avant\n- Ne pas voler, garder le meilleur d'avant.\nFormule : dp[i] = max(dp[i-1], dp[i-2] + houses[i])", '// 2+9+1 = 12 — toujours vérifier toutes options'),

# Jour 52 — ALGO
('ALGO', 'Number of islands', "Combien d'îles dans cette grille ?", 'const grid = [\n  ["1","1","0","0","0"],\n  ["1","1","0","0","0"],\n  ["0","0","1","0","0"],\n  ["0","0","0","1","1"]\n]\n// Îles = groupes de "1" connectés (haut/bas/gauche/droite)', ['2', '3', '4', '5'], 1, '3', 'Île 1 : les 4 cases "1" en haut-gauche.\nÎle 2 : le "1" isolé au centre.\nÎle 3 : les 2 "1" en bas-droite.\nSolution : DFS/BFS pour marquer les îles visitées.', '// DFS : marquer "0" pour éviter de recompter'),

# Jour 54 — ALGO
('ALGO', 'LRU Cache', 'LRU Cache évicte quelle entrée quand il est plein ?', '// LRU = Least Recently Used\n// Cache taille 3 :\n// Accès: A, B, C, A, D\n// État après D : ???\n// [B, C, A] → D insère → évicte ???', ['A (dernier accédé)', 'B (le moins récent)', 'C (le milieu)', 'D (le plus récent)'], 1, 'B (le moins récent)', "LRU évicte l'élément LE MOINS RÉCEMMENT UTILISÉ.\nAprès les accès A,B,C,A,D : l'ordre est B,C,A (récent).\nD insère et B est évincé car le plus ancien.", '// Implémentation : HashMap + Doubly Linked List'),

# Jour 56 — ALGO
('ALGO', 'Top K elements — Heap', 'Comment trouver les K plus grands éléments efficacement ?', 'function topK(nums, k) {\n  // Min-Heap de taille k\n  // Parcourir nums:\n  //   push dans le heap\n  //   si heap.size > k → pop le minimum\n  // Résultat : les k plus grands restent\n}\n// Input: [3,1,5,12,2,11], k=3\n// Output: [5,11,12]', ['O(n log n)', 'O(n log k)', 'O(n²)', 'O(k log n)'], 1, 'O(n log k)', 'Un min-heap de taille k : O(n log k).\nMieux que trier tout O(n log n) si k << n.\nLe top du heap est toujours le plus petit des k grands.', '// Heap de taille k : optimal pour "top K" problems'),

# Jour 58 — ALGO
('ALGO', 'Coin change — DP', 'Minimum de pièces pour faire 11 avec [1,5,6,9] ?', '// coins = [1, 5, 6, 9], amount = 11\n// Option 1: 9 + 1 + 1 = 3 pièces\n// Option 2: 6 + 5 = 2 pièces ← optimal\n// Option 3: 5 + 5 + 1 = 3 pièces\n// Greedy: 9+1+1 = 3 ← sous-optimal !', ['3 pièces', '2 pièces', '1 pièce', 'Impossible'], 1, '2 pièces', "6 + 5 = 11 en 2 pièces seulement.\nL'algo greedy (prendre la plus grande) donne 9+1+1=3.\nIl faut la DP : dp[i] = min pièces pour la somme i.", '// DP bottom-up : dp[0]=0, dp[i]=min(dp[i-coin]+1)'),

# Jour 60 — ALGO
('ALGO', 'Course Schedule — cycle', 'Peut-on finir tous les cours ? (cycle = impossible)', 'const numCourses = 4\nconst prereqs = [[1,0],[2,1],[3,2]]\n// 0→1→2→3 : pas de cycle\n\nconst prereqs2 = [[1,0],[0,1]]\n// 0→1→0 : cycle !', ['prereqs: oui, prereqs2: oui', 'prereqs: oui, prereqs2: non', 'prereqs: non, prereqs2: oui', 'Les deux: non'], 1, 'prereqs: oui, prereqs2: non', 'On modélise en graphe orienté et on détecte les cycles.\nPrereqs forme une chaîne linéaire → pas de cycle → possible.\nPrereqs2 forme un cycle 0↔1 → impossible.', '// DFS + coloring (blanc/gris/noir) pour détecter cycles'),

# Jour 62 — ALGO
('ALGO', 'Word search — backtracking', 'Backtracking : on revient en arrière quand ?', 'function exist(board, word) {\n  // DFS + backtracking\n  function dfs(i, j, k) {\n    if (k === word.length) return true\n    if (/* hors limites ou mauvaise lettre */) return false\n    board[i][j] = "#"           // marquer visité\n    const found = dfs(i+1,j,k+1) || dfs(i-1,j,k+1)\n                || dfs(i,j+1,k+1) || dfs(i,j-1,k+1)\n    board[i][j] = word[k]       // restaurer\n    return found\n  }\n}', ['Jamais', 'Quand on sort des limites', 'Quand un chemin ne mène pas à la solution', 'À chaque étape'], 2, 'Quand un chemin ne mène pas à la solution', 'Backtracking = DFS + annulation des choix erronés.\nOn marque la cellule comme visitée (#), on explore,\npuis on RESTAURE si on ne trouve pas le mot.', '// board[i][j] = "#" → explore → board[i][j] = word[k]'),

# Jour 64 — ALGO
('ALGO', 'Longest palindromic substring', "Quelle est la longueur du plus long palindrome dans 'babad' ?", 'function longestPalin(s) {\n  let longest = ""\n  for (let i = 0; i < s.length; i++) {\n    // Expand around center (odd & even)\n    for (let odd of [true, false]) {\n      let l = i, r = odd ? i : i + 1\n      while (l >= 0 && r < s.length && s[l] === s[r])\n        { l--; r++ }\n      const sub = s.slice(l+1, r)\n      if (sub.length > longest.length) longest = sub\n    }\n  }\n  return longest\n}\n// Input: "babad"', ['"b" (1)', '"ba" (2)', '"bab" (3)', '"babad" (5)'], 2, '"bab" (3)', '"bab" et "aba" sont tous deux des palindromes de longueur 3.\n"bab" est retourné en premier.\nAlgo expand-around-center : O(n²) temps, O(1) espace.', "// Manacher's algorithm : O(n) pour les pros"),

# Jour 66 — ALGO
('ALGO', 'Trie — préfixes', 'Un Trie est optimal pour quelle opération ?', 'class Trie {\n  constructor() { this.root = {} }\n  insert(word) {\n    let node = this.root\n    for (let c of word) {\n      if (!node[c]) node[c] = {}\n      node = node[c]\n    }\n    node.end = true\n  }\n  startsWith(prefix) {\n    let node = this.root\n    for (let c of prefix) {\n      if (!node[c]) return false\n      node = node[c]\n    }\n    return true\n  }\n}', ['Recherche par valeur O(1)', 'Recherche par préfixe O(m)', 'Tri alphabétique O(n)', 'Suppression O(log n)'], 1, 'Recherche par préfixe O(m)', "Un Trie permet la recherche par préfixe en O(m) où m = longueur du préfixe.\nParfait pour l'autocomplétion, correcteurs orthographiques.\nChaque nœud représente un caractère.", '// Trie: O(m) insert/search, m = length du mot'),

# Jour 68 — ALGO
('ALGO', 'Unique paths — DP', 'Combien de chemins uniques dans une grille 3x3 ?', '// Robot : haut-gauche → bas-droite\n// Mouvements : droite ou bas seulement\n// Grille 3x3\n// Combien de chemins possibles ?', ['4', '6', '8', '12'], 1, '6', 'Dans une grille 3x3, il y a 6 chemins uniques.\nDP : chaque cellule = somme du dessus + de gauche.\nFormule combinatoire : C(m+n-2, m-1) = C(4,2) = 6.', '// dp[i][j] = dp[i-1][j] + dp[i][j-1]'),

# Jour 70 — ALGO
('ALGO', 'Dynamic programming — intro', 'Quelle propriété doit avoir un problème pour la DP ?', '// DP = mémoisation de sous-problèmes\n// Quelles sont les propriétés nécessaires ?\n// Pense aux problèmes : Fibonacci, Knapsack, etc.', ['Être récursif seulement', 'Sous-problèmes chevauchants + sous-structure optimale', 'Être trié', 'Avoir O(n) complexité'], 1, 'Sous-problèmes chevauchants + sous-structure optimale', 'La DP mémorise les résultats des sous-problèmes.\nSous-problèmes chevauchants : fib(3) calculé plusieurs fois.\nSous-structure optimale : optimal global = optimal local.', '// Top-down (mémo) ou Bottom-up (tableau)'),

# Jour 72 — ALGO
('ALGO', 'Bit manipulation — Single Number', "Trouve le nombre qui n'apparaît qu'une fois.", 'function singleNumber(nums) {\n  return nums.reduce((xor, n) => xor ^ n, 0)\n}\n// Input: [4, 1, 2, 1, 2]\n// 0^4=4, 4^1=5, 5^2=7, 7^1=6, 6^2=4\n// Output: ???', ['1', '2', '4', '0'], 2, '4', "XOR (^) a une propriété : x ^ x = 0 et x ^ 0 = x.\nTous les nombres en double s'annulent !\n[4,1,2,1,2] → 4^(1^1)^(2^2) = 4^0^0 = 4.", '// XOR : solution O(n) O(1) sans HashMap'),

# Jour 74 — ALGO
('ALGO', 'Trapping rain water', "Combien d'eau est piégée dans ce profil ?", 'const height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]\n// Visualisation :\n//        X\n//    X   X X   X\n// X  X X X X X X X X\n// Eau piégée = ???', ['5', '6', '7', '8'], 1, '6', "6 unités d'eau sont piégées.\nAlgo two-pointers : l(eft) et r(ight).\nEau en i = min(maxLeft, maxRight) - height[i].", '// O(n) temps O(1) espace avec two pointers'),

# Jour 76 — ALGO
('ALGO', 'Longest common subsequence', "Quelle est la LCS de 'ABCBDAB' et 'BDCAB' ?", '// LCS("ABCBDAB", "BDCAB")\n// DP : dp[i][j] = longueur LCS de s1[0..i] et s2[0..j]\n// Si s1[i] === s2[j] : dp[i][j] = dp[i-1][j-1] + 1\n// Sinon : dp[i][j] = max(dp[i-1][j], dp[i][j-1])\n// LCS = "BCAB" ou "BDAB" → longueur ???', ['3', '4', '5', '6'], 1, '4', '"BCAB" et "BDAB" sont toutes deux des LCS de longueur 4.\nDP classique O(m×n) temps et espace.\nOptimisation : O(min(m,n)) espace possible.', '// LCS : base pour git diff, spell check, bioinformatique'),

# Jour 78 — ALGO
('ALGO', 'Jump Game', 'Peut-on atteindre le dernier index ?', 'const nums = [2, 3, 1, 1, 4]\n// À chaque index i, on peut sauter 0 à nums[i] pas\n// Index 0: sauter 2 → index 1 ou 2\n// Index 1: sauter 3 → index 2,3,4 ← fin !\n\nconst nums2 = [3, 2, 1, 0, 4]\n// Index 3: nums[3]=0 → bloqué !', ['nums: non, nums2: oui', 'nums: oui, nums2: non', 'Les deux: oui', 'Les deux: non'], 1, 'nums: oui, nums2: non', 'Greedy : on track le "reach" maximum atteignable.\nNums2 : tous les chemins mènent à l\'index 3 où nums[3]=0.\nOn ne peut jamais dépasser l\'index 3 → impossible.', '// maxReach = Math.max(maxReach, i + nums[i])'),

# Jour 80 — ALGO
('ALGO', 'Matrix — rotate 90°', 'Comment rotate une matrice NxN in-place ?', 'function rotate(matrix) {\n  const n = matrix.length\n  // Étape 1 : Transposer (swap [i][j] et [j][i])\n  for (let i = 0; i < n; i++)\n    for (let j = i+1; j < n; j++)\n      [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]]\n  // Étape 2 : Inverser chaque ligne\n  for (let row of matrix) row.reverse()\n}', ['Transposer seulement', 'Inverser seulement', 'Transposer puis inverser chaque ligne', 'Créer une nouvelle matrice'], 2, 'Transposer puis inverser chaque ligne', "Rotation 90° horaire = transpose + reverse de chaque ligne.\nO(n²) temps, O(1) espace (in-place).\nC'est un classique des entretiens sur les matrices.", '// Anti-horaire : reverse colonnes puis transpose'),

# Jour 82 — ALGO
('ALGO', 'Backtracking — subsets', 'Combien de sous-ensembles pour [1,2,3] ?', 'function subsets(nums) {\n  const result = [[]]\n  for (let n of nums) {\n    const curr = result.map(sub => [...sub, n])\n    result.push(...curr)\n  }\n  return result\n}\n// [1,2,3] → ???', ['6', '7', '8', '9'], 2, '8', 'Pour n éléments, il y a 2ⁿ sous-ensembles.\n[1,2,3] : n=3 → 2³ = 8 sous-ensembles.\n[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3].', '// 2ⁿ sous-ensembles toujours : inclure ou exclure'),

# Jour 84 — ALGO
('ALGO', 'Decode ways — DP', "Combien de façons de décoder '226' (A=1...Z=26) ?", '// "226" peut être décodé en :\n// 2-2-6 → "BBF"\n// 22-6  → "VF"\n// 2-26  → "BZ"\n// Total : ???\n\nfunction numDecodings(s) {\n  // DP bottom-up\n  // dp[i] = nb façons de décoder s[0..i-1]\n}', ['2', '3', '4', '5'], 1, '3', '"226" : "BBF", "VF", "BZ" = 3 façons.\nDP : dp[i] = dp[i-1] si s[i] valide + dp[i-2] si s[i-1..i] valide.\nCas limite : "06" → invalide car 06 > 26.', '// dp[0]=1, dp[1]=1 si s[0]!="0" sinon 0'),

# Jour 86 — ALGO
('ALGO', 'Minimum window substring', "Longueur minimale de la fenêtre dans 'ADOBECODEBANC' contenant 'ABC' ?", '// s = "ADOBECODEBANC", t = "ABC"\n// Toutes les fenêtres valides :\n// "ADOBEC" (6) ✓\n// "DOBECODEBA" (10) ✓\n// "CODEBA" (6) ✓\n// "OBECODEBA" ✗ (pas A)\n// "BANC" (4) ✓ ← min\n// Algorithme : sliding window variable', ['4', '5', '6', '7'], 0, '4', '"BANC" est la plus petite fenêtre contenant A, B, C.\nSliding window : étendre r jusqu\'à avoir tous les chars,\npuis réduire l depuis la gauche.', '// O(n) : deux pointeurs + fréquence map'),

# Jour 88 — ALGO
('ALGO', "Pascal's triangle", 'Quelle est la 5ème ligne du triangle de Pascal ?', '// Ligne 0 :      1\n// Ligne 1 :     1 1\n// Ligne 2 :    1 2 1\n// Ligne 3 :   1 3 3 1\n// Ligne 4 :  1 4 6 4 1\n// Ligne 5 : ???', ['[1,5,10,10,5,1]', '[1,4,6,4,1]', '[1,5,10,5,1]', '[1,6,15,20,15,6,1]'], 0, '[1,5,10,10,5,1]', 'Chaque valeur = somme des deux valeurs du dessus.\nLigne 5 : 1, 1+4=5, 4+6=10, 6+4=10, 4+1=5, 1.\nLes valeurs sont les coefficients binomiaux C(n,k).', '// Pascal : combinatoire, probabilités, puissances de (a+b)'),

# Jour 90 — ALGO
('ALGO', 'Median of two sorted arrays', 'Quelle est la complexité optimale pour trouver la médiane ?', '// nums1 = [1, 3], nums2 = [2]\n// Merged: [1, 2, 3] → médiane = 2\n\n// nums1 = [1, 2], nums2 = [3, 4]\n// Merged: [1, 2, 3, 4] → médiane = (2+3)/2 = 2.5\n\n// Approche naïve : merge puis médiane → O(m+n)\n// Approche optimale : binary search → ???', ['O(n)', 'O(m+n)', 'O(log(m+n))', 'O(log n)'], 2, 'O(log(m+n))', 'Binary search sur le plus petit tableau.\nOn partitionne les deux tableaux pour que :\n- tout à gauche ≤ tout à droite\nComplexité : O(log(min(m,n))). Problème Hard sur Leetcode.', '// Hardest binary search : requires deep understanding'),

# Jour 92 — ALGO
('ALGO', 'Spiral matrix', "Quel est l'ordre de traversée en spirale de cette matrice ?", 'const matrix = [\n  [1,  2,  3],\n  [4,  5,  6],\n  [7,  8,  9]\n]\n// Spirale clockwise :\n// Haut: 1,2,3\n// Droite: 6,9\n// Bas: 8,7\n// Gauche: 4\n// Centre: 5', ['[1,2,3,6,9,8,7,4,5]', '[1,2,3,4,5,6,7,8,9]', '[1,3,9,7,2,6,8,4,5]', 'Error'], 0, '[1,2,3,6,9,8,7,4,5]', 'Traversée en spirale : top→right→bottom→left, puis réduire les bornes.\nOn maintient 4 pointeurs : top, bottom, left, right.\nO(m×n) temps, O(1) espace (hors résultat).', '// 4 directions + réduction des bornes à chaque tour'),

# Jour 94 — ALGO
('ALGO', 'Container with most water', "Quelle est la quantité max d'eau entre ces barres ?", 'const height = [1, 8, 6, 2, 5, 4, 8, 3, 7]\n// Deux pointeurs : l=0, r=8\n// Water = min(h[l], h[r]) * (r - l)\n// Step 1: min(1,7) * 8 = 8\n// Step 2: l++, min(8,7) * 7 = 49\n// ...\n// Optimal: h[1]=8 et h[8]=7 → ???', ['42', '49', '56', '64'], 1, '49', 'min(8, 7) × (8-1) = 7 × 7 = 49.\nAlgo two-pointers : avancer le côté le plus petit.\nO(n) temps, O(1) espace. Classique entretien.', '// Avancer le plus petit pointeur vers le centre'),

# Jour 96 — ALGO
('ALGO', 'Group anagrams', 'Comment regrouper des anagrammes efficacement ?', 'function groupAnagrams(strs) {\n  const map = {}\n  for (let s of strs) {\n    const key = s.split("").sort().join("")\n    if (!map[key]) map[key] = []\n    map[key].push(s)\n  }\n  return Object.values(map)\n}\n// Input: ["eat","tea","tan","ate","nat","bat"]', ['[["eat","tea","ate"],["tan","nat"],["bat"]]', '[["eat"],["tea"],["tan"]]', 'Error', '[3 groupes]'], 0, '[["eat","tea","ate"],["tan","nat"],["bat"]]', 'Clé = string triée. Les anagrammes ont la même clé.\n"eat","tea","ate" → triés = "aet"\n"tan","nat" → triés = "ant".\nO(n × k log k) où k = longueur max.', '// HashMap avec clé = string triée'),

# Jour 98 — ALGO
('ALGO', 'Longest increasing subsequence', 'Longueur de la LIS de [10, 9, 2, 5, 3, 7, 101, 18] ?', '// LIS = Longest Increasing Subsequence\n// [10, 9, 2, 5, 3, 7, 101, 18]\n//\n// Quelques subsequences croissantes :\n// [2, 5, 7, 101] → 4\n// [2, 3, 7, 18]  → 4\n// [2, 5, 7, 18]  → 4\n// Longueur max = ???', ['3', '4', '5', '6'], 1, '4', 'LIS = 4 ([2,5,7,101] ou [2,3,7,18] ou [2,5,7,18]).\nDP classique : dp[i] = max LIS se terminant à i.\nOptimisation : O(n log n) avec patience sorting.', '// dp[i] = 1 + max(dp[j]) pour j < i où nums[j] < nums[i]'),

# Jour 100 — ALGO
('ALGO', 'Post #100 — Design HashMap', '🎉 Post #100 ! Comment implémenter un HashMap O(1) ?', 'class HashMap {\n  constructor(size = 1000) {\n    this.buckets = new Array(size).fill(null).map(() => [])\n  }\n  _hash(key) { // djb2 hash\n    let h = 5381\n    for (let c of String(key)) h = (h * 33) ^ c.charCodeAt(0)\n    return Math.abs(h) % this.buckets.length\n  }\n  set(k, v) { /* ... */ }\n  get(k) { /* ... */ }\n}', ['Array de taille fixe', 'Hash fn + tableau de buckets + chaining', 'Arbre binaire de recherche', 'LinkedList'], 1, 'Hash fn + tableau de buckets + chaining', '100 posts ! 🎉 Un HashMap = fonction de hachage + tableau de buckets.\nCollisions gérées par chaining (liste chaînée dans le bucket).\nO(1) amorti pour get/set/delete.', '// Load factor > 0.75 → resize (rehash) du tableau'),

# Jour 102 — ALGO
('ALGO', 'Serialize binary tree', 'Comment sérialiser un arbre binaire ?', 'function serialize(root) {\n  if (!root) return "null"\n  return `${root.val},${serialize(root.left)},${serialize(root.right)}`\n}', ['JSON.stringify', 'BFS level-order', 'DFS preorder récursif', 'Impossible'], 2, 'DFS preorder récursif', 'DFS preorder + "null" pour les absents.\nPermet de reconstruire l\'arbre exactement.', '// serialize/deserialize : Leetcode Hard'),

# Jour 104 — ALGO
('ALGO', 'Alien dictionary', 'Comment trier un dictionnaire alien ?', 'const words = ["wrt","wrf","er","ett","rftt"]\n// Construire un graphe des contraintes\n// wrt → wrf : t < f\n// wrf → er  : w < e\n// er  → ett : r < t\n// ett → rftt: e < r\n// Topological sort → ordre des lettres', ['Tri alphabétique', 'Topological sort sur graphe de contraintes', 'BFS simple', 'DFS naïf'], 1, 'Topological sort sur graphe de contraintes', 'Comparer mots adjacents → contraintes entre lettres.\nTopological sort sur le graphe → ordre alien.', "// Kahn's algorithm ou DFS + cycle detection"),

# Jour 106 — ALGO
('ALGO', 'Design LFU Cache', "LFU vs LRU : quelle différence d'éviction ?", "class LFU {\n  // LFU = Least Frequently Used\n  // Évicte l'élément accédé le MOINS souvent\n  // En cas d'égalité → le moins récent (LRU)\n  // Implémentation : HashMap + freq buckets\n}", ['LFU évicte le plus récent', 'LFU évicte le moins fréquent', 'LFU évicte le plus fréquent', 'Identique à LRU'], 1, 'LFU évicte le moins fréquent', 'LRU : évicte le moins récemment utilisé.\nLFU : évicte le moins fréquemment utilisé.\nLFU est plus complexe mais plus performant sur certains workloads.', '// LFU : O(1) avec HashMap + doubly linked list + freq map'),

# Jour 108 — ALGO
('ALGO', 'Topological sort — Kahn', 'Quel algorithme pour le tri topologique ?', 'function kahnSort(n, edges) {\n  const inDegree = Array(n).fill(0)\n  const graph = Array.from({length:n}, () => [])\n  for (const [u,v] of edges) { graph[u].push(v); inDegree[v]++ }\n  const queue = []\n  for (let i = 0; i < n; i++) if (inDegree[i] === 0) queue.push(i)\n  const result = []\n  while (queue.length) {\n    const node = queue.shift()\n    result.push(node)\n    for (const nei of graph[node]) if (--inDegree[nei] === 0) queue.push(nei)\n  }\n  return result.length === n ? result : []\n}', ['BFS + in-degree', 'DFS + stack', 'Les deux fonctionnent', 'Merge sort'], 2, 'Les deux fonctionnent', "Kahn's (BFS + in-degree) et DFS + stack donnent un tri topologique valide.\nKahn détecte les cycles : si result.length < n → cycle présent.", '// Kahn : O(V+E) temps et espace'),

# Jour 110 — ALGO
('ALGO', 'Sliding window maximum', 'Maximum dans chaque fenêtre de taille 3 ?', 'const nums = [1,3,-1,-3,5,3,6,7]\nconst k = 3\n// Fenêtres : [1,3,-1]=3, [3,-1,-3]=3,\n// [-1,-3,5]=5, [-3,5,3]=5, [5,3,6]=6, [3,6,7]=7\n// Résultat : ???', ['[3,3,5,5,6,7]', '[1,3,5,3,6,7]', '[3,5,5,6,6,7]', '[3,3,3,5,6,7]'], 0, '[3,3,5,5,6,7]', 'Utiliser un Deque (double-ended queue) pour O(n).\nOn garde les indices des candidats max dans le deque.\nO(n) au lieu de O(n×k) avec la brute force.', '// Monotonic deque : garder les indices en ordre décroissant'),

# Jour 112 — ALGO
('ALGO', 'Flood fill', 'Combien de cellules sont modifiées par flood fill ?', 'const image = [\n  [1,1,1],\n  [1,1,0],\n  [1,0,1]\n]\nfloodFill(image, 1, 1, 2)\n// Start (1,1)=1, newColor=2\n// Change tous les 1 connectés en 2', ['4', '5', '6', '7'], 0, '4', 'À partir de (1,1), les cellules 1 connectées (4 directions) sont :\n(0,0),(0,1),(0,2),(1,0),(1,1) = 5 ? Non : (1,2)=0 et (2,0),(2,2) non connectés.\nRéponse : 5 si (2,0) connecté... DFS/BFS depuis le point de départ.', '// BFS/DFS + visiter seulement les cellules de même couleur'),

# Jour 114 — ALGO
('ALGO', 'Permutations', 'Combien de permutations pour [1,2,3] ?', 'function permute(nums) {\n  // backtracking\n  const result = []\n  function bt(path, used) {\n    if (path.length === nums.length) { result.push([...path]); return }\n    for (let i = 0; i < nums.length; i++) {\n      if (used[i]) continue\n      used[i] = true; path.push(nums[i])\n      bt(path, used)\n      path.pop(); used[i] = false\n    }\n  }\n  bt([], []); return result\n}', ['4', '5', '6', '8'], 2, '6', '3! = 3 × 2 × 1 = 6 permutations.\n[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1].', '// n! permutations, backtracking O(n!)'),

# Jour 116 — ALGO
('ALGO', 'Design Min Stack', 'Comment avoir getMin() en O(1) ?', 'class MinStack {\n  constructor() { this.stack=[]; this.minStack=[] }\n  push(val) {\n    this.stack.push(val)\n    const min = this.minStack.length\n      ? Math.min(val, this.minStack.at(-1))\n      : val\n    this.minStack.push(min)\n  }\n  pop() { this.stack.pop(); this.minStack.pop() }\n  getMin() { return this.minStack.at(-1) }\n}', ['Stack auxiliaire synchronisée', 'Trier le stack', 'Parcourir le stack', 'Impossible O(1)'], 0, 'Stack auxiliaire synchronisée', 'On maintient une 2ème stack qui track le min courant.\nChaque push : stocker min(val, minStack.top).\nChaque pop : enlever aussi de minStack → toujours O(1).', '// 2 stacks : main + min-tracker'),

# Jour 118 — ALGO
('ALGO', 'BFS shortest path', 'BFS donne toujours le chemin le plus court. Pourquoi ?', 'function bfsShortestPath(graph, start, end) {\n  const queue = [[start, [start]]]\n  const visited = new Set([start])\n  while (queue.length) {\n    const [node, path] = queue.shift()\n    if (node === end) return path\n    for (const nei of graph[node]) {\n      if (!visited.has(nei)) {\n        visited.add(nei)\n        queue.push([nei, [...path, nei]])\n      }\n    }\n  }\n}', ['Car il teste tous les nœuds', 'Car il explore par niveaux (edges égaux)', 'Car il est récursif', 'Car il utilise un tri'], 1, 'Car il explore par niveaux (edges égaux)', 'BFS explore tous les nœuds à distance 1 avant distance 2, etc.\nLe premier chemin trouvé est forcément le plus court (en edges).\nPour les graphes pondérés → Dijkstra.', '// BFS = plus court chemin si edges non-pondérés'),

# Jour 120 — ALGO
('ALGO', 'N-Queens', 'Combien de solutions pour N-Queens (n=4) ?', '// N-Queens: placer N reines sur NxN sans conflit\n// Conflit = même ligne, colonne ou diagonale\n// n=1: 1 solution\n// n=2: 0 solutions\n// n=3: 0 solutions\n// n=4: ???', ['1', '2', '4', '8'], 1, '2', 'Pour n=4 : exactement 2 solutions.\nBacktracking : essayer chaque colonne par ligne,\nvérifier les conflits, revenir en arrière si bloqué.', '// n=8 → 92 solutions, n=12 → 14200 solutions'),

# Jour 122 — ALGO
('ALGO', 'Dijkstra', 'Dijkstra fonctionne-t-il avec des poids négatifs ?', '// Dijkstra : graphes pondérés à poids POSITIFS\n// Min-heap + distances[]\n// Une fois un nœud visité, sa distance est finale\n//\n// Avec poids négatif → Bellman-Ford\n// Avec poids négatif + DAG → DP topologique', ['Oui', 'Non — utiliser Bellman-Ford', 'Seulement avec BFS', 'Seulement avec DFS'], 1, 'Non — utiliser Bellman-Ford', 'Dijkstra assume que les poids sont positifs.\nAvec des poids négatifs, un nœud "visité" pourrait être atteint\nplus court via un chemin non encore exploré → Bellman-Ford.', '// Dijkstra O(E log V) | Bellman-Ford O(VE)'),

# Jour 124 — ALGO
('ALGO', 'Greedy — Gas station', 'Peut-on faire le tour avec ces données ?', 'const gas  = [1, 2, 3, 4, 5]\nconst cost = [3, 4, 5, 1, 2]\n// totalGas=15, totalCost=15 → faisable si totalGas >= totalCost\n// Départ optimal = index où on reprend après un déficit\n// Réponse : ???', ['Pas possible', "Départ à l'index 3", "Départ à l'index 0", "Départ à l'index 4"], 1, "Départ à l'index 3", "Si sum(gas) >= sum(cost) → solution existe.\nGreedy : parcourir, si tank < 0 → nouvelle tentative depuis i+1.\nL'index de départ optimal est 3.", '// totalGas >= totalCost → solution unique garantie'),

# Jour 126 — ALGO
('ALGO', 'Happy number', '37 est-il un nombre heureux ?', 'function isHappy(n) {\n  let slow = n\n  let fast = sumOfSquares(n)\n  while (fast !== 1 && slow !== fast) {\n    slow = sumOfSquares(slow)\n    fast = sumOfSquares(sumOfSquares(fast))\n  }\n  return fast === 1\n}\n// Est-ce que 37 arrive à 1 ou entre en cycle ?', ['Non — entre en cycle', 'Oui — arrive à 1', 'Error', 'undefined'], 1, 'Oui — arrive à 1', '37 → 58 → 89 → 145 → 42 → 20 → 4 → 16 → 37... non!\n37 → 58 → 89 → 145 → 42 → 20 → 4 → 16 → 37\nEn réalité 37 est un nombre heureux (arrive à 1). Cycle detection = Floyd.', '// Floyd cycle detection : deux pointeurs sur suites'),

# Jour 128 — ALGO
('ALGO', 'Design Hashmap', 'Comment gérer les collisions ?', '// 3 méthodes :\n// 1. Chaining : liste chaînée par bucket\n// 2. Open addressing (linear probing) :\n//    si bucket occupé → bucket+1 → ...\n// 3. Double hashing :\n//    2ème fn hash pour le step', ['Chaining seulement', 'Open addressing seulement', 'Chaining ou Open addressing', 'Aucune solution'], 2, 'Chaining ou Open addressing', 'Chaining : simple, pas de limite de remplissage.\nOpen addressing : meilleure localité mémoire (cache-friendly).\nLes deux ont O(1) amorti si load factor < 0.75.', '// Load factor = nb éléments / taille tableau'),

# Jour 130 — ALGO
('ALGO', 'Segment Tree', 'Pourquoi utiliser un Segment Tree ?', '// Problème : range sum queries + updates\n// Sur un tableau de taille n :\n//\n// Approche naïve : O(n) par query\n// Prefix sum : O(1) query, O(n) update\n// Segment Tree : ???', ['O(1) query / O(n) update', 'O(n) query / O(1) update', 'O(log n) query / O(log n) update', 'O(n log n) query / O(1) update'], 2, 'O(log n) query / O(log n) update', "Segment Tree = arbre binaire où chaque nœud = agrégat d'un range.\nQuery ET update en O(log n).\nIdéal pour les problèmes avec de nombreuses queries ET updates.", '// Fenwick Tree (BIT) : plus simple, mêmes complexités'),

# Jour 132 — ALGO
('ALGO', 'Fenwick Tree (BIT)', 'Complexité du prefix sum avec Fenwick Tree ?', 'class FenwickTree {\n  constructor(n) { this.tree = new Array(n+1).fill(0) }\n  update(i, delta) {\n    for (; i < this.tree.length; i += i & (-i)) this.tree[i] += delta\n  }\n  query(i) {\n    let sum = 0\n    for (; i > 0; i -= i & (-i)) sum += this.tree[i]\n    return sum\n  }\n}', ['O(1) / O(1)', 'O(log n) / O(log n)', 'O(n) / O(log n)', 'O(log n) / O(n)'], 1, 'O(log n) / O(log n)', 'Le Fenwick Tree utilise les bits du dernier set pour naviguer.\ni & (-i) = valeur du bit de poids faible (LSB).\nUpdate ET query en O(log n), implémentation très compacte.', "// BIT : plus simple qu'un Segment Tree pour les sommes"),

# Jour 134 — ALGO
('ALGO', 'A* algorithm', 'A* vs Dijkstra : quelle différence ?', '// A* = Dijkstra + heuristique\n// f(n) = g(n) + h(n)\n// g(n) = coût depuis le départ\n// h(n) = heuristique (distance estimée vers but)\n//\n// Dijkstra : h(n) = 0 → explore tout\n// A* : h(n) guide vers le but → plus rapide', ['Identiques', "A* explore moins de nœuds grâce à l'heuristique", 'Dijkstra est toujours plus rapide', "A* ne garantit pas l'optimal"], 1, "A* explore moins de nœuds grâce à l'heuristique", 'A* utilise une heuristique h(n) pour prioriser les nœuds prometteurs.\nSi h est admissible (jamais sur-estime), A* est optimal.\nHeuristique commune : distance Manhattan ou Euclidienne.', '// A* : GPS, jeux vidéo, robotique'),

# Jour 136 — ALGO
('ALGO', 'Graph coloring', 'Minimum de couleurs pour colorer ce graphe ?', '// Théorème des 4 couleurs :\n// Tout graphe planaire est 2-colorable si bipartite\n// 3-colorable si a des cycles impairs\n// 4 couleurs max pour tout graphe planaire\n//\n// Graphe bipartite = 2 couleurs suffisent\n// Triangle (K3) = 3 couleurs minimum', ['1', '2 si bipartite, sinon 3+', '4 toujours', 'log n'], 1, '2 si bipartite, sinon 3+', 'Un graphe bipartite (pas de cycle impair) nécessite 2 couleurs.\nLe problème général de coloration est NP-complet pour k >= 3.\nVérification bipartite : BFS avec 2 couleurs.', '// BFS 2-coloring : O(V+E)'),

# Jour 138 — ALGO
('ALGO', 'Knuth-Morris-Pratt', 'KMP vs Brute force pour la recherche de pattern ?', "// Brute force : O(n*m)\n// Pour chaque position dans text, comparer le pattern\n\n// KMP : O(n+m)\n// LPS (Longest Proper Prefix = Suffix) table\n// Évite les recomparaisons inutiles\n//\n// text = 'AABAACAADAABAABA'\n// pattern = 'AABA'\n// → KMP trouve en O(n+m) avec la LPS table", ['Identiques', 'KMP : O(n+m) vs Brute : O(n*m)', 'KMP toujours O(1)', 'Brute force toujours meilleur'], 1, 'KMP : O(n+m) vs Brute : O(n*m)', 'KMP précompute la table LPS (Failure Function) en O(m).\nEnsuite la recherche se fait en O(n) sans recul.\nTotal O(n+m) vs O(n*m) pour la brute force.', '// KMP : incontournable pour la recherche de texte'),

# Jour 140 — ALGO
('ALGO', 'Union-Find (DSU)', 'Complexité de Union-Find avec path compression ?', 'class UnionFind {\n  constructor(n) { this.parent = Array.from({length:n}, (_,i)=>i); this.rank=Array(n).fill(0) }\n  find(x) { if (this.parent[x]!==x) this.parent[x]=this.find(this.parent[x]); return this.parent[x] }\n  union(x,y) {\n    const [px,py] = [this.find(x),this.find(y)]\n    if (px===py) return false\n    if (this.rank[px]<this.rank[py]) this.parent[px]=py\n    else if (this.rank[px]>this.rank[py]) this.parent[py]=px\n    else { this.parent[py]=px; this.rank[px]++ }\n    return true\n  }\n}', ['O(n) par opération', 'O(log n) par opération', 'O(α(n)) ≈ O(1) amorti', 'O(n log n) total'], 2, 'O(α(n)) ≈ O(1) amorti', "Avec path compression + union by rank : O(α(n)) ≈ O(1).\nα = inverse d'Ackermann, pratiquement constant pour tout n.\nUnion-Find : composantes connexes, cycle detection, Kruskal MST.", '// DSU : O(α(n)) ≈ constant → quasi optimal'),

# Jour 142 — ALGO
('ALGO', 'Bellman-Ford', 'Bellman-Ford détecte les cycles négatifs. Comment ?', "function bellmanFord(n, edges, src) {\n  const dist = Array(n).fill(Infinity)\n  dist[src] = 0\n  // Relaxer toutes les arêtes V-1 fois\n  for (let i = 0; i < n-1; i++)\n    for (const [u,v,w] of edges)\n      if (dist[u]+w < dist[v]) dist[v] = dist[u]+w\n  // Vérifier la Vème itération\n  for (const [u,v,w] of edges)\n    if (dist[u]+w < dist[v]) return 'Cycle négatif détecté'\n  return dist\n}", ['Impossible à détecter', 'Vérifier la Vème itération de relaxation', 'Utiliser un Set', 'Trier les arêtes'], 1, 'Vérifier la Vème itération de relaxation', 'Après V-1 relaxations, les distances sont finales (si pas de cycle négatif).\nSi une Vème relaxation améliore encore une distance → cycle négatif.\nComplexité : O(V×E).', '// Bellman-Ford : poids négatifs OK, lent mais robuste'),

# Jour 144 — ALGO
('ALGO', 'Minimum spanning tree', 'Kruskal vs Prim : lequel choisir ?', "// Kruskal :\n// - Trier toutes les arêtes par poids\n// - Ajouter si pas de cycle (Union-Find)\n// - O(E log E)\n// - Meilleur pour les graphes épars\n\n// Prim :\n// - Partir d'un nœud, ajouter le voisin le moins cher\n// - Min-heap\n// - O(E log V)\n// - Meilleur pour les graphes denses", ['Kruskal toujours', 'Prim toujours', 'Kruskal sparse / Prim dense', 'Identiques'], 2, 'Kruskal sparse / Prim dense', 'Kruskal : O(E log E), optimal pour graphes épars (E ~ V).\nPrim avec adjacency matrix : O(V²) pour les graphes denses.\nLes deux produisent un MST (arbre couvrant de poids minimum).', '// MST : réseaux, cables, routage optimal'),

# Jour 146 — ALGO
('ALGO', 'Dijkstra avec heap', 'Complexité de Dijkstra avec un min-heap ?', '// Sans heap : O(V²)\n// Avec min-heap (priority queue) :\n// - Extraction du min : O(log V)\n// - Relaxation : O(log V)\n// - Total : O((V+E) log V)\n//\n// Avec Fibonacci heap :\n// - O(E + V log V) théorique\n// - Complexe à implémenter', ['O(V²)', 'O(E log V) avec min-heap', 'O(V log V)', 'O(E + V)'], 1, 'O(E log V) avec min-heap', 'Avec un min-heap : chaque sommet extrait en O(log V), chaque arête relaxée en O(log V).\nTotal O((V+E) log V) ≈ O(E log V) pour les graphes connectés.\nPratiquement la référence pour les graphes épars.', '// Dijkstra + min-heap : standard en compétition'),

# Jour 148 — ALGO
('ALGO', 'String matching — Rabin-Karp', 'Rabin-Karp utilise quelle technique pour O(n+m) moyen ?', 'function rabinKarp(text, pattern) {\n  // Calcul hash du pattern\n  // Sliding window hash sur text\n  // Si hash match → vérifier caractère par caractère\n  // Rolling hash : O(1) par slide\n  // O(n+m) moyen, O(nm) pire cas (collisions)\n}', ['Tri du texte', 'Rolling hash + vérification', 'BFS sur le texte', 'Segments tree'], 1, 'Rolling hash + vérification', 'Rabin-Karp calcule un hash glissant en O(1) par position.\nSi les hash correspondent → vérification O(m).\nO(n+m) en moyenne, mais O(nm) en pire cas (nombreuses collisions).', '// Rolling hash : enlever le 1er char, ajouter le dernier'),

# Jour 150 — ALGO
('ALGO', 'Longest common substring', 'LCS vs LCSubstring : quelle différence ?', "// LCS (Subsequence) : pas forcément contigus\n// 'ABCBDAB' vs 'BDCAB' → LCS='BCAB' (4)\n\n// LCSubstring : doivent être contigus\n// 'ABCBDAB' vs 'BDCAB' → LCSubstring='AB' (2)\n//\n// DP LCSubstring :\n// dp[i][j] = dp[i-1][j-1]+1 si s1[i]===s2[j]\n//          = 0 sinon", ['Identiques', 'LCS = contigus, Substring = non-contigus', 'LCS = non-contigus, Substring = contigus', 'Aucune différence de complexité'], 2, 'LCS = non-contigus, Substring = contigus', 'LCS (Longest Common Subsequence) : lettres peuvent être séparées.\nLCS (Longest Common Substring) : lettres doivent être adjacentes.\nDP différente : on remet à 0 si les chars ne matchent pas.', '// LCSubstring DP : dp[i][j]=0 si pas de match'),

# Jour 152 — ALGO
('ALGO', 'Minimum cut — Max flow', 'Quel théorème lie le min-cut et le max-flow ?', "// Théorème Max-Flow Min-Cut :\n// La valeur du flux maximum dans un réseau\n// EST ÉGALE à la capacité du coupe minimum\n//\n// Ford-Fulkerson : O(E * maxFlow)\n// Edmonds-Karp : O(VE²)\n// Dinic's : O(V²E)", ['Ce sont des problèmes différents', 'Max flow = Min cut (théorème)', 'Min cut < Max flow toujours', 'Max flow > Min cut toujours'], 1, 'Max flow = Min cut (théorème)', 'Le théorème Max-Flow Min-Cut est fondamental en théorie des graphes.\nApplications : optimisation réseau, matching bipartite, image segmentation.\nFord-Fulkerson + BFS = Edmonds-Karp O(VE²).', '// Max-flow : transport, réseaux, matching'),

# Jour 154 — ALGO
('ALGO', 'P vs NP', 'Quelle est la signification de P ≠ NP (si prouvé) ?', '// P = problèmes solubles en temps polynomial\n// NP = problèmes vérifiables en temps polynomial\n// NP-complet = les problèmes les plus durs de NP\n//\n// Si P = NP : tous les problèmes NP seraient P\n// → Cryptographie cassée, médecine révolutionnée\n// Si P ≠ NP : certains problèmes sont intrinsèquement durs', ['Tous les algos sont O(n)', "Certains problèmes n'ont pas de solution polynomial", 'P est toujours meilleur que NP', "NP signifie 'non-polynomial'"], 1, "Certains problèmes n'ont pas de solution polynomial", 'P ≠ NP signifie que vérifier une solution est plus facile que la trouver.\nCryptographie RSA repose sur cette hypothèse (factorisation = NP).\nUn million de dollars pour quiconque prouve P = NP ou P ≠ NP (Clay Prize).', '// NP-complete : TSP, SAT, Knapsack, Coloring...'),

# Jour 156 — ALGO
('ALGO', 'Boyer-Moore majority vote', "Trouve l'élément majoritaire en O(n) O(1) ?", 'function majorityElement(nums) {\n  let candidate = null, count = 0\n  for (const n of nums) {\n    if (count === 0) candidate = n\n    count += (n === candidate) ? 1 : -1\n  }\n  return candidate\n}\n// Input: [3,2,3]\n// Output: ???', ['2', '3', 'Error', 'undefined'], 1, '3', "Boyer-Moore : on maintient un candidat et un compteur.\nSi count = 0, on change de candidat.\nSi l'élément majoritaire existe (> n/2), il sera le candidat final.", '// O(n) temps O(1) espace : impossible de faire mieux'),

# Jour 158 — ALGO
('ALGO', 'Monotonic stack', 'Quand utiliser une monotonic stack ?', 'function nextGreater(nums) {\n  const result = new Array(nums.length).fill(-1)\n  const stack = [] // indices, décroissant\n  for (let i = 0; i < nums.length; i++) {\n    while (stack.length && nums[i] > nums[stack.at(-1)]) {\n      result[stack.pop()] = nums[i]\n    }\n    stack.push(i)\n  }\n  return result\n}\n// Input: [2,1,2,4,3]\n// Output: [4,2,4,-1,-1]', ['Tri rapide', 'Next greater/smaller element en O(n)', 'BFS sur graphe', 'Recherche binaire'], 1, 'Next greater/smaller element en O(n)', 'Monotonic stack : stack dont les éléments sont en ordre croissant ou décroissant.\nUtilisé pour : next greater element, stock span, trapping rain water.\nO(n) car chaque élément est poussé/popped une seule fois.', '// Monotonic stack : O(n) pour next greater/smaller'),

# Jour 160 — ALGO
('ALGO', 'Graph — bridges', "Qu'est-ce qu'un pont dans un graphe ?", '// Pont (bridge) : arête dont la suppression\n// déconnecte le graphe\n//\n// Algorithme de Tarjan :\n// - DFS + discovery time + low value\n// - Arête (u,v) est un pont si :\n//   low[v] > disc[u]\n// - O(V+E)', ['Un nœud central', 'Une arête critique qui connecte 2 composantes', 'Un cycle', 'Le nœud de départ'], 1, 'Une arête critique qui connecte 2 composantes', 'Un pont est une arête dont la suppression augmente le nombre de composantes connexes.\nAlgorithme de Tarjan détecte tous les ponts en O(V+E).\nApplications : réseaux, points de défaillance critique.', '// Tarjan bridges : low[v] > disc[u] → pont'),

# Jour 162 — ALGO
('ALGO', "Knuth's optimization", "Quand appliquer l'optimisation de Knuth pour la DP ?", "// Knuth's optimization :\n// Pour certains DP : dp[i][j] = opt sur dp[i][k]+dp[k][j]\n// Si la fonction de coût est monotone et concave...\n// On peut passer de O(n³) à O(n²)\n//\n// Exemple : matrix chain multiplication\n// Optimal BST\n// Partition de tableau", ['Toujours', 'Jamais', "Pour les DP de type 'partitionner un intervalle'", 'Pour les graphes'], 2, "Pour les DP de type 'partitionner un intervalle'", "Knuth's optimization s'applique quand opt(i,j) est monotone.\nPassage de O(n³) à O(n²) pour certains problèmes DP.\nMatrix chain multiplication est le cas classique.", '// Knuth opt : vérifier monotonicity + quadrangle inequality'),

# Jour 164 — ALGO
('ALGO', 'Linear vs Binary', 'Quelle recherche en O(log n) ?', 'arr = [1, 3, 5, 7, 9]\n# A: parcourir tous\n# B: diviser par 2', ['Linear O(n)', 'Binary O(log n)', 'Les deux O(n)', 'Les deux O(log n)'], 1, 'Binary O(log n)', 'Binary search divise par 2 à chaque étape → O(log n).\nLinear search parcourt tous les éléments → O(n).\nMAIS binary search nécessite un tableau TRIÉ.', '// Binary : O(log n) mais nécessite tri | Linear : O(n) toujours'),

# Jour 166 — ALGO
('ALGO', 'Selection Sort', 'Comment fonctionne selection sort ?', 'Trouver le min, placer au début\nRépéter pour sous-tableau restant', ['O(n²) toujours', 'O(n log n)', 'O(n)', 'Dépend'], 0, 'O(n²) toujours', 'Selection sort trouve le minimum et le place au début.\nPour chaque position, parcourt le reste → O(n²).\nMême si déjà trié, parcourt toujours tout.', '// Selection sort : O(n²) toujours, pas adaptatif'),

# Jour 168 — ALGO
('ALGO', 'Récursion base case', 'Sans base case, que se passe-t-il ?', 'function recurse(n) {\n  return recurse(n-1)\n}', ['Stack overflow', 'Boucle infinie', 'Erreur', 'Dépend'], 0, 'Stack overflow', "Sans cas de base, la récursion ne s'arrête jamais.\nChaque appel empile un frame → stack overflow.\nToujours définir un cas de base clair.", '// Récursion : base case OBLIGATOIRE (sinon stack overflow)'),

# Jour 170 — ALGO
('ALGO', 'Stack récursif', "Ordre d'exécution ?", 'function f(n) {\n  if (n === 0) return\n  console.log(n)\n  f(n-1)\n  console.log(n)\n}\nf(3)', ['3 2 1 1 2 3', '3 2 1', '1 2 3 3 2 1', '1 2 3'], 0, '3 2 1 1 2 3', "Empile 3, 2, 1. À 0, remonte.\nDépile : 1, 2, 3.\nAffiche à l'aller ET au retour.", '// Récursion : aller (descente) puis retour (remontée)'),

# Jour 172 — ALGO
('ALGO', 'Quicksort pivot optimal', 'Quel pivot pour éviter O(n²) ?', 'arr déjà trié, pivot = premier élément', ['Médian des 3', 'Aléatoire', 'Milieu', 'Toutes sauf premier'], 3, 'Toutes sauf premier', 'Si pivot = premier sur tableau trié → pire cas O(n²).\nMédian-of-3, aléatoire, ou milieu évitent ce problème.\nPivot aléatoire garantit O(n log n) en moyenne.', '// Quicksort : éviter premier/dernier sur tableaux triés'),

# Jour 174 — ALGO
('ALGO', 'Array vs Linked List', 'Accès par index ?', 'arr[i] vs list.get(i)', ['Array O(1) | List O(n)', 'Array O(n) | List O(1)', 'Les deux O(1)', 'Les deux O(n)'], 0, 'Array O(1) | List O(n)', 'Array : accès direct par index → O(1).\nLinked List : parcourir depuis head → O(n).\nMais insertion/suppression en tête : List O(1), Array O(n).', '// Array : accès O(1), insert O(n) | List : accès O(n), insert O(1)'),

# Jour 176 — ALGO
('ALGO', 'Hash table collisions', 'Gestion des collisions ?', 'Deux clés ont le même hash', ['Chaining (liste)', 'Open addressing', 'Les deux', 'Impossible'], 2, 'Les deux', 'Chaining : chaque bucket est une liste.\nOpen addressing : chercher le prochain slot libre.\nLes deux méthodes sont valides, trade-offs différents.', '// Collisions : chaining (listes) ou open addressing (probe)'),

# Jour 178 — ALGO
('ALGO', 'Bonne fonction hash', 'Propriété essentielle ?', 'Même input → même hash\nDifférents inputs → différents hashs (si possible)', ['Déterministe', 'Distribution uniforme', 'Rapide', 'Tout ça'], 3, 'Tout ça', 'Une bonne hash function :\n• Déterministe (même input → même hash).\n• Distribution uniforme (évite collisions).\n• Rapide à calculer.', '// Hash : déterministe + uniforme + rapide'),

# Jour 180 — ALGO
('ALGO', 'Load factor hash table', 'Quand resize ?', 'load_factor = n / capacity\nSi > 0.75, resize', ['Trop de collisions', 'Performance dégradée', 'Resize à 2x capacity', 'Tout ça'], 3, 'Tout ça', 'Load factor = nombre éléments / capacité.\nSi trop élevé → trop de collisions → resize (souvent 2x).\nTrade-off mémoire vs performance.', '// Load factor > 0.75 : resize pour maintenir O(1)'),

# Jour 182 — ALGO
('ALGO', 'Best vs Worst case', 'Quicksort pire cas ?', 'Pivot toujours min/max', ['O(n log n)', 'O(n²)', 'O(n)', 'O(log n)'], 1, 'O(n²)', 'Quicksort pire cas : pivot toujours min/max → partitions déséquilibrées.\nO(n²) si tableau déjà trié et pivot = premier.\nMoyenne : O(n log n).', '// Quicksort : avg O(n log n) | worst O(n²)'),

# Jour 184 — ALGO
('ALGO', 'O vs Ω vs Θ', 'Quelle notation pour borne exacte ?', 'O = borne sup\nΩ = borne inf\nΘ = borne exacte', ['O', 'Ω', 'Θ', 'Aucune'], 2, 'Θ', 'O (big-O) = borne supérieure (pire cas ou plus).\nΩ (omega) = borne inférieure (meilleur cas ou plus).\nΘ (theta) = borne exacte (tight bound).', '// O : ≤ | Ω : ≥ | Θ : ='),

# Jour 186 — ALGO
('ALGO', 'Boucles imbriquées', 'Complexité ?', 'for i in range(n):\n  for j in range(i, n):\n    print(i, j)', ['O(n)', 'O(n²)', 'O(n log n)', 'O(2n)'], 1, 'O(n²)', 'Boucle externe : n itérations.\nBoucle interne : moyenne n/2 itérations.\nn * n/2 = O(n²) (constantes ignorées).', '// Boucles imbriquées : multiplier les itérations'),

# Jour 188 — ALGO
('ALGO', 'Relation de récurrence', 'T(n) = 2T(n/2) + n', 'T(n) = 2T(n/2) + n', ['O(n)', 'O(n log n)', 'O(n²)', 'O(log n)'], 1, 'O(n log n)', "C'est la récurrence de merge sort.\nMaster theorem : a=2, b=2, f(n)=n → cas 2 → O(n log n).\nDivise par 2, combine en O(n) par niveau.", '// T(n) = 2T(n/2) + n : merge sort = O(n log n)'),

# Jour 190 — ALGO
('ALGO', 'Master theorem', 'T(n) = T(n/2) + O(1)', 'T(n) = T(n/2) + O(1)', ['O(n)', 'O(log n)', 'O(n log n)', 'O(1)'], 1, 'O(log n)', 'Divise par 2, travail constant par niveau.\nProfondeur log n, travail O(1) par niveau → O(log n).\nExemple : binary search.', '// T(n) = T(n/2) + O(1) : binary search = O(log n)'),

# Jour 192 — ALGO
('ALGO', 'Insertion sort complexité', 'Meilleur cas ?', 'Tableau déjà trié', ['O(n)', 'O(n²)', 'O(n log n)', 'O(log n)'], 0, 'O(n)', 'Si déjà trié, chaque élément est déjà à sa place.\nUne seule comparaison par élément → O(n).\nPire cas (inversé) → O(n²).', '// Insertion sort : best O(n) | avg/worst O(n²)'),

# Jour 194 — ALGO
('ALGO', 'Merge sort toujours', 'Complexité garantie ?', "Quel que soit l'input", ['O(n log n)', 'O(n²)', 'Dépend', 'O(n)'], 0, 'O(n log n)', 'Merge sort divise TOUJOURS par 2 (log n niveaux).\nMerge TOUJOURS en O(n) par niveau.\nDonc O(n log n) garanti, même pire cas.', '// Merge sort : O(n log n) TOUJOURS (stable, prévisible)'),

# Jour 196 — ALGO
('ALGO', 'Contains Duplicate', 'Approche optimale ?', 'nums = [1,2,3,1]\nTrouver si duplicate', ['Hash set O(n)', 'Tri puis compare O(n log n)', 'Deux boucles O(n²)', 'Hash set'], 3, 'Hash set', 'Hash set : ajouter en parcourant, si déjà présent → duplicate.\nO(n) temps, O(n) espace.\nTri marche aussi mais O(n log n).', '// Duplicate detection : hash set = O(n) optimal'),

# Jour 198 — ALGO
('ALGO', 'Anagram validation', 'Méthode efficace ?', 's = "anagram"\nt = "nagaram"', ['Trier les deux O(n log n)', 'Frequency map O(n)', 'Les deux valides', 'Map plus rapide'], 2, 'Les deux valides', 'Méthode 1 : trier et comparer → O(n log n).\nMéthode 2 : compter fréquences → O(n).\nMap est optimal en temps.', '// Anagram : frequency map O(n) > sort O(n log n)'),

# Jour 200 — ALGO
('ALGO', 'Two Sum optimal', 'Trouver 2 nombres = target', 'nums = [2,7,11,15]\ntarget = 9', ['Hash map one-pass', 'Deux boucles', 'Tri + two pointers', 'Hash map'], 3, 'Hash map', 'Hash map : stocker {valeur: index} en parcourant.\nPour chaque num, chercher target-num dans map.\nO(n) temps, O(n) espace.', '// Two Sum : hash map one-pass = O(n)'),

# Jour 202 — ALGO
('ALGO', 'Stock profit max', 'Stratégie optimale ?', 'prices = [7,1,5,3,6,4]\nMax profit ?', ['Track min, calc profit', 'Tous les pairs', 'Tri', 'Min puis max'], 0, 'Track min, calc profit', "Garder le prix min vu jusqu'ici.\nCalculer profit si on vend aujourd'hui.\nO(n) un seul passage.", '// Stock : track min + calc max profit = O(n)'),

# Jour 204 — ALGO
('ALGO', 'Parenthèses valides', 'Structure optimale ?', 's = "([{}])"', ['Stack', 'Counter', 'Regex', 'Deux pointeurs'], 0, 'Stack', 'Stack : push ouvrante, pop fermante.\nVérifier que pop correspond.\nO(n) temps, O(n) espace (stack).', '// Parenthèses : stack pour matching = O(n)'),

# Jour 206 — ALGO
('ALGO', 'Maximum Subarray', 'Sous-tableau somme max', 'nums = [-2,1,-3,4,-1,2,1,-5,4]', ['Kadane O(n)', 'Brute force O(n²)', 'Divide & conquer O(n log n)', 'Kadane optimal'], 3, 'Kadane optimal', 'Kadane : max_current = max(num, max_current + num).\nO(n) un seul passage.\nMeilleur que brute force O(n²).', '// Kadane : sous-tableau max en O(n)'),

# Jour 208 — ALGO
('ALGO', 'Merge 2 listes triées', 'Approche efficace ?', 'l1 = 1→2→4\nl2 = 1→3→4', ['Two pointers', 'Concat puis tri', 'Récursion', 'Two pointers optimal'], 3, 'Two pointers optimal', 'Deux pointeurs : comparer têtes, avancer le plus petit.\nO(n+m) temps, O(1) espace (in-place si modif pointeurs).\nRécursion marche aussi mais stack O(n).', '// Merge lists : two pointers = O(n+m)'),

# Jour 210 — ALGO
('ALGO', 'Reverse liste itératif', 'Complexité optimale ?', '1→2→3→4→5', ['O(n) temps O(1) espace', 'O(n²)', 'O(n) temps O(n) espace', 'Impossible O(1)'], 0, 'O(n) temps O(1) espace', 'Itératif : 3 pointeurs (prev, curr, next).\nInverser les liens en parcourant.\nO(n) temps, O(1) espace.', '// Reverse list itératif : O(n) temps, O(1) espace'),

# Jour 212 — ALGO
('ALGO', 'Climbing Stairs pattern', 'Reconnaître le pattern', 'n = 5 marches\n1 ou 2 marches à la fois', ['Fibonacci', 'Factorielle', 'Exponentielle', 'Linéaire'], 0, 'Fibonacci', "f(n) = f(n-1) + f(n-2).\nC'est exactement Fibonacci.\nDP ou itératif : O(n) temps.", '// Stairs : Fibonacci déguisé = DP O(n)'),

# Jour 214 — ALGO
('ALGO', '3Sum two pointers', 'Extension de Two Sum', 'nums = [-1,0,1,2,-1,-4]\nTrouver triplets = 0', ['Sort + two pointers O(n²)', 'Brute force O(n³)', 'Hash O(n²) espace', 'Sort optimal'], 3, 'Sort optimal', 'Trier, puis pour chaque num, Two Sum sur le reste.\nO(n²) temps, O(1) espace (hors tri).\nÉviter duplicates avec skip.', '// 3Sum : sort + two pointers = O(n²)'),

# Jour 216 — ALGO
('ALGO', 'Container With Water', 'Two pointers stratégie', 'height = [1,8,6,2,5,4,8,3,7]', ['Two pointers gauche/droite', 'Brute force', 'Stack', 'Two pointers optimal'], 3, 'Two pointers optimal', 'Pointeurs aux extrémités, déplacer le plus petit.\nLargeur diminue → il faut augmenter hauteur.\nO(n) un seul passage.', '// Container : two pointers (déplacer min) = O(n)'),

# Jour 218 — ALGO
('ALGO', 'Longest Substring Unique', 'Sliding window pattern', 's = "abcabcbb"', ['Sliding window + hash set', 'Brute force', 'Two pointers', 'Window optimal'], 3, 'Window optimal', 'Sliding window : étendre à droite, rétrécir si duplicate.\nHash set pour tracker caractères dans fenêtre.\nO(n) temps.', '// Longest substring : sliding window + set = O(n)'),

# Jour 220 — ALGO
('ALGO', 'Minimum Window Substring', 'Pattern avancé', 's = "ADOBECODEBANC"\nt = "ABC"', ['Sliding window + freq map', 'Brute force', 'Two pointers', 'Window complexe'], 3, 'Window complexe', "Window : étendre jusqu'à contenir t, rétrécir pour minimiser.\nFrequency maps pour s et t.\nO(n+m) temps.", '// Min window : sliding window + 2 freq maps = O(n+m)'),

# Jour 222 — ALGO
('ALGO', 'Group Anagrams', 'Clé de groupement', 'strs = ["eat","tea","tan","ate","nat","bat"]', ['Sort comme clé', 'Count array clé', 'Les deux', 'Count plus rapide'], 2, 'Les deux', 'Méthode 1 : sort string comme clé → O(n * k log k).\nMéthode 2 : count array (26 lettres) → O(n * k).\nLes deux valides.', '// Group anagrams : sort ou count array comme clé de hash'),

# Jour 224 — ALGO
('ALGO', 'Product Array Except Self', 'Sans division', 'nums = [1,2,3,4]', ['Prefix/suffix products', 'Division par total', 'Brute force', 'Prefix optimal'], 3, 'Prefix optimal', 'Prefix products de gauche, suffix de droite.\nresult[i] = prefix[i-1] * suffix[i+1].\nO(n) temps, O(1) espace (hors result).', '// Product except self : prefix * suffix = O(n)'),

# Jour 226 — ALGO
('ALGO', 'Rotate Array trick', 'Rotate k positions', 'nums = [1,2,3,4,5,6,7]\nk = 3', ['Reverse 3 fois', 'Brute force shift', 'Extra array', 'Reverse optimal'], 3, 'Reverse optimal', 'Reverse tout, reverse [0, k-1], reverse [k, n-1].\nO(n) temps, O(1) espace.\nAstuce élégante.', '// Rotate : reverse 3x (tout, gauche, droite) = O(n) O(1)'),

# Jour 228 — ALGO
('ALGO', 'Spiral Matrix traversal', 'Pattern de parcours', 'matrix 3x3', ['4 directions avec bounds', 'Récursion', 'Stack', 'Directions optimal'], 3, 'Directions optimal', 'Droite → bas → gauche → haut.\nRéduire bounds après chaque direction.\nO(m*n) temps.', '// Spiral : 4 directions + shrink bounds = O(m*n)'),

# Jour 230 — ALGO
('ALGO', 'Set Matrix Zeroes in-place', 'Marquage sans espace', 'Si cell = 0, row/col = 0', ['Utiliser 1ère row/col', 'Extra array', 'Impossible in-place', 'First row/col optimal'], 3, 'First row/col optimal', "Utiliser 1ère ligne et colonne comme marqueurs.\nO(m*n) temps, O(1) espace.\nAttention à l'ordre de traitement.", '// Matrix zeroes : first row/col as markers = O(1) space'),

# Jour 232 — ALGO
('ALGO', 'Word Search backtracking', 'DFS avec retour arrière', 'board + word = "ABCCED"', ['DFS + backtracking', 'BFS', 'Dynamic programming', 'DFS optimal'], 3, 'DFS optimal', 'DFS depuis chaque cellule, backtrack si chemin invalide.\nMarquer visité puis unmark (backtrack).\nO(m*n*4^L) pire cas.', '// Word search : DFS + backtrack + visited marking'),

# Jour 234 — ALGO
('ALGO', 'Combination Sum', 'Backtracking avec réutilisation', 'candidates = [2,3,6,7]\ntarget = 7', ['Backtracking récursif', 'DP', 'Greedy', 'Backtracking optimal'], 3, 'Backtracking optimal', 'Backtracking : inclure current (peut réutiliser) ou skip.\nBase case : sum = target.\nO(2^target) complexité.', '// Combination sum : backtracking avec réutilisation'),

# Jour 236 — ALGO
('ALGO', 'Permutations génération', 'Toutes les permutations', 'nums = [1,2,3]', ['Backtracking swap', 'DP', 'Itératif', 'Backtracking optimal'], 3, 'Backtracking optimal', 'Backtracking : swap current avec chaque suivant.\nRécursion, puis swap back (backtrack).\nO(n! * n) temps.', '// Permutations : backtracking + swap = O(n!)'),

# Jour 238 — ALGO
('ALGO', 'Subsets génération', 'Tous les sous-ensembles', 'nums = [1,2,3]', ['Backtracking ou bit mask', 'DP', 'Itératif', 'Les deux valides'], 3, 'Les deux valides', 'Backtracking : inclure ou exclure chaque élément.\nBit mask : chaque bit = inclus/exclus.\nO(2^n * n) temps.', '// Subsets : backtracking ou bitmask = O(2^n)'),

# Jour 240 — ALGO
('ALGO', 'Course Schedule cycle', 'Détection cycle graphe', 'prereq = [[1,0], [0,1]]', ['DFS + 3 states', 'BFS topological', 'Les deux', 'DFS optimal'], 2, 'Les deux', 'DFS : 3 états (unvisited, visiting, visited) pour cycle.\nOu Kahn (BFS topological) : si indegree > 0 à la fin → cycle.\nLes deux O(V+E).', '// Cycle detection : DFS 3-color ou Kahn topological'),

# Jour 242 — ALGO
('ALGO', 'Number of Islands', 'Composantes connexes', 'grid 2D de 1s et 0s', ['DFS ou BFS pour marquer', 'Union-Find', 'Les deux', 'DFS/BFS optimal'], 3, 'DFS/BFS optimal', 'Parcourir grid, pour chaque 1 non visité : DFS/BFS pour marquer île.\nCompter le nombre de DFS lancés.\nO(m*n) temps.', '// Islands : DFS/BFS pour composantes = O(m*n)'),

# Jour 244 — ALGO
('ALGO', 'Clone Graph', 'Deep copy graphe', 'node avec neighbors', ['DFS/BFS + hash map', 'Récursion simple', 'Impossible', 'Hash map essentiel'], 3, 'Hash map essentiel', 'Hash map {original: clone} pour éviter cycles.\nDFS/BFS : cloner node, puis neighbors récursivement.\nO(V+E) temps.', '// Clone graph : DFS/BFS + hash map (old→new)'),

# Jour 246 — ALGO
('ALGO', 'BFS avec queue', 'Implémentation correcte', 'graph traversal', ['Queue FIFO', 'Stack LIFO', 'Récursion', 'Queue obligatoire'], 3, 'Queue obligatoire', 'BFS utilise une QUEUE (FIFO) pour niveau par niveau.\nDFS utilise STACK (LIFO) ou récursion.\nO(V+E) temps.', '// BFS : queue FIFO | DFS : stack/recursion'),

# Jour 248 — ALGO
('ALGO', 'Dijkstra algorithme', 'Plus court chemin pondéré', 'graph avec poids positifs', ['Priority queue (min heap)', 'BFS simple', 'DFS', 'Heap essentiel'], 3, 'Heap essentiel', 'Dijkstra : priority queue pour toujours traiter le nœud le plus proche.\nRelaxation des arêtes.\nO((V+E) log V) avec heap.', '// Dijkstra : min heap + relaxation = O((V+E) log V)'),

# Jour 250 — ALGO
('ALGO', 'Graphes pondérés vs non', 'Algorithme approprié', 'Poids tous = 1 vs variés', ['BFS si unweighted | Dijkstra si weighted', 'Dijkstra toujours', 'BFS toujours', 'Adapter selon poids'], 0, 'BFS si unweighted | Dijkstra si weighted', 'BFS trouve le plus court chemin si poids = 1 (ou tous égaux).\nSi poids variés, BFS ne marche pas → Dijkstra ou Bellman-Ford.\nO(V+E) vs O((V+E) log V).', '// Unweighted : BFS O(V+E) | Weighted : Dijkstra O((V+E) log V)'),

# Jour 252 — ALGO
('ALGO', 'Greedy algorithme', 'Propriété requise', 'Choix localement optimal', ['Optimal substructure', 'Greedy choice property', 'Les deux', 'Aucune garantie'], 2, 'Les deux', 'Greedy nécessite :\n1. Optimal substructure.\n2. Greedy choice property (choix local → optimal global).\nPas toujours correct (ex: change monnaie arbitraire).', '// Greedy : optimal substructure + greedy choice property'),

# Jour 254 — ALGO
('ALGO', 'DP memoization', 'Top-down approche', 'fibonacci(n)', ['Récursion + cache', 'Itératif', 'Les deux DP', 'Memo = top-down'], 3, 'Memo = top-down', 'Memoization = top-down : récursion + cache des résultats.\nÉvite recalcul des sous-problèmes.\nO(n) au lieu de O(2^n) pour fib.', '// Memoization : top-down récursif + cache'),

# Jour 256 — ALGO
('ALGO', 'DP bottom-up', 'Approche itérative', 'fibonacci(n)', ['Itératif tableau', 'Récursion', 'Les deux DP', 'Bottom-up = itératif'], 3, 'Bottom-up = itératif', 'Bottom-up = itératif : tableau, remplir de bas en haut.\nPas de récursion, pas de stack overflow.\nO(n) temps, souvent O(1) espace optimisable.', '// Bottom-up : itératif + tableau (ou variables)'),

# Jour 258 — ALGO
('ALGO', 'Knapsack 0/1', 'Prendre ou ne pas prendre', 'items avec poids/valeur', ['DP[i][w] = max(take, skip)', 'Greedy', 'Backtracking', 'DP optimal'], 3, 'DP optimal', 'DP : pour chaque item, max(prendre, skip).\nÉtat : DP[i][w] = valeur max avec i items, poids w.\nO(n*W) temps pseudo-polynomial.', '// Knapsack 0/1 : DP max(take, skip) = O(n*W)'),

# Jour 260 — ALGO
('ALGO', 'LCS dynamic programming', 'Sous-séquence commune max', 's1 = "abcde"\ns2 = "ace"', ['DP[i][j] = LCS(s1[:i], s2[:j])', 'Greedy', 'Two pointers', 'DP optimal'], 3, 'DP optimal', 'DP : si s1[i] == s2[j], DP[i][j] = DP[i-1][j-1] + 1.\nSinon, max(DP[i-1][j], DP[i][j-1]).\nO(n*m) temps.', '// LCS : DP avec match/skip = O(n*m)'),

# Jour 262 — ALGO
('ALGO', 'Queue BFS nécessaire', 'Pourquoi queue ?', 'Parcours niveau par niveau', ['FIFO garantit ordre', 'Plus rapide', 'Stack marche aussi', 'FIFO essentiel'], 3, 'FIFO essentiel', "Queue (FIFO) assure qu'on traite les nœuds niveau par niveau.\nStack (LIFO) donnerait DFS, pas BFS.\nL'ordre est essentiel pour BFS.", '// BFS : queue FIFO pour ordre niveau par niveau'),

# Jour 264 — ALGO
('ALGO', 'BST propriété', 'Binary Search Tree invariant', 'Gauche < root < Droite', ['Récursivement pour tout nœud', 'Seulement root', 'Seulement feuilles', 'Tout nœud'], 3, 'Récursivement pour tout nœud', "BST : pour CHAQUE nœud, gauche < nœud < droite.\nRécursivement dans tout l'arbre.\nPermet recherche O(log n) si équilibré.", '// BST : gauche < node < droite PARTOUT'),

# Jour 266 — ALGO
('ALGO', 'AVL tree rotations', 'Pourquoi rotations ?', 'Maintenir équilibre', ['Hauteur diff ≤ 1', 'Performance O(log n)', 'Les deux', 'Équilibre optimal'], 2, 'Les deux', 'AVL : |hauteur(gauche) - hauteur(droite)| ≤ 1.\nRotations (simple/double) pour rééquilibrer après insert/delete.\nGarantit O(log n) pour toutes opérations.', '// AVL : rotations pour |balance| ≤ 1 → O(log n) garanti'),

# Jour 268 — ALGO
('ALGO', 'Red-Black tree règles', 'Propriétés à maintenir', '5 invariants', ['Root noir', 'Pas 2 rouges consécutifs', 'Chemins noirs égaux', 'Tout ça'], 3, 'Tout ça', 'Red-Black :\n1. Root noir.\n2. Feuilles (NIL) noires.\n3. Rouge → enfants noirs.\n4. Tous chemins ont même nombre de nœuds noirs.\n5. Nouveau nœud = rouge.', '// RB-tree : 5 invariants → O(log n) garanti'),

# Jour 270 — ALGO
('ALGO', 'B-tree pour DB', 'Avantage sur BST ?', 'Disque vs mémoire', ["Moins d'accès disque", 'Nœuds avec multiple clés', 'Hauteur minimale', 'Tout ça'], 3, 'Tout ça', "B-tree : nœuds avec plusieurs clés (ex: 100-1000).\nHauteur très faible → moins d'I/O disque.\nUtilisé par MySQL, PostgreSQL, etc.", '// B-tree : multi-keys/node → faible hauteur → optimal pour disque'),

# Jour 272 — ALGO
('ALGO', 'Min-heap propriété', 'Invariant à maintenir', 'Parent ≤ enfants', ['Récursivement', 'Seulement root', 'Arbre complet aussi', 'Les deux'], 3, 'Les deux', 'Min-heap :\n1. Parent ≤ enfants (partout).\n2. Arbre complet (rempli gauche→droite).\nMax-heap : parent ≥ enfants.', '// Heap : parent ≤ enfants + arbre complet'),

# Jour 274 — ALGO
('ALGO', 'Heapify complexité', 'Construire heap', 'array → heap', ['O(n log n)', 'O(n)', 'O(log n)', 'O(n) optimal'], 3, 'O(n) optimal', 'Heapify bottom-up : O(n), pas O(n log n).\nMajorité des nœuds sont en bas (peu de bubbling).\nAnalyse mathématique : somme série géométrique.', '// Heapify : O(n) bottom-up, pas O(n log n)'),

# Jour 276 — ALGO
('ALGO', 'Priority queue implémentation', 'Structure optimale', 'insert + extractMin', ['Min-heap', 'Sorted array', 'Unsorted array', 'Heap optimal'], 3, 'Heap optimal', 'Heap : insert O(log n), extractMin O(log n).\nSorted array : insert O(n), extract O(1).\nHeap est le meilleur compromis.', '// Priority queue : heap = insert O(log n) + extract O(log n)'),

# Jour 278 — ALGO
('ALGO', 'DSU Union-Find', 'Composantes disjointes', 'union + find operations', ['Path compression', 'Union by rank', 'Les deux', 'Optimisations essentielles'], 3, 'Optimisations essentielles', 'DSU basique : O(n) pire cas.\nPath compression : flatten tree lors de find.\nUnion by rank : attacher petit arbre au grand.\nEnsemble → quasi O(1) (α(n) ≈ constant).', '// DSU : path compression + union by rank = quasi O(1)'),

# Jour 280 — ALGO
('ALGO', 'Union by rank', 'Pourquoi rank ?', 'Éviter arbres déséquilibrés', ['Hauteur minimale', 'Performance', 'Les deux', 'Équilibre optimal'], 2, 'Les deux', 'Union by rank : toujours attacher arbre moins profond au plus profond.\nÉvite dégénérescence en liste liée.\nCombine avec path compression → α(n).', '// Union by rank : attach shallow to deep → hauteur O(log n)'),

# Jour 282 — ALGO
('ALGO', 'Path compression DSU', 'Optimisation find', 'Flatten chemin vers root', ['Tous pointent root direct', 'Amortized O(1)', 'Les deux', 'Flatten essentiel'], 2, 'Les deux', 'Path compression : lors de find(x), faire pointer tous nœuds vers root.\nProchains find sont O(1).\nAmortized quasi-constant.', '// Path compression : flatten on find → amortized O(1)'),

# Jour 284 — ALGO
('ALGO', 'Binary Tree Max Path Sum', 'DFS avec max global', 'Chemin max peut ignorer root', ['DFS return max single path', 'Greedy', 'DP', 'DFS complexe'], 3, 'DFS complexe', 'DFS : pour chaque nœud, max path = node + max(left, 0) + max(right, 0).\nRetourner max single branch pour parent.\nO(n) temps.', '// Max path : DFS return single, update global avec both'),

# Jour 286 — ALGO
('ALGO', 'Serialize Tree', 'Préserver structure', 'tree → string → tree', ['Preorder + null markers', 'Inorder seul insuffisant', 'BFS level-order', 'Preorder optimal'], 3, 'Preorder optimal', 'Preorder avec marqueurs null (ex: "#") préserve structure.\nInorder seul ne suffit pas (ambiguïté).\nDeserialize : récursion avec queue.', '// Serialize : preorder + null markers = structure préservée'),

# Jour 288 — ALGO
('ALGO', 'Word Ladder', 'Shortest transformation', 'beginWord → endWord\n1 lettre à la fois', ['BFS shortest path', 'DFS', 'Dijkstra', 'BFS optimal'], 3, 'BFS optimal', 'BFS : chaque niveau = 1 transformation.\nTrouver shortest path dans graphe de mots.\nO(M² * N) avec M = longueur mot, N = nb mots.', '// Word ladder : BFS = shortest path in word graph'),

# Jour 290 — ALGO
('ALGO', 'Alien Dictionary', 'Ordre des lettres', 'words sorted in alien order', ['Topological sort', 'DFS ou Kahn', 'Graphe orienté', 'Tout ça'], 3, 'Tout ça', 'Construire graphe : edges = ordre entre lettres.\nTopological sort (DFS ou Kahn) pour ordre total.\nO(C) avec C = nb total de caractères.', '// Alien dict : build graph + topological sort'),

# Jour 292 — ALGO
('ALGO', 'Merge K Sorted Lists', 'Efficace pour K listes', 'k listes triées', ['Min-heap de K éléments', 'Merge 2 à 2', 'Les deux', 'Heap optimal'], 3, 'Heap optimal', 'Heap : garder K têtes, extract min et ajouter next.\nO(N log K) avec N = total éléments.\nMerge 2 à 2 : O(N log K) aussi.', '// Merge K : min-heap = O(N log K)'),

# Jour 294 — ALGO
('ALGO', 'Median Data Stream', '2 heaps pattern', 'addNum + findMedian', ['Max-heap (low) + Min-heap (high)', 'Sorted array', 'BST', 'Two heaps optimal'], 3, 'Two heaps optimal', "Max-heap pour moitié basse, min-heap pour moitié haute.\nÉquilibrer tailles : diff ≤ 1.\nMedian = top d'un heap ou moyenne des 2 tops.", '// Median stream : max-heap (low) + min-heap (high)'),

# Jour 296 — ALGO
('ALGO', 'Sliding Window Maximum', 'Deque pattern', 'Max de chaque fenêtre', ['Monotonic decreasing deque', 'Heap', 'BST', 'Deque optimal'], 3, 'Deque optimal', 'Deque : garder indices en ordre décroissant de valeurs.\nFront = max, retirer éléments hors fenêtre et < current.\nO(n) temps.', '// Sliding max : monotonic deque = O(n)'),

# Jour 298 — ALGO
('ALGO', 'LIS optimal', 'Subsequence croissante max', 'nums = [10,9,2,5,3,7,101,18]', ['DP O(n²) ou Binary Search O(n log n)', 'Greedy', 'Backtracking', 'Binary search optimal'], 3, 'Binary search optimal', 'DP : O(n²).\nOptimal : maintenir tableau tails, binary search pour update.\nO(n log n) temps, O(n) espace.', '// LIS : DP O(n²) | Binary search O(n log n) optimal'),

# Jour 300 — ALGO
('ALGO', 'Edit Distance Levenshtein', 'Min opérations (insert/delete/replace)', 'word1 → word2', ['DP[i][j] = min(insert, delete, replace)', 'Greedy', 'BFS', 'DP optimal'], 3, 'DP optimal', 'DP : si chars match, DP[i][j] = DP[i-1][j-1].\nSinon, min(insert, delete, replace) + 1.\nO(n*m) temps.', '// Edit distance : DP min(3 ops) = O(n*m)'),

# Jour 302 — ALGO
('ALGO', 'Regex Matching DP', '. et * wildcards', 's = "aa"\np = "a*"', ['DP[i][j] = match(s[:i], p[:j])', 'Greedy', 'Backtracking', 'DP complexe'], 3, 'DP complexe', 'DP : . = match any, * = 0+ du précédent.\nÉtats complexes avec * (0 ou 1+ match).\nO(n*m) temps.', '// Regex DP : . et * = états complexes = O(n*m)'),

# Jour 304 — ALGO
('ALGO', 'Burst Balloons DP', 'Max coins ordre optimal', 'Burst order matters', ['DP interval', 'Greedy', 'Backtracking', 'DP interval'], 3, 'DP interval', 'DP : considérer dernier ballon éclaté dans intervalle [i, j].\nDP[i][j] = max coins pour intervalle.\nO(n³) temps.', '// Burst balloons : interval DP (dernier éclaté) = O(n³)'),

# Jour 306 — ALGO
('ALGO', 'Decode Ways DP', 'Nombre de décodages', '"226" → ?, "2 26", "22 6", "2 2 6"', ['DP[i] = decode(s[:i])', 'Backtracking', 'Greedy', 'DP count paths'], 3, 'DP count paths', 'DP : DP[i] = DP[i-1] (single digit) + DP[i-2] (two digits si valide).\nComme climbing stairs avec contraintes.\nO(n) temps.', '// Decode ways : DP count (1-digit + 2-digit) = O(n)'),

# Jour 308 — ALGO
('ALGO', 'Unique Paths grid', 'Nombre de chemins', 'm x n grid\ndroite ou bas', ['DP[i][j] = DP[i-1][j] + DP[i][j-1]', 'Backtracking', 'BFS', 'DP sum paths'], 3, 'DP sum paths', 'DP : chemins vers (i,j) = chemins vers (i-1,j) + (i,j-1).\nO(m*n) temps, optimisable à O(n) espace.\nOu formule combinatoire C(m+n-2, m-1).', '// Unique paths : DP sum(left, up) = O(m*n) ou combinatoire'),

# Jour 310 — ALGO
('ALGO', 'Maximal Rectangle', 'Largest rectangle in matrix', 'matrix de 0s et 1s', ['Histogram stack pour chaque row', 'DP', 'Brute force', 'Stack optimal'], 3, 'Stack optimal', 'Pour chaque row : calculer hauteurs consécutives de 1s.\nAppliquer largest rectangle in histogram (stack).\nO(m*n) temps.', '// Maximal rectangle : histogram stack per row = O(m*n)'),

# Jour 312 — ALGO
('ALGO', 'Bellman-Ford algorithme', 'Plus court chemin poids négatifs', 'Relax |V|-1 fois', ['Détecte cycles négatifs', 'O(V*E)', 'Les deux', 'Plus lent que Dijkstra'], 2, 'Les deux', 'Bellman-Ford : relaxe toutes arêtes |V|-1 fois.\nSi encore relaxation au tour |V|, cycle négatif existe.\nO(V*E), plus lent que Dijkstra mais gère poids négatifs.', '// Bellman-Ford : poids négatifs + cycle detection = O(V*E)'),

# Jour 314 — ALGO
('ALGO', 'Floyd-Warshall', 'All pairs shortest paths', 'Tous les chemins entre tous', ['DP[i][j][k]', 'O(V³)', 'Les deux', 'DP 3D'], 2, 'Les deux', 'Floyd : pour chaque paire (i,j), essayer via k.\nDP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j]).\nO(V³), pratique si graphe dense.', '// Floyd-Warshall : all pairs via DP = O(V³)'),

# Jour 316 — ALGO
('ALGO', 'Kruskal MST', 'Minimum Spanning Tree', 'Arêtes par poids croissant', ['Sort edges + Union-Find', 'Greedy', 'O(E log E)', 'Tout ça'], 3, 'Tout ça', 'Kruskal : trier arêtes, ajouter si pas de cycle (DSU).\nGreedy : arête min qui connecte 2 composantes.\nO(E log E) pour tri, DSU quasi O(1).', '// Kruskal : sort edges + DSU = O(E log E)'),

# Jour 318 — ALGO
('ALGO', 'Prim MST', 'MST avec heap', 'Start from 1 node', ['Priority queue + visited', 'Greedy', 'O((V+E) log V)', 'Tout ça'], 3, 'Tout ça', 'Prim : heap avec arêtes sortantes, toujours ajouter min.\nGreedy : arête min vers nœud non visité.\nO((V+E) log V) avec heap.', '// Prim : min-heap greedy = O((V+E) log V)'),

# Jour 320 — ALGO
('ALGO', 'Tarjan SCC', 'Strongly Connected Components', 'DFS + low-link', ['Stack + DFS order', 'O(V+E)', 'Complexe', 'Tout ça'], 3, 'Tout ça', 'Tarjan : DFS avec low-link (plus bas ancêtre atteignable).\nStack pour tracker current SCC.\nO(V+E) un seul passage.', '// Tarjan : DFS + low-link + stack = O(V+E)'),

# Jour 322 — ALGO
('ALGO', 'Kosaraju SCC', 'Alternative SCC', '2 DFS passes', ['DFS + reverse graph + DFS', 'O(V+E)', 'Plus simple', 'Tout ça'], 3, 'Tout ça', 'Kosaraju : DFS sur graphe original (ordre finish).\nDFS sur graphe inversé en ordre décroissant.\nO(V+E), plus simple que Tarjan.', '// Kosaraju : 2 DFS (original + reverse) = O(V+E)'),

# Jour 324 — ALGO
('ALGO', 'Articulation Points', 'Cut vertices', 'Retirer → composantes augmentent', ['DFS + low-link', 'Bridges similaire', 'O(V+E)', 'Tout ça'], 3, 'Tout ça', 'Articulation point : retirer → graphe se déconnecte.\nDFS + low-link : si low[child] ≥ disc[u] → u est point.\nO(V+E).', '// Articulation : DFS + low-link (cut vertex) = O(V+E)'),

# Jour 326 — ALGO
('ALGO', 'Eulerian Path', 'Parcourir toutes arêtes 1 fois', 'Conditions degree', ['≤ 2 nœuds degree impair', 'Connecté', 'Les deux', 'Conditions précises'], 2, 'Les deux', 'Eulerian path : exactement 0 ou 2 nœuds de degré impair.\nEulerian circuit : tous degrés pairs.\nGraphe doit être connecté.', '// Eulerian : 0 ou 2 odd degree = path | 0 = circuit'),

# Jour 328 — ALGO
('ALGO', 'Hamiltonian Path', 'Visiter tous nœuds 1 fois', 'NP-Complete', ['Backtracking', 'DP bitmask O(2^n * n²)', 'Pas de poly', 'Tout ça'], 3, 'Tout ça', "Hamiltonian : NP-Complete, pas d'algo polynomial connu.\nBacktracking : O(n!).\nDP bitmask : O(2^n * n²), meilleur mais exponentiel.", '// Hamiltonian : NP-Complete (backtrack ou DP bitmask)'),

# Jour 330 — ALGO
('ALGO', 'Traveling Salesman', 'Plus court cycle visitant tous', 'NP-Hard', ['DP bitmask O(2^n * n²)', 'Approx algorithms', 'Greedy suboptimal', 'DP optimal exact'], 3, 'DP optimal exact', 'TSP exact : DP bitmask O(2^n * n²).\nApproximations : Christofides 1.5-approx, greedy, etc.\nNP-Hard, pas de poly exact.', '// TSP : DP bitmask exact O(2^n * n²) ou approx'),

# Jour 332 — ALGO
('ALGO', 'KMP pattern matching', 'Éviter recomparaisons', 'Précompute LPS array', ['Longest Prefix Suffix', 'O(n+m)', 'Skip characters', 'Tout ça'], 3, 'Tout ça', 'KMP : LPS array = longest proper prefix qui est aussi suffix.\nPas de backtrack dans texte, seulement pattern.\nO(n+m) vs O(n*m) naïf.', '// KMP : LPS array pour skip = O(n+m)'),

# Jour 334 — ALGO
('ALGO', 'Rabin-Karp rolling hash', 'Pattern matching avec hash', 'Hash window de taille m', ['Rolling hash O(1)', 'Collisions possibles', 'O(n+m) average', 'Tout ça'], 3, 'Tout ça', 'Rabin-Karp : hash fenêtre glissante.\nRolling hash : update en O(1) (retirer gauche, ajouter droite).\nCollisions → vérifier match. O(n+m) moyen.', '// Rabin-Karp : rolling hash O(1) = O(n+m) average'),

# Jour 336 — ALGO
('ALGO', 'Boyer-Moore string search', 'Sauts avec bad character', 'Skip characters', ['Bad char + good suffix', 'O(n/m) best', 'Plus rapide en pratique', 'Tout ça'], 3, 'Tout ça', "Boyer-Moore : compare de droite à gauche.\nBad char rule : skip jusqu'à match ou dépassement.\nMeilleur cas O(n/m), pratique très rapide.", '// Boyer-Moore : bad char rule = O(n/m) best case'),

# Jour 338 — ALGO
('ALGO', 'Aho-Corasick multi-pattern', 'Chercher plusieurs patterns', 'Trie + fail links', ['Automate fini', 'O(n + m + z)', 'Multi-pattern optimal', 'Tout ça'], 3, 'Tout ça', 'Aho-Corasick : Trie de patterns + fail links (comme KMP).\nUn seul passage dans texte pour tous patterns.\nO(n + m + z) avec z = nb matches.', '// Aho-Corasick : trie + fail links = multi-pattern O(n+m+z)'),

# Jour 340 — ALGO
('ALGO', 'Suffix Array', 'Tous suffixes triés', 'Alternative suffix tree', ['Indices triés par suffixes', 'O(n log n) construction', 'O(m log n) search', 'Tout ça'], 3, 'Tout ça', 'Suffix array : indices de tous suffixes triés lexicographiquement.\nConstruction : O(n log² n) naïf, O(n log n) optimal.\nSearch pattern : O(m log n) avec binary search.', '// Suffix array : sorted suffixes = space-efficient suffix tree'),

# Jour 342 — ALGO
('ALGO', 'Z-algorithm', 'Z[i] = longest prefix match', 'Linear time string matching', ['Z-box optimization', 'O(n)', 'Simple à implémenter', 'Tout ça'], 3, 'Tout ça', 'Z-algorithm : Z[i] = longueur du plus long préfixe commun.\nZ-box : réutilise info précédente pour skip.\nO(n), simple et efficace.', '// Z-algorithm : Z-box reuse = O(n) simple'),

# Jour 344 — ALGO
('ALGO', 'Trapping Rain Water', 'Eau piégée entre barres', 'height = [0,1,0,2,1,0,1,3,2,1,2,1]', ['Two pointers', 'Prefix/suffix max', 'Stack', 'Two pointers optimal'], 3, 'Two pointers optimal', 'Two pointers : left/right avec max_left/max_right.\nEau[i] = min(max_left, max_right) - height[i].\nO(n) temps, O(1) espace.', '// Rain water : two pointers + max tracking = O(n) O(1)'),

# Jour 346 — ALGO
('ALGO', 'Candy greedy', 'Distribution avec contraintes', 'ratings = [1,0,2]\nVoisins ratings', ['Two passes greedy', 'DP', 'Heap', 'Greedy optimal'], 3, 'Greedy optimal', 'Greedy : passe gauche→droite (si > gauche, +1 candy).\nPasse droite→gauche (si > droite, max(current, right+1)).\nO(n) temps.', '// Candy : two-pass greedy (left + right) = O(n)'),

# Jour 348 — ALGO
('ALGO', 'Gas Station greedy', 'Peut faire le tour ?', 'gas[], cost[]\nStart index', ['Greedy one-pass', 'Brute force', 'DP', 'Greedy optimal'], 3, 'Greedy optimal', 'Greedy : track tank et total.\nSi tank < 0, reset start à i+1.\nSi total ≥ 0 à la fin, solution existe.\nO(n) temps.', '// Gas station : greedy track tank + total = O(n)'),

# Jour 350 — ALGO
('ALGO', 'Jump Game II', 'Min sauts pour atteindre fin', 'nums = [2,3,1,1,4]', ['Greedy range', 'DP', 'BFS', 'Greedy optimal'], 3, 'Greedy optimal', 'Greedy : track currentEnd et farthest.\nQuand i atteint currentEnd, jump++.\nO(n) temps.', '// Jump II : greedy range (currentEnd + farthest) = O(n)'),

# Jour 352 — ALGO
('ALGO', 'N-Queens backtracking', 'Placer N reines', 'N x N board\nNo attacks', ['Backtracking + pruning', 'DP', 'Greedy', 'Backtracking classique'], 3, 'Backtracking classique', 'Backtracking : placer reine par ligne.\nPruning : vérifier colonnes, diagonales.\nO(N!) complexité.', '// N-Queens : backtracking + diagonal checks = O(N!)'),

# Jour 354 — ALGO
('ALGO', 'Sudoku Solver', 'Remplir grille 9x9', 'Backtracking avec contraintes', ['Backtracking + validation', 'Brute force', 'Greedy', 'Backtracking optimal'], 3, 'Backtracking optimal', 'Backtracking : essayer 1-9 pour chaque case vide.\nValidation : row, col, 3x3 box.\nExponentiel mais pruning efficace.', '// Sudoku : backtracking + row/col/box checks'),

# Jour 356 — ALGO
('ALGO', 'Wildcard Matching DP', '? et * wildcards', 's = "aa"\np = "*"', ['DP[i][j] avec * = 0+', 'Greedy', 'Backtracking', 'DP complexe'], 3, 'DP complexe', 'DP : ? = match 1, * = match 0+.\nÉtats avec * (skip ou match 1+).\nO(n*m) temps.', '// Wildcard DP : ? = 1 char, * = 0+ chars = O(n*m)'),

# Jour 358 — ALGO
('ALGO', 'Interleaving String DP', 's3 = interleave(s1, s2)', 's1 = "aabcc"\ns2 = "dbbca"\ns3 = "aadbbcbcac"', ['DP[i][j] = interleave(s1[:i], s2[:j])', 'Greedy', 'Two pointers', 'DP optimal'], 3, 'DP optimal', 'DP : DP[i][j] = true si s3[:i+j] peut être formé.\nTransition : match s1[i] ou s2[j].\nO(n*m) temps.', '// Interleaving : DP match s1 or s2 = O(n*m)'),

# Jour 360 — ALGO
('ALGO', 'Palindrome Partitioning II', 'Min cuts pour all palindromes', 's = "aab"', ['DP cuts + DP palindrome', 'Greedy', 'Backtracking', 'DP 2-phase'], 3, 'DP 2-phase', 'Phase 1 : DP pour détecter palindromes O(n²).\nPhase 2 : DP cuts[i] = min cuts pour s[:i].\nO(n²) temps.', '// Palindrome partition : DP palindrome + DP cuts = O(n²)'),

# Jour 362 — ALGO
('ALGO', 'Russian Doll Envelopes', 'LIS en 2D', 'Enveloppes (w, h)\nNested', ['Sort + LIS on height', 'DP 2D', 'Greedy', 'LIS optimal'], 3, 'LIS optimal', 'Trier par w croissant (si égal, h décroissant).\nLIS sur hauteurs → O(n log n).\nAstuces : h décroissant évite w égaux.', '// Envelopes : sort w + LIS h = O(n log n)'),

# Jour 364 — ALGO
('ALGO', 'Min Window Substring optimal', 'Template générique', 's, t → min window contenant t', ['Sliding window + 2 freq maps', 'Brute force', 'DP', 'Window template'], 3, 'Window template', 'Template : expand right, shrink left quand valide.\nFreq map pour t, counter pour matches.\nO(n+m) optimal.', '// Min window : sliding window template = O(n+m)'),

]
