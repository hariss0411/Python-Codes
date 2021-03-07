# Hello World program in Python
d={}
d["match1"]={}
d["match2"]={}
d["match3"]={}
d["match3"]["kohli"]=50
d["match3"]["dhoni"]=330
d["match1"]["kohli"]=120
d["match2"]["kohli"]=80
d["match1"]["dhawan"]=12
d["match2"]["dhawan"]=8
t={}
for match in d.keys():
    for player in d[match].keys():
        t[player]=0
        for mat in d.keys():
            if player in d[mat].keys():
                t[player]+=d[mat][player]
#print(sorted(t.values(False)))
#sorted(list(t.values()),reverse=False)
m=(max(for x in t[] )
if m in t.values():
    print(t.key())
#print(str(m),t[m])

#help(max)
