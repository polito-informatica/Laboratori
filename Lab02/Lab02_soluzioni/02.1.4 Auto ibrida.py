# Esercizio 02.1.4
# Auto ibrida

COSTO_AUTO_NUOVA = 15000 # €
KM_PER_ANNO = 30000 # km
COSTO_CARBURANTE = 2.00 # €/l
EFFICIENZA = 12 # km/l
VALORE_RIVENDITA = 6000 # €

# NOTA: modificare il programma in modo che sia l'utente a inserire i valori delle costanti sopra definite

costo_km = COSTO_CARBURANTE/EFFICIENZA # €/km
costo_annuo = KM_PER_ANNO * costo_km # €/anno

costo_5_anni = COSTO_AUTO_NUOVA + 5 * costo_annuo - VALORE_RIVENDITA

print('Costo totale in 5 anni = ', costo_5_anni, '€')