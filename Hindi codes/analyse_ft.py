import fasttext.util
import pickle
relations=pickle.load(open('../Gold Data/Hindi/Hindi/Pickle/hindi_relations.p', 'rb'))
antonyms=pickle.load(open('../Gold Data/Hindi/Hindi/Pickle/hindi_antonyms.p', 'rb'))
plural_hindi=pickle.load(open('../Gold Data/Hindi/Hindi/Pickle/hindi_plurals.p', 'rb'))
verbfem=pickle.load(open('../Gold Data/Hindi/Hindi/Pickle/hindi_verb_fem.p', 'rb'))
verbmasc=pickle.load(open('../Gold Data/Hindi/Hindi/Pickle/hindi_verb_masc.p', 'rb'))
score=[0,0,0,0,0]
ft=fasttext.load_model('cc.hi.300.bin')
for x in antonyms:
    a=x[0]
    b=x[1]
    c=x[2]
    d=x[3]
    d_prime = ft.get_analogies(b, a, c, k=1, on_unicode_error='strict')[0][1]
    print("\t- LOGIC:   " + a + ":" + b + " :: " + c + ": " + d)
    print("\t- ANALOGY: " + a + ":" + b + " :: " + c + ": " + d_prime)
    print()
    if d == d_prime:
        score[0]+=1

for x in plural_hindi:
    a=x[0]
    b=x[1]
    c=x[2]
    d=x[3]
    d_prime = ft.get_analogies(b, a, c, k=1, on_unicode_error='strict')[0][1]
    print("\t- LOGIC:   " + a + ":" + b + " :: " + c + ": " + d)
    print("\t- ANALOGY: " + a + ":" + b + " :: " + c + ": " + d_prime)
    print()
    if d == d_prime:
        score[1]+=1

for x in relations:
    a=x[0]
    b=x[1]
    c=x[2]
    d=x[3]
    d_prime = ft.get_analogies(b, a, c, k=1, on_unicode_error='strict')[0][1]
    print("\t- LOGIC:   " + a + ":" + b + " :: " + c + ": " + d)
    print("\t- ANALOGY: " + a + ":" + b + " :: " + c + ": " + d_prime)
    print()
    if d == d_prime:
        score[2]+=1

for x in verbfem:
    a=x[0]
    b=x[1]
    c=x[2]
    d=x[3]
    d_prime = ft.get_analogies(b, a, c, k=1, on_unicode_error='strict')[0][1]
    print("\t- LOGIC:   " + a + ":" + b + " :: " + c + ": " + d)
    print("\t- ANALOGY: " + a + ":" + b + " :: " + c + ": " + d_prime)
    print()
    if d == d_prime:
        score[3]+=1

for x in verbmasc:
    a=x[0]
    b=x[1]
    c=x[2]
    d=x[3]
    d_prime = ft.get_analogies(b, a, c, k=1, on_unicode_error='strict')[0][1]
    print("\t- LOGIC:   " + a + ":" + b + " :: " + c + ": " + d)
    print("\t- ANALOGY: " + a + ":" + b + " :: " + c + ": " + d_prime)
    print()
    if d == d_prime:
        score[4]+=1
print("antonyms accuracy ",score[0])
print("plural accuracy ", score[1])
print("relations accuracy " , score[2])
print("feminine verb accuracy " , score[3])
print("male verb accuracy " , score[4])
