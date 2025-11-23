---
title: "Crack the Gate 1 - picoCtf"
date: "2025-11-19"
draft: false
tags:
  - PicoCtf
  - Easy
  - Web-exploitation
  - picoMini-by-CMU-Africa
---


## Challenge Name - Crack the Gate 1 - picoCtf
**Category** Web Exploitation
**Difficulty**: Easy


## Description

> We’re in the middle of an investigation. One of our persons of interest, ctf player, is believed to be hiding sensitive data inside a restricted web portal. We’ve uncovered the email address he uses to log in: `ctf-player@picoctf.org`. Unfortunately, we don’t know the password, and the usual guessing techniques haven’t worked. But something feels off... it’s almost like the developer left a secret way in. Can you figure it out?


## Step-by-Step Solution
1. First I launched the instance and opened the login url and logged in with the email they gave and a random password. It says invalid credentials which is expected.
2. I viewed the source page of the web page and noticed a 2 line comment

	!![Image Description](/hariblog/images/Pasted%20image%2020251119130904.png)
3. The String in the first comment looks like a `ROT13` value. So i went to cyberchef and used `ROT13` algorithm.
4. Basically `ROT13` a simple letter substitution that shifts letters by 13 places, it’s common in puzzles.
5. It translated to plain text.

	!![Image Description](/hariblog/images/Pasted%20image%2020251119131247.png)


6. So, the plain text says to use header "X-Dev Access: yes". Which means if the login request has this header, then the server would allow to login without a password.
7. I used the `curl` method.
	- Right click on the page and select inspect
	- Go to the network tab and click login button on the page.
	- you can see the login request and right click it and copy as curl.

		!![Image Description](/hariblog/images/Pasted%20image%2020251119131703.png)

8. Then go to the terminal and paste the url with adding the header.
	```
	-H 'X-Dev-Access: yes' \
	```
9. The response contains the flag.

	!![Image Description](/hariblog/images/Pasted%20image%2020251119132213.png)

## Flag

```picoCTF{brut4_f0rc4_7e5db33b}```

## Tools Used

1. curl 
2. ROT13
