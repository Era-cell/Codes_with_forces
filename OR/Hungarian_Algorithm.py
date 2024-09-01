"""
Assigment of n machines for n jobs, 
such that minimum/maximum cost
   Job1 Job2 Job3 Job4 Job5
A   9    10   12   8    2
B   4    23   21   3    12
C   ...
D   ...
E   ...

For all the jobs atleast one machine is assigned or vise versa

Step 1: reduce rows
       - minus all element with smallest
       - row[i] = row[i]-min(row) for i in len(row)
Step 2: reduce columns
Step 3: If row has single 0, mark the column
         else, skip
Step 4: Same on column
Step 5: If no of marked 0's are == n, then that's the answer
      else, 
         take the smallest of all uncovered values, say minn
         subtract minn from unconvered values
         add minn to all intersections.
         Unmark all, and repeat from Step 3.
"""

