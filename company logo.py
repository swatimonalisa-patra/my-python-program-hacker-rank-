# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter
for i in Counter(sorted(input())).most_common(3):
    print(*i)
