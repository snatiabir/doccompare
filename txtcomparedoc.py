


"""just a simple comparison metric. give it a folder of .txt or .html files
(basically the folder CTools gives you, with every answer in its own file), and
it will return name pairs that pass a certain threshold"""


import nltk, os, argparse, docx


parser = argparse.ArgumentParser(description="find files similar according to \
a chosen metric")
#parser.add_arguement("metric", type=
parser.add_argument("-t", "--threshold", type=float, help="the threshold for the given metric", default=50)
parser.add_argument("-x", "--xgram", type=int, help="the window for ngram searches", default = 4)
parser.add_argument("-n", "--ngram", action="store_true", default=False)
parser.add_argument("-np", "--ngramp", action="store_true", default=False)
#if you wanted to add more metrics, put them here!
args = parser.parse_args()

path = os.getcwd()
docs = os.listdir(path)

def dumbfunct(a):
    
    print a + " is not a .docx file, and was removed from comparison"
    docs.remove(a)
    return

for x in docs:
    try: docx.Document(path+"/"+x)
    except: dumbfunct(x)

def doctext(location):
    dtxt = ""
    d = docx.Document(location)
    for x in d.paragraphs:
        dtxt+= x.text
    return dtxt

def ngramp(path, threshold, xgram):
    """finds overlapping ngrams between """
    nlist = [(x,set(nltk.ngrams(nltk.tokenize.wordpunct_tokenize(doctext(path+"/"+x)),xgram)))
         for x in docs]
    cdic = {}
    for x in nlist:
        cdic[x[0]]=[(y[0],float(len(x[1].intersection(y[1])))/len(x[1]))for y in nlist]
    for x in cdic.itervalues():
        x.sort(key = lambda y:y[1], reverse=True)
    for x, y in cdic.iteritems():
        z = filter(lambda a:a[1]>=threshold, y[1:])
        if z:
            for b in z:
                print x, b
                
    return

def ngram(path, threshold, xgram):
    """finds overlapping ngrams between """
    nlist = [(x,set(nltk.ngrams(nltk.tokenize.wordpunct_tokenize(doctext(path+"/"+x)),xgram)))
         for x in docs]
    cdic = {}
    for x in nlist:
        cdic[x[0]]=[(y[0],len(x[1].intersection(y[1])))for y in nlist]
    for x in cdic.itervalues():
        x.sort(key = lambda y:y[1], reverse=True)
    for x, y in cdic.iteritems():
        z = filter(lambda a:a[1]>=threshold, y[1:])
        if z:
            for b in z:
                print x, b
                
    return

if args.ngram:
    ngram(path, args.threshold, args.xgram)
if args.ngramp:
    ngramp(path, args.threshold, args.xgram)
    

