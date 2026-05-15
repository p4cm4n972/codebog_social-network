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

# Jour 165 — JS
('JS', 'String.slice() négatif', 'Les indices négatifs en JS : magie ou logique ?', 'const str = "JavaScript"\nconsole.log(str.slice(-6, -1))', ['"Java"', '"Script"', '"Scrip"', '"ipt"'], 2, '"Scrip"', 'slice(-6, -1) compte depuis la fin : -6 = index 4 (S), -1 = index 9.\nExclut le dernier index, donc de 4 à 8 = "Scrip".\nLes indices négatifs comptent depuis la fin de la chaîne.', '// slice(start, end) : négatif = depuis la fin'),

# Jour 167 — JS
('JS', 'Précision décimale', 'Pourquoi 0.1 + 0.2 ≠ 0.3 ?', 'console.log(0.1 + 0.2 === 0.3)', ['true', 'false', 'Error', 'undefined'], 1, 'false', '0.1 + 0.2 donne 0.30000000000000004 en JavaScript.\nLes nombres sont stockés en IEEE 754 (64-bit float).\nCertaines décimales ne peuvent pas être représentées exactement.', '// Utilise Number.EPSILON ou des entiers pour la précision'),

# Jour 169 — JS
('JS', 'Short-circuit &&', 'Que va afficher ce code ?', 'let x = 0\nfalse && (x = 10)\nconsole.log(x)', ['0', '10', 'false', 'undefined'], 0, '0', "L'opérateur && évalue le côté droit SEULEMENT si le gauche est vrai.\nComme false est falsy, (x = 10) n'est jamais exécuté.\nC'est le short-circuit evaluation.", "// && : si gauche falsy, n'évalue pas la droite"),

# Jour 171 — JS
('JS', 'Priorité || vs &&', 'Quelle est la valeur de result ?', 'const result = true || false && false\nconsole.log(result)', ['true', 'false', 'Error', 'undefined'], 0, 'true', "&& a une priorité plus élevée que ||.\nDonc false && false s'évalue d'abord = false.\nPuis true || false = true.", '// Priorité : && avant || (comme * avant +)'),

# Jour 173 — JS
('JS', 'for...in sur tableau', 'Que va afficher ce code ?', 'const arr = [10, 20, 30]\nfor (let i in arr) {\n  console.log(typeof i)\n}', ['"number"', '"string"', '"object"', 'Error'], 1, '"string"', 'for...in itère sur les clés (indices), PAS les valeurs.\nEt les clés sont toujours des strings, même pour les tableaux.\nPour les valeurs, utilise for...of.', '// for...in → clés (string) | for...of → valeurs'),

# Jour 175 — JS
('JS', 'do...while comportement', 'Combien de fois "test" s\'affiche ?', 'let i = 10\ndo {\n  console.log("test")\n  i++\n} while (i < 5)', ['0 fois', '1 fois', '5 fois', '10 fois'], 1, '1 fois', 'do...while exécute TOUJOURS le bloc au moins une fois,\npuis vérifie la condition.\nMême si i = 10 > 5, le premier tour est exécuté.', '// do...while : exécute PUIS vérifie (min 1 tour)'),

# Jour 177 — JS
('JS', 'Switch sans break', 'Que va afficher ce code ?', 'const x = 1\nswitch(x) {\n  case 1:\n    console.log("A")\n  case 2:\n    console.log("B")\n  default:\n    console.log("C")\n}', ['"A"', '"A" "B" "C"', '"A" "B"', 'Error'], 1, '"A" "B" "C"', 'Sans break, le switch "tombe" dans les cas suivants (fall-through).\ncase 1 exécute A, puis continue vers case 2 (B), puis default (C).\nToujours mettre break sauf si fall-through voulu.', '// switch : toujours break, sauf fall-through intentionnel'),

# Jour 179 — JS
('JS', 'break vs continue', 'Combien de nombres affichés ?', 'for (let i = 0; i < 5; i++) {\n  if (i === 2) continue\n  if (i === 4) break\n  console.log(i)\n}', ['2', '3', '4', '5'], 1, '3', 'i=0 → log 0, i=1 → log 1, i=2 → continue (skip).\ni=3 → log 3, i=4 → break (stop).\nDonc 0, 1, 3 = 3 nombres affichés.', '// continue = saute 1 tour | break = sort de la boucle'),

# Jour 181 — JS
('JS', 'Label en JS', 'Les labels existent en JavaScript ?', 'outer: for (let i = 0; i < 2; i++) {\n  for (let j = 0; j < 2; j++) {\n    if (i === 1) break outer\n    console.log(i, j)\n  }\n}', ['Error', '0,0 0,1', '0,0 0,1 1,0 1,1', '0,0'], 1, '0,0 0,1', 'Les labels permettent de break/continue une boucle externe.\nbreak outer sort complètement de la boucle i.\nQuand i=1, on break avant de logger.', '// label: rarement utilisé, mais existe pour boucles imbriquées'),

# Jour 183 — JS
('JS', 'String immutable', 'Que contient str après ?', 'let str = "hello"\nstr[0] = "H"\nconsole.log(str)', ['"Hello"', '"hello"', 'Error', '"H"'], 1, '"hello"', 'Les strings en JavaScript sont IMMUTABLES.\nstr[0] = "H" ne fait rien (mode strict : erreur silencieuse).\nPour modifier, il faut créer une nouvelle string.', '// Strings = immutables | utilise replace(), slice(), etc.'),

# Jour 185 — JS
('JS', 'Number.EPSILON', 'À quoi sert Number.EPSILON ?', 'console.log(Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON)', ['false', 'true', 'Error', 'undefined'], 1, 'true', 'Number.EPSILON est la plus petite différence entre 2 nombres.\nUtile pour comparer des floats avec imprécision :\nau lieu de a === b, on fait Math.abs(a - b) < Number.EPSILON.', '// Pour comparer floats : Math.abs(a - b) < Number.EPSILON'),

# Jour 187 — JS
('JS', 'parseInt() radix piège', 'Que va retourner ce code ?', 'console.log(parseInt("08"))', ['8', '0', 'NaN', 'Error'], 0, '8', 'Avant ES5, parseInt("08") pouvait renvoyer 0 (octal).\nDepuis ES5, le radix 10 est par défaut.\nMAIS toujours spécifier : parseInt("08", 10) pour être sûr.', '// parseInt(str, 10) : TOUJOURS spécifier le radix'),

# Jour 189 — JS
('JS', 'isNaN() vs Number.isNaN()', 'Laquelle est vraie ?', 'console.log(isNaN("hello"))\nconsole.log(Number.isNaN("hello"))', ['true / true', 'false / false', 'true / false', 'false / true'], 2, 'true / false', 'isNaN("hello") convertit d\'abord en nombre → NaN → true.\nNumber.isNaN("hello") vérifie si c\'est littéralement NaN → false.\nNumber.isNaN() est plus fiable (pas de coercition).', '// Number.isNaN() : pas de coercition, plus fiable'),

