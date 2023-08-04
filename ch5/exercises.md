# Chapter 5 Exercises & Problems

## 5.1.1

###### Quick note on total and partial order
```
Grimaldi, p. 341:
A relation R on a set A is partial order or a partial oredering relation, if R is reflexive, antisymmetric and transitive. 

Grimaldi, p. 359:
If (A, R) is a poset, we say that A is totally ordered oed linearly ordered, if for all x,y in A, either xRy or yRx. In this case, T is called a total order or a linear order. 
```
```
At each iteration, we are able to decide whether or not the current candidate is better than the best candidate so far. If aRb signifies a being better than b: 
1. a R a
2. If a R b is true, then b R a is not tre. 
3. If a R b and b R c, then a R c. 
4.  R holds for each and every pair of candidate. So, there is a total order on the set of the candidates. 
```

## 5.1.2
```
p = Random(0, 1)
chosen = a + p * (a-b)
E(running time) = chosen * cost-of-each-one-procedure

```

## 5.1.3
```
biased random expectation or f(x) = p
E(f(x)) = p (1) + (1-p) (0) = p
g(x) = 1/2x
E(g(f(x))) = 1/2p * p = 1/2

```
