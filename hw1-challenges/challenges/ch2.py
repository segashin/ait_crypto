
#%%
s = "Uqzwhppahp pzywp tg outcdv pawaqqzk zaqzaaa. Luweaav ptn oivxazzovupwg aaq slv pqzxwq az rtn snpxgwpxspv. Ptn oboyqppwz xp upan xqzensr saxqzi ee nrxywkyqvy vk sli pwyqtlpgeqrlp. Cl pq yq weywywp, ttnz rtn negeywywp zqpqrosvlaa qrwgy upxwvl oe vgienv lz rtn etcwvlaa ywixqyywp ttn 'Giwnyzi' vliivvy cslc. Slo yawgeznosq ls xzq imvcgiizv ptnnepsne slv yvuv vp ievlunqne yq yweonouzywvuo.B"
s = s.replace(" ", "")
s = s.lower()
print(s)

# %%
#single letter ver
d = {}
for c in s:
    c = c.lower()
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

#%%
#double letter ver
d = {}
if len(s)%2 == 1:
    s += "x"
for i in range(0,len(s),1):
    ss = s[i:i+2]
    if ss in d:
        d[ss] += 1
    else:
        d[ss] = 1
print(d)
#{'U': 1, 'q': 23, 'z': 20, 'w': 24, 'h': 2, 'p': 28, 'a': 20, ' ': 57, 'y': 22, 't': 14, 'g': 9, 'o': 12, 'u': 9, 'c': 5, 'd': 1, 'v': 24, 'k': 3, '.': 5, 'L': 1, 'e': 17, 'n': 21, 'i': 13, 'x': 11, 's': 12, 'l': 15, 'r': 8, 'P': 1, 'b': 1, 'C': 1, ',': 1, "'": 2, 'G': 1, 'S': 1, 'm': 1, 'B': 1}
#{'u': 10, 'q': 23, 'z': 20, 'w': 24, 'h': 2, 'p': 29, 'a': 20, ' ': 57, 'y': 22, 't': 14, 'g': 10, 'o': 12, 'c': 6, 'd': 1, 'v': 24, 'k': 3, '.': 5, 'l': 16, 'e': 17, 'n': 21, 'i': 13, 'x': 11, 's': 13, 'r': 8, 'b': 2, ',': 1, "'": 2, 'm': 1}

#%%
d_freq = {}
for k in d.keys():
    d_freq[k] = d[k]/len(s)*100
print(d_freq)

#{'uq': 1, 'qz': 6, 'zw': 1, 'wh': 1, 'hp': 2, 'pp': 3, 'pa': 3, 'ah': 1, 'pz': 2, 'zy': 2, 'yw': 10, 'wp': 5, 'pt': 5, 'tg': 1, 'go': 1, 'ou': 2, 'ut': 1, 'tc': 2, 'cd': 1, 'dv': 1, 'vp': 5, 'aw': 2, 'wa': 1, 'aq': 4, 'qq': 1, 'zk': 1, 'kz': 1, 'za': 2, 'aa': 6, 'a.': 1, '.l': 1, 'lu': 2, 'uw': 1, 'we': 3, 'ea': 1, 'av': 1, 'tn': 8, 'no': 4, 'oi': 1, 'iv': 2, 'vx': 1, 'xa': 1, 'az': 2, 'zz': 1, 'zo': 1, 'ov': 1, 'vu': 3, 'up': 3, 'pw': 3, 'wg': 3, 'ga': 1, 'qs': 1, 'sl': 5, 'lv': 2, 'pq': 3, 'zx': 2, 'xw': 2, 'wq': 1, 'qa': 1, 'zr': 3, 'rt': 3, 'ns': 2, 'sn': 2, 'np': 1, 'px': 3, 'xg': 1, 'gw': 1, 'xs': 1, 'sp': 1, 'pv': 1, 'v.': 1, '.p': 1, 'ob': 1, 'bo': 1, 'oy': 2, 'yq': 5, 'qp': 2, 'wz': 1, 'xp': 1, 'pu': 1, 'an': 1, 'nx': 1, 'xq': 3, 'ze': 1, 'en': 3, 'sr': 1, 'rs': 1, 'sa': 1, 'ax': 1, 'zi': 2, 'ie': 3, 'ee': 1, 'nr': 1, 'rx': 1, 'xy': 1, 'wk': 1, 'ky': 1, 'qv': 1, 'vy': 3, 'yv': 2, 'vk': 1, 'ks': 1, 'li': 2, 'ip': 1, 'wy': 3, 'qt': 1, 'tl': 1, 'lp': 3, 'pg': 1, 'ge': 3, 'eq': 1, 'qr': 3, 'rl': 1, 'p.': 1, '.c': 1, 'cl': 1, 'qy': 3, 'qw': 1, 'ey': 3, 'p,': 1, ',t': 1, 'tt': 2, 'nz': 1, 'nn': 2, 'ne': 5, 'eg': 1, 'zq': 2, 'ro': 1, 'os': 2, 'sv': 1, 'vl': 6, 'la': 2, 'rw': 1, 'gy': 1, 'yu': 1, 'wv': 3, 'lo': 2, 'oe': 1, 'ev': 2, 'vg': 1, 'gi': 3, 'nv': 1, 'lz': 1, 'et': 1, 'cw': 1, 'ay': 1, 'wi': 1, 'ix': 1, 'yy': 1, "n'": 1, "'g": 1, 'iw': 1, 'wn': 1, 'ny': 1, 'yz': 1, "i'": 1, "'v": 1, 'ii': 2, 'vv': 2, 'yc': 1, 'cs': 1, 'lc': 1, 'c.': 1, '.s': 1, 'ya': 1, 'ez': 1, 'zn': 1, 'sq': 1, 'ql': 1, 'ls': 1, 'sx': 1, 'xz': 1, 'qi': 1, 'im': 1, 'mv': 1, 'vc': 1, 'cg': 1, 'iz': 1, 'zv': 1, 'ep': 1, 'ps': 1, 'es': 1, 'uv': 1, 'pi': 1, 'un': 1, 'nq': 1, 'qn': 1, 'eo': 1, 'on': 1, 'uz': 1, 'uo': 1, 'o.': 1, '.b': 1, 'b': 1}
	
#th er on an re he in ed nd ha at en es of or nt ea ti to it st io le is ou ar as de rt ve

# %%
grid1 = [['x' for i in range(5)] for j in range(5)]
grid2 = [['x' for i in range(5)] for j in range(5)]
grid3 = [['x' for i in range(5)] for j in range(5)]
grid4 = [['x' for i in range(5)] for j in range(5)]
grids = [grid1,grid2,grid3,grid4]

# %%
import pprint
pprint.pprint(grid1)
pprint.pprint(grid2)
pprint.pprint(grid3)
pprint.pprint(grid4)

# %%
def decrypt(s, grids):
    for 
