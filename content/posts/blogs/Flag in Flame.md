---
title: "Flag in Flame - picoCtf "
date: "2025-11-18"
draft: false
tags:
  - PicoCtf
  - Easy
  - Forensics
  - picoMini-by-CMU-Africa
---


## Challenge Name - Flag in Flame - picoCtf 
**Category**:Forensics
**Difficulty**:Easy


## Description

> The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within? Your mission is to inspect the resulting file and reveal the real purpose of it. The team is relying on your skills to uncover any concealed information within this unusual log.Download the encoded data here: [Logs Data](https://challenge-files.picoctf.net/c_amiable_citadel/5da19ac1eabba5f0b9287e4a5675612e5bbffc68aaa8fa54c58ebd5ce81e29fd/logs.txt). Be prepared—the file is large, and examining it thoroughly is crucial .

## Hints
>Use `base64` to decode the data and generate the image file.


## Step-by-Step Solution

1. I first views the file and got a base64 value.
2. The hint says to decode the data and generate as the image file.
3. So i ran this command
```
cat logs.txt | base64 -d >> temp.jpg
```
4. the `cat` gives the content in the file and it is piped to base64 tool and the `>>` symbol will save the resulting value to a jpg image.


!![Image Description](/hariblog/images/sad.jpg)
This is the resultant image.
5. now we can see some text in the image and I copied it.
6. I used this [site](https://gchq.github.io/CyberChef/) to decode the text. I used all the operations until i get the flag.


!![Image Description](/hariblog/images/Pasted%20image%2020251118130712.png)

7. As you can see the output is the flag.

## Flag

```
picoCTF{forensics_analysis_is_amazing_b9ac4cb9}
```


## Tools Used

- base64
- [CyberChef](https://gchq.github.io/CyberChef/) - It has various operations for encoding and decoding.
