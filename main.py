import os
import io
import time

# Ez a rész csak egyszer fut le az induláskor
print("A program sikeresen elindult a Railway-en!")

# Ez a rész a végtelenségig ismétlődik
while True:
    print("A szerver aktív és a kód fut...")
    time.sleep(60) # Vár 60 másodpercet a következő kiírásig, hogy ne pörgesse túl a gépet
