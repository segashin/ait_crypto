
#%%
s =  "Fwa  L oatwnakry aoci eastenydnt dgo deta uS dhef pg amrialbtoonroy nmhtr t  aaiPhmHb oeeueiEurnsrtiss taat it cnhcahmlteineoesrt  us  ymbr oy eonlfomnu i uu nanwrsOd ei tr d dg  oe erbifa  eef d"
print(len(s))


# %%

max_try = 10
for j in range(1,max_try+1):
    ans = []
    for i in range(j):
        ans.append("")

    for i in range(len(s)):
        ans[i%j] = ans[i%j] + s[i]
    
    print("skip=", j, ans)

# %%
ans = []
j = 7
for i in range(j):
    ans.append("")

for i in range(len(s)):
    ans[i%j] = ans[i%j] + s[i]

print("skip=", j, ans)

# %%

