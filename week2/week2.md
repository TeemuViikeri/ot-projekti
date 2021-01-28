------------------------------------------------------------------------------------------

# TEHTÄVÄT

------------------------------------------------------------------------------------------

## Armoton Aikamörkö, max 10 XP

###  Kuinka kauan laskenta kestää pahimmillaan (minuutin tarkkuudella), jos leveyteen ensin -haulla käydään läpi binääristä hakupuuta, jossa jokaisella solmulla on kaksi lasta, kunnes lopulta löydetään tavoitesolmu syvyydeltä 30 (30 askelta juuresta), kun oletetaan, että sekunnissa ehditään lisätä tutkittavien solmujen joukkoon 100 000 solmua? (Sen tutkimisen, onko löydetty tavoitesolmu, voi ajatella tapahtuvan ilmaiseksi. Jos solmu ei ole tavoitesolmu, tutkittavien solmujen joukkoa laajennetaan solmun lapsilla. Muuten pysähdytään.) Oletetaan, että muistia on riittävästi jne.

Puussa on 2^0 + 2^1 + 2^2 + ... + 2^n solmua. Kun n = tavoitesolmun syvyys eli 30, on puussa yhteensä 2 147 483 647 solmua. Sekunnissa tutkitaan 100 000 solmua, joten 30 tasoa tutkitaan noin 358 minuutissa.

------------------------------------------------------------------------------------------

## LiisaLuikero, max 10 XP

### Oletetaan, että säästösyistä TAMKin päärakennuksesta on poistettu käytöstä muut kuin kaksi kerrosta (katutaso ja toinen kerros). Myös portaat on tuhottu. Käytössä olevien kerrosten välillä pääsee liikkumaan ainoastaan yhdellä jäljelle jätetyllä hissillä, jonka maksimikuormitus on kaksi oliota. Jottei tuhlattaisi energiaa, voimassa on myös kielto liikutella hissiä kerrosten välillä tyhjänä.Liikkuvassa hississä tulee siis aina olla vähintään yksi ”matkustaja”. Hissistä ei voi poistua eikä siihen voi nousta kerrosten välillä.Hissi on katutasossa, ja siihen pyrkii samaan aikaan kolme opiskelijaa ja kolme mörköä. Kaikki siispyrkivät siirtymään toiseen kerrokseen. Saadaanko kaikki siirrettyä hissillä toiseen kerrokseen (niin, että lopulta kaikki opiskelijat ja möröt ovat siellä), ja jos saadaan, miten tämä tapahtuu, jos missään vaiheessa yhdessä paikassa (katutaso / hissi / toinen kerros) ei saa olla samaan aikaan enempää mörköjä kuin opiskelijoita – paitsi jos opiskelijoita ei ole paikassa ensinkään, jolloin mörköjen paikallinen ylivoima ei pelota ketään? Kun hissi saapuu kerrokseen, kaikki siinä olleet poistuvat aina. Hissiin astumiset ja siitä poistumiset voidaan ajatella atomisina operaatioina, joissa kaikki hississä olevat poistuvat kerralla hissistä tai kaikki hissiin nousevat astuvat siihen kerralla. Selvitä ohjelmallisesti ja raportoi lyhyesti ratkaisu tai sen puute.

Opiskelijat ja möröt saadaan siirrettyä siten toiseen kerrokseen 11 askeleella.

------------------------------------------------------------------------------------------

## J. Jokunen, max 10 XP

### Tutustu geneettisiin algoritmeihin ja selitä perusidea tiiviisti. Toteuta ohjelma, joka ratkaisee jonkinongelman geneettistä algoritmia käyttäen. Testaa ohjelmasi toimivuutta. Raportoi lyhyesti. Palauta myös kooditiedosto (ga.py).

*Vastaus*

------------------------------------------------------------------------------------------