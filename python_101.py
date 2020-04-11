9 #integer
9.2 #float
"Zeus" #string
print("Hades") #also string
type(8) #type of (x), int
type("Kratos") #str
"a" + "b" #ab
"a" " b" #a b
"a "*3 #a a a

#method
boi = "atreus"
len(boi) #6
len("atreus") #6
a = 8
b = 9
a*b #72

#upper() lower()
boi.upper() #kratos is shouting... "ATREUS"
boi.lower() #kratos is calm. "atreus"

boi.islower()
B = boi.upper()
B.islower()
B.isupper()

#replace()
boi.replace("r", "z") #"atzeus"
boi #replacing does not change the original one."atreus"

#strip()
black_hole = "  spaces will be gone  "
black_hole.strip() #baş ve sondaki boşluklar gider

#methods again!
dir(boi)
boi.capitalize() #"Atreus"

#substrings
quote = "Simplicity_is_the_ultimate_sophistication."
len(quote)
quote [40]
quote [0:10]
quote [11:13]

#variables
z =  941
y = "go_to_the_gym"
z*2
type(1881)
type(1881.1919)
type(2+1j)

#type change

#first_num = input()
#second_num = input()

#type(first_num)
#first_num+second_num
#int(first_num) + int(second_num)
int(3.1415)
float(22)
type(str(10))

#print
print("python_101")
print("hello","universe", sep = "_")

#data types

#Lists mutable
#[]
#list()

ListofN =[90,100,110] #list num,str içerebilir.
type(ListofN)

ls = ["a", 22.6, 34]
ls2 = [ListofN, 3, "b", 33.2]
len(ls2)

type(ls2[0]) #int
type(ls2[1]) #list
type(ls2[2]) #str
type(ls2[3]) #float

ls3 = [ls, ls2]
print(ls3)

#del ls3 

rakamlar = [0,1,2,3,4,5,6,7,8,9]
rakamlar [3]

rakamlar [0:2] #0,1
rakamlar [:2] #0,1
rakamlar [2:] #2,3,4,5,6,7,8,9
rakamlar [2::2] #2,4,6,8
rakamlar [2:8] #2,3,4,5,6,7
 
listinlist = ["b", 2, [3,4,5,6]]
listinlist [2][2] #5

#listeler ekle sil değiştir

isimler = ["Ali", "Melisa", "Kaan", "Aleyna"]

isimler[1] = "Helin"

isimler

isimler[1] = "Melisa"

isimler[0:3] ="Mert", "Yigit", "Berke"
isimler

isimler = ["Ali", "Melisa", "Kaan", "Aleyna"]

isimler = isimler + ["Mert"]
isimler

del isimler[4]
isimler

#liste metodları

yazarlar = ["Jane Austen","Virginia Woolf","Margaret Atwood"]

dir(yazarlar)

yazarlar

#append eklemek listelerde değişiklik yapılabilir
#yeniden atama yapmadan append metodu ile ekledik

yazarlar.append("J. K. Rowling")

yazarlar

yazarlar.append("ali")

yazarlar

yazarlar.remove("ali")

yazarlar

#insert
yazarlar = ["Jane Austen","Virginia Woolf","Margaret Atwood"]

yazarlar.insert(0, "J. K. Rowling")

yazarlar

#sona ekleme 

#yazarlar.insert(len(yazarlar)"Elif Şafak")

#pop

yazarlar.pop(0)

yazarlar

#count

markalar = ["Apple","Samsung","Sony","Nokia","Apple"]

markalar.count("Apple")
markalar.count("Sony")

#copy

markalar_yedek = markalar.copy()

markalar_yedek

#extend

markalar.extend(["t","l",13])

markalar

#index()

markalar.index("Sony")

#reverse()

markalar.reverse()

markalar

#sort() sadece sayılar için

sy = [3,92,56,23]
sy.sort()
sy

#clear()

sy.clear()
sy

#TUPLE değiştirilemez, immutable

t = ("kral", "kralice", 1,2,3.4,[5,6,7,8])
t

