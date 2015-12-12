"""

Problem Statement

You are given a string S. Your task is to capitalize each word of S.

Input Format

A single line of input containing the string, S.

Constraints

0<len(S)<1000
The string consists of alphanumeric characters and spaces.

Output Format

Print the capitalized string, S.

Sample Input

hello world
Sample Output

Hello World


"""

a = raw_input().split(' ')

for i,c in enumerate(a):
    if c != '':
        k = list(c)
        k[0] = k[0].upper()
        a[i] = ''.join(k)

print ' '.join(a)