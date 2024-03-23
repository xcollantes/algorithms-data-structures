# Compare programming languages

## Python

### Pros

- Easy to read
- Fast to program
- Extremely versatile as of this writing

  - Different libraries are used in several subsections of software engineering
    - Pandas, Numpy, matplotlib for Data Science
    - Selenium, pyperclip for desktop automation
    - Raspberry Pi libraries hardware controllers
    - Pwntools, crypto for computer security
    - Flask library for hosting web server
    - HuggingFace's Pipeline library for Machine Learning

- High level of support
  - So many libraries for any use case
  - Available APIs for Amazon Web Services and Google Cloud for Python

### Cons

- Types are not natively enforced
  - But you can use Type Hinting as specified in PEP 484
- Slow language since Python is an interpretive language where the binary is
  created and destroyed on each run
  - Technically the `pyinstaller` library can create a binary file to run but
    is incredibly bloated with about 200 MB for a simple Hello World program
- Memory management sucks
  - Not clear when referring to the same memory space
  - Use a "deepcopy" to create new memory space for an instance
  - No warning when infinite recursion eats up memory as opposed to NextJS where
    a warning error will halt program
- No private variables
  - Object-oriented programming can work in Python but private variables don't
    truly exist
  - You can mark functions as private and the function names can be obfuscated
    but are still accessible

## JavaScript

### Pros

- One of the most widely used languages in many forms: TypeScript, Google
  AppScript
- Many frameworks for specific use cases such as frontend: React, middleware:
  NextJS, backend: Node.js

### Cons

- Too many ways to perform the same task so readability might be reduced if an
  engineer is used to one way
- No type enforcement unless you use TypeScript