# Jour 191 — JS
('JS', 'Array.isArray() fiabilité', 'Pourquoi préférer Array.isArray() ?', 'const arr = []\nconsole.log(Array.isArray(arr))\nconsole.log(arr instanceof Array)', ['true / true', 'true / false', 'false / true', 'false / false'], 0, 'true / true', "Array.isArray() fonctionne même avec des tableaux d'autres frames/iframes.\ninstanceof Array peut échouer si le Array vient d'un autre contexte.\nArray.isArray() est la méthode recommandée.", '// Array.isArray() > instanceof (multi-frame safe)'),

# Jour 193 — JS
('JS', 'new String() piège', 'Que va afficher ce code ?', 'const s1 = "hello"\nconst s2 = new String("hello")\nconsole.log(s1 === s2)', ['true', 'false', 'Error', 'undefined'], 1, 'false', 's1 est une primitive string.\ns2 est un objet String (wrapper).\nMême valeur, mais types différents → false.', "// N'utilise JAMAIS new String/Number/Boolean"),

# Jour 195 — JS
('JS', 'Opérateur + coercition', 'Que va afficher ce code ?', 'console.log(1 + "2" + 3)', ['"123"', '6', '"15"', 'Error'], 0, '"123"', '1 + "2" → coercition : 1 devient "1" → "12".\n"12" + 3 → 3 devient "3" → "123".\n+ avec une string = concaténation.', '// + avec string = concat | sans string = addition'),

# Jour 197 — JS
('JS', 'Valeurs falsy complètes', 'Combien de valeurs falsy en JS ?', 'const falsies = [false, 0, "", null, undefined, NaN]\nconsole.log(falsies.length)', ['5', '6', '7', '8'], 1, '6', 'Les 6 valeurs falsy en JavaScript :\nfalse, 0, "", null, undefined, NaN.\nTOUT le reste est truthy (même [], {}, "0", "false").', '// 6 falsy : false, 0, "", null, undefined, NaN'),

# Jour 199 — JS
('JS', 'var sans déclaration', 'Que se passe-t-il ici ?', 'function test() {\n  x = 10  // oubli de var/let/const\n}\ntest()\nconsole.log(x)', ['Error', '10', 'undefined', 'null'], 1, '10', "Sans var/let/const, x devient une variable GLOBALE.\nC'est un des pièges majeurs de JS (pollution du scope global).\nToujours déclarer avec let/const.", '// "use strict" détecte ce piège'),

# Jour 201 — JS
('JS', 'ASI piège return', 'Que retourne cette fonction ?', 'function test() {\n  return\n  {\n    value: 10\n  }\n}', ['{ value: 10 }', 'undefined', 'Error', '10'], 1, 'undefined', "ASI (Automatic Semicolon Insertion) ajoute un ; après return.\nLa fonction retourne undefined, l'objet n'est jamais atteint.\nToujours mettre { sur la même ligne que return.", '// return { sur même ligne pour éviter ASI'),

# Jour 203 — JS
('JS', 'Expression vs déclaration', 'Que va se passer ?', 'console.log(foo())\nfunction foo() { return "A" }\nvar foo = function() { return "B" }', ['"A"', '"B"', 'Error', 'undefined'], 0, '"A"', 'function foo() est hoisted (déclaration).\nvar foo = function() n\'est hoisted que pour var (undefined).\nL\'appel se fait avant la réassignation → "A".', '// Function declaration : hoisted complètement'),

# Jour 205 — JS
('JS', "arguments n'est pas array", 'Que va se passer ?', 'function sum() {\n  return arguments.reduce((a,b) => a+b)\n}\nsum(1, 2, 3)', ['6', 'Error', 'undefined', '[1,2,3]'], 1, 'Error', "arguments est un objet array-like, PAS un vrai tableau.\nIl n'a pas les méthodes comme reduce().\nConversion : Array.from(arguments) ou [...arguments].", '// arguments : array-like | conversion : [...arguments]'),

# Jour 207 — JS
('JS', 'eval() dangers', 'Pourquoi éviter eval() ?', 'const code = "console.log(\'injection\')"\neval(code)', ['Sécurité', 'Performance', 'Scope pollution', 'Tout ça'], 3, 'Tout ça', 'eval() est dangereux : injection de code, performance dégradée,\npollution du scope, difficile à debugger.\nAlternatives : JSON.parse(), Function(), ou refactorer.', '// eval() = mal | alternatives : JSON.parse, new Function()'),

# Jour 209 — JS
('JS', 'with statement problème', 'Pourquoi with est déprécié ?', 'with (obj) {\n  x = 10\n}', ['Ambiguïté', 'Performance', 'Mode strict interdit', 'Tout ça'], 3, 'Tout ça', "with() crée de l'ambiguïté (x est-il local ou dans obj ?).\nRalentit les optimisations JS.\nInterdit en mode strict.", '// with() : déprécié, interdit en strict mode'),

# Jour 211 — JS
('JS', 'delete sur variable', 'Que va se passer ?', 'let x = 10\ndelete x\nconsole.log(x)', ['undefined', '10', 'Error', 'null'], 1, '10', "delete fonctionne sur les propriétés d'objets, PAS sur les variables.\ndelete x ne fait rien sur une variable déclarée.\nEn mode strict : erreur.", '// delete : pour propriétés objet, pas variables'),

# Jour 213 — JS
('JS', 'Array.some() vs every()', 'Quels résultats ?', 'const arr = [2, 4, 6, 7]\nconsole.log(arr.some(x => x > 5))\nconsole.log(arr.every(x => x > 5))', ['true / true', 'false / false', 'true / false', 'false / true'], 2, 'true / false', 'some() vérifie si AU MOINS un élément satisfait → true (7 > 5).\nevery() vérifie si TOUS satisfont → false (2, 4 ne sont pas > 5).', '// some = OU logique | every = ET logique'),

# Jour 215 — JS
('JS', 'find() vs findIndex()', 'Que retournent-ils ?', 'const arr = [10, 20, 30]\nconsole.log(arr.find(x => x > 15))\nconsole.log(arr.findIndex(x => x > 15))', ['20 / 20', '20 / 1', '1 / 20', 'undefined / -1'], 1, '20 / 1', "find() retourne le premier ÉLÉMENT qui satisfait → 20.\nfindIndex() retourne l'INDEX → 1 (position de 20).\nSi rien trouvé : undefined / -1.", '// find = élément | findIndex = index'),

# Jour 217 — JS
('JS', 'Array.flat() profondeur', 'Que contient result ?', 'const arr = [1, [2, [3, [4]]]]\nconst result = arr.flat(2)\nconsole.log(result)', ['[1,2,3,4]', '[1,2,[3,[4]]]', '[1,2,3,[4]]', '[1,[2,[3,[4]]]]'], 2, '[1,2,3,[4]]', 'flat(2) aplatit 2 niveaux de profondeur.\nNiveau 1 : [1, 2, [3, [4]]].\nNiveau 2 : [1, 2, 3, [4]].\nflat(Infinity) aplatit complètement.', '// flat(n) : aplatit n niveaux | flat(Infinity) : tout'),

