---
title: "Hidden in plainsight - picoCtf"
date: "2025-11-18"
draft: false
tags:
  - PicoCtf
  - Easy
  - Forensics
  - picoMini-by-CMU-Africa
---


## Challenge Name - Hidden in plainsight - picoCtf

**Category**: Forensics
**Difficulty**: Easy


## Description

> You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag.Download the jpg image [here](https://challenge-files.picoctf.net/c_amiable_citadel/0e679342e0fe04fa2efa860dda0923cba52108031ac4e1ab519df850c2764b5c/img.jpg).

## Hints
> Download the jpg image and read its metadata

## Step-by-Step Solution

1. First when I download the image, I saw its metadata using `exiftool`.

```
ExifTool Version Number         : 13.25
File Name                       : img.jpg
Directory                       : .
File Size                       : 74 kB
File Modification Date/Time     : 2025:11:16 20:02:16+05:30
File Access Date/Time           : 2025:11:18 12:39:09+05:30
File Inode Change Date/Time     : 2025:11:16 20:02:17+05:30
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Comment                         : c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9
Image Width                     : 640
Image Height                    : 640
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 640x640
Megapixels                      : 0.410

```

2. In this Metadata, we can see `Comment` is something like a base64 value.
3. So, i decoded it with base64
	```echo c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9 | base64 -d ```
4. It gave the output: `steghide:cEF6endvcmQ=`
5. The first half of the output is a tool and other half is also a base64.
6. I then decoded the second half.
	```echo cEF6endvcmQ= | base64 -d```
7. it gives the Output: `pAzzword`
8. Not I ran the steghide tool which extracts the img with the passphrase.
```
steghide extract -sf img.jpg 
```

```
sams3pi0l@sams3pi0l:~/Downloads$ steghide extract -sf img.jpg 
Enter passphrase: 
the file "flag.txt" does already exist. overwrite ? (y/n) y
wrote extracted data to "flag.txt".
sams3pi0l@sams3pi0l:~/Downloads$ cat flag.txt 
picoCTF{h1dd3n_1n_1m4g3_54e31417}
```

## Flag
`picoCTF{h1dd3n_1n_1m4g3_54e31417}
`

## Tools Used
- base64
- steghide -  is  a  steganography  program that is able to hide data in various kinds of image- and audio-files. The color- respectivly sample-frequencies are not changed thus making the embedding resistant against first-order statistical tests.


