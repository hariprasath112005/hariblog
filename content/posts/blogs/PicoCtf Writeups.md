---
title: Riddle Registry
date: 2025-11-17
draft: false
tags:
  - PicoCtf
  - easy
---

# Challenge Name - Riddle Registry - picoMini by CMU-Africa

**Category:** Forensics
**Difficulty**: Easy

# Description:


>  Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered.Find the PDF file here [Hidden Confidential Document](https://challenge-files.picoctf.net/c_amiable_citadel/3f00b89eeac6ac5242f747889ea4de24c804d9144cfa71e23d754e6a8e80e435/confidential.pdf) and uncover the flag within the metadata.


The pdf file provided: 
!![Image Description](./images/Pasted%20image%2020251118094747.png)



# Solution: 

1. The pdf content is not needed for this ctf, it is only a decoy.
2. First I used `exiftool` to analyse the pdf and noticed this output


```
ExifTool Version Number         : 13.25
File Name                       : confidential.pdf
Directory                       : .
File Size                       : 183 kB
File Modification Date/Time     : 2025:11:17 20:09:04+05:30
File Access Date/Time           : 2025:11:17 20:09:15+05:30
File Inode Change Date/Time     : 2025:11:17 20:09:06+05:30
File Permissions                : -rw-rw-r--
File Type                       : PDF
File Type Extension             : pdf
MIME Type                       : application/pdf
PDF Version                     : 1.7
Linearized                      : No
Page Count                      : 1
Producer                        : PyPDF2
Author                          : cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jOTk5ZTJhNH0=
```


3. Notice the Author value here, which is not the name of an author and it also ends with a `=` symbol which means it can be a base64 value.
4. So, I decoded the value with base64. `echo  cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jOTk5ZTJhNH0= | base64 -d
5. The base64 will decode it and `echo` returns the output.
6. Finally got the output. `picoCTF{puzzl3d_m3tadata_f0und!_c999e2a4}`

# Flag : `picoCTF{puzzl3d_m3tadata_f0und!_c999e2a4}`


# Tools used
1. `exiftool` -  used to give metadata of the file.
2. `base64` - used to decode the base64 values.