# Jour 219 — JS
('JS', 'flatMap() utilité', 'Que fait flatMap() ?', 'const arr = [1, 2, 3]\nconst result = arr.flatMap(x => [x, x * 2])\nconsole.log(result)', ['[[1,2],[2,4],[3,6]]', '[1,2,2,4,3,6]', '[2,4,6]', 'Error'], 1, '[1,2,2,4,3,6]', "flatMap() = map() + flat(1).\nChaque élément est mappé puis le résultat est aplati d'un niveau.\nÉquivaut à arr.map(fn).flat().", '// flatMap = map + flat(1) en une passe'),

# Jour 221 — JS
('JS', 'Object.fromEntries()', 'Que contient result ?', 'const entries = [["a", 1], ["b", 2]]\nconst result = Object.fromEntries(entries)\nconsole.log(result)', ['[["a",1],["b",2]]', '{ a: 1, b: 2 }', '["a","b"]', 'Error'], 1, '{ a: 1, b: 2 }', "Object.fromEntries() convertit un tableau de paires [clé, valeur]\nen objet. C'est l'inverse de Object.entries().\nUtile pour transformer des Map en objets.", '// fromEntries(pairs) → objet | entries(obj) → pairs'),

# Jour 223 — JS
('JS', 'Object.assign() shallow', 'Que contient b.nested.x ?', 'const a = { nested: { x: 1 } }\nconst b = Object.assign({}, a)\nb.nested.x = 99\nconsole.log(a.nested.x)', ['1', '99', 'undefined', 'Error'], 1, '99', 'Object.assign() fait une copie SUPERFICIELLE (shallow).\nLes objets imbriqués sont copiés par référence.\nModifier b.nested affecte a.nested.', '// Object.assign = shallow copy | deep = structuredClone()'),

# Jour 225 — JS
('JS', 'Object.is() différences', 'Quelles différences avec === ?', 'console.log(Object.is(NaN, NaN))\nconsole.log(NaN === NaN)\nconsole.log(Object.is(+0, -0))\nconsole.log(+0 === -0)', ['true/false/false/true', 'false/false/true/true', 'true/true/false/false', 'false/true/false/true'], 0, 'true/false/false/true', 'Object.is() corrige 2 bizarreries de === :\n1. Object.is(NaN, NaN) = true (vs false avec ===).\n2. Object.is(+0, -0) = false (vs true avec ===).', '// Object.is : comme ===, mais corrige NaN et ±0'),

# Jour 227 — JS
('JS', 'Symbol.for() registre', 'Que va afficher ce code ?', 'const s1 = Symbol.for("key")\nconst s2 = Symbol.for("key")\nconsole.log(s1 === s2)', ['true', 'false', 'Error', 'undefined'], 0, 'true', 'Symbol.for() utilise un registre GLOBAL.\nDeux appels avec la même clé retournent le MÊME Symbol.\nSymbol() sans for() crée un nouveau Symbol à chaque fois.', '// Symbol.for(key) : global, réutilisable'),

# Jour 229 — JS
('JS', 'Symbol.toPrimitive', 'Conversion personnalisée ?', 'const obj = {\n  [Symbol.toPrimitive](hint) {\n    return hint === "number" ? 42 : "hello"\n  }\n}\nconsole.log(+obj, `${obj}`)', ['42 / "hello"', '"hello" / 42', 'Error', 'undefined'], 0, '42 / "hello"', 'Symbol.toPrimitive permet de contrôler la coercition.\nhint = "number" → +obj → 42.\nhint = "string" → template literal → "hello".', '// Symbol.toPrimitive : contrôle la conversion'),

# Jour 231 — JS
('JS', 'Regex lookahead', 'Que matche ce regex ?', 'const regex = /\\d(?=px)/\nconst str = "10px 20em"\nconsole.log(str.match(regex))', ['["10"]', '["10px"]', '["10", "20"]', 'null'], 0, '["10"]', '(?=px) est un lookahead positif : cherche un chiffre suivi de "px",\nmais ne capture PAS "px".\n10 est suivi de px → match. 20 est suivi de em → pas de match.', '// (?=...) : lookahead positif (ne capture pas)'),

# Jour 233 — JS
('JS', 'Groupes de capture', 'Combien de groupes capturés ?', 'const regex = /(\\d+)-(\\d+)-(\\d+)/\nconst match = "2024-05-15".match(regex)\nconsole.log(match.length)', ['1', '3', '4', '5'], 2, '4', 'match[0] = chaîne complète "2024-05-15".\nmatch[1] = "2024", match[2] = "05", match[3] = "15".\nDonc 4 éléments : match complet + 3 groupes.', '// Groupes () : match[0] = tout, match[1+] = groupes'),

# Jour 235 — JS
('JS', 'JSON.stringify() filtrage', 'Que contient result ?', 'const obj = { a: 1, b: 2, c: 3 }\nconst result = JSON.stringify(obj, ["a", "c"])\nconsole.log(result)', ['{"a":1,"b":2,"c":3}', '{"a":1,"c":3}', '{"b":2}', 'Error'], 1, '{"a":1,"c":3}', 'Le 2e paramètre (replacer) peut être un tableau de clés à garder.\nSeules "a" et "c" sont incluses, "b" est filtré.\nOn peut aussi passer une fonction.', '// stringify(obj, [keys]) : filtre les propriétés'),

# Jour 237 — JS
('JS', 'JSON.parse() reviver', 'Transformation à la lecture ?', 'const json = \'{"date":"2024-05-15"}\'\nconst obj = JSON.parse(json, (k, v) => \n  k === "date" ? new Date(v) : v\n)\nconsole.log(obj.date instanceof Date)', ['true', 'false', 'Error', 'undefined'], 0, 'true', 'Le 2e paramètre (reviver) transforme les valeurs à la lecture.\nIci, la clé "date" est convertie en objet Date.\nUtile pour désérialiser des types complexes.', '// parse(json, reviver) : transforme à la lecture'),

# Jour 239 — JS
('JS', 'let scope de bloc', 'Que va afficher ce code ?', 'if (true) {\n  let x = 10\n}\nconsole.log(x)', ['10', 'undefined', 'Error', 'null'], 2, 'Error', "let a un scope de BLOC { }.\nx n'existe que dans le bloc if.\nAccéder à x dehors → ReferenceError.", '// let/const : block scope | var : function scope'),

# Jour 241 — JS
('JS', 'const mutation objet', 'Que se passe-t-il ?', 'const obj = { x: 1 }\nobj.x = 99\nconsole.log(obj.x)', ['1', '99', 'Error', 'undefined'], 1, '99', 'const empêche la RÉASSIGNATION, pas la MUTATION.\nobj = {} → Error.\nobj.x = 99 → OK (mutation de propriété).', '// const : pas de réassignation, mutation OK'),

