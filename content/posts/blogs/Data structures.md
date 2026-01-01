---
title: Data structures
date: 2026-01-01
draft: false
tags:
  - Programming
  - Placement_Preparation
---
# Time Complexity

## Big O Notation

- Big O notation is special notation that tells you how fast an algorithm is.
- Big O notation is about the worst-case scenario. It’s a reassurance—you know that simple search will never be slower than O(n) time.
- Algorithm running times grow at diﬀerent rates
- This tells you the number of operations an algorithm will make. It’s called Big O Notation because you put a “big O” in front of the number of operations


**O(log n), also known as log time. Example: Binary search .**
**O(n), also known as linear time. Example: Simple search .**
**O(n * log n). Example: A fast sorting algorithm , like** **quicksort**
**2**
**O(n ). Example: A slow sorting algorith m , like selection**
**sor t.**
**O(n!). Example: A really slow algorith m , like the** **traveling salesperson **



## ARRAYS AND LINKED LISTS

- Using an array means all your tasks are stored contiguously (right next to each other) in memory.
- even if you have only 3 items in your task list, you can ask the computer for 10 slots, just in case. Then you can add 10 items to your task list without having to move. This is a good workaround.
- You may not need the extra slots that you asked for, and then that memory will be wasted. You aren’t using it, but no one else can use it either.  
- You may add more than 10 items to your task list and have to move anyway.
- You know the address for every item in your array
- Arrays are great if you want to read random elements, because you can look up any element in your array instantly

### Linked lists solve this problem of adding items.

- Each item stores the address of the next item in the list.
- It’s like a treasure hunt. Y ou go to the first address, and it says, “The next item can be found at address 123.” So you go to address 123, and it says, “The next item can be found at address 847,” and so on
- Linked lists are great if you’re going to read all the items one at a time: you can read one item, follow the address to the next item, and so on.
- But if you’re going to keep jumping around, linked lists are terrible.
- With a linked list, the elements aren’t next to each other, so you can’t instantly calculate the position of the fifth element in memory—you have to go to the first element to get the address to the second element, then go to the second element to get the address of the third element, and so on until you get to the fifth element.

!![Image Description](/hariblog/images/Pasted%20image%2020251231095817.png)



# BFS (breadth first search)

- Graph
- Uses Queue

**BFS** is a traversal algorithm where you: > Visit **all neighbors first**, then move to the next level.

It explores **level by level**.


# DFS (depth first search)

- Graph
- trees
- Uses stack

**DFS** is a traversal algorithm where you: > Go **as deep as possible** along one path before backtracking.


       1
       / \
      2   3
     / \
    4   5


## Inorder Traversal

Left → Root → Right
4 2 5 1 3


## Preorder Traversal

Root → Left → Right
Root → Left → Right


## Postorder Traversal

Left → Right → Root
1 2 4 5 3




# Scheduling Algorithms

**CPU Scheduling** is the method used by the **operating system** to decide:

 **Which process gets the CPU and for how long**
 When multiple processes are in the **ready state**, the OS uses a **scheduling algorithm** to select one.

## 1️⃣ Non-Preemptive Scheduling

Once a process gets the CPU, **it runs till completion** or blocks itself.

### Types of Non-Preemptive Algorithms

#### 1. First Come First Serve (FCFS)

- Processes are executed **in order of arrival**

#### 2. Shortest Job First (SJF)

- Process with **smallest burst time** executes first

#### 3. Longest Job First

#### 4.  Highest Response Ration next


## 2️⃣ Preemptive Scheduling

CPU **can be taken away** from a running process.

### Types of Preemptive Algorithms

####  1. Shortest Remaining Time First (SRTF)

- Preemptive version of SJF

#### 2. Priority Scheduling
- CPU allocated based on **priority**

#### 3.Round Robin (RR)
Each process gets CPU for a **fixed time quantum**

#### 4. Longest Remaining Time first
