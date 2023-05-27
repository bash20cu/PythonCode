import pickle

listaNombre=["Pedro", "Ana", "Maria", "Isabel"]
ficheroBinario=open("ListaNombre", "wb")

pickle.dump(listaNombre, ficheroBinario)

ficheroBinario.close()
del (ficheroBinario)
