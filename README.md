A very poor attempt to make a self programming program. This contains its own scripting language and interpreter, which contains the commands;

 * set A B - sets the value of A to be B
 * add A B - sets the value of A to be A+B
 * mul A B - sets the value of A to be A*B
 * div A B - sets the value of A to be A/B {for B!=0)
 * sub A B - sets the value of A to be A-B
 * print A 0 - prints the value of A
 * goto A 0 - goes to line A {if A is a variable, then the value referred to by A)
 * ifg A B - if A <= B executes next line, if not ignores it
 * end 0 0 - ends script

So a program;

```
0 set a 1
1 set b 0
2 set c a
3 add a b
4 set b c
5 print b 0
6 ifg a 9
7 goto 2 0
8 end 0 0
```

Will output

```
1.0
1.0
2.0
3.0
5.0
8.0
```

ie the Fibonacci series.

As the scripting language is very limited in which commands can be used, it is possible to plot it as a line in space. If we limit the variables to be A-F, X and Y, plus 0-9, then the above program can be converted to coordinates;

```{{0, 0, 9), {0, 1, 8), {0, 2, 0), {1, 0, 1), {0, 1, 2), {6, 1, 8), {8, 17, 0), {7, 10, 8), {9, 8, 8))```

![Plot of program](x.png)

What the rest of the program does is to generate a population of these scripts. It then executes each script for a range of test variables (at the moment these are ((1, 1), (6, 36), (10, 100), (20, 400), (25, 625))) and then rank these based on how well they convert the first value (x) into the second (y).

The best 10 of these are then cloned and randomly changed. An additional 30 random scripts are also produced. This continues until either 500 time steps have expired or a program which exactly matches the output is found.

On running interpret.py as found in this repository, the output will be along the lines of (random variation means it will likely not be exact);

```
0, -540911.0, -561356.43, -561422.0
1, -540911.0, -557958.512345679, -561422.0
...
18, -1120.0, -1665150.4232617284, -36908.0
19, 500.0, -1643604.7430340557, -36908.0

ifg 8 b
goto y 7
add 0 9
mul x x
mul y 2
sub 6 9
add 6 5
print 4 7
add a y
add y x
```

And so in this case we can analyse the program it has generated. The first three lines are irrelevant (b = 0, so 8 > b and we jump to add 0 to 9, which does nothing). We then set x to be x * x, and multiply y (0) by 2 (to give 0). Then we take 9 away from 6 to give -3, add 6 to 5 to give 11, print 4, set a (0) to be a(0) + y(0). Finally, we set y (0) to be y (0) + x. And so getting rid of the fluff and pointless crap in this program we are left with;

```
mul x x
add y x
```

And that's about as far as I've gone with this idea.
