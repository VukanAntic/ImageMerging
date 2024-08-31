# Image merging


# :memo: Opis aplikacije

Image Merging je aplikacija napravljena u okviru kursa Mašinskog učenja na master studijama Matematičkog fakulteta. Aplikacija je namenjena da za zadate dve slike, sa razmakom između, spoji prazan prostor, tako da izgleda kao celina. 
Naknadno smo dodali opciju tako da imamo unutrašnjost slike, a model će proširiti tu sliku spolja. 

# :books: Korišćene tehnologije

1. **Programski jezik:** 
   - Python

2. **Skup podataka:**
   - https://www.kaggle.com/datasets/puneet6060/intel-image-classification/data

# :books: Korišćena literatura:

1. [Generative Deep Learning, David Foster, O'Reilly Media, Inc., 2nd Edition](https://www.oreilly.com/library/view/generative-deep-learning/9781098134174/)

2. [Tensorflow-ov tutorijal vezan za pix2pix](https://www.tensorflow.org/tutorials/generative/pix2pix)
  
# 🛠️ Instalacije i pokretanje

Sve potrebne biblioteke koje su korišćene u toku izrade projekta se nalaze u `requirements.txt`, i možete ih instalirati pokretanjem sledećih komandi:

```
sudo apt-get update
sudo apt-get install python3.6
sudo apt-get install python3-pip
pip install -r requirements.txt
```

# Istrenirani modeli:
-  https://drive.google.com/drive/folders/108du_DMhl00KozMGHTOTjSygIEir_jYh?usp=sharing
-  https://drive.google.com/drive/folders/18BYvsyPY3wz8JsboLbi-F0iBAL44tO3V?usp=sharing


Da biste izabrali spajanje dve fotografije, potrebno je da u `11`-om bloku koda promenite:

```
blackout_area_type = BLACKOUT_AREA_TYPE.HORIZONTAL
```

### Pokretanje aplikacije:

U direktorijumu `./src` pokrenuti sledeće komande:

```jupyter notebook```

i zatim pokretati ćelije sveski u redosledu označenim u imenima fajlova.

# 💻 Projekat radili
- Katarina Dimitrijević 1080/2022
- Vukan Antić 1071/2022
