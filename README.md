# Tähtisadetta

Elokuvien ensi-ilta arvosteluja

![Tähtisadetta, katsaus elokuvien ensi-ilta-arvosteluihin](./tahtisade-kansi-leikattu.svg)

Kerään teatterilevityksessä olevien elokuvien ensi-ilta-arvosteluja.

Miksi ihmeessä?

No, koska:

- tykkään käydä elokuvissa, joten arviot esitettävistä elokuvista kiinnostavat jo sinänsä
- harrastan ohjelmointia, joten arvostelut tarjoavat myös materiaalia omille projekteille. 

Arvostelut olen kerännyt lehdistä ja netistä.

Tämän repositoryn aineisto on minun puolestani vapaasti kaikkien aiheesta kiinnostuneiden käytettävissä.

Arvostelut löytyvät hakemistosta: DB

Aineisto koostuu seuraavista tiedostoista:

elokuvat.csv
- sisältää perustiedot tallennetuista elokuvista
- sarake id toimii tietueiden avainkenttänä

arvostelut.csv
- sisältää elokuvista kerätyt arvostelut
- sarake googleId toimii viiteavaimena elokuvat sisältävään taulukkoon

Näin ollen arvostelua koskevan elokuvan tiedot löytyy, kun etsii elokuvat taulukosta rivin jonka id-sarakkeen arvo vastaa arvostelun googleId-sarakkeen arvoa.

Esim. 
- jos googleId on 17, on kyseessä elokuvaa Just Mercy koskeva arvostelu

genret.csv
- sisältää kunkin elokuvan lajityyppi luokituksen
- tiedot ovat peräisin imdb:stä
- sarake googleId kertoo mistä elokuvasta on kyse

kasikirjoitus.csv
- sisältää tietoa kunkin elokuvan käsikirjoittajista
- tiedot ovat peräisinelonet.finna.fi -palvelusta
- sarake googleId kertoo mistä elokuvasta on kyse

levittaja.csv
- sisältää tietoa kunkin elokuvan levityksestä vastaavasta yhtiöstä
- tiedot ovat peräisinelonet.finna.fi -palvelusta
- sarake googleId kertoo mistä elokuvasta on kyse

nayttelijat.csv
- sisältää listauksen kunkin elokuvan näyttelijöistä
- tiedot ovat peräisinelonet.finna.fi -palvelusta
- sarake googleId kertoo mistä elokuvasta on kyse

ohjaajat.csv
- kertoo kuka elokuvan ohjasi
- tiedot ovat peräisinelonet.finna.fi -palvelusta
- sarake googleId kertoo mistä elokuvasta on kyse



