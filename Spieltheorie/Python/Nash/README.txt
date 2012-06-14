Voraussetzung:
lp_solve f�r Python muss installiert sein:
http://lpsolve.sourceforge.net/5.5/Python.htm#Compile_the_lpsolve_driver

Ausf�hrung:
P1.1 (Einlesen von NFG-Dateien, API):
...
game = NfgReader.read(PfadZurNfg)
...

P1.2 (Reine NGs, API):
...
game.findPureNash()
...

P1.3 (Berechnung gemischter NGs), API:
...
game.findMixedNash()
...

Lesen, NG-Berechnung, Zeitmessung:
ausf�hren von "python P1Main <PfadZurNfg>" 