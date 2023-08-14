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
RANDOM(a,b)
    p = Random(0, 1)
    chosen = a + p * (b-a)
    return chosen

It is Θ(1). 

```

## 5.1.3
```
UNIFORM-RANDOM:
// estimate p; whatever the distribution, CLT ensures we get a good estimate of p as long as we have a large sample, let's say 10000. 
    c = 0
    for i = 1 to 10000:
        x = BIASED-RANDOM()
        if x == 1:
            c++
    p = c / 10000
// compose 
    chosen = p * 1/2p
    return chosen

```

## 5.2.1
```
Hiring exactly once: best candidate being the first candidate. 
(n-1)! / n! = 1/n

Hiring exactly n times: best candidate being the last, and the rest being sorted in terms of their rank: 1/n!
```

## 5.2.2
```
Two configurations that lead to hiring exactly twice:
(a) second best candidate being the first person 
(b) best candidate being the second to be interviewed

#a = 1 * (n-1)!
#b = (n-2) * 1 * (n-2)! (first person cannot be the best candidate and the second best candidate; second best being first was coundted in case (a)). 
#S = n!

P(two hires) = ((n-1)! + (n-2) * (n-2)!) / n! = 
((n-1) * (n-2)!  + (n-2) * (n-2)!) / n! =  
((n-2)! [(n-1) + (n-2)]) / n! = 
((n-2)! [(n-1) + (n-2)]) / (n * (n-1) * (n-2)!) = 
([(n-1) + (n-2)]) / (n * (n-1)) = (2n-3) / (n(n-1))
```

## 5.2.3
```
E(X) = Σ xi * P(xi) = 1 * 1/6 + 2 * 1/6 + 3 * 1/6 + ... + 6 * 1/6 = 3.5
n dice:
E(X) = E(X) + E(X) + ... + E(X) = nE(X) = 3.5n (by linearity of expectation)
```

## 5.2.4
```
Xi = I{person i gets their own hat} = {1 if person i gets their hat; 0 if person i gets someone else's hat}
E(Xi) = 1 * 1/n + 0 * (n-1)/n = 1/n
Y = number of people that get their own hats
E(Y) = E(ΣYi) = Σ E(Yi) = Σ 1/n = n * 1/n = 1
```

## 5.2.5
```
```

## 5.3.2
```
This cannot produce "any" permutation, because at each i, A[i] absolutely has to move to a a higher index, so permutations whose beginning element is the same as the original array cannot be produced; for example, if the original array is [1,2,3], we can never get [1, 3, 2], because 1 has to move to index 2 or 3 of the array at iteration 1 and will nevere get the chance to go back to index 1 later, since future potential places of it are i+1 to n. 
```