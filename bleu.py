import sacrebleu
from sacremoses import MosesDetokenizer
md = MosesDetokenizer(lang='en')

filegpt = 't1-gpt35.txt'
filellama = 't1-llama13b.txt'
filemistral = 't1-mistral.txt'
fileyandex = 't1-ygpt.txt'


# Open the test dataset human translation file and detokenize the references
refs = []

with open("test100.txt") as test:
    for line in test: 
        line = line.strip().split() 
        line = md.detokenize(line) 
        refs.append(line)
    
print("Reference 1st sentence:", refs[0])

refs = [refs]  # Yes, it is a list of list(s) as required by sacreBLEU


# Open the translation file by the NMT model and detokenize the predictions
preds1 = []
preds2 = []
preds3 = []
preds4 = []
preds5 = []

with open(filegpt) as pred:  
    for line in pred: 
        line = line.strip().split() 
        line = md.detokenize(line) 
        preds1.append(line)
with open(filellama) as pred:  
    for line in pred: 
        line = line.strip().split() 
        line = md.detokenize(line) 
        preds2.append(line)
with open(filemistral) as pred:  
    for line in pred: 
        line = line.strip().split() 
        line = md.detokenize(line) 
        preds3.append(line)
with open(fileyandex) as pred:  
    for line in pred: 
        line = line.strip().split() 
        line = md.detokenize(line) 
        preds4.append(line)
with open('t1-madlad.txt') as pred:  
    for line in pred: 
        line = line.strip().split() 
        line = md.detokenize(line) 
        preds5.append(line)



print("MTed 1st sentence:", preds3[0])

# Calculate and print the BLEU score
bleu1 = sacrebleu.corpus_bleu(preds1, refs)
bleu2 = sacrebleu.corpus_bleu(preds2, refs)
bleu3 = sacrebleu.corpus_bleu(preds3, refs)
#bleu4 = sacrebleu.corpus_bleu(preds4, refs)
#bleu5 = sacrebleu.corpus_bleu(preds5, refs)
print("Average BLEU score (GPT-3.5): " + str(bleu1.score))
print("Average BLEU score (LLaMa-13B): " + str(bleu2.score))
print("Average BLEU score (Mistral-7B): " + str(bleu3.score))
#print("Average BLEU score (YandexGPT): " + str(bleu4.score))
#print("Average BLEU score (MADLAD): " + str(bleu5.score))