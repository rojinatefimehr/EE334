 BRANCH TARGET BUFFER PROJECT: 

Objective: To write a program that simulates a branch target buffer (BTB) that performs dynamic branch prediction.
Input: A long set of PC addresses from program traces.
Programming language: Use any programming language (C++, Phyton, Java, ...). Program/code sharing: Code sharing is not allowed. Students with code sharing will get 0
(zero) points for the project.
Figure 1 below shows the basic structure of the BTB which was introduced in class. It has four fields with an entry: Entry number, Current PC, Target PC, and Prediction. In this project the BTB number of entries is 1024; thus, only 10 bits are needed to address the entire BTB.
Entry Num. Current PC Target PC Prediction 0:
1:
1023:
Figure 1. 1024-entry Branch Target Buffer.
In order to determine the BTB entry, 10 bits (from bit 2 to bit 11) from the PC address are used as shown in Figure 2. The least significant bits (0 and 1) are always 0; thus, they are not needed.
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
           PC
10
             PC
Here is an example how the BTB index is determined. Let us assume the current PC address is:
Figure 2. 10-bit BTB address obtained from the 32-bit PC. 0x4001c4 (this is an hexadecimal number).
31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
004001c4
We need only the last 3 hexadecimal numbers: The binary number are shown as well.
Using the binary number we can obtained the BTB entry.
11 10 9 8 7 6 5 4 3 2 1 0
1c4 000111000100
0001110001 = 26 +25 +24 +20 =113
We can obtain the address using the hexadecimal numbers (this might be a bit easier).
1c4=1*162 +12*16+4 = 452
Now, we need to remove the 2 least significant bits (we divide by 4): 452/4 = 113
 Trace .
400190
400194
400198
40019c
4001a0
4001a4
4001a8
4001ac 2n → 4001b0
4001b4
4001b8
4001bc
4001c0
4001c4
4202b0
4202b4 index 4202b8
To compute index, 10 bits are need (for 1024-entry BTB).
We used the 3 least significant bytes (in red);
the 2 least significat bits are not considered (they are always 00)
4001c4 1*162 + 12*16 + 4 452 / 4 =113 000111000100 = 26 +25 +24 +20 =113
↑↑↑↑ ↑↑↑↑ ↑↑
9876 5432 10
4202bc 4202c0 4202c4 4202c8 4202cc 4202d0 4202d4 4202d8 4202dc 42ac30 42ac34 42ac38 42ac3c 42ac40 42ac44 42ac48 42ac5c 42ac60 42ac64 42ac68 42ac6c 42ac70 42ac74 42ac78 42ac7c 42ac80 42ac84 42ac88 42ac8c 42ac90 42ac94 42ac98 42ac9c
 732 / 4 =183
10
113 183
786
Current PC
Target PC
Prediction
4202dc 2*162 + 13*16 + 12
001011011100=27 +25 +24 +22 +21 +20 =183
42ac48
12*162 + 4*16 + 8
 3144/4 =786
  4001c4
4202b0
Taken (00)
4202dc
42ac30
Taken (00)
42ac48
42ac5c
Taken (00)
:
:
::
  1024 entries
  
Specifications:
 BTB size: 1024 Entries
 Two Benchmarks. Use the least significant digit in your WSU ID*: - Even   ): Li_int and Doduc_FP
- Odd (   ): Espresso_int and Spice_FP
 Two prediction state machines. Use second least significant digit of ID*: - Even:Class state machine (Figure 3) and State Machines A (Figure 4) - Odd: Class state machine (Figure 3) and State Machines B (Figure 5)
 Total number of instructions executed: instruction count (IC).
 Number of hits (Hit): number of times a branch is found in BTB.
 Number of misses (Miss): number of times a branch is not found in BTB.
 Number of right predictions (Right): number of times the prediction is right.
 Number of wrong predictions (Wrong) ): number of times the prediction is wrong.
 Number of taken branches/jumps (B_Taken)
 Number of collisions (Collisions): number of times a branch displaces a branch in
BTB.
 Number of wrong address predictions (Wrong_addr): A wrong addres is when a
branch is predicted (as taken) but the address is not right.
 Hit rate: This is defined as follows
𝐻𝑖𝑡 𝑟𝑎𝑡𝑒 (%) = 𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 h𝑖𝑡𝑠
(𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 h𝑖𝑡𝑠) + (𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑚𝑖𝑠𝑠𝑒𝑠)
 Prediction accuracy:
𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦 (%) = 𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑐𝑜𝑟𝑟𝑒𝑐𝑡 (𝑟𝑖𝑔h𝑡) 𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑖𝑜𝑛𝑠
(𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 h𝑖𝑡𝑠)
 Incorrect address (%)
𝐴𝑑𝑑𝑟𝑒𝑠𝑠_𝑤𝑟𝑜𝑛𝑔 (%) = 𝑊𝑟𝑜𝑛𝑔_𝑎𝑑𝑑𝑟
(0, 2, 4, 6 or 8
1, 3, 5, 7 or 9
   (𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑤𝑟𝑜𝑛𝑔 𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑖𝑜𝑛𝑠)
  Taken
  00
Predicted Taken
Initial state
11
Predicted not Taken
Not taken
Taken
Not taken
Taken
01
Predicted Taken
     Taken
Predicted not Taken
Not taken
   10
     Not taken
Figure 3. Class Prediction State Machine
 
    T
00
Initial state
T
01
   Prediction
T: Taken NT: Not taken
     Actual Branch
Taken Not taken
       NT NT
10 11
Figure 4. Prediction State Machine A.
     T
00
NT
10
T
01
NT
11
Initial state
    Prediction
T: Taken NT: Not taken
    Actual Branch
Taken Not taken
        Figure 5. Prediction State Machine B.
 
                 Deadlines
Deadline
April 12 (11:59 pm)
BTB w/ branches
April 19 (11:59 pm)
BTB w/ predictions
Monday, May 1
Project Report
Items
A list of branches (PC and Target) and their entry number in BTB. (See Appendix A, below). Program code needs be included as a file.
The trace sample is used (11,154 addresses).
Mid-project report using sample trace.
This will include the status of BTB with prediction at the end of the run. (See Appendix B, below)
Project report with all the results (11:59 pm). An outline of the report will be provided at a later time.
(Final exam 11am - 12noon.)
Grade
10 points
10 points 80 points
               Appendix A. BTB entries with PC and Target PC. Please include only entries with content.
42E01C 42E028 42E02C 42B30C :: 422FE8 4230A8
Appendix B. BTB entries with PC, Target PC, and Prediction.
42E01C 42E028 00 42E02C 42B30C 00
::: 422FE8 4230A8 00
 Entry PC Target
   
 0
423000
425E40
   
7
423020
4230A8
8
11
423038
425E40
14
:
:
:
:
1018
    Entry PC Target
Pred.
    
  0
423000
425E40
00
    
7
423020
4230A8
00
8
11
423038
425E40
00
14
:
:
:
:
:
1018
   
