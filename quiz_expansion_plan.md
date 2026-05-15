# Plan d'Expansion Codebog : 202 Nouveaux Quizzes

**Objectif** : Passer de 163 à 365 quizzes quotidiens
**Manquants** : 101 JS + 101 ALGO

---

## Sources d'Inspiration

### JavaScript (101 quizzes)
- **Eloquent JavaScript** (Marijn Haverbeke)
- **JavaScript: The Good Parts** (Douglas Crockford)
- **You Don't Know JS** (Kyle Simpson)

### Algorithmique (101 quizzes)
- **Grokking Algorithms** (Aditya Bhargava)
- **Introduction to Algorithms** (Cormen/CLRS)
- **LeetCode** (patterns d'interview)

---

## PHASE 1 : FONDATIONS (Jours 1-90)

### JavaScript - Phase 1 (24 nouveaux topics)

**Eloquent JavaScript - Basics**
1. String methods (slice, substring, indexOf)
2. Number precision & floating point
3. Boolean operators short-circuit
4. Logical operators (&& || priority)
5. for...in loop gotchas
6. while vs do...while
7. Switch statement fall-through
8. Break vs continue in loops
9. Label statements

**YDKJS - Types & Grammar**
10. String immutability
11. Number.EPSILON
12. parseInt() radix trap
13. isNaN() vs Number.isNaN()
14. Array.isArray() vs instanceof
15. Object wrapper (new String vs string)
16. Coercion with +
17. Truthy/Falsy values comprehensive

**Good Parts - Pitfalls**
18. Global scope pollution
19. Semicolon insertion
20. Function expression vs declaration
21. arguments object (not array)
22. eval() dangers
23. with statement problems
24. delete operator quirks

### Algorithmique - Phase 1 (25 nouveaux topics)

**Grokking Algorithms - Foundations**
1. Linear search vs Binary search
2. Selection sort implementation
3. Recursion base case importance
4. Recursion stack visualization
5. Quicksort pivot selection
6. Arrays vs Linked Lists trade-offs
7. Hash table collisions
8. Hash function properties
9. Load factor in hash tables

**CLRS - Basic Analysis**
10. Best/Worst/Average case
11. Asymptotic notation (Θ, Ω, O)
12. Loop analysis for complexity
13. Recurrence relations T(n)
14. Master theorem application
15. Insertion sort analysis
16. Merge sort complexity proof

**LeetCode - Easy Patterns**
17. Contains Duplicate (hash set)
18. Valid Anagram (frequency map)
19. Two Sum (hash map)
20. Best Time to Buy/Sell Stock
21. Valid Parentheses (stack)
22. Maximum Subarray (Kadane intro)
23. Merge Two Sorted Lists
24. Reverse Linked List (iterative)
25. Climbing Stairs (Fibonacci pattern)

---

## PHASE 2 : INTERMÉDIAIRE (Jours 91-180)

### JavaScript - Phase 2 (25 nouveaux topics)

**Eloquent JavaScript - Advanced**
1. Higher-order functions (filter edge cases)
2. Array.some() vs every()
3. Array.find() vs findIndex()
4. Array.flat() depth
5. Array.flatMap() use case
6. Object.entries() / fromEntries()
7. Object.assign() shallow copy
8. Object.is() vs ===
9. Symbol.for() global registry
10. Symbol.toPrimitive
11. Regular expressions lookahead
12. Regex capturing groups
13. JSON.stringify() replacer
14. JSON.parse() reviver

**YDKJS - Async & Scope**
15. let block scope vs var function scope
16. const reassignment vs mutation
17. IIFE pattern
18. Module pattern encapsulation
19. Promise.race() behavior
20. Promise chain error propagation
21. async/await error handling
22. Parallel vs Sequential promises
23. Event loop phases
24. Callback hell vs Promises
25. Microtask vs Macrotask queue

### Algorithmique - Phase 2 (25 nouveaux topics)

**Grokking Algorithms - Intermediate**
1. Breadth-first search (BFS) implementation
2. Queue for BFS
3. Dijkstra's algorithm shortest path
4. Weighted vs unweighted graphs
5. Greedy algorithms characteristics
6. Dynamic programming memoization
7. DP bottom-up vs top-down
8. Knapsack problem (0/1)
9. Longest common subsequence

**LeetCode - Medium Patterns**
10. 3Sum (two pointers extension)
11. Container With Most Water
12. Longest Substring Without Repeating
13. Minimum Window Substring
14. Group Anagrams
15. Product of Array Except Self
16. Rotate Array (reversal trick)
17. Spiral Matrix traversal
18. Set Matrix Zeroes (in-place)
19. Word Search (backtracking)
20. Combination Sum (backtracking)
21. Permutations (backtracking)
22. Subsets (backtracking)
23. Course Schedule (topological sort)
24. Number of Islands (DFS/BFS)
25. Clone Graph

---

## PHASE 3 : AVANCÉ (Jours 181-270)

### JavaScript - Phase 3 (25 nouveaux topics)

**YDKJS - Deep Dives**
1. Prototype chain traversal
2. Object.create() vs constructor
3. Class syntax vs function constructor
4. super keyword behavior
5. Static methods vs instance
6. Getter/Setter traps
7. Proxy handler traps
8. Reflect methods vs Object
9. Private fields (#field)
10. WeakMap memory management
11. WeakSet use cases
12. FinalizationRegistry
13. Iterator protocol implementation
14. Generator delegation (yield*)
15. Async generators

**Good Parts - Performance**
16. String concatenation performance
17. Object property access speed
18. Array pre-allocation
19. Function call overhead
20. Memory leak patterns (closures)
21. Event listener memory leaks
22. Detached DOM nodes
23. V8 hidden classes
24. Inline caching
25. Deoptimization triggers

### Algorithmique - Phase 3 (24 nouveaux topics)

**CLRS - Advanced Structures**
1. Binary Search Tree (BST) properties
2. AVL tree rotations
3. Red-Black tree invariants
4. B-tree for databases
5. Heap property (min/max)
6. Heapify operation
7. Priority queue with heap
8. Disjoint Set Union (DSU)
9. Union by rank optimization
10. Path compression in DSU

**LeetCode - Hard Patterns**
11. Binary Tree Maximum Path Sum
12. Serialize/Deserialize Binary Tree
13. Word Ladder (BFS shortest path)
14. Alien Dictionary (topological sort)
15. Merge K Sorted Lists (heap)
16. Find Median from Data Stream (two heaps)
17. Sliding Window Maximum (deque)
18. Longest Increasing Subsequence (DP)
19. Edit Distance (Levenshtein)
20. Regular Expression Matching (DP)
21. Burst Balloons (DP)
22. Decode Ways (DP)
23. Unique Paths (DP grid)
24. Maximal Rectangle (stack)

---

## PHASE 4 : EXPERT (Jours 271-365)

### JavaScript - Phase 4 (27 nouveaux topics)

**Eloquent JavaScript - Browser & Node**
1. Event bubbling vs capturing
2. event.preventDefault() vs stopPropagation()
3. Event delegation pattern
4. requestAnimationFrame timing
5. Web Workers communication
6. SharedArrayBuffer & Atomics
7. LocalStorage vs SessionStorage
8. IndexedDB basics
9. Service Worker lifecycle
10. Fetch API vs XMLHttpRequest
11. CORS preflight requests
12. AbortController for fetch
13. Streams API (ReadableStream)

**Advanced Modern JS**
14. Top-level await (modules)
15. Dynamic import()
16. import.meta.url
17. Optional catch binding
18. Numeric separators (1_000_000)
19. Promise.allSettled() vs all()
20. Promise.any() vs race()
21. String.prototype.matchAll()
22. Array.prototype.at() negative indices
23. Object.hasOwn() vs hasOwnProperty
24. Error.cause chaining
25. Temporal API (future replacement for Date)
26. Pattern matching proposal
27. Records & Tuples proposal

### Algorithmique - Phase 4 (27 nouveaux topics)

**CLRS - Advanced Algorithms**
1. Bellman-Ford (negative weights)
2. Floyd-Warshall (all pairs shortest)
3. Kruskal's algorithm (MST)
4. Prim's algorithm (MST)
5. Tarjan's SCC (strongly connected)
6. Kosaraju's SCC algorithm
7. Articulation points (bridges)
8. Eulerian path/circuit
9. Hamiltonian path (NP-complete)
10. Traveling Salesman (approximation)
11. Knuth-Morris-Pratt (KMP) string
12. Rabin-Karp (rolling hash)
13. Boyer-Moore string search
14. Aho-Corasick (multi-pattern)
15. Suffix array construction
16. Z-algorithm for strings

**LeetCode - Expert Level**
17. Trapping Rain Water (two pointers)
18. Candy distribution (greedy)
19. Gas Station (greedy)
20. Jump Game II (greedy/DP)
21. N-Queens (backtracking)
22. Sudoku Solver (backtracking)
23. Wildcard Matching (DP)
24. Interleaving String (DP)
25. Palindrome Partitioning II (DP)
26. Russian Doll Envelopes (LIS variant)
27. Minimum Window Substring (sliding window)

---

## Répartition Finale

| Phase | JS Actuels | JS Nouveaux | ALGO Actuels | ALGO Nouveaux | Total/Phase |
|-------|------------|-------------|--------------|---------------|-------------|
| 1     | 21         | 24          | 20           | 25            | 90          |
| 2     | 20         | 25          | 20           | 25            | 90          |
| 3     | 20         | 25          | 21           | 24            | 90          |
| 4     | 21         | 27          | 20           | 27            | 95          |
| **Total** | **82** | **101**     | **81**       | **101**       | **365**     |

---

## Format de Quiz à Respecter

```python
('TYPE',  # 'JS' ou 'ALGO'
 'Topic Name',  # 2-3 mots
 'Hook engageant',  # Curiosité, défi, autorité
 'code snippet',  # 1-15 lignes
 [opt1, opt2, opt3, opt4],  # 4 options plausibles
 correct_index,  # 0-3
 'réponse correcte',  # Texte de la bonne réponse
 'explication détaillée',  # Pourquoi + détails techniques
 'tip mémorable'  # Best practice actionable
)
```

---

## Prochaines Étapes

1. ✅ Plan créé avec sources d'inspiration
2. 🔄 Générer les 101 nouveaux quizzes JS
3. 🔄 Générer les 101 nouveaux quizzes ALGO
4. 🔄 Valider la qualité et cohérence
5. 🔄 Intégrer dans quizzes_js.py et quizzes_algo.py
6. 🔄 Tester la génération complète (365 jours)
