def allparams(a,b,/,c=42, *args,d=256,**kwargs):
    print("a,b",a,b)
    print("c,d", c, d)
    print("args", args)
    print("kwargs", kwargs)

allparams(1,2)
allparams(1,2,3)
allparams(1,2,3,4)
allparams(1,2,3,4,5)
allparams(1,2,3,4,5,6,7,8,9)
allparams(1,2,3,4,5,6, d=100)
allparams(1,2,3,4,5,6, d=100, e=5456, name="Radek")
#allparams(a=1, b=2)

#jesli mamy / w argumentach
# a i b musimy przekazac obowiazkowo jako rg pozycyjne

allparams(1,2)
allparams(1,2,c=9)
allparams(1,2,a=5, b=9)
