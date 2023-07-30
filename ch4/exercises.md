# Chapter 4 Exercises & Problems

## 4.1.1
```
The least element.
```

## 4.1.2
```
max-sum = 0
b = 0
e = 0
for i = 1 to A.length:
    sum-i-b = A[i]
    for j = i+1 to A.length:
        sum-i-b += A[j] 
        if max-sum < sum-i-b:
            max-sum = sum-i-b
            b = i 
            e = j     
```

## 4.1.4

```

Lines 7-9, p. 72, another condition can be checked to make sure that the max is positive. If not, we can return 0. 

```

## 4.1.5