t2 = "kral", "kralice", 1,2,3.4,[5,6,7,8]
t2

t3 = ("prens",) #sonda virgül yoksa type str, varsa tuple
type(t3)

t[2] 
#elemanlara erişme listeler ile aynı

# t[2] = 99 yapılamaz, değiştirilemez

#Veri Yapıları - Dictionary(Sözlük) 
#kapsayıcı, sırasız, değiştirilebilir, sıralama yapılamaz
#key value konsepti vardır.

sozluk = {"TR" : "Türkce",
          "ENG": "İngilizce",
          "FR": "Fransizca"}

sozluk

len(sozluk)

basamaklar ={"Onlar": "10-99", "Yüzler": "100-999",
             "Binler": "1000-9999"} 
#shift ok tuşları kolay seçme


sozluk = {"TR" : ["Türkce", 1],
          "ENG": ["İngilizce",2],
          "FR": ["Fransizca",3]}

sozluk

#sözük eleman işlemleri


sozluk = {"TR" : "Türkce",
          "ENG": "İngilizce",
          "FR": "Fransizca"}

# sozluk[2] çalışmaz

sozluk["ENG"] #eleman seçimi key üzerinden yapılır


sozluk2 = {"Sebze": { "Havuc": 1,
                      "Fasulye": 2,
                      "Bezelye": 3},

          "Meyve":  { "Muz": 1,
                      "Cilek": 2,
                      "Kiraz": 3},   
                     
          "Cicek":  { "Kana": 1,
                      "Gala": 2,
                      "Begonya": 3}}

sozluk2

sozluk2["Meyve"]["Kiraz"]


#Eleman ekleme ve değiştirme

sozluk = {"TR" : "Türkce",
          "ENG": "İngilizce",
          "FR": "Fransizca"}

sozluk["SP"] = "İspanyolca"
sozluk

#yoksa ekliyor

sozluk["FR"] = "French"
sozluk

#varsa değiştiriyor

sozluk[1] = "Almanca"
sozluk

l = [2,3]
l

sozluk["l"] = l
sozluk

t = ("tuple",)

sozluk[t] = "new"
sozluk

#setler-kümeler
#sırasız, değerler eşsiz, mutable, farklı tipler olabilir.

#set

s = set()
s

l = [1,"h", "j",321]
s = set(l)
s

t = ("jane", "claudia")

s = set(t)
s

kid = "listen close"
type(kid)

s = set(kid)
s

l = ["t", "t", "t22", "t222", "t2"]

l

s = set(l)
s

len(s)

l[0]

#s[0] 

#eleman ekleme ve çıkarma

l = ["crysis","crytech"]

s = set(l)
s

dir(s)

s.add("cryengine")
s

s.add("crysis4?")
s

s.remove("crysis4?")
s

#setler - küme işlemleri

# =============================================================================
# difference ile kümenin farkı 
# intersaction() iki küme kesişimi
# union() birleşimi
# symmetric_difference() iki kümede de bulunmayanlar
# =============================================================================

#difference()

set1 = set([1,2,5])
set2 = set([1,2,3,4])

set1.difference(set2) #5

set2.difference(set1) #3,4

set1.intersection(set2) #1,2
set2.intersection(set1) #same result 1,2

set1.symmetric_difference(set2) #3,4,5
#birbirlerinden farklı sahip olduğu değerler.

set1.union(set2) #1,2,3,4,5

set1 & set2 #same as intersaction 1,2


#setlerde sorgu

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

#iki kümenin kesişimi boş mu değil mi

set1.isdisjoint(set2)

#küme elemanları başka bir kümede var mı

set1.issubset(set2)

#bir küme diğer kümeyi kapsıyor mu

set2.issuperset(set1)

# ======================================================
#listeler; değiştirilebilir, sıralı ve kapsayıcı.
#tuple; değiştirilemez, sıralı ve kapsayıcı.
#sözlük; değiştirilebilir, sırasız, kapsayıcı.
#setler; değiştirilebilir, sırasız+eşsiz, kapsayıcı.
# ======================================================