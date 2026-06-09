# Interface-POO AGENTS.MD
 
## Coding style guidelines

- ALL VARIABLES should be typed out in AMERICAN ENGLISH, do not set variables with names in any other language, independently of your internal working language or the committer's prompt.

- Do not write lines that are over 80 characters in length. If you are a thinking model, always cross-verify the rough number of characters in the new lines you've written. If you cannot do such a thing quickly with certainty, always err on the side of caution.

- You are writing code FOR HUMANS. Avoid making changes to the overall structure of the program directly. Always contain new functionality you add to classes or methods with simple type-hinted interfaces.

## Comment guidelines

- Do not make annoying, overbearing comments. WRITE LARGE COMMENTS AT THE TOP OF METHODS/CLASSES/ETC RATHER THAN SMALL COMMENTS.

- **NEVER** write comments besides lines of code, like this:

```
print("Hello, world!") # Prints "Hello, world!"
```

**ALWAYS** move them above the line instead, like this:

```
# Prints "Hello, world!"
print("Hello, world!")
```