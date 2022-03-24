# Easy Eval

## Writeup
In JavaScript,

```js 
myFunction`a{1}b{2}c{3}`
```
is equivalent to

```js
myFunction(["a", "b", "c"], 1, 2, 3)
```

Hence, use payload

```js
directory`flag`
```

to get the flag. 