# Jour 243 — JS
('JS', 'IIFE utilité', 'À quoi sert ce pattern ?', '(function() {\n  var secret = 42\n})()\nconsole.log(secret)', ['42', 'undefined', 'Error', 'null'], 2, 'Error', "IIFE (Immediately Invoked Function Expression) crée un scope isolé.\nsecret n'existe que dans la fonction.\nAvant les modules, on utilisait ça pour éviter la pollution globale.", '// IIFE : scope isolé avant les modules ES6'),

# Jour 245 — JS
('JS', 'Module pattern', 'Encapsulation en JS classique ?', 'const module = (function() {\n  let private = 0\n  return {\n    increment: () => ++private,\n    get: () => private\n  }\n})()\nmodule.increment()\nconsole.log(module.private)', ['0', '1', 'undefined', 'Error'], 2, 'undefined', "Le module pattern utilise une IIFE + closure.\nprivate est encapsulé, inaccessible de l'extérieur.\nSeules les méthodes publiques (increment, get) y accèdent.", '// Module pattern : encapsulation avec closure'),

# Jour 247 — JS
('JS', 'Promise.race() comportement', 'Que se passe-t-il ?', 'Promise.race([\n  new Promise(r => setTimeout(() => r(1), 100)),\n  new Promise(r => setTimeout(() => r(2), 50))\n]).then(v => console.log(v))', ['1', '2', '[1, 2]', 'Error'], 1, '2', 'Promise.race() se résout avec la PREMIÈRE promise terminée.\nLa 2e promise (50ms) termine avant la 1ère (100ms).\nLes autres promises continuent mais sont ignorées.', '// race() : première promise (resolve ou reject)'),

# Jour 249 — JS
('JS', 'Promise chaîne erreur', 'Que va se passer ?', 'Promise.resolve()\n  .then(() => { throw new Error("oops") })\n  .then(() => console.log("A"))\n  .catch(() => console.log("B"))\n  .then(() => console.log("C"))', ['"A"', '"B"', '"B" "C"', 'Error'], 2, '"B" "C"', 'Une erreur dans .then() saute vers le prochain .catch().\nLe 2e .then("A") est sauté.\ncatch("B") attrape l\'erreur, puis .then("C") continue.', '// catch() attrape, puis la chaîne continue'),

# Jour 251 — JS
('JS', 'async/await try/catch', "Comment attraper l'erreur ?", 'async function test() {\n  const data = await fetch(url)\n}\ntest()', ['try/catch autour await', '.catch() sur test()', 'Les deux', 'Aucun'], 2, 'Les deux', "async function retourne TOUJOURS une Promise.\nOption 1 : try/catch autour de await (dans la fonction).\nOption 2 : .catch() sur l'appel test() (dehors).", '// async = Promise | try/catch dedans OU .catch() dehors'),

# Jour 253 — JS
('JS', 'Promises parallèles', 'Le plus rapide ?', '// Option A\nawait promise1\nawait promise2\n\n// Option B\nawait Promise.all([promise1, promise2])', ['A', 'B', 'Égal', 'Dépend'], 1, 'B', 'Option A : séquentiel (attend promise1, PUIS promise2).\nOption B : parallèle (lance les 2 en même temps).\nSi indépendantes, toujours Promise.all() pour la performance.', '// Parallèle : Promise.all() > séquentiel await await'),

# Jour 255 — JS
('JS', 'Event loop ordre', "Ordre d'affichage ?", 'console.log(1)\nsetTimeout(() => console.log(2), 0)\nPromise.resolve().then(() => console.log(3))\nconsole.log(4)', ['1 2 3 4', '1 4 2 3', '1 4 3 2', '1 3 4 2'], 2, '1 4 3 2', 'Code synchrone : 1, 4.\nMicrotasks (Promises) : 3.\nMacrotasks (setTimeout) : 2.\nOrdre : sync → microtasks → macrotasks.', '// Event loop : sync > microtasks > macrotasks'),

# Jour 257 — JS
('JS', 'Callback hell problème', 'Pourquoi éviter ce pattern ?', 'getData(function(a) {\n  getMore(a, function(b) {\n    getMore(b, function(c) {\n      // ...\n    })\n  })\n})', ['Lisibilité', 'Gestion erreurs', 'Maintenabilité', 'Tout ça'], 3, 'Tout ça', 'Callback hell ("pyramid of doom") :\n• Difficile à lire (indentation).\n• Erreurs difficiles à gérer.\nSolutions : Promises ou async/await.', '// Promises/async-await > callback hell'),

# Jour 259 — JS
('JS', 'Microtask vs Macrotask', 'Quelle différence ?', 'setTimeout(() => console.log("macro"), 0)\nqueueMicrotask(() => console.log("micro"))\nconsole.log("sync")', ['"sync" "macro" "micro"', '"sync" "micro" "macro"', '"micro" "sync" "macro"', '"macro" "micro" "sync"'], 1, '"sync" "micro" "macro"', "Ordre d'exécution :\n1. Code synchrone.\n2. Microtasks (queueMicrotask, Promises).\n3. Macrotasks (setTimeout, setInterval).\nLes microtasks ont priorité.", '// Microtasks (Promises) > Macrotasks (setTimeout)'),

# Jour 261 — JS
('JS', 'Promise.then() chaînage', 'Valeur retournée ?', 'Promise.resolve(1)\n  .then(x => x + 1)\n  .then(x => console.log(x))', ['1', '2', 'undefined', 'Promise'], 1, '2', '.then() reçoit la valeur retournée par le .then() précédent.\nPromise.resolve(1) → 1.\nthen(x => x + 1) → 2.\nthen(x => console.log(x)) → log 2.', '// then() chaîne : retour du précédent = input du suivant'),

# Jour 263 — JS
('JS', 'Prototype chain lookup', 'Comment JS trouve une propriété ?', 'const obj = { a: 1 }\nconsole.log(obj.toString)', ['undefined', 'Error', 'function', 'null'], 2, 'function', "obj n'a pas toString, mais JS remonte la chaîne de prototypes.\nobj → Object.prototype → toString.\nC'est la délégation prototypale.", '// Lookup : objet → prototype → prototype... → null'),

# Jour 265 — JS
('JS', 'Object.create() héritage', 'Différence avec constructor ?', 'const proto = { greet() { return "hi" } }\nconst obj = Object.create(proto)\nconsole.log(obj.greet())', ['"hi"', 'undefined', 'Error', 'null'], 0, '"hi"', 'Object.create(proto) crée un objet avec proto comme prototype.\nPas de fonction constructor, héritage prototypal pur.\nPlus flexible que new Constructor().', '// Object.create(proto) : héritage sans constructor'),

# Jour 267 — JS
('JS', 'class syntaxe vs fonction', 'Quelle est la différence ?', 'class A {}\nfunction B() {}\nconsole.log(typeof A, typeof B)', ['"class" "function"', '"function" "function"', '"object" "function"', 'Error'], 1, '"function" "function"', 'class est du sucre syntaxique sur les fonctions.\nSous le capot, class A {} est une fonction.\nMais class a un mode strict implicite et pas de hoisting.', '// class = sucre syntaxique sur function constructor'),

