#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour générer les 202 nouveaux quizzes Codebog.
Basé sur : Eloquent JS, Good Parts, YDKJS, Aditya, Cormen, LeetCode
"""

# PHASE 1 - NOUVEAUX QUIZZES JS (24 quizzes)
NEW_JS_PHASE1 = [

# String methods
('JS', 'String.slice() négatif', 'Les indices négatifs en JS : magie ou logique ?', 'const str = "JavaScript"\nconsole.log(str.slice(-6, -1))', ['"Java"', '"Script"', '"Scrip"', '"ipt"'], 2, '"Scrip"', 'slice(-6, -1) compte depuis la fin : -6 = index 4 (S), -1 = index 9.\nExclut le dernier index, donc de 4 à 8 = "Scrip".\nLes indices négatifs comptent depuis la fin de la chaîne.', '// slice(start, end) : négatif = depuis la fin'),

# Number precision
('JS', 'Précision décimale', 'Pourquoi 0.1 + 0.2 ≠ 0.3 ?', 'console.log(0.1 + 0.2 === 0.3)', ['true', 'false', 'Error', 'undefined'], 1, 'false', '0.1 + 0.2 donne 0.30000000000000004 en JavaScript.\nLes nombres sont stockés en IEEE 754 (64-bit float).\nCertaines décimales ne peuvent pas être représentées exactement.', '// Utilise Number.EPSILON ou des entiers pour la précision'),

# Boolean short-circuit
('JS', 'Short-circuit &&', 'Que va afficher ce code ?', 'let x = 0\nfalse && (x = 10)\nconsole.log(x)', ['0', '10', 'false', 'undefined'], 0, '0', 'L\'opérateur && évalue le côté droit SEULEMENT si le gauche est vrai.\nComme false est falsy, (x = 10) n\'est jamais exécuté.\nC\'est le short-circuit evaluation.', '// && : si gauche falsy, n\'évalue pas la droite'),

# Logical operators priority
('JS', 'Priorité || vs &&', 'Quelle est la valeur de result ?', 'const result = true || false && false\nconsole.log(result)', ['true', 'false', 'Error', 'undefined'], 0, 'true', '&& a une priorité plus élevée que ||.\nDonc false && false s\'évalue d\'abord = false.\nPuis true || false = true.', '// Priorité : && avant || (comme * avant +)'),

# for...in gotchas
('JS', 'for...in sur tableau', 'Que va afficher ce code ?', 'const arr = [10, 20, 30]\nfor (let i in arr) {\n  console.log(typeof i)\n}', ['"number"', '"string"', '"object"', 'Error'], 1, '"string"', 'for...in itère sur les clés (indices), PAS les valeurs.\nEt les clés sont toujours des strings, même pour les tableaux.\nPour les valeurs, utilise for...of.', '// for...in → clés (string) | for...of → valeurs'),

# while vs do...while
('JS', 'do...while comportement', 'Combien de fois "test" s\'affiche ?', 'let i = 10\ndo {\n  console.log("test")\n  i++\n} while (i < 5)', ['0 fois', '1 fois', '5 fois', '10 fois'], 1, '1 fois', 'do...while exécute TOUJOURS le bloc au moins une fois,\npuis vérifie la condition.\nMême si i = 10 > 5, le premier tour est exécuté.', '// do...while : exécute PUIS vérifie (min 1 tour)'),

# Switch fall-through
('JS', 'Switch sans break', 'Que va afficher ce code ?', 'const x = 1\nswitch(x) {\n  case 1:\n    console.log("A")\n  case 2:\n    console.log("B")\n  default:\n    console.log("C")\n}', ['"A"', '"A" "B" "C"', '"A" "B"', 'Error'], 1, '"A" "B" "C"', 'Sans break, le switch "tombe" dans les cas suivants (fall-through).\ncase 1 exécute A, puis continue vers case 2 (B), puis default (C).\nToujours mettre break sauf si fall-through voulu.', '// switch : toujours break, sauf fall-through intentionnel'),

# Break vs continue
('JS', 'break vs continue', 'Combien de nombres affichés ?', 'for (let i = 0; i < 5; i++) {\n  if (i === 2) continue\n  if (i === 4) break\n  console.log(i)\n}', ['2', '3', '4', '5'], 1, '3', 'i=0 → log 0, i=1 → log 1, i=2 → continue (skip).\ni=3 → log 3, i=4 → break (stop).\nDonc 0, 1, 3 = 3 nombres affichés.', '// continue = saute 1 tour | break = sort de la boucle'),

# Label statements
('JS', 'Label en JS', 'Les labels existent en JavaScript ?', 'outer: for (let i = 0; i < 2; i++) {\n  for (let j = 0; j < 2; j++) {\n    if (i === 1) break outer\n    console.log(i, j)\n  }\n}', ['Error', '0,0 0,1', '0,0 0,1 1,0 1,1', '0,0'], 1, '0,0 0,1', 'Les labels permettent de break/continue une boucle externe.\nbreak outer sort complètement de la boucle i.\nQuand i=1, on break avant de logger.', '// label: rarement utilisé, mais existe pour boucles imbriquées'),

# String immutability
('JS', 'String immutable', 'Que contient str après ?', 'let str = "hello"\nstr[0] = "H"\nconsole.log(str)', ['"Hello"', '"hello"', 'Error', '"H"'], 1, '"hello"', 'Les strings en JavaScript sont IMMUTABLES.\nstr[0] = "H" ne fait rien (mode strict : erreur silencieuse).\nPour modifier, il faut créer une nouvelle string.', '// Strings = immutables | utilise replace(), slice(), etc.'),

# Number.EPSILON
('JS', 'Number.EPSILON', 'À quoi sert Number.EPSILON ?', 'console.log(Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON)', ['false', 'true', 'Error', 'undefined'], 1, 'true', 'Number.EPSILON est la plus petite différence entre 2 nombres.\nUtile pour comparer des floats avec imprécision :\nau lieu de a === b, on fait Math.abs(a - b) < Number.EPSILON.', '// Pour comparer floats : Math.abs(a - b) < Number.EPSILON'),

# parseInt radix
('JS', 'parseInt() radix piège', 'Que va retourner ce code ?', 'console.log(parseInt("08"))', ['8', '0', 'NaN', 'Error'], 0, '8', 'Avant ES5, parseInt("08") pouvait renvoyer 0 (octal).\nDepuis ES5, le radix 10 est par défaut.\nMAIS toujours spécifier : parseInt("08", 10) pour être sûr.', '// parseInt(str, 10) : TOUJOURS spécifier le radix'),

# isNaN vs Number.isNaN
('JS', 'isNaN() vs Number.isNaN()', 'Laquelle est vraie ?', 'console.log(isNaN("hello"))\nconsole.log(Number.isNaN("hello"))', ['true / true', 'false / false', 'true / false', 'false / true'], 2, 'true / false', 'isNaN("hello") convertit d\'abord en nombre → NaN → true.\nNumber.isNaN("hello") vérifie si c\'est littéralement NaN → false.\nNumber.isNaN() est plus fiable (pas de coercition).', '// Number.isNaN() : pas de coercition, plus fiable'),

# Array.isArray vs instanceof
('JS', 'Array.isArray() fiabilité', 'Pourquoi préférer Array.isArray() ?', 'const arr = []\nconsole.log(Array.isArray(arr))\nconsole.log(arr instanceof Array)', ['true / true', 'true / false', 'false / true', 'false / false'], 0, 'true / true', 'Array.isArray() fonctionne même avec des tableaux d\'autres frames/iframes.\ninstanceof Array peut échouer si le Array vient d\'un autre contexte.\nArray.isArray() est la méthode recommandée.', '// Array.isArray() > instanceof (multi-frame safe)'),

# Object wrapper
('JS', 'new String() piège', 'Que va afficher ce code ?', 'const s1 = "hello"\nconst s2 = new String("hello")\nconsole.log(s1 === s2)', ['true', 'false', 'Error', 'undefined'], 1, 'false', 's1 est une primitive string.\ns2 est un objet String (wrapper).\nMême valeur, mais types différents → false.', '// N\'utilise JAMAIS new String/Number/Boolean'),

# Coercion with +
('JS', 'Opérateur + coercition', 'Que va afficher ce code ?', 'console.log(1 + "2" + 3)', ['"123"', '6', '"15"', 'Error'], 0, '"123"', '1 + "2" → coercition : 1 devient "1" → "12".\n"12" + 3 → 3 devient "3" → "123".\n+ avec une string = concaténation.', '// + avec string = concat | sans string = addition'),

# Truthy/Falsy comprehensive
('JS', 'Valeurs falsy complètes', 'Combien de valeurs falsy en JS ?', 'const falsies = [false, 0, "", null, undefined, NaN]\nconsole.log(falsies.length)', ['5', '6', '7', '8'], 1, '6', 'Les 6 valeurs falsy en JavaScript :\nfalse, 0, "", null, undefined, NaN.\nTOUT le reste est truthy (même [], {}, "0", "false").', '// 6 falsy : false, 0, "", null, undefined, NaN'),

# Global scope pollution
('JS', 'var sans déclaration', 'Que se passe-t-il ici ?', 'function test() {\n  x = 10  // oubli de var/let/const\n}\ntest()\nconsole.log(x)', ['Error', '10', 'undefined', 'null'], 1, '10', 'Sans var/let/const, x devient une variable GLOBALE.\nC\'est un des pièges majeurs de JS (pollution du scope global).\nToujours déclarer avec let/const.', '// "use strict" détecte ce piège'),

# Semicolon insertion
('JS', 'ASI piège return', 'Que retourne cette fonction ?', 'function test() {\n  return\n  {\n    value: 10\n  }\n}', ['{ value: 10 }', 'undefined', 'Error', '10'], 1, 'undefined', 'ASI (Automatic Semicolon Insertion) ajoute un ; après return.\nLa fonction retourne undefined, l\'objet n\'est jamais atteint.\nToujours mettre { sur la même ligne que return.', '// return { sur même ligne pour éviter ASI'),

# Function expression vs declaration
('JS', 'Expression vs déclaration', 'Que va se passer ?', 'console.log(foo())\nfunction foo() { return "A" }\nvar foo = function() { return "B" }', ['"A"', '"B"', 'Error', 'undefined'], 0, '"A"', 'function foo() est hoisted (déclaration).\nvar foo = function() n\'est hoisted que pour var (undefined).\nL\'appel se fait avant la réassignation → "A".', '// Function declaration : hoisted complètement'),

# arguments object
('JS', 'arguments n\'est pas array', 'Que va se passer ?', 'function sum() {\n  return arguments.reduce((a,b) => a+b)\n}\nsum(1, 2, 3)', ['6', 'Error', 'undefined', '[1,2,3]'], 1, 'Error', 'arguments est un objet array-like, PAS un vrai tableau.\nIl n\'a pas les méthodes comme reduce().\nConversion : Array.from(arguments) ou [...arguments].', '// arguments : array-like | conversion : [...arguments]'),

# eval dangers
('JS', 'eval() dangers', 'Pourquoi éviter eval() ?', 'const code = "console.log(\'injection\')"\neval(code)', ['Sécurité', 'Performance', 'Scope pollution', 'Tout ça'], 3, 'Tout ça', 'eval() est dangereux : injection de code, performance dégradée,\npollution du scope, difficile à debugger.\nAlternatives : JSON.parse(), Function(), ou refactorer.', '// eval() = mal | alternatives : JSON.parse, new Function()'),

# with statement
('JS', 'with statement problème', 'Pourquoi with est déprécié ?', 'with (obj) {\n  x = 10\n}', ['Ambiguïté', 'Performance', 'Mode strict interdit', 'Tout ça'], 3, 'Tout ça', 'with() crée de l\'ambiguïté (x est-il local ou dans obj ?).\nRalentit les optimisations JS.\nInterdit en mode strict.', '// with() : déprécié, interdit en strict mode'),

# delete operator
('JS', 'delete sur variable', 'Que va se passer ?', 'let x = 10\ndelete x\nconsole.log(x)', ['undefined', '10', 'Error', 'null'], 1, '10', 'delete fonctionne sur les propriétés d\'objets, PAS sur les variables.\ndelete x ne fait rien sur une variable déclarée.\nEn mode strict : erreur.', '// delete : pour propriétés objet, pas variables'),

]

# PHASE 2 - NOUVEAUX QUIZZES JS (25 quizzes)
NEW_JS_PHASE2 = [

# Array.some vs every
('JS', 'Array.some() vs every()', 'Quels résultats ?', 'const arr = [2, 4, 6, 7]\nconsole.log(arr.some(x => x > 5))\nconsole.log(arr.every(x => x > 5))', ['true / true', 'false / false', 'true / false', 'false / true'], 2, 'true / false', 'some() vérifie si AU MOINS un élément satisfait → true (7 > 5).\nevery() vérifie si TOUS satisfont → false (2, 4 ne sont pas > 5).', '// some = OU logique | every = ET logique'),

# Array.find vs findIndex
('JS', 'find() vs findIndex()', 'Que retournent-ils ?', 'const arr = [10, 20, 30]\nconsole.log(arr.find(x => x > 15))\nconsole.log(arr.findIndex(x => x > 15))', ['20 / 20', '20 / 1', '1 / 20', 'undefined / -1'], 1, '20 / 1', 'find() retourne le premier ÉLÉMENT qui satisfait → 20.\nfindIndex() retourne l\'INDEX → 1 (position de 20).\nSi rien trouvé : undefined / -1.', '// find = élément | findIndex = index'),

# Array.flat depth
('JS', 'Array.flat() profondeur', 'Que contient result ?', 'const arr = [1, [2, [3, [4]]]]\nconst result = arr.flat(2)\nconsole.log(result)', ['[1,2,3,4]', '[1,2,[3,[4]]]', '[1,2,3,[4]]', '[1,[2,[3,[4]]]]'], 2, '[1,2,3,[4]]', 'flat(2) aplatit 2 niveaux de profondeur.\nNiveau 1 : [1, 2, [3, [4]]].\nNiveau 2 : [1, 2, 3, [4]].\nflat(Infinity) aplatit complètement.', '// flat(n) : aplatit n niveaux | flat(Infinity) : tout'),

# Array.flatMap
('JS', 'flatMap() utilité', 'Que fait flatMap() ?', 'const arr = [1, 2, 3]\nconst result = arr.flatMap(x => [x, x * 2])\nconsole.log(result)', ['[[1,2],[2,4],[3,6]]', '[1,2,2,4,3,6]', '[2,4,6]', 'Error'], 1, '[1,2,2,4,3,6]', 'flatMap() = map() + flat(1).\nChaque élément est mappé puis le résultat est aplati d\'un niveau.\nÉquivaut à arr.map(fn).flat().', '// flatMap = map + flat(1) en une passe'),

# Object.entries / fromEntries
('JS', 'Object.fromEntries()', 'Que contient result ?', 'const entries = [["a", 1], ["b", 2]]\nconst result = Object.fromEntries(entries)\nconsole.log(result)', ['[["a",1],["b",2]]', '{ a: 1, b: 2 }', '["a","b"]', 'Error'], 1, '{ a: 1, b: 2 }', 'Object.fromEntries() convertit un tableau de paires [clé, valeur]\nen objet. C\'est l\'inverse de Object.entries().\nUtile pour transformer des Map en objets.', '// fromEntries(pairs) → objet | entries(obj) → pairs'),

# Object.assign shallow
('JS', 'Object.assign() shallow', 'Que contient b.nested.x ?', 'const a = { nested: { x: 1 } }\nconst b = Object.assign({}, a)\nb.nested.x = 99\nconsole.log(a.nested.x)', ['1', '99', 'undefined', 'Error'], 1, '99', 'Object.assign() fait une copie SUPERFICIELLE (shallow).\nLes objets imbriqués sont copiés par référence.\nModifier b.nested affecte a.nested.', '// Object.assign = shallow copy | deep = structuredClone()'),

# Object.is vs ===
('JS', 'Object.is() différences', 'Quelles différences avec === ?', 'console.log(Object.is(NaN, NaN))\nconsole.log(NaN === NaN)\nconsole.log(Object.is(+0, -0))\nconsole.log(+0 === -0)', ['true/false/false/true', 'false/false/true/true', 'true/true/false/false', 'false/true/false/true'], 0, 'true/false/false/true', 'Object.is() corrige 2 bizarreries de === :\n1. Object.is(NaN, NaN) = true (vs false avec ===).\n2. Object.is(+0, -0) = false (vs true avec ===).', '// Object.is : comme ===, mais corrige NaN et ±0'),

# Symbol.for global
('JS', 'Symbol.for() registre', 'Que va afficher ce code ?', 'const s1 = Symbol.for("key")\nconst s2 = Symbol.for("key")\nconsole.log(s1 === s2)', ['true', 'false', 'Error', 'undefined'], 0, 'true', 'Symbol.for() utilise un registre GLOBAL.\nDeux appels avec la même clé retournent le MÊME Symbol.\nSymbol() sans for() crée un nouveau Symbol à chaque fois.', '// Symbol.for(key) : global, réutilisable'),

# Symbol.toPrimitive
('JS', 'Symbol.toPrimitive', 'Conversion personnalisée ?', 'const obj = {\n  [Symbol.toPrimitive](hint) {\n    return hint === "number" ? 42 : "hello"\n  }\n}\nconsole.log(+obj, `${obj}`)', ['42 / "hello"', '"hello" / 42', 'Error', 'undefined'], 0, '42 / "hello"', 'Symbol.toPrimitive permet de contrôler la coercition.\nhint = "number" → +obj → 42.\nhint = "string" → template literal → "hello".', '// Symbol.toPrimitive : contrôle la conversion'),

# Regex lookahead
('JS', 'Regex lookahead', 'Que matche ce regex ?', 'const regex = /\\d(?=px)/\nconst str = "10px 20em"\nconsole.log(str.match(regex))', ['["10"]', '["10px"]', '["10", "20"]', 'null'], 0, '["10"]', '(?=px) est un lookahead positif : cherche un chiffre suivi de "px",\nmais ne capture PAS "px".\n10 est suivi de px → match. 20 est suivi de em → pas de match.', '// (?=...) : lookahead positif (ne capture pas)'),

# Regex capturing groups
('JS', 'Groupes de capture', 'Combien de groupes capturés ?', 'const regex = /(\\d+)-(\\d+)-(\\d+)/\nconst match = "2024-05-15".match(regex)\nconsole.log(match.length)', ['1', '3', '4', '5'], 2, '4', 'match[0] = chaîne complète "2024-05-15".\nmatch[1] = "2024", match[2] = "05", match[3] = "15".\nDonc 4 éléments : match complet + 3 groupes.', '// Groupes () : match[0] = tout, match[1+] = groupes'),

# JSON.stringify replacer
('JS', 'JSON.stringify() filtrage', 'Que contient result ?', 'const obj = { a: 1, b: 2, c: 3 }\nconst result = JSON.stringify(obj, ["a", "c"])\nconsole.log(result)', ['{"a":1,"b":2,"c":3}', '{"a":1,"c":3}', '{"b":2}', 'Error'], 1, '{"a":1,"c":3}', 'Le 2e paramètre (replacer) peut être un tableau de clés à garder.\nSeules "a" et "c" sont incluses, "b" est filtré.\nOn peut aussi passer une fonction.', '// stringify(obj, [keys]) : filtre les propriétés'),

# JSON.parse reviver
('JS', 'JSON.parse() reviver', 'Transformation à la lecture ?', 'const json = \'{"date":"2024-05-15"}\'\nconst obj = JSON.parse(json, (k, v) => \n  k === "date" ? new Date(v) : v\n)\nconsole.log(obj.date instanceof Date)', ['true', 'false', 'Error', 'undefined'], 0, 'true', 'Le 2e paramètre (reviver) transforme les valeurs à la lecture.\nIci, la clé "date" est convertie en objet Date.\nUtile pour désérialiser des types complexes.', '// parse(json, reviver) : transforme à la lecture'),

# let block scope
('JS', 'let scope de bloc', 'Que va afficher ce code ?', 'if (true) {\n  let x = 10\n}\nconsole.log(x)', ['10', 'undefined', 'Error', 'null'], 2, 'Error', 'let a un scope de BLOC { }.\nx n\'existe que dans le bloc if.\nAccéder à x dehors → ReferenceError.', '// let/const : block scope | var : function scope'),

# const mutation
('JS', 'const mutation objet', 'Que se passe-t-il ?', 'const obj = { x: 1 }\nobj.x = 99\nconsole.log(obj.x)', ['1', '99', 'Error', 'undefined'], 1, '99', 'const empêche la RÉASSIGNATION, pas la MUTATION.\nobj = {} → Error.\nobj.x = 99 → OK (mutation de propriété).', '// const : pas de réassignation, mutation OK'),

# IIFE pattern
('JS', 'IIFE utilité', 'À quoi sert ce pattern ?', '(function() {\n  var secret = 42\n})()\nconsole.log(secret)', ['42', 'undefined', 'Error', 'null'], 2, 'Error', 'IIFE (Immediately Invoked Function Expression) crée un scope isolé.\nsecret n\'existe que dans la fonction.\nAvant les modules, on utilisait ça pour éviter la pollution globale.', '// IIFE : scope isolé avant les modules ES6'),

# Module pattern
('JS', 'Module pattern', 'Encapsulation en JS classique ?', 'const module = (function() {\n  let private = 0\n  return {\n    increment: () => ++private,\n    get: () => private\n  }\n})()\nmodule.increment()\nconsole.log(module.private)', ['0', '1', 'undefined', 'Error'], 2, 'undefined', 'Le module pattern utilise une IIFE + closure.\nprivate est encapsulé, inaccessible de l\'extérieur.\nSeules les méthodes publiques (increment, get) y accèdent.', '// Module pattern : encapsulation avec closure'),

# Promise.race
('JS', 'Promise.race() comportement', 'Que se passe-t-il ?', 'Promise.race([\n  new Promise(r => setTimeout(() => r(1), 100)),\n  new Promise(r => setTimeout(() => r(2), 50))\n]).then(v => console.log(v))', ['1', '2', '[1, 2]', 'Error'], 1, '2', 'Promise.race() se résout avec la PREMIÈRE promise terminée.\nLa 2e promise (50ms) termine avant la 1ère (100ms).\nLes autres promises continuent mais sont ignorées.', '// race() : première promise (resolve ou reject)'),

# Promise error propagation
('JS', 'Promise chaîne erreur', 'Que va se passer ?', 'Promise.resolve()\n  .then(() => { throw new Error("oops") })\n  .then(() => console.log("A"))\n  .catch(() => console.log("B"))\n  .then(() => console.log("C"))', ['"A"', '"B"', '"B" "C"', 'Error'], 2, '"B" "C"', 'Une erreur dans .then() saute vers le prochain .catch().\nLe 2e .then("A") est sauté.\ncatch("B") attrape l\'erreur, puis .then("C") continue.', '// catch() attrape, puis la chaîne continue'),

# async/await error
('JS', 'async/await try/catch', 'Comment attraper l\'erreur ?', 'async function test() {\n  const data = await fetch(url)\n}\ntest()', ['try/catch autour await', '.catch() sur test()', 'Les deux', 'Aucun'], 2, 'Les deux', 'async function retourne TOUJOURS une Promise.\nOption 1 : try/catch autour de await (dans la fonction).\nOption 2 : .catch() sur l\'appel test() (dehors).', '// async = Promise | try/catch dedans OU .catch() dehors'),

# Parallel vs Sequential
('JS', 'Promises parallèles', 'Le plus rapide ?', '// Option A\nawait promise1\nawait promise2\n\n// Option B\nawait Promise.all([promise1, promise2])', ['A', 'B', 'Égal', 'Dépend'], 1, 'B', 'Option A : séquentiel (attend promise1, PUIS promise2).\nOption B : parallèle (lance les 2 en même temps).\nSi indépendantes, toujours Promise.all() pour la performance.', '// Parallèle : Promise.all() > séquentiel await await'),

# Event loop phases
('JS', 'Event loop ordre', 'Ordre d\'affichage ?', 'console.log(1)\nsetTimeout(() => console.log(2), 0)\nPromise.resolve().then(() => console.log(3))\nconsole.log(4)', ['1 2 3 4', '1 4 2 3', '1 4 3 2', '1 3 4 2'], 2, '1 4 3 2', 'Code synchrone : 1, 4.\nMicrotasks (Promises) : 3.\nMacrotasks (setTimeout) : 2.\nOrdre : sync → microtasks → macrotasks.', '// Event loop : sync > microtasks > macrotasks'),

# Callback hell
('JS', 'Callback hell problème', 'Pourquoi éviter ce pattern ?', 'getData(function(a) {\n  getMore(a, function(b) {\n    getMore(b, function(c) {\n      // ...\n    })\n  })\n})', ['Lisibilité', 'Gestion erreurs', 'Maintenabilité', 'Tout ça'], 3, 'Tout ça', 'Callback hell ("pyramid of doom") :\n• Difficile à lire (indentation).\n• Erreurs difficiles à gérer.\nSolutions : Promises ou async/await.', '// Promises/async-await > callback hell'),

# Microtask queue
('JS', 'Microtask vs Macrotask', 'Quelle différence ?', 'setTimeout(() => console.log("macro"), 0)\nqueueMicrotask(() => console.log("micro"))\nconsole.log("sync")', ['"sync" "macro" "micro"', '"sync" "micro" "macro"', '"micro" "sync" "macro"', '"macro" "micro" "sync"'], 1, '"sync" "micro" "macro"', 'Ordre d\'exécution :\n1. Code synchrone.\n2. Microtasks (queueMicrotask, Promises).\n3. Macrotasks (setTimeout, setInterval).\nLes microtasks ont priorité.', '// Microtasks (Promises) > Macrotasks (setTimeout)'),

# Promise chaining
('JS', 'Promise.then() chaînage', 'Valeur retournée ?', 'Promise.resolve(1)\n  .then(x => x + 1)\n  .then(x => console.log(x))', ['1', '2', 'undefined', 'Promise'], 1, '2', '.then() reçoit la valeur retournée par le .then() précédent.\nPromise.resolve(1) → 1.\nthen(x => x + 1) → 2.\nthen(x => console.log(x)) → log 2.', '// then() chaîne : retour du précédent = input du suivant'),

]

# PHASE 3 - NOUVEAUX QUIZZES JS (25 quizzes)
NEW_JS_PHASE3 = [

# Prototype chain
('JS', 'Prototype chain lookup', 'Comment JS trouve une propriété ?', 'const obj = { a: 1 }\nconsole.log(obj.toString)', ['undefined', 'Error', 'function', 'null'], 2, 'function', 'obj n\'a pas toString, mais JS remonte la chaîne de prototypes.\nobj → Object.prototype → toString.\nC\'est la délégation prototypale.', '// Lookup : objet → prototype → prototype... → null'),

# Object.create vs constructor
('JS', 'Object.create() héritage', 'Différence avec constructor ?', 'const proto = { greet() { return "hi" } }\nconst obj = Object.create(proto)\nconsole.log(obj.greet())', ['"hi"', 'undefined', 'Error', 'null'], 0, '"hi"', 'Object.create(proto) crée un objet avec proto comme prototype.\nPas de fonction constructor, héritage prototypal pur.\nPlus flexible que new Constructor().', '// Object.create(proto) : héritage sans constructor'),

# Class vs function constructor
('JS', 'class syntaxe vs fonction', 'Quelle est la différence ?', 'class A {}\nfunction B() {}\nconsole.log(typeof A, typeof B)', ['"class" "function"', '"function" "function"', '"object" "function"', 'Error'], 1, '"function" "function"', 'class est du sucre syntaxique sur les fonctions.\nSous le capot, class A {} est une fonction.\nMais class a un mode strict implicite et pas de hoisting.', '// class = sucre syntaxique sur function constructor'),

# super keyword
('JS', 'super dans class', 'Que fait super ?', 'class Parent {\n  greet() { return "parent" }\n}\nclass Child extends Parent {\n  greet() { return super.greet() + " child" }\n}\nnew Child().greet()', ['"parent"', '"child"', '"parent child"', 'Error'], 2, '"parent child"', 'super.greet() appelle la méthode greet() du parent.\nC\'est comme this.__proto__.greet() mais avec le bon binding.\nIndispensable pour étendre des méthodes.', '// super : appel méthode parent dans class'),

# Static methods
('JS', 'Méthodes static', 'Comment appeler une méthode static ?', 'class Math2 {\n  static add(a, b) { return a + b }\n}\nconsole.log(Math2.add(1, 2))', ['3', 'Error', 'undefined', 'null'], 0, '3', 'Les méthodes static appartiennent à la CLASSE, pas aux instances.\nOn appelle Math2.add(), pas new Math2().add().\nUtile pour des utilitaires (Math.max, Array.from).', '// static : sur la classe, pas sur l\'instance'),

# Getter/Setter
('JS', 'Getter/Setter piège', 'Que va se passer ?', 'const obj = {\n  _x: 0,\n  get x() { return this._x },\n  set x(v) { this._x = v * 2 }\n}\nobj.x = 5\nconsole.log(obj.x)', ['5', '10', 'undefined', 'Error'], 1, '10', 'setter x() multiplie par 2 avant d\'assigner.\nobj.x = 5 → _x = 10.\ngetter x() retourne _x → 10.', '// get/set : propriétés calculées avec logique'),

# Proxy handler traps
('JS', 'Proxy get trap', 'Que va afficher ce code ?', 'const obj = new Proxy({}, {\n  get(target, prop) {\n    return prop in target ? target[prop] : 42\n  }\n})\nconsole.log(obj.any)', ['undefined', '42', 'null', 'Error'], 1, '42', 'Le trap get() intercepte TOUS les accès de propriétés.\nobj.any n\'existe pas, donc on retourne 42.\nUtile pour des valeurs par défaut.', '// Proxy : intercepte opérations (get, set, etc.)'),

# Reflect vs Object
('JS', 'Reflect.get() vs obj[prop]', 'Pourquoi utiliser Reflect ?', 'const obj = { x: 1 }\nReflect.get(obj, "x")\nobj["x"]', ['Même résultat', 'Reflect retourne bool', 'Reflect plus rapide', 'Aucune'], 0, 'Même résultat', 'Reflect est l\'API standard pour les opérations objet.\nReflect.get(obj, prop) = obj[prop].\nMais Reflect est plus cohérent (toujours retourne bool ou valeur).', '// Reflect : API standard pour opérations objet'),

# Private fields
('JS', 'Private fields #', 'Accessible comment ?', 'class A {\n  #secret = 42\n  get() { return this.#secret }\n}\nconst a = new A()\nconsole.log(a.#secret)', ['42', 'Error', 'undefined', 'null'], 1, 'Error', 'Les champs # sont VRAIMENT privés (pas juste convention _).\nAccessibles SEULEMENT dans la classe.\na.#secret → SyntaxError.', '// #field : private, inaccessible hors classe'),

# WeakMap memory
('JS', 'WeakMap garbage collection', 'Pourquoi WeakMap ?', 'let obj = { data: "big" }\nconst map = new WeakMap()\nmap.set(obj, "metadata")\nobj = null  // plus de référence', ['map garde obj', 'obj peut être GC', 'Error', 'undefined'], 1, 'obj peut être GC', 'WeakMap a des clés "faibles" : si plus de référence ailleurs,\nl\'objet peut être garbage collected.\nMap normal garde la référence → fuite mémoire potentielle.', '// WeakMap : clés faibles, évite fuites mémoire'),

# WeakSet use case
('JS', 'WeakSet utilité', 'Cas d\'usage typique ?', 'const visited = new WeakSet()\nfunction track(obj) {\n  if (visited.has(obj)) return\n  visited.add(obj)\n  // process...\n}', ['Tracking objets', 'Liste unique', 'Cache', 'Set normal'], 0, 'Tracking objets', 'WeakSet est parfait pour tracker des objets sans empêcher GC.\nSi l\'objet est détruit ailleurs, il disparaît du WeakSet.\nImpossible avec Set normal.', '// WeakSet : tracking temporaire d\'objets'),

# FinalizationRegistry
('JS', 'FinalizationRegistry', 'Notification GC ?', 'const registry = new FinalizationRegistry((val) => {\n  console.log(`${val} was GC\'d`)\n})\nlet obj = {}\nregistry.register(obj, "obj")', ['Callback quand GC', 'Empêche GC', 'Force GC', 'Rien'], 0, 'Callback quand GC', 'FinalizationRegistry appelle un callback quand un objet est GC.\nUtile pour cleanup de ressources externes (fichiers, sockets).\nAttention : timing non garanti.', '// FinalizationRegistry : cleanup après GC'),

# Iterator protocol
('JS', 'Iterator protocol', 'Comment rendre un objet iterable ?', 'const obj = {\n  [Symbol.iterator]() {\n    let i = 0\n    return {\n      next: () => ({ value: i++, done: i > 3 })\n    }\n  }\n}\nconsole.log([...obj])', ['[0,1,2]', '[1,2,3]', 'Error', '[]'], 0, '[0,1,2]', 'Symbol.iterator rend un objet iterable (for...of, spread).\nLa méthode retourne un iterator avec next().\nnext() retourne { value, done }.', '// Symbol.iterator : rend objet iterable'),

# Generator delegation
('JS', 'yield* délégation', 'Que va afficher ce code ?', 'function* gen1() { yield 1; yield 2 }\nfunction* gen2() { yield* gen1(); yield 3 }\nconsole.log([...gen2()])', ['[1,2,3]', '[gen1,3]', '[1,2]', 'Error'], 0, '[1,2,3]', 'yield* délègue à un autre generator.\ngen2() yield les valeurs de gen1() d\'abord (1, 2), puis 3.\nC\'est comme yield gen1().next().value en boucle.', '// yield* : délégation à un autre generator'),

# Async generators
('JS', 'Async generator', 'Itération asynchrone ?', 'async function* gen() {\n  yield await Promise.resolve(1)\n  yield await Promise.resolve(2)\n}\n(async () => {\n  for await (let v of gen()) console.log(v)\n})()', ['1 2', 'Promise Promise', 'Error', '[1,2]'], 0, '1 2', 'async function* = generator asynchrone.\nfor await...of itère sur les valeurs résolues.\nUtile pour streams, pagination API, etc.', '// async function* : generator async avec for await...of'),

# String concat performance
('JS', 'Concat performance', 'Le plus rapide pour 1000 strings ?', '// Option A\nlet s = ""\nfor (...) s += str\n\n// Option B\nconst arr = []\nfor (...) arr.push(str)\narr.join("")', ['A', 'B', 'Égal', 'Dépend'], 1, 'B', 'Les strings sont immutables → += crée une nouvelle string à chaque fois.\nO(n²) pour n concaténations.\nArray + join() est O(n). Beaucoup plus rapide.', '// Concat : array.join() > += pour performance'),

# Object property access
('JS', 'Accès propriété performance', 'Le plus rapide ?', 'const obj = { a: { b: { c: 1 } } }\n// Option A : obj.a.b.c\n// Option B : const c = obj.a.b.c', ['A', 'B', 'Égal', 'Dépend'], 1, 'B', 'Chaque accès de propriété a un coût.\nSi utilisé plusieurs fois, mettre en cache dans une variable.\nLe moteur JS peut optimiser, mais c\'est une bonne pratique.', '// Cache accès imbriqués dans variable locale'),

# Array pre-allocation
('JS', 'Array pré-allocation', 'Performance amélioration ?', '// Option A\nconst arr = []\nfor (...) arr.push(i)\n\n// Option B\nconst arr = new Array(size)\nfor (...) arr[i] = i', ['A plus rapide', 'B plus rapide', 'Égal', 'Négligeable'], 3, 'Négligeable', 'En théorie, pré-allocation évite resize dynamique.\nEn pratique, les moteurs modernes (V8) optimisent très bien.\nL\'impact est négligeable sauf tableaux énormes.', '// Pré-allocation : impact mineur avec moteurs modernes'),

# Function call overhead
('JS', 'Inline vs function', 'Performance overhead ?', '// Option A\nfor (...) { x = i * 2 }\n\n// Option B\nfunction double(i) { return i * 2 }\nfor (...) { x = double(i) }', ['A plus rapide', 'B plus rapide', 'Égal', 'Négligeable'], 3, 'Négligeable', 'Appel de fonction a un coût, mais inlining JIT l\'élimine.\nLes moteurs modernes inline les petites fonctions automatiquement.\nPrivilégier la lisibilité.', '// JIT inline les petites fonctions → pas d\'overhead'),

# Closure memory leak
('JS', 'Closure fuite mémoire', 'Fuite possible ?', 'function create() {\n  const big = new Array(1000000)\n  return function() {\n    console.log(big.length)\n  }\n}\nconst fn = create()', ['Oui', 'Non', 'Seulement si appelé', 'Dépend'], 0, 'Oui', 'La fonction retournée garde une référence à big.\nMême si on n\'utilise que .length, TOUT big reste en mémoire.\nSolution : copier seulement ce qui est nécessaire.', '// Closures gardent TOUTE la variable, pas juste ce qui est utilisé'),

# Event listener leak
('JS', 'Event listener fuite', 'Problème ici ?', 'element.addEventListener("click", function() {\n  // handler\n})\n// element removed from DOM', ['Fuite mémoire', 'Pas de fuite', 'Erreur', 'Dépend'], 0, 'Fuite mémoire', 'Si element est retiré du DOM mais le listener n\'est pas removeEventListener,\nl\'élément reste en mémoire (le listener garde la référence).\nToujours cleanup les listeners.', '// removeEventListener avant de retirer du DOM'),

# Detached DOM
('JS', 'Detached DOM nodes', 'Fuite mémoire ?', 'let div = document.createElement("div")\ndocument.body.appendChild(div)\ndocument.body.removeChild(div)\n// div variable garde référence', ['Oui', 'Non', 'Seulement si listeners', 'Dépend'], 0, 'Oui', 'removeChild retire du DOM mais la variable div garde la référence.\nLe nœud est "detached" : pas visible, mais en mémoire.\nSolution : div = null après usage.', '// Detached nodes : retirés du DOM mais référencés en JS'),

# V8 hidden classes
('JS', 'Hidden classes V8', 'Impact performance ?', '// Option A\nconst obj1 = { a: 1, b: 2 }\nconst obj2 = { a: 3, b: 4 }\n\n// Option B\nconst obj1 = { a: 1 }\nobj1.b = 2\nconst obj2 = { a: 3, b: 4 }', ['A plus rapide', 'B plus rapide', 'Égal', 'Négligeable'], 0, 'A plus rapide', 'V8 crée des "hidden classes" pour optimiser l\'accès.\nSi objets créés avec mêmes propriétés dans même ordre → même classe.\nAjout dynamique de propriété → nouvelle classe → déoptimisation.', '// Créer objets avec mêmes propriétés dans même ordre'),

# Inline caching
('JS', 'Inline caching monomorphe', 'Optimisation V8 ?', 'function getX(obj) { return obj.x }\ngetX({ x: 1 })\ngetX({ x: 2 })\ngetX({ x: 3, y: 9 })  // shape différente', ['Déoptimisation', 'Aucun impact', 'Plus rapide', 'Erreur'], 0, 'Déoptimisation', 'Si getX() reçoit toujours des objets de même shape → monomorphe → très rapide.\nSi shapes différentes → polymorphe → cache moins efficace.\nToujours passer objets de même structure.', '// Inline cache : monomorphe > polymorphe > megamorphe'),

# Deoptimization triggers
('JS', 'Déoptimisation V8', 'Cause de déoptimisation ?', 'function add(a, b) {\n  return a + b\n}\nadd(1, 2)\nadd(1, 2)\nadd("hello", "world")', ['Changement de type', 'Trop d\'appels', 'Aucun', 'Erreur'], 0, 'Changement de type', 'V8 optimise add() pour des numbers.\nQuand appelé avec strings, le code optimisé est invalide.\n→ Déoptimisation, retour à version générique (plus lente).', '// Déoptimisation : changements de types, arguments.length variable'),

]

# PHASE 4 - NOUVEAUX QUIZZES JS (27 quizzes)
NEW_JS_PHASE4 = [

# Event bubbling vs capturing
('JS', 'Event bubbling vs capturing', 'Ordre de propagation ?', 'parent.addEventListener("click", () => console.log("P"))\nchild.addEventListener("click", () => console.log("C"))\n// click sur child', ['"C" "P"', '"P" "C"', '"C"', '"P"'], 0, '"C" "P"', 'Par défaut, les événements "bubblent" (remontent).\nCapture : parent → enfant.\nBubbling : enfant → parent.\n3e param addEventListener(event, handler, true) = capture.', '// Bubbling (défaut) : enfant → parent | Capturing : parent → enfant'),

# preventDefault vs stopPropagation
('JS', 'preventDefault() différence', 'Quelle est la différence ?', 'e.preventDefault()  // A\ne.stopPropagation()  // B', ['A: empêche action | B: stop bubbling', 'A: stop bubbling | B: empêche action', 'Pareil', 'Aucune'], 0, 'A: empêche action | B: stop bubbling', 'preventDefault() empêche l\'action par défaut (lien, form submit).\nstopPropagation() empêche la propagation aux parents.\nDeux concepts différents.', '// preventDefault : action par défaut | stopPropagation : bubbling'),

# Event delegation
('JS', 'Event delegation pattern', 'Avantage ?', 'parent.addEventListener("click", (e) => {\n  if (e.target.matches(".item")) {\n    // handle\n  }\n})', ['1 listener pour tous enfants', 'Plus rapide', 'Marche pour éléments futurs', 'Tout ça'], 3, 'Tout ça', 'Délégation : 1 listener sur parent au lieu de N sur enfants.\nMoins de mémoire, meilleure performance.\nMarche même pour éléments ajoutés dynamiquement.', '// Event delegation : 1 listener parent > N listeners enfants'),

# requestAnimationFrame timing
('JS', 'requestAnimationFrame', 'Timing optimal ?', 'requestAnimationFrame(() => {\n  element.style.left = "100px"\n})', ['Avant prochain repaint', '16.67ms', '1 frame', 'Immédiat'], 0, 'Avant prochain repaint', 'rAF appelle le callback juste avant le prochain repaint (60 FPS = ~16ms).\nSynchronisé avec le refresh du navigateur → animations fluides.\nPlus optimal que setTimeout.', '// rAF : sync avec repaint (~60 FPS) > setTimeout'),

# Web Workers
('JS', 'Web Worker communication', 'Comment communiquer ?', 'const worker = new Worker("worker.js")\nworker.postMessage({ data: 42 })\nworker.onmessage = (e) => console.log(e.data)', ['postMessage / onmessage', 'Shared memory', 'Fonctions directes', 'Aucune'], 0, 'postMessage / onmessage', 'Workers communiquent par messages (structured cloning).\nPas de mémoire partagée par défaut (sauf SharedArrayBuffer).\nC\'est asynchrone et isolé.', '// Workers : postMessage (copie) | SharedArrayBuffer (partagé)'),

# SharedArrayBuffer & Atomics
('JS', 'SharedArrayBuffer', 'Cas d\'usage ?', 'const sab = new SharedArrayBuffer(1024)\nconst view = new Int32Array(sab)\nAtomics.add(view, 0, 1)', ['Mémoire partagée multi-thread', 'Array normal', 'Buffer réseau', 'Aucun'], 0, 'Mémoire partagée multi-thread', 'SharedArrayBuffer permet de partager la mémoire entre Workers.\nAtomics garantit les opérations thread-safe.\nUtile pour calculs parallèles intensifs.', '// SharedArrayBuffer + Atomics : mémoire partagée thread-safe'),

# LocalStorage vs SessionStorage
('JS', 'LocalStorage différence', 'Quelle différence ?', 'localStorage.setItem("key", "val")\nsessionStorage.setItem("key", "val")', ['localStorage persiste | sessionStorage = session', 'Même chose', 'localStorage plus rapide', 'Aucune'], 0, 'localStorage persiste | sessionStorage = session', 'localStorage persiste même après fermeture du navigateur.\nsessionStorage est effacé à la fermeture de l\'onglet.\nLimite : ~5-10 MB, synchrone, strings uniquement.', '// localStorage : persistent | sessionStorage : tab scope'),

# IndexedDB basics
('JS', 'IndexedDB utilité', 'Avantage vs localStorage ?', 'const request = indexedDB.open("myDB", 1)', ['Stockage gros volumes', 'Asynchrone', 'Transactions', 'Tout ça'], 3, 'Tout ça', 'IndexedDB est une vraie base de données navigateur.\nAsynchrone, supporte gros volumes, transactions, indices.\nPlus complexe mais plus puissant que localStorage.', '// IndexedDB : DB complète | localStorage : simple key-value'),

# Service Worker lifecycle
('JS', 'Service Worker phases', 'Ordre du lifecycle ?', 'navigator.serviceWorker.register("sw.js")', ['install → activate → fetch', 'fetch → install → activate', 'activate → install → fetch', 'install → fetch → activate'], 0, 'install → activate → fetch', 'Lifecycle : install (1ère fois), activate (prise de contrôle), fetch (intercept).\nwaitUntil() dans install pour cacher des assets.\nskipWaiting() pour activer immédiatement.', '// SW lifecycle : install → activate → fetch'),

# Fetch vs XMLHttpRequest
('JS', 'Fetch avantage', 'Pourquoi préférer fetch() ?', 'fetch("/api/data")\n  .then(r => r.json())\n  .then(data => console.log(data))', ['Promise-based', 'Plus moderne', 'Syntaxe propre', 'Tout ça'], 3, 'Tout ça', 'fetch() retourne une Promise → async/await friendly.\nPlus propre que XMLHttpRequest (callback hell).\nSupport streaming, CORS, etc.', '// fetch() : Promise-based, moderne > XMLHttpRequest'),

# CORS preflight
('JS', 'CORS preflight request', 'Quand déclenché ?', 'fetch("https://api.com", {\n  method: "POST",\n  headers: { "Content-Type": "application/json" }\n})', ['Requête OPTIONS avant POST', 'Direct POST', 'Erreur CORS', 'Dépend'], 0, 'Requête OPTIONS avant POST', 'CORS preflight (OPTIONS) est envoyé pour requêtes "non-simples".\nPOST avec Content-Type application/json → preflight.\nGET simple → pas de preflight.', '// CORS : requêtes complexes → preflight OPTIONS'),

# AbortController for fetch
('JS', 'AbortController utilité', 'Annuler un fetch ?', 'const controller = new AbortController()\nfetch(url, { signal: controller.signal })\ncontroller.abort()', ['Annule requête', 'Timeout', 'Cleanup', 'Tout ça'], 3, 'Tout ça', 'AbortController permet d\'annuler fetch, event listeners, etc.\ncontroller.abort() déclenche une AbortError.\nUtile pour cleanup, timeout, navigation.', '// AbortController : cancel fetch, listeners, async ops'),

# Streams API
('JS', 'ReadableStream', 'Lecture en continu ?', 'const stream = response.body\nconst reader = stream.getReader()\nawait reader.read()', ['Lecture chunk par chunk', 'Tout en mémoire', 'Synchrone', 'Aucune'], 0, 'Lecture chunk par chunk', 'Streams permettent de lire/écrire des données progressivement.\nUtile pour gros fichiers (pas tout en mémoire).\nread() retourne { value, done }.', '// Streams : lecture/écriture progressive (chunk par chunk)'),

# Top-level await
('JS', 'Top-level await modules', 'Valide en module ?', 'const data = await fetch("/api").then(r => r.json())\nexport default data', ['Oui en module ES', 'Non', 'Seulement dans async', 'Erreur'], 0, 'Oui en module ES', 'Top-level await fonctionne dans les modules ES (type="module").\nLe module attend que l\'await se résolve avant export.\nAttention : bloque l\'import du module.', '// Top-level await : OK en module ES, bloque import'),

# Dynamic import
('JS', 'import() dynamique', 'Cas d\'usage ?', 'button.addEventListener("click", async () => {\n  const module = await import("./heavy.js")\n  module.run()\n})', ['Lazy loading', 'Code splitting', 'Conditionnel', 'Tout ça'], 3, 'Tout ça', 'import() est une Promise → chargement à la demande.\nUtile pour lazy loading, code splitting, imports conditionnels.\nRéduit le bundle initial.', '// import() : lazy load, code split, conditionnel'),

# import.meta.url
('JS', 'import.meta.url', 'Contient quoi ?', 'console.log(import.meta.url)', ['URL du module actuel', 'URL de la page', 'undefined', 'Erreur'], 0, 'URL du module actuel', 'import.meta.url est l\'URL absolue du module courant.\nUtile pour construire des chemins relatifs (Workers, assets).\nDisponible uniquement dans les modules ES.', '// import.meta.url : URL absolue du module'),

# Optional catch binding
('JS', 'Optional catch binding', 'Valide ?', 'try {\n  riskyOp()\n} catch {\n  console.log("error")\n}', ['Oui, (e) optionnel', 'Non, erreur syntaxe', 'Seulement async', 'Aucun'], 0, 'Oui, (e) optionnel', 'Depuis ES2019, catch(e) peut omettre le paramètre.\nUtile si on ne se sert pas de l\'erreur.\nPlus propre que catch(e) sans utiliser e.', '// catch { } : paramètre optionnel depuis ES2019'),

# Numeric separators
('JS', 'Numeric separators', 'Lisibilité améliorée ?', 'const billion = 1_000_000_000\nconsole.log(billion)', ['1000000000', 'Error', '"1_000_000_000"', '1'], 0, '1000000000', 'Les _ dans les nombres sont ignorés par JS (syntaxe visuelle).\n1_000_000_000 = 1000000000.\nAméliore la lisibilité des gros nombres.', '// _ dans nombres : purement visuel, ignoré par JS'),

# Promise.allSettled vs all
('JS', 'Promise.allSettled() différence', 'Comportement si 1 échoue ?', 'Promise.allSettled([p1, p2, p3])\nPromise.all([p1, p2, p3])', ['allSettled attend toutes | all reject si 1 fail', 'Pareil', 'all attend toutes', 'Aucune'], 0, 'allSettled attend toutes | all reject si 1 fail', 'Promise.all() reject dès qu\'une promise échoue.\nPromise.allSettled() attend TOUTES les promises (success ou fail).\nRetourne { status, value/reason } pour chacune.', '// all : fail fast | allSettled : attend toutes'),

# Promise.any vs race
('JS', 'Promise.any() comportement', 'Différence avec race() ?', 'Promise.any([p1, p2, p3])\nPromise.race([p1, p2, p3])', ['any : 1ère réussie | race : 1ère terminée', 'Pareil', 'any plus rapide', 'Aucune'], 0, 'any : 1ère réussie | race : 1ère terminée', 'Promise.race() retourne la PREMIÈRE terminée (resolve ou reject).\nPromise.any() retourne la PREMIÈRE réussie (ignore les rejets).\nany() reject seulement si TOUTES échouent (AggregateError).', '// race : 1ère finie | any : 1ère réussie'),

# String.matchAll
('JS', 'String.matchAll()', 'Retourne quoi ?', 'const str = "test1 test2"\nconst matches = str.matchAll(/test(\\d)/g)\nconsole.log(matches)', ['Iterator', 'Array', 'null', 'String'], 0, 'Iterator', 'matchAll() retourne un ITERATOR de matches (pas un array).\nUtile pour capturer tous les groupes de toutes les correspondances.\nNécessite le flag g (global).', '// matchAll : iterator de matches avec groupes (nécessite /g)'),

# Array.at negative
('JS', 'Array.at() indices négatifs', 'Différence avec [] ?', 'const arr = [1, 2, 3]\nconsole.log(arr.at(-1))\nconsole.log(arr[-1])', ['3 / undefined', 'undefined / 3', '3 / 3', 'Error'], 0, '3 / undefined', 'at(-1) accède au dernier élément (indices négatifs depuis la fin).\narr[-1] cherche la propriété "-1" → undefined.\nat() est plus intuitif pour indices négatifs.', '// at(-n) : depuis la fin | [-n] : propriété string'),

# Object.hasOwn
('JS', 'Object.hasOwn() vs hasOwnProperty', 'Pourquoi hasOwn() ?', 'const obj = { a: 1 }\nObject.hasOwn(obj, "a")\nobj.hasOwnProperty("a")', ['Même résultat, hasOwn plus sûr', 'hasOwn plus rapide', 'Différent', 'Aucune'], 0, 'Même résultat, hasOwn plus sûr', 'hasOwnProperty() peut être overridden sur l\'objet.\nObject.hasOwn() est une méthode statique → plus fiable.\nC\'est la méthode recommandée maintenant.', '// Object.hasOwn(obj, key) > obj.hasOwnProperty(key)'),

# Error.cause
('JS', 'Error.cause chaînage', 'Utilité ?', 'try {\n  // ...\n} catch (err) {\n  throw new Error("Failed", { cause: err })\n}', ['Chaîner erreurs', 'Debug plus facile', 'Traçabilité', 'Tout ça'], 3, 'Tout ça', 'Error.cause permet de chaîner les erreurs (error wrapping).\nGarde le contexte de l\'erreur originale.\nFacilite le debugging et la traçabilité.', '// Error(msg, { cause }) : chaînage erreurs'),

# Temporal API
('JS', 'Temporal API futur', 'Remplacement de Date ?', 'const now = Temporal.Now.plainDateTimeISO()\nconsole.log(now.year)', ['Oui, plus moderne', 'Non, obsolète', 'Pareil que Date', 'Aucun'], 0, 'Oui, plus moderne', 'Temporal est la future API pour dates/heures (stage 3).\nCorrige tous les problèmes de Date (immutable, timezone, précis).\nPas encore standard, mais bientôt.', '// Temporal : future API dates (immutable, timezone, précis)'),

# Pattern matching proposal
('JS', 'Pattern matching proposition', 'Syntaxe future ?', 'match (value) {\n  when 1: return "one"\n  when 2: return "two"\n  default: return "other"\n}', ['Stage 1 proposal', 'Déjà standard', 'Abandonné', 'Aucun'], 0, 'Stage 1 proposal', 'Pattern matching est une proposition TC39 (stage 1).\nComme switch mais plus puissant (destructuring, guards).\nPas encore disponible, à suivre.', '// Pattern matching : stage 1, comme switch++'),

# Records & Tuples
('JS', 'Records & Tuples', 'Immutabilité profonde ?', 'const rec = #{ a: 1, b: 2 }\nconst tup = #[1, 2, 3]', ['Proposition immutables', 'Déjà standard', 'Syntaxe invalide', 'Aucun'], 0, 'Proposition immutables', 'Records (#{ }) et Tuples (#[ ]) sont des structures immutables.\nProposition TC39 (stage 2).\nComparaison par valeur (pas par référence).', '// Records/Tuples : immutables, comparison par valeur (stage 2)'),

]

# ============================================================================
# QUIZZES ALGORITHMIQUES - 101 NOUVEAUX
# ============================================================================

# PHASE 1 - NOUVEAUX QUIZZES ALGO (25 quizzes)
NEW_ALGO_PHASE1 = [

# Linear vs Binary search
('ALGO', 'Linear vs Binary', 'Quelle recherche en O(log n) ?', 'arr = [1, 3, 5, 7, 9]\n# A: parcourir tous\n# B: diviser par 2', ['Linear O(n)', 'Binary O(log n)', 'Les deux O(n)', 'Les deux O(log n)'], 1, 'Binary O(log n)', 'Binary search divise par 2 à chaque étape → O(log n).\nLinear search parcourt tous les éléments → O(n).\nMAIS binary search nécessite un tableau TRIÉ.', '// Binary : O(log n) mais nécessite tri | Linear : O(n) toujours'),

# Selection sort
('ALGO', 'Selection Sort', 'Comment fonctionne selection sort ?', 'Trouver le min, placer au début\nRépéter pour sous-tableau restant', ['O(n²) toujours', 'O(n log n)', 'O(n)', 'Dépend'], 0, 'O(n²) toujours', 'Selection sort trouve le minimum et le place au début.\nPour chaque position, parcourt le reste → O(n²).\nMême si déjà trié, parcourt toujours tout.', '// Selection sort : O(n²) toujours, pas adaptatif'),

# Recursion base case
('ALGO', 'Récursion base case', 'Sans base case, que se passe-t-il ?', 'function recurse(n) {\n  return recurse(n-1)\n}', ['Stack overflow', 'Boucle infinie', 'Erreur', 'Dépend'], 0, 'Stack overflow', 'Sans cas de base, la récursion ne s\'arrête jamais.\nChaque appel empile un frame → stack overflow.\nToujours définir un cas de base clair.', '// Récursion : base case OBLIGATOIRE (sinon stack overflow)'),

# Recursion stack visualization
('ALGO', 'Stack récursif', 'Ordre d\'exécution ?', 'function f(n) {\n  if (n === 0) return\n  console.log(n)\n  f(n-1)\n  console.log(n)\n}\nf(3)', ['3 2 1 1 2 3', '3 2 1', '1 2 3 3 2 1', '1 2 3'], 0, '3 2 1 1 2 3', 'Empile 3, 2, 1. À 0, remonte.\nDépile : 1, 2, 3.\nAffiche à l\'aller ET au retour.', '// Récursion : aller (descente) puis retour (remontée)'),

# Quicksort pivot
('ALGO', 'Quicksort pivot optimal', 'Quel pivot pour éviter O(n²) ?', 'arr déjà trié, pivot = premier élément', ['Médian des 3', 'Aléatoire', 'Milieu', 'Toutes sauf premier'], 3, 'Toutes sauf premier', 'Si pivot = premier sur tableau trié → pire cas O(n²).\nMédian-of-3, aléatoire, ou milieu évitent ce problème.\nPivot aléatoire garantit O(n log n) en moyenne.', '// Quicksort : éviter premier/dernier sur tableaux triés'),

# Arrays vs Linked Lists
('ALGO', 'Array vs Linked List', 'Accès par index ?', 'arr[i] vs list.get(i)', ['Array O(1) | List O(n)', 'Array O(n) | List O(1)', 'Les deux O(1)', 'Les deux O(n)'], 0, 'Array O(1) | List O(n)', 'Array : accès direct par index → O(1).\nLinked List : parcourir depuis head → O(n).\nMais insertion/suppression en tête : List O(1), Array O(n).', '// Array : accès O(1), insert O(n) | List : accès O(n), insert O(1)'),

# Hash collisions
('ALGO', 'Hash table collisions', 'Gestion des collisions ?', 'Deux clés ont le même hash', ['Chaining (liste)', 'Open addressing', 'Les deux', 'Impossible'], 2, 'Les deux', 'Chaining : chaque bucket est une liste.\nOpen addressing : chercher le prochain slot libre.\nLes deux méthodes sont valides, trade-offs différents.', '// Collisions : chaining (listes) ou open addressing (probe)'),

# Hash function properties
('ALGO', 'Bonne fonction hash', 'Propriété essentielle ?', 'Même input → même hash\nDifférents inputs → différents hashs (si possible)', ['Déterministe', 'Distribution uniforme', 'Rapide', 'Tout ça'], 3, 'Tout ça', 'Une bonne hash function :\n• Déterministe (même input → même hash).\n• Distribution uniforme (évite collisions).\n• Rapide à calculer.', '// Hash : déterministe + uniforme + rapide'),

# Load factor
('ALGO', 'Load factor hash table', 'Quand resize ?', 'load_factor = n / capacity\nSi > 0.75, resize', ['Trop de collisions', 'Performance dégradée', 'Resize à 2x capacity', 'Tout ça'], 3, 'Tout ça', 'Load factor = nombre éléments / capacité.\nSi trop élevé → trop de collisions → resize (souvent 2x).\nTrade-off mémoire vs performance.', '// Load factor > 0.75 : resize pour maintenir O(1)'),

# Best/Worst/Average case
('ALGO', 'Best vs Worst case', 'Quicksort pire cas ?', 'Pivot toujours min/max', ['O(n log n)', 'O(n²)', 'O(n)', 'O(log n)'], 1, 'O(n²)', 'Quicksort pire cas : pivot toujours min/max → partitions déséquilibrées.\nO(n²) si tableau déjà trié et pivot = premier.\nMoyenne : O(n log n).', '// Quicksort : avg O(n log n) | worst O(n²)'),

# Asymptotic notation
('ALGO', 'O vs Ω vs Θ', 'Quelle notation pour borne exacte ?', 'O = borne sup\nΩ = borne inf\nΘ = borne exacte', ['O', 'Ω', 'Θ', 'Aucune'], 2, 'Θ', 'O (big-O) = borne supérieure (pire cas ou plus).\nΩ (omega) = borne inférieure (meilleur cas ou plus).\nΘ (theta) = borne exacte (tight bound).', '// O : ≤ | Ω : ≥ | Θ : ='),

# Loop complexity
('ALGO', 'Boucles imbriquées', 'Complexité ?', 'for i in range(n):\n  for j in range(i, n):\n    print(i, j)', ['O(n)', 'O(n²)', 'O(n log n)', 'O(2n)'], 1, 'O(n²)', 'Boucle externe : n itérations.\nBoucle interne : moyenne n/2 itérations.\nn * n/2 = O(n²) (constantes ignorées).', '// Boucles imbriquées : multiplier les itérations'),

# Recurrence relations
('ALGO', 'Relation de récurrence', 'T(n) = 2T(n/2) + n', ['O(n)', 'O(n log n)', 'O(n²)', 'O(log n)'], 1, 'O(n log n)', 'C\'est la récurrence de merge sort.\nMaster theorem : a=2, b=2, f(n)=n → cas 2 → O(n log n).\nDivise par 2, combine en O(n) par niveau.', '// T(n) = 2T(n/2) + n : merge sort = O(n log n)'),

# Master theorem
('ALGO', 'Master theorem', 'T(n) = T(n/2) + O(1)', ['O(n)', 'O(log n)', 'O(n log n)', 'O(1)'], 1, 'O(log n)', 'Divise par 2, travail constant par niveau.\nProfondeur log n, travail O(1) par niveau → O(log n).\nExemple : binary search.', '// T(n) = T(n/2) + O(1) : binary search = O(log n)'),

# Insertion sort analysis
('ALGO', 'Insertion sort complexité', 'Meilleur cas ?', 'Tableau déjà trié', ['O(n)', 'O(n²)', 'O(n log n)', 'O(log n)'], 0, 'O(n)', 'Si déjà trié, chaque élément est déjà à sa place.\nUne seule comparaison par élément → O(n).\nPire cas (inversé) → O(n²).', '// Insertion sort : best O(n) | avg/worst O(n²)'),

# Merge sort proof
('ALGO', 'Merge sort toujours', 'Complexité garantie ?', 'Quel que soit l\'input', ['O(n log n)', 'O(n²)', 'Dépend', 'O(n)'], 0, 'O(n log n)', 'Merge sort divise TOUJOURS par 2 (log n niveaux).\nMerge TOUJOURS en O(n) par niveau.\nDonc O(n log n) garanti, même pire cas.', '// Merge sort : O(n log n) TOUJOURS (stable, prévisible)'),

# Contains Duplicate
('ALGO', 'Contains Duplicate', 'Approche optimale ?', 'nums = [1,2,3,1]\nTrouver si duplicate', ['Hash set O(n)', 'Tri puis compare O(n log n)', 'Deux boucles O(n²)', 'Hash set'], 3, 'Hash set', 'Hash set : ajouter en parcourant, si déjà présent → duplicate.\nO(n) temps, O(n) espace.\nTri marche aussi mais O(n log n).', '// Duplicate detection : hash set = O(n) optimal'),

# Valid Anagram
('ALGO', 'Anagram validation', 'Méthode efficace ?', 's = "anagram"\nt = "nagaram"', ['Trier les deux O(n log n)', 'Frequency map O(n)', 'Les deux valides', 'Map plus rapide'], 2, 'Les deux valides', 'Méthode 1 : trier et comparer → O(n log n).\nMéthode 2 : compter fréquences → O(n).\nMap est optimal en temps.', '// Anagram : frequency map O(n) > sort O(n log n)'),

# Two Sum
('ALGO', 'Two Sum optimal', 'Trouver 2 nombres = target', 'nums = [2,7,11,15]\ntarget = 9', ['Hash map one-pass', 'Deux boucles', 'Tri + two pointers', 'Hash map'], 3, 'Hash map', 'Hash map : stocker {valeur: index} en parcourant.\nPour chaque num, chercher target-num dans map.\nO(n) temps, O(n) espace.', '// Two Sum : hash map one-pass = O(n)'),

# Best Time Stock
('ALGO', 'Stock profit max', 'Stratégie optimale ?', 'prices = [7,1,5,3,6,4]\nMax profit ?', ['Track min, calc profit', 'Tous les pairs', 'Tri', 'Min puis max'], 0, 'Track min, calc profit', 'Garder le prix min vu jusqu\'ici.\nCalculer profit si on vend aujourd\'hui.\nO(n) un seul passage.', '// Stock : track min + calc max profit = O(n)'),

# Valid Parentheses
('ALGO', 'Parenthèses valides', 'Structure optimale ?', 's = "([{}])"', ['Stack', 'Counter', 'Regex', 'Deux pointeurs'], 0, 'Stack', 'Stack : push ouvrante, pop fermante.\nVérifier que pop correspond.\nO(n) temps, O(n) espace (stack).', '// Parenthèses : stack pour matching = O(n)'),

# Kadane intro
('ALGO', 'Maximum Subarray', 'Sous-tableau somme max', 'nums = [-2,1,-3,4,-1,2,1,-5,4]', ['Kadane O(n)', 'Brute force O(n²)', 'Divide & conquer O(n log n)', 'Kadane optimal'], 3, 'Kadane optimal', 'Kadane : max_current = max(num, max_current + num).\nO(n) un seul passage.\nMeilleur que brute force O(n²).', '// Kadane : sous-tableau max en O(n)'),

# Merge Sorted Lists
('ALGO', 'Merge 2 listes triées', 'Approche efficace ?', 'l1 = 1→2→4\nl2 = 1→3→4', ['Two pointers', 'Concat puis tri', 'Récursion', 'Two pointers optimal'], 3, 'Two pointers optimal', 'Deux pointeurs : comparer têtes, avancer le plus petit.\nO(n+m) temps, O(1) espace (in-place si modif pointeurs).\nRécursion marche aussi mais stack O(n).', '// Merge lists : two pointers = O(n+m)'),

# Reverse Linked List
('ALGO', 'Reverse liste itératif', 'Complexité optimale ?', '1→2→3→4→5', ['O(n) temps O(1) espace', 'O(n²)', 'O(n) temps O(n) espace', 'Impossible O(1)'], 0, 'O(n) temps O(1) espace', 'Itératif : 3 pointeurs (prev, curr, next).\nInverser les liens en parcourant.\nO(n) temps, O(1) espace.', '// Reverse list itératif : O(n) temps, O(1) espace'),

# Climbing Stairs
('ALGO', 'Climbing Stairs pattern', 'Reconnaître le pattern', 'n = 5 marches\n1 ou 2 marches à la fois', ['Fibonacci', 'Factorielle', 'Exponentielle', 'Linéaire'], 0, 'Fibonacci', 'f(n) = f(n-1) + f(n-2).\nC\'est exactement Fibonacci.\nDP ou itératif : O(n) temps.', '// Stairs : Fibonacci déguisé = DP O(n)'),

]

# PHASE 2 - NOUVEAUX QUIZZES ALGO (25 quizzes)
NEW_ALGO_PHASE2 = [

# 3Sum
('ALGO', '3Sum two pointers', 'Extension de Two Sum', 'nums = [-1,0,1,2,-1,-4]\nTrouver triplets = 0', ['Sort + two pointers O(n²)', 'Brute force O(n³)', 'Hash O(n²) espace', 'Sort optimal'], 3, 'Sort optimal', 'Trier, puis pour chaque num, Two Sum sur le reste.\nO(n²) temps, O(1) espace (hors tri).\nÉviter duplicates avec skip.', '// 3Sum : sort + two pointers = O(n²)'),

# Container Most Water
('ALGO', 'Container With Water', 'Two pointers stratégie', 'height = [1,8,6,2,5,4,8,3,7]', ['Two pointers gauche/droite', 'Brute force', 'Stack', 'Two pointers optimal'], 3, 'Two pointers optimal', 'Pointeurs aux extrémités, déplacer le plus petit.\nLargeur diminue → il faut augmenter hauteur.\nO(n) un seul passage.', '// Container : two pointers (déplacer min) = O(n)'),

# Longest Substring
('ALGO', 'Longest Substring Unique', 'Sliding window pattern', 's = "abcabcbb"', ['Sliding window + hash set', 'Brute force', 'Two pointers', 'Window optimal'], 3, 'Window optimal', 'Sliding window : étendre à droite, rétrécir si duplicate.\nHash set pour tracker caractères dans fenêtre.\nO(n) temps.', '// Longest substring : sliding window + set = O(n)'),

# Minimum Window
('ALGO', 'Minimum Window Substring', 'Pattern avancé', 's = "ADOBECODEBANC"\nt = "ABC"', ['Sliding window + freq map', 'Brute force', 'Two pointers', 'Window complexe'], 3, 'Window complexe', 'Window : étendre jusqu\'à contenir t, rétrécir pour minimiser.\nFrequency maps pour s et t.\nO(n+m) temps.', '// Min window : sliding window + 2 freq maps = O(n+m)'),

# Group Anagrams
('ALGO', 'Group Anagrams', 'Clé de groupement', 'strs = ["eat","tea","tan","ate","nat","bat"]', ['Sort comme clé', 'Count array clé', 'Les deux', 'Count plus rapide'], 2, 'Les deux', 'Méthode 1 : sort string comme clé → O(n * k log k).\nMéthode 2 : count array (26 lettres) → O(n * k).\nLes deux valides.', '// Group anagrams : sort ou count array comme clé de hash'),

# Product Except Self
('ALGO', 'Product Array Except Self', 'Sans division', 'nums = [1,2,3,4]', ['Prefix/suffix products', 'Division par total', 'Brute force', 'Prefix optimal'], 3, 'Prefix optimal', 'Prefix products de gauche, suffix de droite.\nresult[i] = prefix[i-1] * suffix[i+1].\nO(n) temps, O(1) espace (hors result).', '// Product except self : prefix * suffix = O(n)'),

# Rotate Array
('ALGO', 'Rotate Array trick', 'Rotate k positions', 'nums = [1,2,3,4,5,6,7]\nk = 3', ['Reverse 3 fois', 'Brute force shift', 'Extra array', 'Reverse optimal'], 3, 'Reverse optimal', 'Reverse tout, reverse [0, k-1], reverse [k, n-1].\nO(n) temps, O(1) espace.\nAstuce élégante.', '// Rotate : reverse 3x (tout, gauche, droite) = O(n) O(1)'),

# Spiral Matrix
('ALGO', 'Spiral Matrix traversal', 'Pattern de parcours', 'matrix 3x3', ['4 directions avec bounds', 'Récursion', 'Stack', 'Directions optimal'], 3, 'Directions optimal', 'Droite → bas → gauche → haut.\nRéduire bounds après chaque direction.\nO(m*n) temps.', '// Spiral : 4 directions + shrink bounds = O(m*n)'),

# Set Matrix Zeroes
('ALGO', 'Set Matrix Zeroes in-place', 'Marquage sans espace', 'Si cell = 0, row/col = 0', ['Utiliser 1ère row/col', 'Extra array', 'Impossible in-place', 'First row/col optimal'], 3, 'First row/col optimal', 'Utiliser 1ère ligne et colonne comme marqueurs.\nO(m*n) temps, O(1) espace.\nAttention à l\'ordre de traitement.', '// Matrix zeroes : first row/col as markers = O(1) space'),

# Word Search
('ALGO', 'Word Search backtracking', 'DFS avec retour arrière', 'board + word = "ABCCED"', ['DFS + backtracking', 'BFS', 'Dynamic programming', 'DFS optimal'], 3, 'DFS optimal', 'DFS depuis chaque cellule, backtrack si chemin invalide.\nMarquer visité puis unmark (backtrack).\nO(m*n*4^L) pire cas.', '// Word search : DFS + backtrack + visited marking'),

# Combination Sum
('ALGO', 'Combination Sum', 'Backtracking avec réutilisation', 'candidates = [2,3,6,7]\ntarget = 7', ['Backtracking récursif', 'DP', 'Greedy', 'Backtracking optimal'], 3, 'Backtracking optimal', 'Backtracking : inclure current (peut réutiliser) ou skip.\nBase case : sum = target.\nO(2^target) complexité.', '// Combination sum : backtracking avec réutilisation'),

# Permutations
('ALGO', 'Permutations génération', 'Toutes les permutations', 'nums = [1,2,3]', ['Backtracking swap', 'DP', 'Itératif', 'Backtracking optimal'], 3, 'Backtracking optimal', 'Backtracking : swap current avec chaque suivant.\nRécursion, puis swap back (backtrack).\nO(n! * n) temps.', '// Permutations : backtracking + swap = O(n!)'),

# Subsets
('ALGO', 'Subsets génération', 'Tous les sous-ensembles', 'nums = [1,2,3]', ['Backtracking ou bit mask', 'DP', 'Itératif', 'Les deux valides'], 3, 'Les deux valides', 'Backtracking : inclure ou exclure chaque élément.\nBit mask : chaque bit = inclus/exclus.\nO(2^n * n) temps.', '// Subsets : backtracking ou bitmask = O(2^n)'),

# Course Schedule
('ALGO', 'Course Schedule cycle', 'Détection cycle graphe', 'prereq = [[1,0], [0,1]]', ['DFS + 3 states', 'BFS topological', 'Les deux', 'DFS optimal'], 2, 'Les deux', 'DFS : 3 états (unvisited, visiting, visited) pour cycle.\nOu Kahn (BFS topological) : si indegree > 0 à la fin → cycle.\nLes deux O(V+E).', '// Cycle detection : DFS 3-color ou Kahn topological'),

# Number of Islands
('ALGO', 'Number of Islands', 'Composantes connexes', 'grid 2D de 1s et 0s', ['DFS ou BFS pour marquer', 'Union-Find', 'Les deux', 'DFS/BFS optimal'], 3, 'DFS/BFS optimal', 'Parcourir grid, pour chaque 1 non visité : DFS/BFS pour marquer île.\nCompter le nombre de DFS lancés.\nO(m*n) temps.', '// Islands : DFS/BFS pour composantes = O(m*n)'),

# Clone Graph
('ALGO', 'Clone Graph', 'Deep copy graphe', 'node avec neighbors', ['DFS/BFS + hash map', 'Récursion simple', 'Impossible', 'Hash map essentiel'], 3, 'Hash map essentiel', 'Hash map {original: clone} pour éviter cycles.\nDFS/BFS : cloner node, puis neighbors récursivement.\nO(V+E) temps.', '// Clone graph : DFS/BFS + hash map (old→new)'),

# BFS implementation
('ALGO', 'BFS avec queue', 'Implémentation correcte', 'graph traversal', ['Queue FIFO', 'Stack LIFO', 'Récursion', 'Queue obligatoire'], 3, 'Queue obligatoire', 'BFS utilise une QUEUE (FIFO) pour niveau par niveau.\nDFS utilise STACK (LIFO) ou récursion.\nO(V+E) temps.', '// BFS : queue FIFO | DFS : stack/recursion'),

# Dijkstra shortest path
('ALGO', 'Dijkstra algorithme', 'Plus court chemin pondéré', 'graph avec poids positifs', ['Priority queue (min heap)', 'BFS simple', 'DFS', 'Heap essentiel'], 3, 'Heap essentiel', 'Dijkstra : priority queue pour toujours traiter le nœud le plus proche.\nRelaxation des arêtes.\nO((V+E) log V) avec heap.', '// Dijkstra : min heap + relaxation = O((V+E) log V)'),

# Weighted vs unweighted
('ALGO', 'Graphes pondérés vs non', 'Algorithme approprié', 'Poids tous = 1 vs variés', ['BFS si unweighted | Dijkstra si weighted', 'Dijkstra toujours', 'BFS toujours', 'Adapter selon poids'], 0, 'BFS si unweighted | Dijkstra si weighted', 'BFS trouve le plus court chemin si poids = 1 (ou tous égaux).\nSi poids variés, BFS ne marche pas → Dijkstra ou Bellman-Ford.\nO(V+E) vs O((V+E) log V).', '// Unweighted : BFS O(V+E) | Weighted : Dijkstra O((V+E) log V)'),

# Greedy characteristics
('ALGO', 'Greedy algorithme', 'Propriété requise', 'Choix localement optimal', ['Optimal substructure', 'Greedy choice property', 'Les deux', 'Aucune garantie'], 2, 'Les deux', 'Greedy nécessite :\n1. Optimal substructure.\n2. Greedy choice property (choix local → optimal global).\nPas toujours correct (ex: change monnaie arbitraire).', '// Greedy : optimal substructure + greedy choice property'),

# DP memoization
('ALGO', 'DP memoization', 'Top-down approche', 'fibonacci(n)', ['Récursion + cache', 'Itératif', 'Les deux DP', 'Memo = top-down'], 3, 'Memo = top-down', 'Memoization = top-down : récursion + cache des résultats.\nÉvite recalcul des sous-problèmes.\nO(n) au lieu de O(2^n) pour fib.', '// Memoization : top-down récursif + cache'),

# DP bottom-up
('ALGO', 'DP bottom-up', 'Approche itérative', 'fibonacci(n)', ['Itératif tableau', 'Récursion', 'Les deux DP', 'Bottom-up = itératif'], 3, 'Bottom-up = itératif', 'Bottom-up = itératif : tableau, remplir de bas en haut.\nPas de récursion, pas de stack overflow.\nO(n) temps, souvent O(1) espace optimisable.', '// Bottom-up : itératif + tableau (ou variables)'),

# Knapsack 0/1
('ALGO', 'Knapsack 0/1', 'Prendre ou ne pas prendre', 'items avec poids/valeur', ['DP[i][w] = max(take, skip)', 'Greedy', 'Backtracking', 'DP optimal'], 3, 'DP optimal', 'DP : pour chaque item, max(prendre, skip).\nÉtat : DP[i][w] = valeur max avec i items, poids w.\nO(n*W) temps pseudo-polynomial.', '// Knapsack 0/1 : DP max(take, skip) = O(n*W)'),

# Longest Common Subsequence
('ALGO', 'LCS dynamic programming', 'Sous-séquence commune max', 's1 = "abcde"\ns2 = "ace"', ['DP[i][j] = LCS(s1[:i], s2[:j])', 'Greedy', 'Two pointers', 'DP optimal'], 3, 'DP optimal', 'DP : si s1[i] == s2[j], DP[i][j] = DP[i-1][j-1] + 1.\nSinon, max(DP[i-1][j], DP[i][j-1]).\nO(n*m) temps.', '// LCS : DP avec match/skip = O(n*m)'),

# Queue for BFS
('ALGO', 'Queue BFS nécessaire', 'Pourquoi queue ?', 'Parcours niveau par niveau', ['FIFO garantit ordre', 'Plus rapide', 'Stack marche aussi', 'FIFO essentiel'], 3, 'FIFO essentiel', 'Queue (FIFO) assure qu\'on traite les nœuds niveau par niveau.\nStack (LIFO) donnerait DFS, pas BFS.\nL\'ordre est essentiel pour BFS.', '// BFS : queue FIFO pour ordre niveau par niveau'),

]

# PHASE 3 - NOUVEAUX QUIZZES ALGO (24 quizzes)
NEW_ALGO_PHASE3 = [

# BST properties
('ALGO', 'BST propriété', 'Binary Search Tree invariant', 'Gauche < root < Droite', ['Récursivement pour tout nœud', 'Seulement root', 'Seulement feuilles', 'Tout nœud'], 3, 'Récursivement pour tout nœud', 'BST : pour CHAQUE nœud, gauche < nœud < droite.\nRécursivement dans tout l\'arbre.\nPermet recherche O(log n) si équilibré.', '// BST : gauche < node < droite PARTOUT'),

# AVL rotations
('ALGO', 'AVL tree rotations', 'Pourquoi rotations ?', 'Maintenir équilibre', ['Hauteur diff ≤ 1', 'Performance O(log n)', 'Les deux', 'Équilibre optimal'], 2, 'Les deux', 'AVL : |hauteur(gauche) - hauteur(droite)| ≤ 1.\nRotations (simple/double) pour rééquilibrer après insert/delete.\nGarantit O(log n) pour toutes opérations.', '// AVL : rotations pour |balance| ≤ 1 → O(log n) garanti'),

# Red-Black invariants
('ALGO', 'Red-Black tree règles', 'Propriétés à maintenir', '5 invariants', ['Root noir', 'Pas 2 rouges consécutifs', 'Chemins noirs égaux', 'Tout ça'], 3, 'Tout ça', 'Red-Black :\n1. Root noir.\n2. Feuilles (NIL) noires.\n3. Rouge → enfants noirs.\n4. Tous chemins ont même nombre de nœuds noirs.\n5. Nouveau nœud = rouge.', '// RB-tree : 5 invariants → O(log n) garanti'),

# B-tree databases
('ALGO', 'B-tree pour DB', 'Avantage sur BST ?', 'Disque vs mémoire', ['Moins d\'accès disque', 'Nœuds avec multiple clés', 'Hauteur minimale', 'Tout ça'], 3, 'Tout ça', 'B-tree : nœuds avec plusieurs clés (ex: 100-1000).\nHauteur très faible → moins d\'I/O disque.\nUtilisé par MySQL, PostgreSQL, etc.', '// B-tree : multi-keys/node → faible hauteur → optimal pour disque'),

# Heap property
('ALGO', 'Min-heap propriété', 'Invariant à maintenir', 'Parent ≤ enfants', ['Récursivement', 'Seulement root', 'Arbre complet aussi', 'Les deux'], 3, 'Les deux', 'Min-heap :\n1. Parent ≤ enfants (partout).\n2. Arbre complet (rempli gauche→droite).\nMax-heap : parent ≥ enfants.', '// Heap : parent ≤ enfants + arbre complet'),

# Heapify operation
('ALGO', 'Heapify complexité', 'Construire heap', 'array → heap', ['O(n log n)', 'O(n)', 'O(log n)', 'O(n) optimal'], 3, 'O(n) optimal', 'Heapify bottom-up : O(n), pas O(n log n).\nMajorité des nœuds sont en bas (peu de bubbling).\nAnalyse mathématique : somme série géométrique.', '// Heapify : O(n) bottom-up, pas O(n log n)'),

# Priority queue
('ALGO', 'Priority queue implémentation', 'Structure optimale', 'insert + extractMin', ['Min-heap', 'Sorted array', 'Unsorted array', 'Heap optimal'], 3, 'Heap optimal', 'Heap : insert O(log n), extractMin O(log n).\nSorted array : insert O(n), extract O(1).\nHeap est le meilleur compromis.', '// Priority queue : heap = insert O(log n) + extract O(log n)'),

# Disjoint Set Union
('ALGO', 'DSU Union-Find', 'Composantes disjointes', 'union + find operations', ['Path compression', 'Union by rank', 'Les deux', 'Optimisations essentielles'], 3, 'Optimisations essentielles', 'DSU basique : O(n) pire cas.\nPath compression : flatten tree lors de find.\nUnion by rank : attacher petit arbre au grand.\nEnsemble → quasi O(1) (α(n) ≈ constant).', '// DSU : path compression + union by rank = quasi O(1)'),

# Union by rank
('ALGO', 'Union by rank', 'Pourquoi rank ?', 'Éviter arbres déséquilibrés', ['Hauteur minimale', 'Performance', 'Les deux', 'Équilibre optimal'], 2, 'Les deux', 'Union by rank : toujours attacher arbre moins profond au plus profond.\nÉvite dégénérescence en liste liée.\nCombine avec path compression → α(n).', '// Union by rank : attach shallow to deep → hauteur O(log n)'),

# Path compression
('ALGO', 'Path compression DSU', 'Optimisation find', 'Flatten chemin vers root', ['Tous pointent root direct', 'Amortized O(1)', 'Les deux', 'Flatten essentiel'], 2, 'Les deux', 'Path compression : lors de find(x), faire pointer tous nœuds vers root.\nProchains find sont O(1).\nAmortized quasi-constant.', '// Path compression : flatten on find → amortized O(1)'),

# Binary Tree Max Path
('ALGO', 'Binary Tree Max Path Sum', 'DFS avec max global', 'Chemin max peut ignorer root', ['DFS return max single path', 'Greedy', 'DP', 'DFS complexe'], 3, 'DFS complexe', 'DFS : pour chaque nœud, max path = node + max(left, 0) + max(right, 0).\nRetourner max single branch pour parent.\nO(n) temps.', '// Max path : DFS return single, update global avec both'),

# Serialize Binary Tree
('ALGO', 'Serialize Tree', 'Préserver structure', 'tree → string → tree', ['Preorder + null markers', 'Inorder seul insuffisant', 'BFS level-order', 'Preorder optimal'], 3, 'Preorder optimal', 'Preorder avec marqueurs null (ex: "#") préserve structure.\nInorder seul ne suffit pas (ambiguïté).\nDeserialize : récursion avec queue.', '// Serialize : preorder + null markers = structure préservée'),

# Word Ladder BFS
('ALGO', 'Word Ladder', 'Shortest transformation', 'beginWord → endWord\n1 lettre à la fois', ['BFS shortest path', 'DFS', 'Dijkstra', 'BFS optimal'], 3, 'BFS optimal', 'BFS : chaque niveau = 1 transformation.\nTrouver shortest path dans graphe de mots.\nO(M² * N) avec M = longueur mot, N = nb mots.', '// Word ladder : BFS = shortest path in word graph'),

# Alien Dictionary
('ALGO', 'Alien Dictionary', 'Ordre des lettres', 'words sorted in alien order', ['Topological sort', 'DFS ou Kahn', 'Graphe orienté', 'Tout ça'], 3, 'Tout ça', 'Construire graphe : edges = ordre entre lettres.\nTopological sort (DFS ou Kahn) pour ordre total.\nO(C) avec C = nb total de caractères.', '// Alien dict : build graph + topological sort'),

# Merge K Lists
('ALGO', 'Merge K Sorted Lists', 'Efficace pour K listes', 'k listes triées', ['Min-heap de K éléments', 'Merge 2 à 2', 'Les deux', 'Heap optimal'], 3, 'Heap optimal', 'Heap : garder K têtes, extract min et ajouter next.\nO(N log K) avec N = total éléments.\nMerge 2 à 2 : O(N log K) aussi.', '// Merge K : min-heap = O(N log K)'),

# Median from Stream
('ALGO', 'Median Data Stream', '2 heaps pattern', 'addNum + findMedian', ['Max-heap (low) + Min-heap (high)', 'Sorted array', 'BST', 'Two heaps optimal'], 3, 'Two heaps optimal', 'Max-heap pour moitié basse, min-heap pour moitié haute.\nÉquilibrer tailles : diff ≤ 1.\nMedian = top d\'un heap ou moyenne des 2 tops.', '// Median stream : max-heap (low) + min-heap (high)'),

# Sliding Window Max
('ALGO', 'Sliding Window Maximum', 'Deque pattern', 'Max de chaque fenêtre', ['Monotonic decreasing deque', 'Heap', 'BST', 'Deque optimal'], 3, 'Deque optimal', 'Deque : garder indices en ordre décroissant de valeurs.\nFront = max, retirer éléments hors fenêtre et < current.\nO(n) temps.', '// Sliding max : monotonic deque = O(n)'),

# Longest Increasing Subsequence
('ALGO', 'LIS optimal', 'Subsequence croissante max', 'nums = [10,9,2,5,3,7,101,18]', ['DP O(n²) ou Binary Search O(n log n)', 'Greedy', 'Backtracking', 'Binary search optimal'], 3, 'Binary search optimal', 'DP : O(n²).\nOptimal : maintenir tableau tails, binary search pour update.\nO(n log n) temps, O(n) espace.', '// LIS : DP O(n²) | Binary search O(n log n) optimal'),

# Edit Distance
('ALGO', 'Edit Distance Levenshtein', 'Min opérations (insert/delete/replace)', 'word1 → word2', ['DP[i][j] = min(insert, delete, replace)', 'Greedy', 'BFS', 'DP optimal'], 3, 'DP optimal', 'DP : si chars match, DP[i][j] = DP[i-1][j-1].\nSinon, min(insert, delete, replace) + 1.\nO(n*m) temps.', '// Edit distance : DP min(3 ops) = O(n*m)'),

# Regex Matching DP
('ALGO', 'Regex Matching DP', '. et * wildcards', 's = "aa"\np = "a*"', ['DP[i][j] = match(s[:i], p[:j])', 'Greedy', 'Backtracking', 'DP complexe'], 3, 'DP complexe', 'DP : . = match any, * = 0+ du précédent.\nÉtats complexes avec * (0 ou 1+ match).\nO(n*m) temps.', '// Regex DP : . et * = états complexes = O(n*m)'),

# Burst Balloons
('ALGO', 'Burst Balloons DP', 'Max coins ordre optimal', 'Burst order matters', ['DP interval', 'Greedy', 'Backtracking', 'DP interval'], 3, 'DP interval', 'DP : considérer dernier ballon éclaté dans intervalle [i, j].\nDP[i][j] = max coins pour intervalle.\nO(n³) temps.', '// Burst balloons : interval DP (dernier éclaté) = O(n³)'),

# Decode Ways
('ALGO', 'Decode Ways DP', 'Nombre de décodages', '"226" → ?, "2 26", "22 6", "2 2 6"', ['DP[i] = decode(s[:i])', 'Backtracking', 'Greedy', 'DP count paths'], 3, 'DP count paths', 'DP : DP[i] = DP[i-1] (single digit) + DP[i-2] (two digits si valide).\nComme climbing stairs avec contraintes.\nO(n) temps.', '// Decode ways : DP count (1-digit + 2-digit) = O(n)'),

# Unique Paths
('ALGO', 'Unique Paths grid', 'Nombre de chemins', 'm x n grid\ndroite ou bas', ['DP[i][j] = DP[i-1][j] + DP[i][j-1]', 'Backtracking', 'BFS', 'DP sum paths'], 3, 'DP sum paths', 'DP : chemins vers (i,j) = chemins vers (i-1,j) + (i,j-1).\nO(m*n) temps, optimisable à O(n) espace.\nOu formule combinatoire C(m+n-2, m-1).', '// Unique paths : DP sum(left, up) = O(m*n) ou combinatoire'),

# Maximal Rectangle
('ALGO', 'Maximal Rectangle', 'Largest rectangle in matrix', 'matrix de 0s et 1s', ['Histogram stack pour chaque row', 'DP', 'Brute force', 'Stack optimal'], 3, 'Stack optimal', 'Pour chaque row : calculer hauteurs consécutives de 1s.\nAppliquer largest rectangle in histogram (stack).\nO(m*n) temps.', '// Maximal rectangle : histogram stack per row = O(m*n)'),

]

# PHASE 4 - NOUVEAUX QUIZZES ALGO (27 quizzes)
NEW_ALGO_PHASE4 = [

# Bellman-Ford
('ALGO', 'Bellman-Ford algorithme', 'Plus court chemin poids négatifs', 'Relax |V|-1 fois', ['Détecte cycles négatifs', 'O(V*E)', 'Les deux', 'Plus lent que Dijkstra'], 2, 'Les deux', 'Bellman-Ford : relaxe toutes arêtes |V|-1 fois.\nSi encore relaxation au tour |V|, cycle négatif existe.\nO(V*E), plus lent que Dijkstra mais gère poids négatifs.', '// Bellman-Ford : poids négatifs + cycle detection = O(V*E)'),

# Floyd-Warshall
('ALGO', 'Floyd-Warshall', 'All pairs shortest paths', 'Tous les chemins entre tous', ['DP[i][j][k]', 'O(V³)', 'Les deux', 'DP 3D'], 2, 'Les deux', 'Floyd : pour chaque paire (i,j), essayer via k.\nDP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j]).\nO(V³), pratique si graphe dense.', '// Floyd-Warshall : all pairs via DP = O(V³)'),

# Kruskal MST
('ALGO', 'Kruskal MST', 'Minimum Spanning Tree', 'Arêtes par poids croissant', ['Sort edges + Union-Find', 'Greedy', 'O(E log E)', 'Tout ça'], 3, 'Tout ça', 'Kruskal : trier arêtes, ajouter si pas de cycle (DSU).\nGreedy : arête min qui connecte 2 composantes.\nO(E log E) pour tri, DSU quasi O(1).', '// Kruskal : sort edges + DSU = O(E log E)'),

# Prim MST
('ALGO', 'Prim MST', 'MST avec heap', 'Start from 1 node', ['Priority queue + visited', 'Greedy', 'O((V+E) log V)', 'Tout ça'], 3, 'Tout ça', 'Prim : heap avec arêtes sortantes, toujours ajouter min.\nGreedy : arête min vers nœud non visité.\nO((V+E) log V) avec heap.', '// Prim : min-heap greedy = O((V+E) log V)'),

# Tarjan SCC
('ALGO', 'Tarjan SCC', 'Strongly Connected Components', 'DFS + low-link', ['Stack + DFS order', 'O(V+E)', 'Complexe', 'Tout ça'], 3, 'Tout ça', 'Tarjan : DFS avec low-link (plus bas ancêtre atteignable).\nStack pour tracker current SCC.\nO(V+E) un seul passage.', '// Tarjan : DFS + low-link + stack = O(V+E)'),

# Kosaraju SCC
('ALGO', 'Kosaraju SCC', 'Alternative SCC', '2 DFS passes', ['DFS + reverse graph + DFS', 'O(V+E)', 'Plus simple', 'Tout ça'], 3, 'Tout ça', 'Kosaraju : DFS sur graphe original (ordre finish).\nDFS sur graphe inversé en ordre décroissant.\nO(V+E), plus simple que Tarjan.', '// Kosaraju : 2 DFS (original + reverse) = O(V+E)'),

# Articulation points
('ALGO', 'Articulation Points', 'Cut vertices', 'Retirer → composantes augmentent', ['DFS + low-link', 'Bridges similaire', 'O(V+E)', 'Tout ça'], 3, 'Tout ça', 'Articulation point : retirer → graphe se déconnecte.\nDFS + low-link : si low[child] ≥ disc[u] → u est point.\nO(V+E).', '// Articulation : DFS + low-link (cut vertex) = O(V+E)'),

# Eulerian path
('ALGO', 'Eulerian Path', 'Parcourir toutes arêtes 1 fois', 'Conditions degree', ['≤ 2 nœuds degree impair', 'Connecté', 'Les deux', 'Conditions précises'], 2, 'Les deux', 'Eulerian path : exactement 0 ou 2 nœuds de degré impair.\nEulerian circuit : tous degrés pairs.\nGraphe doit être connecté.', '// Eulerian : 0 ou 2 odd degree = path | 0 = circuit'),

# Hamiltonian path
('ALGO', 'Hamiltonian Path', 'Visiter tous nœuds 1 fois', 'NP-Complete', ['Backtracking', 'DP bitmask O(2^n * n²)', 'Pas de poly', 'Tout ça'], 3, 'Tout ça', 'Hamiltonian : NP-Complete, pas d\'algo polynomial connu.\nBacktracking : O(n!).\nDP bitmask : O(2^n * n²), meilleur mais exponentiel.', '// Hamiltonian : NP-Complete (backtrack ou DP bitmask)'),

# TSP
('ALGO', 'Traveling Salesman', 'Plus court cycle visitant tous', 'NP-Hard', ['DP bitmask O(2^n * n²)', 'Approx algorithms', 'Greedy suboptimal', 'DP optimal exact'], 3, 'DP optimal exact', 'TSP exact : DP bitmask O(2^n * n²).\nApproximations : Christofides 1.5-approx, greedy, etc.\nNP-Hard, pas de poly exact.', '// TSP : DP bitmask exact O(2^n * n²) ou approx'),

# KMP string
('ALGO', 'KMP pattern matching', 'Éviter recomparaisons', 'Précompute LPS array', ['Longest Prefix Suffix', 'O(n+m)', 'Skip characters', 'Tout ça'], 3, 'Tout ça', 'KMP : LPS array = longest proper prefix qui est aussi suffix.\nPas de backtrack dans texte, seulement pattern.\nO(n+m) vs O(n*m) naïf.', '// KMP : LPS array pour skip = O(n+m)'),

# Rabin-Karp
('ALGO', 'Rabin-Karp rolling hash', 'Pattern matching avec hash', 'Hash window de taille m', ['Rolling hash O(1)', 'Collisions possibles', 'O(n+m) average', 'Tout ça'], 3, 'Tout ça', 'Rabin-Karp : hash fenêtre glissante.\nRolling hash : update en O(1) (retirer gauche, ajouter droite).\nCollisions → vérifier match. O(n+m) moyen.', '// Rabin-Karp : rolling hash O(1) = O(n+m) average'),

# Boyer-Moore
('ALGO', 'Boyer-Moore string search', 'Sauts avec bad character', 'Skip characters', ['Bad char + good suffix', 'O(n/m) best', 'Plus rapide en pratique', 'Tout ça'], 3, 'Tout ça', 'Boyer-Moore : compare de droite à gauche.\nBad char rule : skip jusqu\'à match ou dépassement.\nMeilleur cas O(n/m), pratique très rapide.', '// Boyer-Moore : bad char rule = O(n/m) best case'),

# Aho-Corasick
('ALGO', 'Aho-Corasick multi-pattern', 'Chercher plusieurs patterns', 'Trie + fail links', ['Automate fini', 'O(n + m + z)', 'Multi-pattern optimal', 'Tout ça'], 3, 'Tout ça', 'Aho-Corasick : Trie de patterns + fail links (comme KMP).\nUn seul passage dans texte pour tous patterns.\nO(n + m + z) avec z = nb matches.', '// Aho-Corasick : trie + fail links = multi-pattern O(n+m+z)'),

# Suffix array
('ALGO', 'Suffix Array', 'Tous suffixes triés', 'Alternative suffix tree', ['Indices triés par suffixes', 'O(n log n) construction', 'O(m log n) search', 'Tout ça'], 3, 'Tout ça', 'Suffix array : indices de tous suffixes triés lexicographiquement.\nConstruction : O(n log² n) naïf, O(n log n) optimal.\nSearch pattern : O(m log n) avec binary search.', '// Suffix array : sorted suffixes = space-efficient suffix tree'),

# Z-algorithm
('ALGO', 'Z-algorithm', 'Z[i] = longest prefix match', 'Linear time string matching', ['Z-box optimization', 'O(n)', 'Simple à implémenter', 'Tout ça'], 3, 'Tout ça', 'Z-algorithm : Z[i] = longueur du plus long préfixe commun.\nZ-box : réutilise info précédente pour skip.\nO(n), simple et efficace.', '// Z-algorithm : Z-box reuse = O(n) simple'),

# Trapping Rain Water
('ALGO', 'Trapping Rain Water', 'Eau piégée entre barres', 'height = [0,1,0,2,1,0,1,3,2,1,2,1]', ['Two pointers', 'Prefix/suffix max', 'Stack', 'Two pointers optimal'], 3, 'Two pointers optimal', 'Two pointers : left/right avec max_left/max_right.\nEau[i] = min(max_left, max_right) - height[i].\nO(n) temps, O(1) espace.', '// Rain water : two pointers + max tracking = O(n) O(1)'),

# Candy distribution
('ALGO', 'Candy greedy', 'Distribution avec contraintes', 'ratings = [1,0,2]\nVoisins ratings', ['Two passes greedy', 'DP', 'Heap', 'Greedy optimal'], 3, 'Greedy optimal', 'Greedy : passe gauche→droite (si > gauche, +1 candy).\nPasse droite→gauche (si > droite, max(current, right+1)).\nO(n) temps.', '// Candy : two-pass greedy (left + right) = O(n)'),

# Gas Station
('ALGO', 'Gas Station greedy', 'Peut faire le tour ?', 'gas[], cost[]\nStart index', ['Greedy one-pass', 'Brute force', 'DP', 'Greedy optimal'], 3, 'Greedy optimal', 'Greedy : track tank et total.\nSi tank < 0, reset start à i+1.\nSi total ≥ 0 à la fin, solution existe.\nO(n) temps.', '// Gas station : greedy track tank + total = O(n)'),

# Jump Game II
('ALGO', 'Jump Game II', 'Min sauts pour atteindre fin', 'nums = [2,3,1,1,4]', ['Greedy range', 'DP', 'BFS', 'Greedy optimal'], 3, 'Greedy optimal', 'Greedy : track currentEnd et farthest.\nQuand i atteint currentEnd, jump++.\nO(n) temps.', '// Jump II : greedy range (currentEnd + farthest) = O(n)'),

# N-Queens
('ALGO', 'N-Queens backtracking', 'Placer N reines', 'N x N board\nNo attacks', ['Backtracking + pruning', 'DP', 'Greedy', 'Backtracking classique'], 3, 'Backtracking classique', 'Backtracking : placer reine par ligne.\nPruning : vérifier colonnes, diagonales.\nO(N!) complexité.', '// N-Queens : backtracking + diagonal checks = O(N!)'),

# Sudoku Solver
('ALGO', 'Sudoku Solver', 'Remplir grille 9x9', 'Backtracking avec contraintes', ['Backtracking + validation', 'Brute force', 'Greedy', 'Backtracking optimal'], 3, 'Backtracking optimal', 'Backtracking : essayer 1-9 pour chaque case vide.\nValidation : row, col, 3x3 box.\nExponentiel mais pruning efficace.', '// Sudoku : backtracking + row/col/box checks'),

# Wildcard Matching
('ALGO', 'Wildcard Matching DP', '? et * wildcards', 's = "aa"\np = "*"', ['DP[i][j] avec * = 0+', 'Greedy', 'Backtracking', 'DP complexe'], 3, 'DP complexe', 'DP : ? = match 1, * = match 0+.\nÉtats avec * (skip ou match 1+).\nO(n*m) temps.', '// Wildcard DP : ? = 1 char, * = 0+ chars = O(n*m)'),

# Interleaving String
('ALGO', 'Interleaving String DP', 's3 = interleave(s1, s2)', 's1 = "aabcc"\ns2 = "dbbca"\ns3 = "aadbbcbcac"', ['DP[i][j] = interleave(s1[:i], s2[:j])', 'Greedy', 'Two pointers', 'DP optimal'], 3, 'DP optimal', 'DP : DP[i][j] = true si s3[:i+j] peut être formé.\nTransition : match s1[i] ou s2[j].\nO(n*m) temps.', '// Interleaving : DP match s1 or s2 = O(n*m)'),

# Palindrome Partitioning II
('ALGO', 'Palindrome Partitioning II', 'Min cuts pour all palindromes', 's = "aab"', ['DP cuts + DP palindrome', 'Greedy', 'Backtracking', 'DP 2-phase'], 3, 'DP 2-phase', 'Phase 1 : DP pour détecter palindromes O(n²).\nPhase 2 : DP cuts[i] = min cuts pour s[:i].\nO(n²) temps.', '// Palindrome partition : DP palindrome + DP cuts = O(n²)'),

# Russian Doll Envelopes
('ALGO', 'Russian Doll Envelopes', 'LIS en 2D', 'Enveloppes (w, h)\nNested', ['Sort + LIS on height', 'DP 2D', 'Greedy', 'LIS optimal'], 3, 'LIS optimal', 'Trier par w croissant (si égal, h décroissant).\nLIS sur hauteurs → O(n log n).\nAstuces : h décroissant évite w égaux.', '// Envelopes : sort w + LIS h = O(n log n)'),

# Minimum Window Substring advanced
('ALGO', 'Min Window Substring optimal', 'Template générique', 's, t → min window contenant t', ['Sliding window + 2 freq maps', 'Brute force', 'DP', 'Window template'], 3, 'Window template', 'Template : expand right, shrink left quand valide.\nFreq map pour t, counter pour matches.\nO(n+m) optimal.', '// Min window : sliding window template = O(n+m)'),

]

print(f"\n{'='*60}")
print(f"Phase 1 JS: {len(NEW_JS_PHASE1)} quizzes")
print(f"Phase 2 JS: {len(NEW_JS_PHASE2)} quizzes")
print(f"Phase 3 JS: {len(NEW_JS_PHASE3)} quizzes")
print(f"Phase 4 JS: {len(NEW_JS_PHASE4)} quizzes")
print(f"Total NEW JS: {len(NEW_JS_PHASE1) + len(NEW_JS_PHASE2) + len(NEW_JS_PHASE3) + len(NEW_JS_PHASE4)}")
print(f"\nPhase 1 ALGO: {len(NEW_ALGO_PHASE1)} quizzes")
print(f"Phase 2 ALGO: {len(NEW_ALGO_PHASE2)} quizzes")
print(f"Phase 3 ALGO: {len(NEW_ALGO_PHASE3)} quizzes")
print(f"Phase 4 ALGO: {len(NEW_ALGO_PHASE4)} quizzes")
print(f"Total NEW ALGO: {len(NEW_ALGO_PHASE1) + len(NEW_ALGO_PHASE2) + len(NEW_ALGO_PHASE3) + len(NEW_ALGO_PHASE4)}")
print(f"\n{'='*60}")
print(f"TOTAL NEW QUIZZES: {len(NEW_JS_PHASE1) + len(NEW_JS_PHASE2) + len(NEW_JS_PHASE3) + len(NEW_JS_PHASE4) + len(NEW_ALGO_PHASE1) + len(NEW_ALGO_PHASE2) + len(NEW_ALGO_PHASE3) + len(NEW_ALGO_PHASE4)}")
print(f"{'='*60}")
