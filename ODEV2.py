import pandas as pd

sozluk = {"Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],

  "Ürün" : ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],

"Fiyat" : [300,180,450,50,700,400,150,80,850,900]}

magaza=pd.DataFrame(sozluk)
print(magaza.loc[2,"Kategori"])
print(magaza[2:3]["Kategori"])
magaza.index=["a","b","c","d","e","f","g","h","i","j"]
print(magaza[2:3]["Ürün"])
print(magaza[4:])
print(magaza[1:7]["Ürün"])
print(magaza[["Ürün"]][magaza["Kategori"]=="Giyim"])
print(magaza[["Ürün"]][magaza["Kategori"]=="Ayakkabı"])
print(magaza[["Ürün"]][magaza["Kategori"]=="Aksesuar"])
print(magaza[magaza["Fiyat"]>300])
print(magaza[(magaza["Fiyat"]>300) &(magaza["Kategori"]=="Giyim")])
print(magaza[(magaza["Fiyat"]<600) &(magaza["Kategori"]=="Ayakkabı")])
print(magaza[(magaza["Fiyat"]>100) &(magaza["Kategori"]=="Aksesuar")])