# Jour 269 — JS
('JS', 'super dans class', 'Que fait super ?', 'class Parent {\n  greet() { return "parent" }\n}\nclass Child extends Parent {\n  greet() { return super.greet() + " child" }\n}\nnew Child().greet()', ['"parent"', '"child"', '"parent child"', 'Error'], 2, '"parent child"', "super.greet() appelle la méthode greet() du parent.\nC'est comme this.__proto__.greet() mais avec le bon binding.\nIndispensable pour étendre des méthodes.", '// super : appel méthode parent dans class'),

# Jour 271 — JS
('JS', 'Méthodes static', 'Comment appeler une méthode static ?', 'class Math2 {\n  static add(a, b) { return a + b }\n}\nconsole.log(Math2.add(1, 2))', ['3', 'Error', 'undefined', 'null'], 0, '3', 'Les méthodes static appartiennent à la CLASSE, pas aux instances.\nOn appelle Math2.add(), pas new Math2().add().\nUtile pour des utilitaires (Math.max, Array.from).', "// static : sur la classe, pas sur l'instance"),

# Jour 273 — JS
('JS', 'Getter/Setter piège', 'Que va se passer ?', 'const obj = {\n  _x: 0,\n  get x() { return this._x },\n  set x(v) { this._x = v * 2 }\n}\nobj.x = 5\nconsole.log(obj.x)', ['5', '10', 'undefined', 'Error'], 1, '10', "setter x() multiplie par 2 avant d'assigner.\nobj.x = 5 → _x = 10.\ngetter x() retourne _x → 10.", '// get/set : propriétés calculées avec logique'),

# Jour 275 — JS
('JS', 'Proxy get trap', 'Que va afficher ce code ?', 'const obj = new Proxy({}, {\n  get(target, prop) {\n    return prop in target ? target[prop] : 42\n  }\n})\nconsole.log(obj.any)', ['undefined', '42', 'null', 'Error'], 1, '42', "Le trap get() intercepte TOUS les accès de propriétés.\nobj.any n'existe pas, donc on retourne 42.\nUtile pour des valeurs par défaut.", '// Proxy : intercepte opérations (get, set, etc.)'),

# Jour 277 — JS
('JS', 'Reflect.get() vs obj[prop]', 'Pourquoi utiliser Reflect ?', 'const obj = { x: 1 }\nReflect.get(obj, "x")\nobj["x"]', ['Même résultat', 'Reflect retourne bool', 'Reflect plus rapide', 'Aucune'], 0, 'Même résultat', "Reflect est l'API standard pour les opérations objet.\nReflect.get(obj, prop) = obj[prop].\nMais Reflect est plus cohérent (toujours retourne bool ou valeur).", '// Reflect : API standard pour opérations objet'),

# Jour 279 — JS
('JS', 'Private fields #', 'Accessible comment ?', 'class A {\n  #secret = 42\n  get() { return this.#secret }\n}\nconst a = new A()\nconsole.log(a.#secret)', ['42', 'Error', 'undefined', 'null'], 1, 'Error', 'Les champs # sont VRAIMENT privés (pas juste convention _).\nAccessibles SEULEMENT dans la classe.\na.#secret → SyntaxError.', '// #field : private, inaccessible hors classe'),

# Jour 281 — JS
('JS', 'WeakMap garbage collection', 'Pourquoi WeakMap ?', 'let obj = { data: "big" }\nconst map = new WeakMap()\nmap.set(obj, "metadata")\nobj = null  // plus de référence', ['map garde obj', 'obj peut être GC', 'Error', 'undefined'], 1, 'obj peut être GC', 'WeakMap a des clés "faibles" : si plus de référence ailleurs,\nl\'objet peut être garbage collected.\nMap normal garde la référence → fuite mémoire potentielle.', '// WeakMap : clés faibles, évite fuites mémoire'),

# Jour 283 — JS
('JS', 'WeakSet utilité', "Cas d'usage typique ?", 'const visited = new WeakSet()\nfunction track(obj) {\n  if (visited.has(obj)) return\n  visited.add(obj)\n  // process...\n}', ['Tracking objets', 'Liste unique', 'Cache', 'Set normal'], 0, 'Tracking objets', "WeakSet est parfait pour tracker des objets sans empêcher GC.\nSi l'objet est détruit ailleurs, il disparaît du WeakSet.\nImpossible avec Set normal.", "// WeakSet : tracking temporaire d'objets"),

# Jour 285 — JS
('JS', 'FinalizationRegistry', 'Notification GC ?', 'const registry = new FinalizationRegistry((val) => {\n  console.log(`${val} was GC\'d`)\n})\nlet obj = {}\nregistry.register(obj, "obj")', ['Callback quand GC', 'Empêche GC', 'Force GC', 'Rien'], 0, 'Callback quand GC', 'FinalizationRegistry appelle un callback quand un objet est GC.\nUtile pour cleanup de ressources externes (fichiers, sockets).\nAttention : timing non garanti.', '// FinalizationRegistry : cleanup après GC'),

# Jour 287 — JS
('JS', 'Iterator protocol', 'Comment rendre un objet iterable ?', 'const obj = {\n  [Symbol.iterator]() {\n    let i = 0\n    return {\n      next: () => ({ value: i++, done: i > 3 })\n    }\n  }\n}\nconsole.log([...obj])', ['[0,1,2]', '[1,2,3]', 'Error', '[]'], 0, '[0,1,2]', 'Symbol.iterator rend un objet iterable (for...of, spread).\nLa méthode retourne un iterator avec next().\nnext() retourne { value, done }.', '// Symbol.iterator : rend objet iterable'),

# Jour 289 — JS
('JS', 'yield* délégation', 'Que va afficher ce code ?', 'function* gen1() { yield 1; yield 2 }\nfunction* gen2() { yield* gen1(); yield 3 }\nconsole.log([...gen2()])', ['[1,2,3]', '[gen1,3]', '[1,2]', 'Error'], 0, '[1,2,3]', "yield* délègue à un autre generator.\ngen2() yield les valeurs de gen1() d'abord (1, 2), puis 3.\nC'est comme yield gen1().next().value en boucle.", '// yield* : délégation à un autre generator'),

# Jour 291 — JS
('JS', 'Async generator', 'Itération asynchrone ?', 'async function* gen() {\n  yield await Promise.resolve(1)\n  yield await Promise.resolve(2)\n}\n(async () => {\n  for await (let v of gen()) console.log(v)\n})()', ['1 2', 'Promise Promise', 'Error', '[1,2]'], 0, '1 2', 'async function* = generator asynchrone.\nfor await...of itère sur les valeurs résolues.\nUtile pour streams, pagination API, etc.', '// async function* : generator async avec for await...of'),

