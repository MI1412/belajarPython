from string import Template
t = Template('${village} folk send $$10 $cause.')

# substitute
d = dict(village="konoha",cause="wakanda")
subst = t.substitute(d)
print(subst)

# safe_substitute
t = Template("mengembalikan item $item ke $pemilik")
d = dict(item="tas")
safe_substitute = t.safe_substitute(d)
print(safe_substitute)

