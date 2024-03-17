---
title: Keywords In C language
tags:
  - C
categories:
  - Technology
  - C
date: 2024-03-17 20:23:12
description: Keywords In C language
lang: en
comments: true
---
In C Programming language, there are many rules so to avoid different types of errors. One of such rule is not able to declare variable names with auto, long, etc. This is all because these are keywords. Let us check all keywords in C language.

## What are Keywords?
> Keywords are predefined or reserved words that have special meanings to the compiler. These are part of the syntax and cannot be used as identifiers in the program. A list of keywords in C or reserved words in the C programming language are mentioned below:

|  auto |  break |  case |  char|  const|  continue|  default|  do| 
|:----------|:-------------|:-------------|:-------------|:-------------|:-------------|:-------------|:-------------|  
|double|else|enum|extern|float|for|goto|if |
|int|long|register|return|short|signed|sizeof|static | 
|struct|switch|typedef|union|unsigned|void|volatile|while |

### auto
> auto is the default storage class variable that is declared inside a function or a block. auto variables can only be accessed within the function/block they are declared. By default, auto variables have garbage values assigned to them. Automatic variables are also called local variables as they are local to a function. 
```
auto int num;
```
Here num is the variable of the storage class auto and its type is int. Below is the C program to demonstrate the auto keyword:

### break and continue
> The break statement is used to terminate the innermost loop. It generally terminates a loop or a switch statement. The switch statement skips to the next iteration of the loop. Below is the C program to demonstrate break and continue in C:
```
// C program to show use 
// of break and continue
#include <stdio.h>

// Driver code
int main()
{
  for (int i = 1; i <= 10; i++) 
  {
    if (i == 2) 
    {
      continue;
    }
    if (i == 6) 
    {
      break;
    }
    printf("%d ", i);
  }
  return 0;
}
```

### switch, case, and default
> The switch statement in C is used as an alternate to the if-else ladder statement. For a single variable i.e, switch variable it allows us to execute multiple operations for different possible values of a single variable. 
```
switch(Expression)
{
    case '1': // operation 1
            break;
    case:'2': // operation 2
            break;
    default: // default statement to be executed 
}
```



## Referce
[geeksforgeeks.org](https://www.geeksforgeeks.org/keywords-in-c/?ref=xxl4.github)