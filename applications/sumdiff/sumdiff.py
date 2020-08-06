"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6
    
table_with_totals_add = {}
table_with_totals_sub = {}
# Your code here

for ele in q:
    for next_ele in q:
        table_with_totals_add[(ele, next_ele)] = f(ele) + f(next_ele)
for ele in q:
    for next_ele in q:
        table_with_totals_sub[(ele, next_ele)] = f(ele) - f(next_ele)


for pair in table_with_totals_add.items():
    for other_pair in table_with_totals_sub.items():
        if pair != other_pair:
            reversed_tuple = (other_pair[0][1], other_pair[0][0])
            if pair[0] != reversed_tuple:
                if pair[1] == other_pair[1]:
                    print(f"{f(pair[0][0])} + {f(pair[0][1])} = {f(other_pair[0][0])} + {f(other_pair[0][1])}")