# Jour 293 — JS
('JS', 'Concat performance', 'Le plus rapide pour 1000 strings ?', '// Option A\nlet s = ""\nfor (...) s += str\n\n// Option B\nconst arr = []\nfor (...) arr.push(str)\narr.join("")', ['A', 'B', 'Égal', 'Dépend'], 1, 'B', 'Les strings sont immutables → += crée une nouvelle string à chaque fois.\nO(n²) pour n concaténations.\nArray + join() est O(n). Beaucoup plus rapide.', '// Concat : array.join() > += pour performance'),

# Jour 295 — JS
('JS', 'Accès propriété performance', 'Le plus rapide ?', 'const obj = { a: { b: { c: 1 } } }\n// Option A : obj.a.b.c\n// Option B : const c = obj.a.b.c', ['A', 'B', 'Égal', 'Dépend'], 1, 'B', "Chaque accès de propriété a un coût.\nSi utilisé plusieurs fois, mettre en cache dans une variable.\nLe moteur JS peut optimiser, mais c'est une bonne pratique.", '// Cache accès imbriqués dans variable locale'),

# Jour 297 — JS
('JS', 'Array pré-allocation', 'Performance amélioration ?', '// Option A\nconst arr = []\nfor (...) arr.push(i)\n\n// Option B\nconst arr = new Array(size)\nfor (...) arr[i] = i', ['A plus rapide', 'B plus rapide', 'Égal', 'Négligeable'], 3, 'Négligeable', "En théorie, pré-allocation évite resize dynamique.\nEn pratique, les moteurs modernes (V8) optimisent très bien.\nL'impact est négligeable sauf tableaux énormes.", '// Pré-allocation : impact mineur avec moteurs modernes'),

# Jour 299 — JS
('JS', 'Inline vs function', 'Performance overhead ?', '// Option A\nfor (...) { x = i * 2 }\n\n// Option B\nfunction double(i) { return i * 2 }\nfor (...) { x = double(i) }', ['A plus rapide', 'B plus rapide', 'Égal', 'Négligeable'], 3, 'Négligeable', "Appel de fonction a un coût, mais inlining JIT l'élimine.\nLes moteurs modernes inline les petites fonctions automatiquement.\nPrivilégier la lisibilité.", "// JIT inline les petites fonctions → pas d'overhead"),

# Jour 301 — JS
('JS', 'Closure fuite mémoire', 'Fuite possible ?', 'function create() {\n  const big = new Array(1000000)\n  return function() {\n    console.log(big.length)\n  }\n}\nconst fn = create()', ['Oui', 'Non', 'Seulement si appelé', 'Dépend'], 0, 'Oui', "La fonction retournée garde une référence à big.\nMême si on n'utilise que .length, TOUT big reste en mémoire.\nSolution : copier seulement ce qui est nécessaire.", '// Closures gardent TOUTE la variable, pas juste ce qui est utilisé'),

# Jour 303 — JS
('JS', 'Event listener fuite', 'Problème ici ?', 'element.addEventListener("click", function() {\n  // handler\n})\n// element removed from DOM', ['Fuite mémoire', 'Pas de fuite', 'Erreur', 'Dépend'], 0, 'Fuite mémoire', "Si element est retiré du DOM mais le listener n'est pas removeEventListener,\nl'élément reste en mémoire (le listener garde la référence).\nToujours cleanup les listeners.", '// removeEventListener avant de retirer du DOM'),

# Jour 305 — JS
('JS', 'Detached DOM nodes', 'Fuite mémoire ?', 'let div = document.createElement("div")\ndocument.body.appendChild(div)\ndocument.body.removeChild(div)\n// div variable garde référence', ['Oui', 'Non', 'Seulement si listeners', 'Dépend'], 0, 'Oui', 'removeChild retire du DOM mais la variable div garde la référence.\nLe nœud est "detached" : pas visible, mais en mémoire.\nSolution : div = null après usage.', '// Detached nodes : retirés du DOM mais référencés en JS'),

# Jour 307 — JS
('JS', 'Hidden classes V8', 'Impact performance ?', '// Option A\nconst obj1 = { a: 1, b: 2 }\nconst obj2 = { a: 3, b: 4 }\n\n// Option B\nconst obj1 = { a: 1 }\nobj1.b = 2\nconst obj2 = { a: 3, b: 4 }', ['A plus rapide', 'B plus rapide', 'Égal', 'Négligeable'], 0, 'A plus rapide', 'V8 crée des "hidden classes" pour optimiser l\'accès.\nSi objets créés avec mêmes propriétés dans même ordre → même classe.\nAjout dynamique de propriété → nouvelle classe → déoptimisation.', '// Créer objets avec mêmes propriétés dans même ordre'),

# Jour 309 — JS
('JS', 'Inline caching monomorphe', 'Optimisation V8 ?', 'function getX(obj) { return obj.x }\ngetX({ x: 1 })\ngetX({ x: 2 })\ngetX({ x: 3, y: 9 })  // shape différente', ['Déoptimisation', 'Aucun impact', 'Plus rapide', 'Erreur'], 0, 'Déoptimisation', 'Si getX() reçoit toujours des objets de même shape → monomorphe → très rapide.\nSi shapes différentes → polymorphe → cache moins efficace.\nToujours passer objets de même structure.', '// Inline cache : monomorphe > polymorphe > megamorphe'),

# Jour 311 — JS
('JS', 'Déoptimisation V8', 'Cause de déoptimisation ?', 'function add(a, b) {\n  return a + b\n}\nadd(1, 2)\nadd(1, 2)\nadd("hello", "world")', ['Changement de type', "Trop d'appels", 'Aucun', 'Erreur'], 0, 'Changement de type', 'V8 optimise add() pour des numbers.\nQuand appelé avec strings, le code optimisé est invalide.\n→ Déoptimisation, retour à version générique (plus lente).', '// Déoptimisation : changements de types, arguments.length variable'),

# Jour 313 — JS
('JS', 'Event bubbling vs capturing', 'Ordre de propagation ?', 'parent.addEventListener("click", () => console.log("P"))\nchild.addEventListener("click", () => console.log("C"))\n// click sur child', ['"C" "P"', '"P" "C"', '"C"', '"P"'], 0, '"C" "P"', 'Par défaut, les événements "bubblent" (remontent).\nCapture : parent → enfant.\nBubbling : enfant → parent.\n3e param addEventListener(event, handler, true) = capture.', '// Bubbling (défaut) : enfant → parent | Capturing : parent → enfant'),

# Jour 315 — JS
('JS', 'preventDefault() différence', 'Quelle est la différence ?', 'e.preventDefault()  // A\ne.stopPropagation()  // B', ['A: empêche action | B: stop bubbling', 'A: stop bubbling | B: empêche action', 'Pareil', 'Aucune'], 0, 'A: empêche action | B: stop bubbling', "preventDefault() empêche l'action par défaut (lien, form submit).\nstopPropagation() empêche la propagation aux parents.\nDeux concepts différents.", '// preventDefault : action par défaut | stopPropagation : bubbling'),

