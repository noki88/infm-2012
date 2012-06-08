Voraussetzung:
lp_solve für Python muss installiert sein:
http://lpsolve.sourceforge.net/5.5/Python.htm#Compile_the_lpsolve_driver

Ausführung:
P1.1 (Einlesen von NFG-Dateien):
...
game = NfgReader.read(PfadZurNfg)
...

P1.2 (Reine NGs):
...
game.findPureNash()
...

P1.3 (Berechnung gemischter NGs):
...
game.findMixedNash()
...

Lesen, NG-Berechnung, Zeitmessung:
ausführen von "python P1Main <PfadZurNfg>" 