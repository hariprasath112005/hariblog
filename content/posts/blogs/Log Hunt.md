---
title: Log Hunt - PicoCtf
date: 2025-11-18
draft: false
tags:
  - PicoCtf
  - Easy
  - General-Skills
  - picoMini-by-CMU-Africa
---
# Challenge Name - Log Hunt- picoMini by CMU-Africa

**Category:** General
**Difficulty**: Easy

## Description 

> Our server seems to be leaking pieces of a secret flag in its logs. The parts are scattered and sometimes repeated. Can you reconstruct the original flag?Download the [logs](https://challenge-files.picoctf.net/c_amiable_citadel/49cec6157142f24a599f4164d5b63322c2494f801390d6f22eb91b3aa592bc66/server.log) and figure out the full flag from the fragments.


### Hints
 >You can use `grep` to filter only matching lines from the log.
 >Some lines are duplicates; ignore extra occurrences.
 

## Solution

1. As the Hint says to use `grep` and filter the matching lines. 
2. So, I views the file. Output is very long.


!![Image Description](/hariblog/images/Pasted%20image%2020251118121114.png)
1. You can see the flag which has `INFO FLAGPART:` 
2. We need to filter the results with `grep` tool and only filter the lines which has `INFO FLAGPART` in it.
3. `cat server.log | grep 'INFO FLAGPART:'


!![Image Description](/hariblog/images/Pasted%20image%2020251118121540.png)


6. The flag is repeated, but we can easily copy the flag.

## Flag: picoCTF{us3_y0urlinux_sk1lls_cedfa5fb}


## Tools used

- grep
- cat