# Jour 317 — JS
('JS', 'Event delegation pattern', 'Avantage ?', 'parent.addEventListener("click", (e) => {\n  if (e.target.matches(".item")) {\n    // handle\n  }\n})', ['1 listener pour tous enfants', 'Plus rapide', 'Marche pour éléments futurs', 'Tout ça'], 3, 'Tout ça', 'Délégation : 1 listener sur parent au lieu de N sur enfants.\nMoins de mémoire, meilleure performance.\nMarche même pour éléments ajoutés dynamiquement.', '// Event delegation : 1 listener parent > N listeners enfants'),

# Jour 319 — JS
('JS', 'requestAnimationFrame', 'Timing optimal ?', 'requestAnimationFrame(() => {\n  element.style.left = "100px"\n})', ['Avant prochain repaint', '16.67ms', '1 frame', 'Immédiat'], 0, 'Avant prochain repaint', 'rAF appelle le callback juste avant le prochain repaint (60 FPS = ~16ms).\nSynchronisé avec le refresh du navigateur → animations fluides.\nPlus optimal que setTimeout.', '// rAF : sync avec repaint (~60 FPS) > setTimeout'),

# Jour 321 — JS
('JS', 'Web Worker communication', 'Comment communiquer ?', 'const worker = new Worker("worker.js")\nworker.postMessage({ data: 42 })\nworker.onmessage = (e) => console.log(e.data)', ['postMessage / onmessage', 'Shared memory', 'Fonctions directes', 'Aucune'], 0, 'postMessage / onmessage', "Workers communiquent par messages (structured cloning).\nPas de mémoire partagée par défaut (sauf SharedArrayBuffer).\nC'est asynchrone et isolé.", '// Workers : postMessage (copie) | SharedArrayBuffer (partagé)'),

# Jour 323 — JS
('JS', 'SharedArrayBuffer', "Cas d'usage ?", 'const sab = new SharedArrayBuffer(1024)\nconst view = new Int32Array(sab)\nAtomics.add(view, 0, 1)', ['Mémoire partagée multi-thread', 'Array normal', 'Buffer réseau', 'Aucun'], 0, 'Mémoire partagée multi-thread', 'SharedArrayBuffer permet de partager la mémoire entre Workers.\nAtomics garantit les opérations thread-safe.\nUtile pour calculs parallèles intensifs.', '// SharedArrayBuffer + Atomics : mémoire partagée thread-safe'),

# Jour 325 — JS
('JS', 'LocalStorage différence', 'Quelle différence ?', 'localStorage.setItem("key", "val")\nsessionStorage.setItem("key", "val")', ['localStorage persiste | sessionStorage = session', 'Même chose', 'localStorage plus rapide', 'Aucune'], 0, 'localStorage persiste | sessionStorage = session', "localStorage persiste même après fermeture du navigateur.\nsessionStorage est effacé à la fermeture de l'onglet.\nLimite : ~5-10 MB, synchrone, strings uniquement.", '// localStorage : persistent | sessionStorage : tab scope'),

# Jour 327 — JS
('JS', 'IndexedDB utilité', 'Avantage vs localStorage ?', 'const request = indexedDB.open("myDB", 1)', ['Stockage gros volumes', 'Asynchrone', 'Transactions', 'Tout ça'], 3, 'Tout ça', 'IndexedDB est une vraie base de données navigateur.\nAsynchrone, supporte gros volumes, transactions, indices.\nPlus complexe mais plus puissant que localStorage.', '// IndexedDB : DB complète | localStorage : simple key-value'),

# Jour 329 — JS
('JS', 'Service Worker phases', 'Ordre du lifecycle ?', 'navigator.serviceWorker.register("sw.js")', ['install → activate → fetch', 'fetch → install → activate', 'activate → install → fetch', 'install → fetch → activate'], 0, 'install → activate → fetch', 'Lifecycle : install (1ère fois), activate (prise de contrôle), fetch (intercept).\nwaitUntil() dans install pour cacher des assets.\nskipWaiting() pour activer immédiatement.', '// SW lifecycle : install → activate → fetch'),

# Jour 331 — JS
('JS', 'Fetch avantage', 'Pourquoi préférer fetch() ?', 'fetch("/api/data")\n  .then(r => r.json())\n  .then(data => console.log(data))', ['Promise-based', 'Plus moderne', 'Syntaxe propre', 'Tout ça'], 3, 'Tout ça', 'fetch() retourne une Promise → async/await friendly.\nPlus propre que XMLHttpRequest (callback hell).\nSupport streaming, CORS, etc.', '// fetch() : Promise-based, moderne > XMLHttpRequest'),

# Jour 333 — JS
('JS', 'CORS preflight request', 'Quand déclenché ?', 'fetch("https://api.com", {\n  method: "POST",\n  headers: { "Content-Type": "application/json" }\n})', ['Requête OPTIONS avant POST', 'Direct POST', 'Erreur CORS', 'Dépend'], 0, 'Requête OPTIONS avant POST', 'CORS preflight (OPTIONS) est envoyé pour requêtes "non-simples".\nPOST avec Content-Type application/json → preflight.\nGET simple → pas de preflight.', '// CORS : requêtes complexes → preflight OPTIONS'),

# Jour 335 — JS
('JS', 'AbortController utilité', 'Annuler un fetch ?', 'const controller = new AbortController()\nfetch(url, { signal: controller.signal })\ncontroller.abort()', ['Annule requête', 'Timeout', 'Cleanup', 'Tout ça'], 3, 'Tout ça', "AbortController permet d'annuler fetch, event listeners, etc.\ncontroller.abort() déclenche une AbortError.\nUtile pour cleanup, timeout, navigation.", '// AbortController : cancel fetch, listeners, async ops'),

# Jour 337 — JS
('JS', 'ReadableStream', 'Lecture en continu ?', 'const stream = response.body\nconst reader = stream.getReader()\nawait reader.read()', ['Lecture chunk par chunk', 'Tout en mémoire', 'Synchrone', 'Aucune'], 0, 'Lecture chunk par chunk', 'Streams permettent de lire/écrire des données progressivement.\nUtile pour gros fichiers (pas tout en mémoire).\nread() retourne { value, done }.', '// Streams : lecture/écriture progressive (chunk par chunk)'),

# Jour 339 — JS
('JS', 'Top-level await modules', 'Valide en module ?', 'const data = await fetch("/api").then(r => r.json())\nexport default data', ['Oui en module ES', 'Non', 'Seulement dans async', 'Erreur'], 0, 'Oui en module ES', 'Top-level await fonctionne dans les modules ES (type="module").\nLe module attend que l\'await se résolve avant export.\nAttention : bloque l\'import du module.', '// Top-level await : OK en module ES, bloque import'),

