from tkinter import *



def algorithm(result, name, partner):
	name, partner = list(name.lower()), list(partner.lower())

	flames = {"F":"Friends", "L":"Lovers", "A":"Affectionate", "M":"Marriage", "E":"Enemies", "S":"Sibling"}
	similiar = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


	# chars
	sim = {}
	removes = {}
	for i in range(len(name)):
		if name[i] in sim:
			removes[name[i]].append(i)
			sim[name[i]]+=1
		else:
			removes[name[i]] = [i]
			sim[name[i]]=1
	for i in range(len(partner)):
		if partner[i] in sim:
			removes[partner[i]].append(i)
			sim[partner[i]]+=1
		else:
			removes[partner[i]] = [i]
			sim[partner[i]]=1

	



algorithm(None, "John", "joe")

