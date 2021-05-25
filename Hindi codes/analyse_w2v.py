import gensim
import gensim.models.keyedvectors as word2vec
model = word2vec.KeyedVectors.load_word2vec_format('hindi_w2v_embeddings.bin', binary=True, unicode_errors='ignore')

import pickle
relations=pickle.load(open('../Gold Data/Hindi/Hindi/Pickle/hindi_relations.p', 'rb'))
antonyms=pickle.load(open('../Gold Data/Hindi/Hindi/Pickle/hindi_antonyms.p', 'rb'))
plural_hindi=pickle.load(open('../Gold Data/Hindi/Hindi/Pickle/hindi_plurals.p', 'rb'))
verbfem=pickle.load(open('../Gold Data/Hindi/Hindi/Pickle/hindi_verb_fem.p', 'rb'))
verbmasc=pickle.load(open('../Gold Data/Hindi/Hindi/Pickle/hindi_verb_masc.p', 'rb'))
score=[0,0,0,0,0]
tot=0
ant_skipped=0
plu=0
rel=0
vfem=0
vmasc=0
for x in antonyms:
    a=x[0]
    b=x[1]
    c=x[2]
    d=x[3]
    if a in model and b in model and c in model:
        d_prime=model.most_similar(negative=[a], positive=[b,c])[0][0]
        print("\t- LOGIC:   " + a + ":" + b + " :: " + c + ": " + d)
        print("\t- ANALOGY: " + a + ":" + b + " :: " + c + ": " + d_prime)
        print()
        tot+=1
        if d == d_prime:
            score[0]+=1
    else:
        ant_skipped+=1
for x in plural_hindi:
    a=x[0]
    b=x[1]
    c=x[2]
    d=x[3]
    if a in model and b in model and c in model:
        d_prime=model.most_similar(negative=[a], positive=[b,c])[0][0]
        print("\t- LOGIC:   " + a + ":" + b + " :: " + c + ": " + d)
        print("\t- ANALOGY: " + a + ":" + b + " :: " + c + ": " + d_prime)
        print()
        tot+=1
        if d == d_prime:
            score[1]+=1
    else:
        plu+=1

for x in relations:
    a=x[0]
    b=x[1]
    c=x[2]
    d=x[3]
    if a in model and b in model and c in model:
        d_prime=model.most_similar(negative=[a], positive=[b,c])[0][0]
        print("\t- LOGIC:   " + a + ":" + b + " :: " + c + ": " + d)
        print("\t- ANALOGY: " + a + ":" + b + " :: " + c + ": " + d_prime)
        print()
        tot+=1
        if d == d_prime:
            score[2]+=1
    else:
        rel+=1
            

for x in verbfem:
    a=x[0]
    b=x[1]
    c=x[2]
    d=x[3]
    if a in model and b in model and c in model:
        d_prime=model.most_similar(negative=[a], positive=[b,c])[0][0]
        print("\t- LOGIC:   " + a + ":" + b + " :: " + c + ": " + d)
        print("\t- ANALOGY: " + a + ":" + b + " :: " + c + ": " + d_prime)
        print()
        tot+=1
        if d == d_prime:
            score[3]+=1
    else:
        vfem+=1

for x in verbmasc:
    a=x[0]
    b=x[1]
    c=x[2]
    d=x[3]
    if a in model and b in model and c in model:
        d_prime=model.most_similar(negative=[a], positive=[b,c])[0][0]
        print("\t- LOGIC:   " + a + ":" + b + " :: " + c + ": " + d)
        print("\t- ANALOGY: " + a + ":" + b + " :: " + c + ": " + d_prime)
        print()
        tot+=1
        if d == d_prime:
            score[4]+=1

    else:
        vmasc+=1
print("antonyms accuracy ",score[0])
print("plural accuracy ", score[1])
print("relations accuracy " , score[2])
print("feminine verb accuracy " , score[3])
print("male verb accuracy " , score[4])

print(tot)
print(ant_skipped)
print(plu)
print(rel)
print(vfem)
print(vmasc)