# Jour 341 — JS
('JS', 'import() dynamique', "Cas d'usage ?", 'button.addEventListener("click", async () => {\n  const module = await import("./heavy.js")\n  module.run()\n})', ['Lazy loading', 'Code splitting', 'Conditionnel', 'Tout ça'], 3, 'Tout ça', 'import() est une Promise → chargement à la demande.\nUtile pour lazy loading, code splitting, imports conditionnels.\nRéduit le bundle initial.', '// import() : lazy load, code split, conditionnel'),

# Jour 343 — JS
('JS', 'import.meta.url', 'Contient quoi ?', 'console.log(import.meta.url)', ['URL du module actuel', 'URL de la page', 'undefined', 'Erreur'], 0, 'URL du module actuel', "import.meta.url est l'URL absolue du module courant.\nUtile pour construire des chemins relatifs (Workers, assets).\nDisponible uniquement dans les modules ES.", '// import.meta.url : URL absolue du module'),

# Jour 345 — JS
('JS', 'Optional catch binding', 'Valide ?', 'try {\n  riskyOp()\n} catch {\n  console.log("error")\n}', ['Oui, (e) optionnel', 'Non, erreur syntaxe', 'Seulement async', 'Aucun'], 0, 'Oui, (e) optionnel', "Depuis ES2019, catch(e) peut omettre le paramètre.\nUtile si on ne se sert pas de l'erreur.\nPlus propre que catch(e) sans utiliser e.", '// catch { } : paramètre optionnel depuis ES2019'),

# Jour 347 — JS
('JS', 'Numeric separators', 'Lisibilité améliorée ?', 'const billion = 1_000_000_000\nconsole.log(billion)', ['1000000000', 'Error', '"1_000_000_000"', '1'], 0, '1000000000', 'Les _ dans les nombres sont ignorés par JS (syntaxe visuelle).\n1_000_000_000 = 1000000000.\nAméliore la lisibilité des gros nombres.', '// _ dans nombres : purement visuel, ignoré par JS'),

# Jour 349 — JS
('JS', 'Promise.allSettled() différence', 'Comportement si 1 échoue ?', 'Promise.allSettled([p1, p2, p3])\nPromise.all([p1, p2, p3])', ['allSettled attend toutes | all reject si 1 fail', 'Pareil', 'all attend toutes', 'Aucune'], 0, 'allSettled attend toutes | all reject si 1 fail', "Promise.all() reject dès qu'une promise échoue.\nPromise.allSettled() attend TOUTES les promises (success ou fail).\nRetourne { status, value/reason } pour chacune.", '// all : fail fast | allSettled : attend toutes'),

# Jour 351 — JS
('JS', 'Promise.any() comportement', 'Différence avec race() ?', 'Promise.any([p1, p2, p3])\nPromise.race([p1, p2, p3])', ['any : 1ère réussie | race : 1ère terminée', 'Pareil', 'any plus rapide', 'Aucune'], 0, 'any : 1ère réussie | race : 1ère terminée', 'Promise.race() retourne la PREMIÈRE terminée (resolve ou reject).\nPromise.any() retourne la PREMIÈRE réussie (ignore les rejets).\nany() reject seulement si TOUTES échouent (AggregateError).', '// race : 1ère finie | any : 1ère réussie'),

# Jour 353 — JS
('JS', 'String.matchAll()', 'Retourne quoi ?', 'const str = "test1 test2"\nconst matches = str.matchAll(/test(\\d)/g)\nconsole.log(matches)', ['Iterator', 'Array', 'null', 'String'], 0, 'Iterator', 'matchAll() retourne un ITERATOR de matches (pas un array).\nUtile pour capturer tous les groupes de toutes les correspondances.\nNécessite le flag g (global).', '// matchAll : iterator de matches avec groupes (nécessite /g)'),

# Jour 355 — JS
('JS', 'Array.at() indices négatifs', 'Différence avec [] ?', 'const arr = [1, 2, 3]\nconsole.log(arr.at(-1))\nconsole.log(arr[-1])', ['3 / undefined', 'undefined / 3', '3 / 3', 'Error'], 0, '3 / undefined', 'at(-1) accède au dernier élément (indices négatifs depuis la fin).\narr[-1] cherche la propriété "-1" → undefined.\nat() est plus intuitif pour indices négatifs.', '// at(-n) : depuis la fin | [-n] : propriété string'),

# Jour 357 — JS
('JS', 'Object.hasOwn() vs hasOwnProperty', 'Pourquoi hasOwn() ?', 'const obj = { a: 1 }\nObject.hasOwn(obj, "a")\nobj.hasOwnProperty("a")', ['Même résultat, hasOwn plus sûr', 'hasOwn plus rapide', 'Différent', 'Aucune'], 0, 'Même résultat, hasOwn plus sûr', "hasOwnProperty() peut être overridden sur l'objet.\nObject.hasOwn() est une méthode statique → plus fiable.\nC'est la méthode recommandée maintenant.", '// Object.hasOwn(obj, key) > obj.hasOwnProperty(key)'),

# Jour 359 — JS
('JS', 'Error.cause chaînage', 'Utilité ?', 'try {\n  // ...\n} catch (err) {\n  throw new Error("Failed", { cause: err })\n}', ['Chaîner erreurs', 'Debug plus facile', 'Traçabilité', 'Tout ça'], 3, 'Tout ça', "Error.cause permet de chaîner les erreurs (error wrapping).\nGarde le contexte de l'erreur originale.\nFacilite le debugging et la traçabilité.", '// Error(msg, { cause }) : chaînage erreurs'),

# Jour 361 — JS
('JS', 'Temporal API futur', 'Remplacement de Date ?', 'const now = Temporal.Now.plainDateTimeISO()\nconsole.log(now.year)', ['Oui, plus moderne', 'Non, obsolète', 'Pareil que Date', 'Aucun'], 0, 'Oui, plus moderne', 'Temporal est la future API pour dates/heures (stage 3).\nCorrige tous les problèmes de Date (immutable, timezone, précis).\nPas encore standard, mais bientôt.', '// Temporal : future API dates (immutable, timezone, précis)'),

# Jour 363 — JS
('JS', 'Pattern matching proposition', 'Syntaxe future ?', 'match (value) {\n  when 1: return "one"\n  when 2: return "two"\n  default: return "other"\n}', ['Stage 1 proposal', 'Déjà standard', 'Abandonné', 'Aucun'], 0, 'Stage 1 proposal', 'Pattern matching est une proposition TC39 (stage 1).\nComme switch mais plus puissant (destructuring, guards).\nPas encore disponible, à suivre.', '// Pattern matching : stage 1, comme switch++'),

# Jour 365 — JS
('JS', 'Records & Tuples', 'Immutabilité profonde ?', 'const rec = #{ a: 1, b: 2 }\nconst tup = #[1, 2, 3]', ['Proposition immutables', 'Déjà standard', 'Syntaxe invalide', 'Aucun'], 0, 'Proposition immutables', 'Records (#{ }) et Tuples (#[ ]) sont des structures immutables.\nProposition TC39 (stage 2).\nComparaison par valeur (pas par référence).', '// Records/Tuples : immutables, comparison par valeur (stage 2)'),

]
