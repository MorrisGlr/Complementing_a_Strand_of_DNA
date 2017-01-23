file = open('rosalind_revc.txt', 'r')                       #tells python to read a file
dna = file.readlines()
print(dna)                                    #we give all of the data in the file a name so that we can work with it. remember, the data is a one item list in this case
dnastring = ''.join(dna)                                    #convert list to string and joining everything
print(dnastring)
complement = {'A': 'T', 'C':'G', 'G':'C', 'T':'A'}          #this dictionary designates a key and value which I designated as the nucleotide commplement
listdna = list(dnastring)                                   #turn string into a list on pers character basis
listdna.remove('\n')                                        #remove the '\n' item at the end of the list because this messes up the list to string conversion
cDNAlist =[]                                                #this is an empty list that I will populate with the complementary nucleotide
for nucleotide in listdna:                                  #in a sense it scans for every item (in this case nucleotiides) withib the listdna
    addtocDNAlist = complement.get(nucleotide)              #the "get" function returns the value of the key within a dictionary. The values of the keys were designated as the nucelottide complement
    cDNAlist.append(addtocDNAlist)                          #addtocDNAlist is the name that I gave to the nucleotide complement that needs to be added to the empty list
reverse_complement = ''.join(cDNAlist)                      #the nucleotide coomplement list is in the proper order and now needs to be converted to a string
f=open('rosalind_cDNA_output.txt','w')
f.write(reverse_complement[::-1])                            #final step is it reverse the order of the sequence.[begin:end:step] by leaving begin and end as blank and the step as -1 to reverse the string
