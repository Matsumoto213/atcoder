s = input()
a_index = []
z_index = []
 
for i in range(len(s)):
    if s[i] == 'A':
        a_index.append(i)
    
    if s[i] == 'Z':
        z_index.append(i)
 
a = min(a_index)
z = max(z_index)
print(z - a + 1)