## 10.1.1
```
null, null, null, null, null, null
4, null, null, null, null, null
1, 4, null, null, null, null
3, 1, 4, null, null, null
1, 4, null, null, null, null
8, 1, 4, null, null, null
1, 4, null, null, null, null
```
## 10.1.2
```
Two ends of the array can be used as the two tops of the stack. 
Stack 1 top: 0
Stack 2 top: n
When the end of one Stack is adjacent to the end of the other, we are full. 
See bistack.py. 
```
## 10.1.3
```
null, null, null, null, null, null
4, null, null, null, null, null
4, 1, null, null, null, null
4, 1, 3, null, null, null
null, 1, 3, null, null, null
null, 1, 3, 8, null, null
null, null, 3, 8, null, null
```
## 10.1.4
```
enqueue(Q, x):
    if Q.head = 1 and Q.tail == Q.length:
        return 'overflow'
    Q[Q.tail] = x
    if Q.tail == Q.length
        Q.tail = 1
    else Q.tail = Q.tail + 1

dequeue(Q):
    if Q.head == Q.tail:
        return 'underflow'
    x = Q[Q.head]
    if Q.head == Q.length:
        Q.head = 1
    else Q.head = Q.head + 1
    return x
```

## 10.1.5
```
```
## 10.1.6
```
S1, S2

If you want to enqueue:
    push x O(1)
If you want to dequeue:
    pop everything from one stack (let's say S1) and push them to S2. O(n)
    pop from S2. O(1)
```

## 10.1.7
```
Q1, Q2
If you want to push:
    dequeue all elements in Q1 O(n) and enqueue them in Q2
    add x to Q1 (empty)
    dequeue all from Q2 and enqueue in Q1 O(n)

If you want to pop:
    dequeue Q1 until only one element is left O(n)


In 10.1.6 I chose a 'hard dequeue' and in 10.1.7 a hard push. I could have also seen it as a 'hard enqueue' and a 'hard pop'. 
```
## 10.2.1
```
INSERT: 
Yes: 
    Q.head.next = x
    Q.head = x
DELETE: 
No, we have to go through the queue to fetch x, so it'll be O(n). 
```
## 10.2.2
```
push(x):
    L.head.next = x
    L.head = x
pop:
    return L.head
#### Implement this
```
## 10.2.3
```
enqueue(x): 
    x.next = L.tail
    L.tail = x
dequeue():
    return L.head

#### Implement this
```
## 10.2.4
```
If k is assigned to the sentinel's key, we can skip x≠L.nil check.  
```
## 10.2.5
```
```
## 10.2.6
```
S2.next = S1.tail
```
## 10.2.7
```

```
## 10.4.1
```
                18
            12       10
        7       4   2   21
              5
```
## 10.4.2
```

```