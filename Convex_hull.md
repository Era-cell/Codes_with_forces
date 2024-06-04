# 1. Graham scan

 * Find first point i.e, bottom most
 * Sort all others relative to angle for bottom most
 * Use stack to go over points and pop if new point makes clockwise angle with present line
   ** Using Cross Product. Cross product is negative if new vertex x makes clockcwise angle with stk.top(), stk[-2]. i.e line segment formed by x,stk[-1] and stk[-1],stk[-2]
O( N + N*log(N) + N)
   
![image](https://github.com/Era-cell/Codes_with_forces/assets/77973415/03b97b83-c064-4ccd-8a36-a5621df3ede0)


# 2. Jarvis march

- Start from bottom most
- Iterate over all and choose the point which makes the most acute angle with the present line segment as X-axis, OR can say most convex angle relative to itself.
O( N*H ) - H is points in the Hull
