A = 0
for k in range(1, 11):
    A += k

B = 0
for k in range(1, 11):
    B += k**3

C = 1
for k in range(1, 11):
    C *= k

D = 0.0
for k in range(1, 11):
    D += 1 / (k**2)

print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")
print(f"D = {D}")