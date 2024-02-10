# data_extraction
Imenovana entitetska identifikacija

Ovaj program koristi spaCy, popularnu biblioteku za obradu prirodnog jezika (NLP), kako bi 
identifikovao imenovane entitete u tekstu. Imenovani entiteti su posebne vrste riječi u tekstu, kao što su
imena osoba, mjesta, organizacija i drugih ključnih informacija.
SPACY je open-source biblioteka za obradu prirodnog jezika napisana u programskom jeziku Python. 
Ona pruža alate za različite zadatke u području NLP-a, uključujući tokenizaciju, lematizaciju, 
prepoznavanje entiteta, analizu relacija između riječi i druge korisne funkcionalnosti. 
U ovom programu koristi se spaCy model `hr_core_news_sm`. To je model za hrvatski jezik smanjene 
veličine (small) koji dolazi s osnovnim sposobnostima obrade teksta. Ovaj model uključuje 
prepoznavanje imenovanih entiteta, što znači da je posebno dobar za identifikaciju osoba, mjesta, 
organizacija i drugih entiteta u tekstu.
Program omogućava korisniku unos teksta putem grafičkog korisničkog interfejsa (GUI) ili učitavanje 
teksta iz datoteke. Nakon unosa ili učitavanja teksta, koristi se spaCy model za analizu teksta i 
prepoznavanje imenovanih entiteta.
Program koristi Tkinter, standardni Python modul za izradu grafičkog korisničkog interfejsa. Tkinter 
olakšava izradu prozora, gumba i polja za unos teksta kako bi korisnik mogao lako interagovati s 
programom.

Kako Koristiti Program:
1. Unos Teksta: Korisnik može ručno unijeti tekst u polje za unos teksta.
2. Analiza Teksta: Klikom na "Analiziraj Tekst" program će koristiti spaCy model za analizu unesenog 
teksta te prikazati identifikovane imenovane entitete i njihove tipove u rezultatnom polju.
3. Učitavanje Teksta iz datoteke: Klikom na "Učitaj Tekst iz datoteke" korisnik može odabrati tekstualnu 
datoteku, a program će učitati njen sadržaj u polje za unos teksta.
4. Rezultati: Identifikovani imenovani entiteti i njihovi tipovi bit će prikazani u rezultatnom polju.
Autor: Siniša Jelisavac
