"""
Quiz JavaScript pour Codebog.
"""

JS_CHALLENGES = [
# Jour 1 — JS
('JS', 'typeof null', '90% des devs JS se trompent sur cette ligne.', 'console.log(typeof null)', ['"null"', '"object"', '"undefined"', '"boolean"'], 1, '"object"', 'typeof null retourne "object" — un bug historique depuis 1995.\nnull n\'est PAS un objet, mais la spec l\'a encodé ainsi\net personne n\'ose corriger ça pour ne pas casser Internet.', 'if (x === null) { ... } // ✅ toujours ça'),

# Jour 3 — JS
('JS', '== vs ===', 'Vrai ou faux ? 0 == false renvoie true.', 'console.log(0 == false)\nconsole.log(0 === false)', ['true / true', 'false / false', 'true / false', 'false / true'], 2, 'true / false', '== applique la coercition de type : 0 est converti en false.\n=== compare sans conversion : 0 (number) ≠ false (boolean).\nToujours utiliser === sauf raison explicite.', '// Règle : toujours ===, jamais =='),

# Jour 5 — JS
('JS', 'var hoisting', 'Que va afficher ce code ?', 'console.log(x)\nvar x = 5\nconsole.log(x)', ['Error / 5', 'undefined / 5', '5 / 5', 'undefined / undefined'], 1, 'undefined / 5', 'var est "hoisted" (remonté) en haut du scope.\nLa déclaration est levée mais PAS l\'initialisation.\nC\'est comme si le moteur écrivait var x; en premier.', '// var → hoisted | let/const → TDZ (erreur)'),

# Jour 7 — JS
('JS', 'let/const TDZ', 'Que se passe-t-il ici ?', 'console.log(a)\nlet a = 10', ['"undefined"', '10', 'ReferenceError', 'null'], 2, 'ReferenceError', 'let et const ont une Temporal Dead Zone (TDZ).\nContrairement à var, ils ne sont pas initialisés\navant leur déclaration → ReferenceError.', '// TDZ : la var existe mais est inaccessible'),

# Jour 9 — JS
('JS', 'Closure', "Qu'affiche ce code ?", 'function outer() {\n  let count = 0\n  return function() {\n    count++\n    return count\n  }\n}\nconst inc = outer()\nconsole.log(inc(), inc(), inc())', ['0, 0, 0', '1, 1, 1', '1, 2, 3', 'Error'], 2, '1, 2, 3', 'La fonction retournée forme une closure sur count.\nElle garde une référence à la variable count\nde outer(), même après que outer() ait terminé.', '// Closure = fonction + son environnement lexical'),

# Jour 11 — JS
('JS', 'this — méthode vs fonction', 'Que va afficher ce code ?', 'const obj = {\n  name: "Codebog",\n  greet: function() {\n    return this.name\n  }\n}\nconsole.log(obj.greet())', ['"Codebog"', 'undefined', 'Error', 'null'], 0, '"Codebog"', 'Quand greet() est appelée comme méthode d\'obj,\nthis fait référence à obj lui-même.\nDonc this.name = "Codebog" ✅', "// this dépend du contexte d'appel, pas de la définition"),

# Jour 13 — JS
('JS', 'Arrow function et this', 'Que va afficher ce code ?', 'const obj = {\n  name: "Codebog",\n  greet: () => {\n    return this.name\n  }\n}\nconsole.log(obj.greet())', ['"Codebog"', 'undefined', 'Error', 'null'], 1, 'undefined', "Les arrow functions n'ont PAS leur propre this.\nElles héritent du this du contexte englobant.\nIci, le contexte est global → this.name est undefined.", '// Arrow fn : this lexical | function : this dynamique'),

# Jour 15 — JS
('JS', 'Array.map() vs forEach()', 'Lequel retourne un nouveau tableau ?', 'const nums = [1, 2, 3]\nconst a = nums.map(x => x * 2)\nconst b = nums.forEach(x => x * 2)\nconsole.log(a, b)', ['undefined, [2,4,6]', '[2,4,6], [2,4,6]', '[2,4,6], undefined', '[1,2,3], [1,2,3]'], 2, '[2,4,6], undefined', 'map() retourne un nouveau tableau transformé.\nforEach() retourne toujours undefined.\nForEach est pour les effets de bord, map pour la transformation.', '// map → nouveau tableau | forEach → undefined'),

# Jour 17 — JS
('JS', 'Array.reduce()', 'Que retourne ce code ?', 'const arr = [1, 2, 3, 4, 5]\nconst result = arr.reduce((acc, curr) => acc + curr, 0)\nconsole.log(result)', ['[1,2,3,4,5]', '15', '0', 'Error'], 1, '15', 'reduce() accumule les valeurs avec une fonction.\nAcc commence à 0, puis on additionne chaque élément :\n0+1=1, 1+2=3, 3+3=6, 6+4=10, 10+5=15.', '// reduce(fn, initialValue) : le couteau suisse des arrays'),

# Jour 19 — JS
('JS', 'Promise — then/catch', "Dans quel ordre s'affichent ces logs ?", 'console.log("1")\nPromise.resolve("2").then(v => console.log(v))\nconsole.log("3")', ['1, 2, 3', '2, 1, 3', '1, 3, 2', '3, 1, 2'], 2, '1, 3, 2', "Le code synchrone s'exécute en premier (1, 3).\nLes .then() sont des microtasks : ils s'exécutent\naprès le code synchrone, avant le prochain tick.", '// Microtasks > Macrotasks (setTimeout, setInterval)'),

# Jour 21 — JS
('JS', 'Spread operator', 'Que contient newArr ?', 'const arr1 = [1, 2, 3]\nconst arr2 = [4, 5, 6]\nconst newArr = [...arr1, ...arr2]\nconsole.log(newArr)', ['[[1,2,3],[4,5,6]]', '[1,2,3,4,5,6]', '[1,2,3]', 'Error'], 1, '[1,2,3,4,5,6]', 'L\'opérateur spread (...) "étale" les éléments.\n[...arr1, ...arr2] crée un nouveau tableau fusionné.\nC\'est l\'équivalent moderne de arr1.concat(arr2).', '// Spread: copie, fusion, args de fonction'),

# Jour 23 — JS
('JS', 'Destructuring objets', 'Que contient name et age ?', 'const user = { name: "Alice", age: 25, city: "Paris" }\nconst { name, age } = user\nconsole.log(name, age)', ['"Alice", 25', 'undefined, undefined', 'Error', '"Alice", undefined'], 0, '"Alice", 25', 'La destructuration extrait les propriétés par leur nom.\nOn peut aussi renommer : const { name: n } = user\nOu définir une valeur par défaut : const { age = 0 } = user', '// const { a, b = "default" } = obj'),

# Jour 25 — JS
('JS', 'Template literals', 'Que va afficher ce code ?', 'const name = "monde"\nconst age = 2026\nconsole.log(`Bonjour ${name} en ${age}`)', ['"Bonjour ${name} en ${age}"', '"Bonjour monde en 2026"', 'Error', 'undefined'], 1, '"Bonjour monde en 2026"', 'Les backticks (`) permettent l\'interpolation avec ${}.\nOn peut y mettre n\'importe quelle expression JS :\n`${1 + 1}` → "2", `${fn()}` → résultat de fn()', '// Backtick = strings puissantes avec interpolation'),

# Jour 27 — JS
('JS', 'null vs undefined', 'Laquelle de ces comparaisons est vraie ?', 'console.log(null == undefined)\nconsole.log(null === undefined)', ['false / false', 'true / true', 'true / false', 'false / true'], 2, 'true / false', "null == undefined → true (cas spécial de la spec JS).\nnull === undefined → false (types différents).\nC'est la seule valeur pour laquelle == et === divergent ainsi.", '// null == undefined SEULEMENT entre eux'),

# Jour 29 — JS
('JS', 'Optional chaining ?.', 'Que retourne ce code sans planter ?', 'const user = { profile: null }\nconsole.log(user?.profile?.name)\nconsole.log(user.profile.name)', ['undefined / Error', '"null" / Error', 'null / Error', 'undefined / undefined'], 0, 'undefined / Error', "user?.profile?.name → si profile est null/undefined, renvoie undefined sans planter.\nuser.profile.name → TypeError car on tente d'accéder à .name sur null.", '// ?. = accès sécurisé | sans : TypeError'),

# Jour 31 — JS
('JS', 'Nullish coalescing ??', 'Que va afficher ce code ?', 'const a = null ?? "défaut"\nconst b = 0 ?? "défaut"\nconst c = "" ?? "défaut"\nconsole.log(a, b, c)', ['"défaut", "défaut", "défaut"', '"défaut", 0, ""', '3 fois "défaut"', 'Error'], 1, '"défaut", 0, ""', '?? retourne le côté droit UNIQUEMENT si gauche est null/undefined.\n0 et "" ne sont pas null/undefined → ils passent.\nContrairement à ||, qui considère 0 et "" comme falsy.', '// ?? = seulement null/undefined | || = tout falsy'),

# Jour 33 — JS
('JS', 'Array.filter()', 'Que retourne ce code ?', 'const nums = [1, 2, 3, 4, 5, 6]\nconst even = nums.filter(n => n % 2 === 0)\nconsole.log(even)', ['[1,3,5]', '[2,4,6]', 'true', '[1,2,3,4,5,6]'], 1, '[2,4,6]', 'filter() retourne un nouveau tableau avec les éléments\npour lesquels la fonction retourne true.\nn % 2 === 0 → vrai pour 2, 4, 6.', '// filter + map + reduce = la trilogie FP'),

# Jour 35 — JS
('JS', 'Object.keys()', 'Que retourne Object.keys() sur cet objet ?', 'const obj = { a: 1, b: 2, c: 3 }\nconsole.log(Object.keys(obj))\nconsole.log(Object.values(obj))', ['[1,2,3] / ["a","b","c"]', '["a","b","c"] / [1,2,3]', '{"a":1} / [1]', 'Error'], 1, '["a","b","c"] / [1,2,3]', 'Object.keys() retourne les clés (noms des propriétés).\nObject.values() retourne les valeurs.\nObject.entries() retourne [clé, valeur] pour chaque prop.', '// Object.entries(obj) → [["a",1],["b",2],...]'),

# Jour 37 — JS
('JS', 'async/await vs Promise', 'Ces deux codes sont-ils équivalents ?', '// Version A — Promise\nfetch(url).then(r => r.json()).then(d => console.log(d))\n\n// Version B — async/await\nasync function get() {\n  const r = await fetch(url)\n  const d = await r.json()\n  console.log(d)\n}', ['Oui, strictement équivalents', 'Non, A est plus rapide', 'Non, B bloque le thread', 'Non, syntaxe différente seulement'], 0, 'Oui, strictement équivalents', 'async/await est du sucre syntaxique sur les Promises.\nLes deux font exactement la même chose sous le capot.\nasync/await est juste plus lisible (style synchrone).', '// async fn retourne toujours une Promise'),

# Jour 39 — JS
('JS', 'Prototype chain', 'Que retourne ce code ?', 'function Animal(name) {\n  this.name = name\n}\nAnimal.prototype.speak = function() {\n  return `${this.name} parle`\n}\nconst dog = new Animal("Rex")\nconsole.log(dog.speak())', ['Error: speak is not a function', '"Rex parle"', '"Animal parle"', 'undefined'], 1, '"Rex parle"', "dog n'a pas la méthode speak en propre.\nJS remonte la chaîne de prototype : dog → Animal.prototype.\nIl y trouve speak() et l'exécute avec this = dog.", '// Chaque objet a un __proto__ vers son prototype'),

# Jour 41 — JS
('JS', 'Event Loop — setTimeout', "Dans quel ordre s'affichent ces logs ?", 'console.log("A")\nsetTimeout(() => console.log("B"), 0)\nPromise.resolve().then(() => console.log("C"))\nconsole.log("D")', ['A, B, C, D', 'A, D, C, B', 'A, D, B, C', 'A, C, D, B'], 1, 'A, D, C, B', "Ordre d'exécution :\n1. Synchrone : A, D\n2. Microtasks (Promise.then) : C\n3. Macrotasks (setTimeout) : B\nMicrotasks toujours avant Macrotasks !", '// Microtask queue > Callback queue'),

# Jour 43 — JS
('JS', 'Symbol', 'Que retourne cette comparaison ?', 'const s1 = Symbol("id")\nconst s2 = Symbol("id")\nconsole.log(s1 === s2)\nconsole.log(typeof s1)', ['true / "symbol"', 'false / "symbol"', 'true / "object"', 'Error'], 1, 'false / "symbol"', 'Chaque Symbol() est unique, même avec la même description.\ns1 !== s2 car ce sont deux valeurs primitives distinctes.\nSymbol est le 7ème type primitif de JS (après ES6).', '// Symbol : clés uniques, non-énumérables'),

# Jour 45 — JS
('JS', 'WeakMap vs Map', 'Quelle est la différence clé entre Map et WeakMap ?', 'const map = new Map()\nconst wmap = new WeakMap()\nlet obj = { id: 1 }\nmap.set(obj, "data")\nwmap.set(obj, "data")\nobj = null // obj déréférencé', ['Identiques', 'WeakMap: GC libère | Map: garde la ref', 'Map est plus rapide', 'WeakMap accepte les strings'], 1, 'WeakMap: GC libère | Map: garde la ref', "Map garde une référence forte → obj ne sera jamais GC'd.\nWeakMap garde une référence faible → si obj = null,\nle GC peut libérer la mémoire automatiquement.", "// WeakMap = pas d'itération, pas de size, GC-friendly"),

# Jour 47 — JS
('JS', 'try/catch/finally', 'Que retourne cette fonction ?', 'function test() {\n  try {\n    throw new Error("oups")\n    return "try"\n  } catch (e) {\n    return "catch"\n  } finally {\n    return "finally"\n  }\n}\nconsole.log(test())', ['"try"', '"catch"', '"finally"', 'Error'], 2, '"finally"', 'finally s\'exécute TOUJOURS, même si try/catch retourne.\nLe return "finally" écrase le return "catch".\nC\'est un piège classique : finally peut override le return !', '// finally écrase les return de try/catch'),

# Jour 49 — JS
('JS', 'Array destructuring avec default', 'Que contient b ?', 'const [a, b = 10, c] = [1, undefined, 3]\nconsole.log(b)', ['undefined', '10', '1', 'Error'], 1, '10', 'La valeur par défaut (= 10) s\'applique UNIQUEMENT\nsi la valeur est undefined (pas null, pas 0, pas "").\nIci, le 2ème élément est undefined → b = 10.', '// Default destructuring : seulement pour undefined'),

# Jour 51 — JS
('JS', 'Promise.all()', 'Que se passe-t-il si une Promise rejette dans Promise.all() ?', 'Promise.all([\n  Promise.resolve(1),\n  Promise.reject("erreur"),\n  Promise.resolve(3)\n]).then(r => console.log(r))\n  .catch(e => console.log(e))', ['"erreur"', '[1, "erreur", 3]', '[1, 3]', 'Error'], 0, '"erreur"', 'Promise.all() est "fail-fast" : si UNE rejette, tout échoue.\nOn passe immédiatement dans .catch() avec la raison du rejet.\nPour tolérer les erreurs, utiliser Promise.allSettled().', '// Promise.allSettled() → attend TOUTES même si erreur'),

# Jour 53 — JS
('JS', 'Generator function', 'Que va afficher ce code ?', 'function* count() {\n  yield 1\n  yield 2\n  yield 3\n}\nconst gen = count()\nconsole.log(gen.next().value)\nconsole.log(gen.next().value)', ['Error', '1, 1', '1, 2', '3, 3'], 2, '1, 2', "Un générateur est une fonction pausable.\nYield suspend l'exécution et retourne une valeur.\nNext() reprend depuis le dernier yield.", '// { value, done } : structure retournée par next()'),

# Jour 55 — JS
('JS', 'for...of vs for...in', 'Que va logger ce code ?', 'const arr = [10, 20, 30]\nfor (let i in arr) {\n  console.log(typeof i)\n}\nfor (let v of arr) {\n  console.log(typeof v)\n}', ['"number" x3 / "number" x3', '"string" x3 / "number" x3', '"number" x3 / "string" x3', '"string" x3 / "string" x3'], 1, '"string" x3 / "number" x3', 'for...in itère sur les INDICES (comme clés) → strings "0","1","2".\nfor...of itère sur les VALEURS → numbers 10, 20, 30.\nfor...in sur les arrays est déconseillé (peut itérer les proto props).', '// for...of pour les valeurs | for...in pour les clés'),

# Jour 57 — JS
('JS', 'Object.freeze()', 'Que se passe-t-il avec Object.freeze() ?', 'const obj = Object.freeze({ x: 1, y: 2 })\nobj.x = 99\nobj.z = 3\nconsole.log(obj)', ['{ x: 99, y: 2, z: 3 }', '{ x: 1, y: 2 }', 'TypeError', '{ x: 1, y: 2, z: 3 }'], 1, '{ x: 1, y: 2 }', "freeze() empêche toute modification de l'objet.\nEn mode strict → TypeError. En mode normal → silencieux.\nAttention : freeze est SHALLOW (pas récursif).", '// Deep freeze : appeler freeze() sur chaque sous-objet'),

# Jour 59 — JS
('JS', 'Currying', 'Que retourne curry(1)(2)(3) ?', 'function curry(a) {\n  return function(b) {\n    return function(c) {\n      return a + b + c\n    }\n  }\n}\nconsole.log(curry(1)(2)(3))', ['Error', '6', '"123"', 'undefined'], 1, '6', 'Le currying transforme f(a,b,c) en f(a)(b)(c).\nChaque appel retourne une fonction qui "se souvient"\ndes arguments précédents grâce aux closures.', '// Currying : application partielle et composition'),

# Jour 61 — JS
('JS', 'Debounce', 'À quoi sert le debounce ?', 'function debounce(fn, delay) {\n  let timer\n  return function(...args) {\n    clearTimeout(timer)\n    timer = setTimeout(() => fn(...args), delay)\n  }\n}\n// Utilisé pour : recherche live, resize, scroll', ['Répéter fn toutes les N ms', "Délayer fn jusqu'à arrêt des appels", 'Limiter fn à 1 appel/sec', 'Mettre fn en cache'], 1, "Délayer fn jusqu'à arrêt des appels", "Debounce attend que les appels s'arrêtent N ms\navant d'exécuter la fonction. Idéal pour les événements\nfréquents : resize, keyup de recherche, scroll.", "// Debounce: attend l'arrêt | Throttle: limite la cadence"),

# Jour 63 — JS
('JS', 'Memoization', 'Combien de fois fib(3) est-il calculé sans mémo ?', 'function fib(n) {\n  if (n <= 1) return n\n  return fib(n-1) + fib(n-2)\n}\nfib(5)\n// fib(5) appelle fib(4) et fib(3)\n// fib(4) appelle fib(3) et fib(2)\n// fib(3) est calculé ???', ['1 fois', '2 fois', '3 fois', '5 fois'], 1, '2 fois', 'Sans mémo, fib(3) est calculé 2 fois dans fib(5).\nAvec mémo (cache), chaque valeur est calculée 1 seule fois.\nO(2ⁿ) → O(n) avec la mémoisation !', '// const memo = {}; if(memo[n]) return memo[n]'),

# Jour 65 — JS
('JS', 'Throttle', 'Quelle est la différence entre debounce et throttle ?', 'function throttle(fn, limit) {\n  let lastCall = 0\n  return function(...args) {\n    const now = Date.now()\n    if (now - lastCall >= limit) {\n      lastCall = now\n      return fn(...args)\n    }\n  }\n}\n// scroll, mousemove, resize...', ["Throttle = attend l'arrêt", 'Throttle = exécute max 1 fois/période', 'Debounce = 1 appel/période', 'Identiques'], 1, 'Throttle = exécute max 1 fois/période', "Throttle garantit max 1 exécution par période de temps.\nMême si 100 scroll events arrivent, fn s'exécute max 1x/250ms.\nDebounce attend que TOUT soit arrêté.", '// Throttle: cadence fixe | Debounce: après silence'),

# Jour 67 — JS
('JS', 'Error types', "Quel type d'erreur est lancé ici ?", 'null.toString()', ['Error', 'TypeError', 'ReferenceError', 'SyntaxError'], 1, 'TypeError', 'Accéder à une propriété sur null/undefined = TypeError.\nReferenceError : variable non déclarée.\nSyntaxError : code malformé (parsé avant exécution).', '// TypeError: null.x | ReferenceError: x (non déclaré)'),

# Jour 69 — JS
('JS', 'Set — collection unique', 'Que contient ce Set ?', 'const set = new Set([1, 2, 2, 3, 3, 3])\nset.add(4)\nset.add(2)\nconsole.log(set.size)\nconsole.log([...set])', ['6 / [1,2,2,3,3,3,4,2]', '4 / [1,2,3,4]', '4 / [1,2,3,3,4]', '3 / [1,2,3]'], 1, '4 / [1,2,3,4]', 'Set stocke des valeurs UNIQUES. Les doublons sont ignorés.\nAdd(2) est ignoré car 2 est déjà présent.\nSize = 4 car {1, 2, 3, 4}.', '// Set : dédoublonnage ultra-rapide O(1) par op'),

# Jour 71 — JS
('JS', 'Proxy', 'Que va afficher ce code ?', 'const handler = {\n  get(target, key) {\n    return key in target ? target[key] : `${key} non trouvé`\n  }\n}\nconst obj = new Proxy({ name: "Codebog" }, handler)\nconsole.log(obj.name)\nconsole.log(obj.age)', ['"Codebog" / undefined', '"Codebog" / "age non trouvé"', 'Error / Error', '"Codebog" / null'], 1, '"Codebog" / "age non trouvé"', 'Proxy intercepte les accès aux propriétés.\nLe handler get() est appelé à chaque lecture.\nOn peut valider, logger, retourner une valeur par défaut.', '// Proxy = méta-programmation puissante en JS'),

# Jour 73 — JS
('JS', 'Promise.allSettled()', 'Que retourne Promise.allSettled() si une rejette ?', 'Promise.allSettled([\n  Promise.resolve("A"),\n  Promise.reject("B"),\n  Promise.resolve("C")\n]).then(results => {\n  results.forEach(r => console.log(r.status))\n})', ['"rejected" seulement', 'Error', '"fulfilled", "rejected", "fulfilled"', '"fulfilled", "fulfilled"'], 2, '"fulfilled", "rejected", "fulfilled"', 'allSettled() attend TOUTES les promises, succès ou échec.\nChaque résultat a un status : "fulfilled" ou "rejected".\nContraindrement à all() qui fail-fast dès la première erreur.', '// allSettled: robuste | all: fail-fast'),

# Jour 75 — JS
('JS', 'Class private fields', 'Que se passe-t-il avec les champs privés # ?', 'class Counter {\n  #count = 0\n  increment() { this.#count++ }\n  get value() { return this.#count }\n}\nconst c = new Counter()\nc.increment()\nconsole.log(c.value)\nconsole.log(c.#count)', ['1 / 1', '1 / Error', '0 / Error', 'Error / Error'], 1, '1 / Error', "Les champs avec # sont vraiment privés en JS.\nc.value retourne 1 via le getter public.\nc.#count depuis l'extérieur → SyntaxError.", '// # = privé, inaccessible même via Reflect/Proxy'),

# Jour 77 — JS
('JS', 'Logical assignment operators', 'Quelle est la valeur finale de a ?', 'let a = null\na ??= "défaut"\nconsole.log(a)\n\nlet b = "existant"\nb ??= "défaut"\nconsole.log(b)', ['"défaut" / "défaut"', '"défaut" / "existant"', 'null / "existant"', 'Error'], 1, '"défaut" / "existant"', '??= (nullish assignment) : assigne SEULEMENT si null/undefined.\na était null → a = "défaut".\nb était "existant" (non null) → pas de changement.', '// ||= : falsy | &&= : truthy | ??= : null/undefined'),

# Jour 79 — JS
('JS', 'structuredClone()', 'Quelle différence avec le spread pour les objets imbriqués ?', 'const obj = { a: 1, b: { c: 2 } }\nconst shallow = { ...obj }       // spread\nconst deep = structuredClone(obj) // deep clone\n\nshallow.b.c = 99\ndeep.b.c = 99\nconsole.log(obj.b.c)', ['99', '2', '99 puis 2', 'Error'], 0, '99', 'Spread fait une copie SHALLOW (superficielle).\nshallow.b est la MÊME référence que obj.b.\nDonc modifier shallow.b.c modifie obj.b.c aussi.', '// structuredClone() : deep clone natif (Node 17+)'),

# Jour 81 — JS
('JS', 'Array.at()', 'Que retourne arr.at(-1) ?', 'const arr = [10, 20, 30, 40, 50]\nconsole.log(arr.at(-1))\nconsole.log(arr.at(-2))\nconsole.log(arr[arr.length - 1])', ['undefined / undefined / 50', '50 / 40 / 50', '10 / 20 / 50', 'Error'], 1, '50 / 40 / 50', 'Array.at() accepte des indices négatifs (depuis la fin).\nat(-1) = dernier élément = 50.\nat(-2) = avant-dernier = 40.\nÉquivalent de arr[arr.length - 1] mais plus lisible.', '// at(-1) remplace arr[arr.length-1]'),

# Jour 83 — JS
('JS', 'Object.hasOwn()', 'Quelle différence avec hasOwnProperty() ?', 'const obj = { a: 1 }\nconsole.log(Object.hasOwn(obj, "a"))\nconsole.log(Object.hasOwn(obj, "toString"))\n\n// hasOwnProperty peut être surchargé :\nconst evil = { hasOwnProperty: () => true }\nconsole.log(evil.hasOwnProperty("anything"))', ['true/false/false', 'true/false/true', 'true/true/true', 'Error'], 1, 'true/false/true', 'evil.hasOwnProperty est surchargé → retourne toujours true !\nObject.hasOwn() est une méthode statique → impossible à surcharger.\nPlus sûr et recommandé depuis ES2022.', '// Object.hasOwn() > hasOwnProperty() : plus sûr'),

# Jour 85 — JS
('JS', 'WeakRef', 'Pourquoi utiliser WeakRef ?', 'let obj = { data: "important" }\nconst ref = new WeakRef(obj)\n\n// Plus tard...\nobj = null // obj peut être GC\'d\n\nconst val = ref.deref()\nif (val) {\n  console.log(val.data)\n} else {\n  console.log("GC\'d")\n}', ['Performance uniquement', 'Éviter les fuites mémoire en gardant une ref faible', 'Créer des refs immuables', 'Logger les objets'], 1, 'Éviter les fuites mémoire en gardant une ref faible', 'WeakRef garde une référence faible qui ne bloque pas le GC.\nSi l\'objet original est collecté, deref() retourne undefined.\nUtile pour les caches qui doivent "laisser partir" les objets.', '// deref() peut retourner undefined : toujours vérifier'),

# Jour 87 — JS
('JS', 'Tagged template literals', 'Que retourne highlight`Bonjour ${name}` ?', 'function highlight(strings, ...vals) {\n  return strings.reduce((acc, str, i) => {\n    return acc + str + (vals[i] ? `<b>${vals[i]}</b>` : "")\n  }, "")\n}\nconst name = "Codebog"\nconsole.log(highlight`Bonjour ${name} !`)', ['"Bonjour Codebog !"', '"Bonjour <b>Codebog</b> !"', 'Error', '["Bonjour ", " !"]'], 1, '"Bonjour <b>Codebog</b> !"', 'Les tagged templates interceptent les backtick strings.\nstrings = ["Bonjour ", " !"], vals = ["Codebog"].\nOn peut transformer les interpolations librement.', '// Utilisé par : styled-components, GraphQL gql, sql'),

# Jour 89 — JS
('JS', 'import.meta', 'Que contient import.meta.url ?', '// Dans un module ES6 (ex: Node.js avec type:module)\n// ou navigateur avec <script type="module">\n\nconsole.log(import.meta.url)\n// → "file:///path/to/current/module.js"\n// ou "https://site.com/js/app.js"', ['Le package.json', "L'URL du module courant", 'Le répertoire racine', 'undefined'], 1, "L'URL du module courant", 'import.meta.url = URL absolue du fichier module courant.\nUtile pour construire des chemins relatifs au module.\nRemplace __dirname en CommonJS.', '// new URL("./data.json", import.meta.url)'),

# Jour 91 — JS
('JS', 'top-level await', 'Dans quel contexte peut-on utiliser await sans async ?', '// Fichier module.mjs (ES Module)\nconst data = await fetch("https://api.example.com/data")\nconst json = await data.json()\nconsole.log(json)\n\n// Ceci est du top-level await\n// Disponible depuis Node 14.8 + ESM', ['Partout en JS', 'Seulement dans les ES Modules', 'Seulement dans Node.js', "Jamais en dehors d'async"], 1, 'Seulement dans les ES Modules', "Top-level await ne fonctionne que dans les ES Modules (.mjs).\nPas dans les scripts classiques ou CommonJS.\nBloque l'import du module jusqu'à la résolution de la Promise.", '// "type":"module" dans package.json ou .mjs'),

# Jour 93 — JS
('JS', 'AbortController', 'À quoi sert AbortController avec fetch() ?', 'const controller = new AbortController()\nconst { signal } = controller\n\nfetch("https://api.slow.com/data", { signal })\n  .then(r => r.json())\n  .catch(e => console.log(e.name)) // "AbortError"\n\nsetTimeout(() => controller.abort(), 5000) // timeout 5s', ['Retenter automatiquement', 'Annuler la requête en cours', 'Mettre en cache la réponse', 'Limiter la taille de la réponse'], 1, 'Annuler la requête en cours', "AbortController permet d'annuler une requête fetch en cours.\nSi abort() est appelé, le fetch rejette avec AbortError.\nEssentiel pour les composants React qui se démontent.", '// useEffect cleanup : controller.abort()'),

# Jour 95 — JS
('JS', 'Promise.any()', 'Que retourne Promise.any() si toutes rejettent ?', 'Promise.any([\n  Promise.reject("A"),\n  Promise.reject("B"),\n  Promise.reject("C")\n]).catch(e => {\n  console.log(e.constructor.name)\n  console.log(e.errors)\n})', ['"Error" / undefined', '"AggregateError" / ["A","B","C"]', '"TypeError" / null', '"RejectionError" / 3'], 1, '"AggregateError" / ["A","B","C"]', 'Promise.any() : résout avec la PREMIÈRE Promise qui réussit.\nSi TOUTES rejettent → AggregateError contenant toutes les erreurs.\nOpposé de Promise.race() qui prend le premier résultat (succès ou échec).', '// any → premier succès | race → premier résultat'),

# Jour 97 — JS
('JS', 'Generator — iterator protocol', "Que se passe-t-il à l'appel de next() après le dernier yield ?", 'function* gen() {\n  yield 1\n  yield 2\n}\nconst g = gen()\nconsole.log(g.next()) // { value: 1, done: false }\nconsole.log(g.next()) // { value: 2, done: false }\nconsole.log(g.next()) // ???', ['{ value: 1, done: true }', '{ value: undefined, done: true }', '{ value: null, done: true }', 'Error'], 1, '{ value: undefined, done: true }', "Après le dernier yield, le générateur est exhausted.\nNext() retourne { value: undefined, done: true }.\nDone: true signale qu'il n'y a plus rien à itérer.", "// for...of s'arrête automatiquement quand done: true"),

# Jour 99 — JS
('JS', 'Reflect API', 'Que fait Reflect.ownKeys() vs Object.keys() ?', 'const sym = Symbol("id")\nconst obj = {\n  name: "test",\n  [sym]: 123,\n  get hidden() { return 42 }\n}\nconsole.log(Object.keys(obj).length)      // ???\nconsole.log(Reflect.ownKeys(obj).length)  // ???', ['1 / 1', '2 / 2', '1 / 3', '2 / 3'], 2, '1 / 3', 'Object.keys() : seulement les clés strings énumérables = ["name"].\nReflect.ownKeys() : TOUTES les clés, y compris Symbols et non-énumérables.\nIci : "name" + Symbol(id) + "hidden" = 3.', '// Reflect.ownKeys = Object.keys + getOwnPropertySymbols + non-enum'),

# Jour 101 — JS
('JS', 'Array.groupBy()', 'Comment utiliser Object.groupBy() ?', "const arr=[{t:'A',v:1},{t:'B',v:2},{t:'A',v:3}]\nconst g = Object.groupBy(arr, x => x.t)\nconsole.log(g)", ['{"A":[...],"B":[...]}', '[[1,3],[2]]', 'Error', 'undefined'], 0, '{"A":[...],"B":[...]}', 'Object.groupBy() regroupe les éléments par clé.\nECMA 2024 natif, plus besoin de reduce pour grouper.', 'Object.groupBy(arr, fn) // natif depuis 2024'),

# Jour 103 — JS
('JS', 'Promise.withResolvers()', 'Que retourne Promise.withResolvers() ?', 'const { promise, resolve, reject } = Promise.withResolvers()\nsetTimeout(() => resolve("ok"), 1000)\nconst r = await promise', ['Une Promise seulement', '{ promise, resolve, reject }', 'Error', 'undefined'], 1, '{ promise, resolve, reject }', "withResolvers() expose resolve/reject à l'extérieur.\nPlus propre que le pattern new Promise((res,rej) => ...).", '// ES2024 : clean deferred pattern'),

# Jour 105 — JS
('JS', 'using — resource management', "Que fait le mot-clé 'using' (TC39) ?", "// Proposal Stage 3\n// using assure le cleanup automatique\nfunction processFile() {\n  using handle = openFile('data.txt')\n  // handle[Symbol.dispose]() appelé automatiquement\n  // à la sortie du scope, même en cas d'erreur\n}", ['Déclare une constante', 'Assure le cleanup automatique via Symbol.dispose', 'Import dynamique', 'Créer un WeakRef'], 1, 'Assure le cleanup automatique via Symbol.dispose', 'using appelle Symbol.dispose() automatiquement en fin de scope.\nComme le using de C# ou with de Python.', '// await using pour les ressources async'),

# Jour 107 — JS
('JS', 'Pipe operator |>', "Que fait l'opérateur pipe (TC39 Stage 2) ?", 'const result = [1,2,3]\n  |> map(%, x => x * 2)\n  |> filter(%, x => x > 2)\n  |> reduce(%, (a,b) => a+b, 0)\n// Équivalent à :\nconst r = reduce(filter(map([1,2,3], x=>x*2), x=>x>2), (a,b)=>a+b, 0)', ['Opérateur bitwise', 'Composition de fonctions left-to-right', 'Import de module', 'Division entière'], 1, 'Composition de fonctions left-to-right', 'Le pipe operator passe la valeur de gauche dans la fonction de droite.\nRend le code plus lisible (style "fluent") sans nesting.', '// Disponible via Babel plugin en attendant le standard'),

# Jour 109 — JS
('JS', 'Intl.NumberFormat', 'Comment formatter 1234567.89 en euros ?', "const fmt = new Intl.NumberFormat('fr-FR', {\n  style: 'currency',\n  currency: 'EUR'\n})\nconsole.log(fmt.format(1234567.89))", ['"1234567.89 EUR"', '"1 234 567,89 €"', '"€1,234,567.89"', 'Error'], 1, '"1 234 567,89 €"', 'Intl.NumberFormat respecte les conventions locales.\nfr-FR : espace comme séparateur de milliers, virgule pour décimales.\nAPI native, pas besoin de library.', '// Intl : localisation native pour nombres, dates, textes'),

# Jour 111 — JS
('JS', 'Decorators — stage 3', 'Que fait ce décorateur @readonly ?', "function readonly(target, context) {\n  if (context.kind === 'field') {\n    return function(initialValue) {\n      Object.defineProperty(this, context.name, {\n        value: initialValue,\n        writable: false\n      })\n      return initialValue\n    }\n  }\n}\n\nclass Config {\n  @readonly\n  VERSION = '1.0.0'\n}", ['Crée une constante', 'Rend la propriété non-modifiable', 'Cache la propriété', 'Valide la valeur'], 1, 'Rend la propriété non-modifiable', 'Le décorateur @readonly appelle defineProperty avec writable: false.\nTente de modifier VERSION → TypeError en mode strict.', '// Decorators TC39 Stage 3 : TypeScript les supporte déjà'),

# Jour 113 — JS
('JS', 'Number.isNaN()', 'isNaN() vs Number.isNaN() : quelle différence ?', "console.log(isNaN('hello'))\nconsole.log(Number.isNaN('hello'))", ['"true / true"', 'true / false', 'false / false', 'false / true'], 1, 'true / false', 'isNaN() convertit la valeur avant de tester → "hello" → NaN → true.\nNumber.isNaN() ne convertit PAS → "hello" est une string → false.', '// Toujours préférer Number.isNaN()'),

# Jour 115 — JS
('JS', 'BigInt', 'Que retourne Number.MAX_SAFE_INTEGER + 1 ?', 'console.log(Number.MAX_SAFE_INTEGER)\nconsole.log(Number.MAX_SAFE_INTEGER + 1)\nconsole.log(Number.MAX_SAFE_INTEGER + 2)\nconsole.log(9007199254740993n)', ['"perd la précision"', 'les deux affichent la même valeur', 'Error', 'NaN'], 1, 'les deux affichent la même valeur', "Au-delà de MAX_SAFE_INTEGER (2⁵³-1), JS perd la précision.\nMAX + 1 === MAX + 2 car ils s'arrondissent au même float64.\nBigInt (suffixe n) résout ce problème pour les grands entiers.", '// BigInt : n suffixe, pas mixable avec Number'),

# Jour 117 — JS
('JS', 'void operator', 'Que retourne void 0 ?', "console.log(void 0)\nconsole.log(void 'anything')\nconsole.log(void function() { return 42 }())", ["'undefined, undefined, 42'", "'undefined, undefined, undefined'", "'0, anything, undefined'", 'Error'], 1, "'undefined, undefined, undefined'", "void évalue l'expression et retourne toujours undefined.\nUtilisé pour garantir undefined (avant ES5, undefined était reassignable).\nVoir dans les librairies minifiées : void 0 au lieu de undefined.", '// void expr : évalue sans retourner la valeur'),

# Jour 119 — JS
('JS', 'Comma operator', 'Que retourne (1, 2, 3) ?', "console.log((1, 2, 3))\nconsole.log((console.log('A'), console.log('B'), 'C'))", ['1', "3 (puis 'A','B','C')", 'Error', 'undefined'], 1, "3 (puis 'A','B','C')", "L'opérateur virgule évalue chaque expression et retourne la dernière.\n(1, 2, 3) → évalue 1, 2, puis retourne 3.\nRarement utilisé intentionnellement (souvent source de bugs).", '// Comma : évalue gauche→droite, retourne la dernière valeur'),

# Jour 121 — JS
('JS', 'in operator', "Que retourne 'toString' in obj ?", "const obj = { name: 'test' }\nconsole.log('name' in obj)\nconsole.log('toString' in obj)\nconsole.log('missing' in obj)", ['true / false / false', 'true / true / false', 'false / true / false', 'true / false / true'], 1, 'true / true / false', "'in' vérifie TOUTE la chaîne de prototype.\ntoString vient de Object.prototype → true.\nPour vérifier les props propres uniquement → Object.hasOwn().", '// in : prototype inclus | hasOwn : propres uniquement'),

# Jour 123 — JS
('JS', 'delete operator', 'Que retourne delete obj.prop ?', 'const obj = { a: 1, b: 2 }\nconsole.log(delete obj.a)\nconsole.log(obj)\nconsole.log(delete obj.toString)', ['false / {b:2} / false', 'true / {b:2} / false', 'true / {b:2} / true', 'Error'], 1, 'true / {b:2} / false', 'delete retourne true si la suppression réussit.\ndelete obj.a → {b:2}.\ndelete obj.toString → false car toString est hérité (non-propre).', '// delete retourne false seulement pour les non-configurables'),

# Jour 125 — JS
('JS', 'Array.from()', "Que retourne Array.from('hello') ?", "console.log(Array.from('hello'))\nconsole.log(Array.from({length:3}, (_,i) => i*2))\nconsole.log(Array.from(new Set([1,2,2,3])))", ['Error', "['h','e','l','l','o'], [0,2,4], [1,2,3]", "['hello'], [0,1,2], [1,2,2,3]", 'undefined'], 1, "['h','e','l','l','o'], [0,2,4], [1,2,3]", 'Array.from() accepte tout itérable ou array-like.\nString → chars, Set → valeurs uniques.\nAvec mapping fn → Array.from({length:n}, fn) pour créer des tableaux.', '// Array.from({length:n}, (_,i)=>i) → [0,1,...,n-1]'),

# Jour 127 — JS
('JS', 'instanceof', 'Que retourne ce code ?', 'class A {}\nclass B extends A {}\nconst b = new B()\nconsole.log(b instanceof B)\nconsole.log(b instanceof A)\nconsole.log(b instanceof Object)', ['true / false / false', 'true / true / true', 'false / true / true', 'true / true / false'], 1, 'true / true / true', 'instanceof parcourt la chaîne de prototype.\nb → B.prototype → A.prototype → Object.prototype.\nDonc b est instanceof B, A ET Object.', '// instanceof : vérifie toute la chaîne de proto'),

# Jour 129 — JS
('JS', 'Event loop deep dive', 'Macrotasks vs Microtasks : ordre exact ?', "// Ordre d'exécution :\n// 1. Script (synchrone)\n// 2. Microtasks (Promise.then, queueMicrotask, MutationObserver)\n// 3. Render (navigateur)\n// 4. Macrotasks (setTimeout, setInterval, I/O, MessageChannel)\n// → Répéter 2-4", ['Macro puis Micro', 'Micro puis Macro', 'Simultanés', 'Aléatoire'], 1, 'Micro puis Macro', "Après chaque tâche, TOUTE la queue microtask est vidée.\nSeulement ensuite une macrotask est extraite.\nOn peut 'starver' les macrotasks avec des microtasks infinis!", '// queueMicrotask(() => {...}) : microtask explicite'),

# Jour 131 — JS
('JS', 'Memory leaks patterns', 'Lequel cause une fuite mémoire ?', "// Scénario A:\nlet cache = {}\nfunction store(key, val) { cache[key] = val }\n\n// Scénario B:\nconst listeners = []\nfunction addListener(el, fn) {\n  el.addEventListener('click', fn)\n  listeners.push({el, fn})\n}\n// removeEventListener jamais appelé... 😱", ['Seulement A', 'Seulement B', 'Les deux', 'Aucun'], 1, 'Seulement B', "Les event listeners non supprimés gardent des références.\nL'élément ne peut pas être GC car il est référencé dans le closure.\nToujours supprimer les listeners dans cleanup (useEffect return, componentWillUnmount).", '// removeEventListener dans cleanup : essentiel'),

# Jour 133 — JS
('JS', 'WeakMap — use case réel', "Quel est le cas d'usage réel d'un WeakMap ?", "// Pattern courant :\nconst privateData = new WeakMap()\n\nclass Person {\n  constructor(name, age) {\n    privateData.set(this, { name, age })\n  }\n  getName() { return privateData.get(this).name }\n}\n\nconst p = new Person('Alice', 30)\nconsole.log(p.getName())\n// La data est GC'd avec l'instance !", ['Cache mémoire infini', 'Données privées liées à un objet (GC-friendly)', 'Itérer des objets', 'Remplacer Map'], 1, 'Données privées liées à un objet (GC-friendly)', "WeakMap permet de lier des données privées à une instance.\nSi l'instance est déréférencée → le GC libère aussi ses données.\nEn production, on préfère les private class fields (#).", '// WeakMap private : pattern pré-# fields'),

# Jour 135 — JS
('JS', 'Structural typing', 'Duck typing en JS : exemple pratique ?', "function makeAnimal(name) {\n  return { name, speak() { return `${name} parle` } }\n}\nfunction makeRobot(model) {\n  return { name: model, speak() { return `${model} bip` } }\n}\nfunction speak(entity) {\n  // Pas de vérification de type !\n  return entity.speak()\n}\nconsole.log(speak(makeAnimal('Rex')))\nconsole.log(speak(makeRobot('R2D2')))", ['Error sur le robot', "'Rex parle' / 'R2D2 bip'", 'TypeError', 'undefined'], 1, "'Rex parle' / 'R2D2 bip'", 'JS utilise le duck typing : si ça a une méthode speak(), ça marche.\nPas besoin d\'héritage ou d\'interface formelle.\n"Si ça ressemble à un canard et cancane comme un canard..."', '// Duck typing = composition over inheritance en JS'),

# Jour 137 — JS
('JS', 'Temporal API', 'Pourquoi remplacer Date ?', "// Problems with Date :\n// 1. Date() est mutable\n// 2. Mois 0-indexés (Jan=0)\n// 3. Pas de timezone robuste\n// 4. Comparaisons via getTime()\n\n// Temporal (TC39 Stage 3) :\nconst now = Temporal.Now.plainDateISO()\nconst meeting = Temporal.PlainDate.from('2026-12-31')\nconst diff = now.until(meeting)", ['Date est parfait', 'Date a des problèmes de mutable/timezone/API', 'Temporal est plus lent', 'Aucune raison'], 1, 'Date a des problèmes de mutable/timezone/API', 'Date est muable, les mois sont 0-indexés, les timezone sont fragiles.\nTemporal propose une API immutable, claire et timezone-aware.\nStage 3 TC39, polyfill disponible (@js-temporal/polyfill).', '// Temporal : remplacement moderne de Date'),

# Jour 139 — JS
('JS', 'Async iteration', 'Comment itérer une source async avec for await ?', 'async function processStream(url) {\n  const response = await fetch(url)\n  const reader = response.body.getReader()\n  const decoder = new TextDecoder()\n  // Generator async :\n  async function* readChunks() {\n    while (true) {\n      const { done, value } = await reader.read()\n      if (done) return\n      yield decoder.decode(value)\n    }\n  }\n  for await (const chunk of readChunks()) {\n    console.log(chunk)\n  }\n}', ['for...of suffit', 'for await...of pour les async generators', 'Promises.all sur les chunks', 'fetch gère tout automatiquement'], 1, 'for await...of pour les async generators', "for await...of permet d'itérer les async generators et async iterables.\nEssentiel pour traiter les streams Node.js, Server-Sent Events, etc.\nLe générateur async yield des chunks au fur et à mesure.", '// for await...of : clé pour les streams et pagination'),

# Jour 141 — JS
('JS', 'Proxy — validation', 'Comment valider des données avec Proxy ?', "const validator = {\n  set(target, key, value) {\n    if (key === 'age') {\n      if (!Number.isInteger(value) || value < 0 || value > 150)\n        throw new TypeError('Age invalide')\n    }\n    target[key] = value\n    return true // obligatoire !\n  }\n}\nconst person = new Proxy({}, validator)\nperson.age = 25  // OK\nperson.age = -1  // TypeError !", ['Proxy ne peut pas valider', 'Proxy avec set trap intercepte les assignations', 'Seulement avec getter', 'Seulement avec defineProperty'], 1, 'Proxy avec set trap intercepte les assignations', "Le set trap intercepte toutes les assignations de propriétés.\nOn peut y mettre toute logique de validation.\nReturn true obligatoire pour confirmer l'assignation.", '// Proxy : validation, logging, immutabilité, API REST mock'),

# Jour 143 — JS
('JS', 'Microtask starvation', 'Peut-on bloquer les macrotasks avec des microtasks ?', "function infinite() {\n  Promise.resolve().then(infinite)\n}\ninfinite()\nsetTimeout(() => console.log('Jamais affiché?'), 0)", ["Oui, le setTimeout ne s'exécute jamais", 'Non, le scheduler équilibre', 'Le code plante', 'setTimeout passe avant'], 0, "Oui, le setTimeout ne s'exécute jamais", "Les microtasks sont vidées ENTIÈREMENT avant chaque macrotask.\nSi on crée une microtask infinie, la queue n'est jamais vide.\nLe setTimeout (macrotask) ne s'exécute jamais → starvation!", '// Éviter les boucles infinies dans les microtasks'),

# Jour 145 — JS
('JS', 'Object.defineProperty()', 'Comment créer une propriété non-énumérable ?', "const obj = {}\nObject.defineProperty(obj, 'secret', {\n  value: 42,\n  writable: false,\n  enumerable: false,\n  configurable: false\n})\nconsole.log(obj.secret)\nconsole.log(Object.keys(obj))\nfor (let k in obj) console.log(k)", ["42 / ['secret'] / 'secret'", '42 / [] / (rien)', 'Error', "42 / [] / 'secret'"], 1, '42 / [] / (rien)', 'enumerable: false → exclu de for...in et Object.keys().\nwritable: false → obj.secret = 99 échoue silencieusement.\nconfigurable: false → impossible de re-définir ou supprimer.', '// defineProperty : contrôle précis des propriétés'),

# Jour 147 — JS
('JS', 'Prototype vs __proto__', 'Quelle est la différence entre prototype et __proto__ ?', 'function Foo() {}\nconst foo = new Foo()\nconsole.log(foo.__proto__ === Foo.prototype)\nconsole.log(foo.prototype)\nconsole.log(Foo.prototype.constructor === Foo)', ['false / {} / true', 'true / undefined / true', 'true / {} / false', 'Error'], 1, 'true / undefined / true', "Foo.prototype : objet partagé entre toutes les instances de Foo.\nfoo.__proto__ : lien vers le prototype de l'objet (= Foo.prototype).\nfoo.prototype : undefined car foo est une instance, pas une fonction.", '// prototype : sur les fn | __proto__ : sur les objets'),

# Jour 149 — JS
('JS', 'Symbol.iterator', 'Comment rendre un objet itérable ?', 'class Range {\n  constructor(start, end) {\n    this.start = start; this.end = end\n  }\n  [Symbol.iterator]() {\n    let current = this.start\n    const end = this.end\n    return {\n      next() {\n        return current <= end\n          ? { value: current++, done: false }\n          : { done: true }\n      }\n    }\n  }\n}\nfor (const n of new Range(1, 5)) console.log(n)', ["Erreur, Range n'est pas itérable", 'Affiche 1,2,3,4,5', 'Affiche undefined', 'Boucle infinie'], 1, 'Affiche 1,2,3,4,5', "Implémenter Symbol.iterator rend l'objet itérable.\nfor...of, spread, destructuring utilisent tous cet iterator.\nLe protocole retourne { value, done }.", "// Symbol.iterator : duck typing pour l'itération"),

# Jour 151 — JS
('JS', 'Error.cause', 'Quelle nouveauté apporte Error cause (ES2022) ?', "try {\n  try {\n    throw new Error('DB connection failed')\n  } catch (e) {\n    throw new Error('Service unavailable', { cause: e })\n  }\n} catch (err) {\n  console.log(err.message)\n  console.log(err.cause.message)\n}", ['Error non supporté', "'Service unavailable' / 'DB connection failed'", 'Error: message seulement, pas cause', 'TypeError'], 1, "'Service unavailable' / 'DB connection failed'", "Error({ cause }) permet de chaîner les erreurs.\nOn garde le contexte original tout en ajoutant un niveau d'abstraction.\nEssentiel pour les logs et le debugging en production.", "// err.cause : chaînage d'erreurs pour mieux déboguer"),

# Jour 153 — JS
('JS', 'Object.create() vs new', 'Quelle est la différence ?', "const proto = {\n  greet() { return `Hello ${this.name}` }\n}\n\n// Object.create() :\nconst obj = Object.create(proto)\nobj.name = 'Alice'\n\n// new :\nfunction Person(name) { this.name = name }\nPerson.prototype = proto\nconst p = new Person('Bob')\n\nconsole.log(obj.greet(), p.greet())", ["'Hello Alice', Error", "'Hello Alice', 'Hello Bob'", "Error, 'Hello Bob'", 'undefined, undefined'], 1, "'Hello Alice', 'Hello Bob'", 'Object.create(proto) crée un objet dont le __proto__ = proto.\nnew Person() crée une instance et appelle le constructeur.\nObject.create(null) crée un objet sans prototype (pure map).', '// Object.create(null) : HashMap ultra-performant'),

# Jour 155 — JS
('JS', 'WeakRef + FinalizationRegistry', "Comment détecter le GC d'un objet ?", "const registry = new FinalizationRegistry((heldValue) => {\n  console.log(`${heldValue} a été GC'd`)\n})\n\nlet obj = { name: 'test' }\nconst ref = new WeakRef(obj)\nregistry.register(obj, 'mon objet')\n\nobj = null\n// Plus tard, après un GC :\n// → 'mon objet a été GC'd'", ['Impossible en JS', 'FinalizationRegistry callback après GC', 'WeakRef.deref() lance une event', 'Error: GC non accessible'], 1, 'FinalizationRegistry callback après GC', "FinalizationRegistry enregistre une callback appelée après GC.\nUtile pour nettoyer des ressources externes (fichiers, sockets).\nLa callback n'est PAS garantie d'être appelée (GC = non-déterministe).", '// FinalizationRegistry : best-effort cleanup, pas garanti'),

# Jour 157 — JS
('JS', 'Performance — Object vs Map', 'Quand préférer Map à un objet classique ?', 'const obj = {}\nconst map = new Map()\n// Insertions : obj[key]=v vs map.set(key,v)\n// Taille : Object.keys(obj).length vs map.size\n// Itération : for...in vs for...of\n// Clés : strings/Symbols vs any type', ['Toujours obj', 'Toujours Map', 'Map : fréquentes insertions/suppressions et clés non-string', 'Identiques'], 2, 'Map : fréquentes insertions/suppressions et clés non-string', "Map est optimisé pour les insertions/suppressions fréquentes.\nMap.size est O(1) contrairement à Object.keys().length O(n).\nMap accepte n'importe quel type de clé.", '// Map : perf + key-any | obj : JSON, static data'),

# Jour 159 — JS
('JS', 'Generators — infinite sequences', 'Comment créer une séquence infinie ?', 'function* naturals() {\n  let n = 1\n  while (true) yield n++\n}\n\nfunction take(gen, n) {\n  const result = []\n  for (const v of gen) {\n    result.push(v)\n    if (result.length >= n) break\n  }\n  return result\n}\nconsole.log(take(naturals(), 5))', ['Boucle infinie, freeze', '[1,2,3,4,5]', 'Error', 'undefined'], 1, '[1,2,3,4,5]', "Les générateurs sont lazy : ils ne calculent que ce dont on a besoin.\nUne séquence infinie ne plante pas car on contrôle l'arrêt.\nEssentiel pour les streams de données, pagination, etc.", '// Générateurs : lazy evaluation = puissance et efficacité'),

# Jour 161 — JS
('JS', 'Currying avancé — curry() générique', "Comment implémenter curry() pour n'importe quelle fn ?", 'function curry(fn) {\n  return function curried(...args) {\n    if (args.length >= fn.length) {\n      return fn.apply(this, args)\n    }\n    return function(...args2) {\n      return curried.apply(this, args.concat(args2))\n    }\n  }\n}\nconst add = curry((a,b,c) => a+b+c)\nconsole.log(add(1)(2)(3))\nconsole.log(add(1,2)(3))\nconsole.log(add(1)(2,3))', ['Seulement add(1)(2)(3) fonctionne', 'Les 3 fonctionnent et retournent 6', 'Error', 'undefined'], 1, 'Les 3 fonctionnent et retournent 6', "curry() générique accumule les args jusqu'à fn.length.\nLe même résultat peu importe comment on fournit les arguments.\nUtilisé dans la programmation fonctionnelle (Ramda, Lodash/fp).", '// fn.length : arity (nombre de params déclarés)'),

# Jour 163 — JS
('JS', '[FINAL] Bilan Codebog Phase 4', "🏆 Dernier post de l'année ! Quel concept est le plus utile en entretien ?", '// 241 posts accomplis !\n// Top concepts vus :\n// ✓ Closures & prototypes\n// ✓ Event loop & Promises\n// ✓ Array methods (map/filter/reduce)\n// ✓ Modern JS (ES2022-2024)\n// ✓ Performance patterns', ['Closures', 'Event loop', 'Les deux + les array methods', "Tout ce qu'on a vu !"], 3, "Tout ce qu'on a vu !", "241 posts, une année de JavaScript et algorithmie.\nDe typeof null aux algorithmes avancés en passant par l'event loop.\nMerci de nous avoir suivi — rendez-vous l'année prochaine ! 🚀", '// 👉 learning.itmade.fr pour aller plus loin'),

]
