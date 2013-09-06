# NLP Programming Assignment #3
# NaiveBayes
# 2012

#
# The area for you to implement is marked with TODO!
# Generally, you should not need to touch things *not* marked TODO
#
# Remember that when you submit your code, it is not run from the command line 
# and your main() will *not* be run. To be safest, restrict your changes to
# addExample() and classify() and anything you further invoke from there.
#


import sys
import getopt
import os
import math

import GetSegFromIO

class NaiveBayes:
    ###Sub class definition

    class Example:
        """Represents a document with a label. klass is 'pos' or 'neg' by convention.
        words is a list of strings.
        """
        def __init__(self):
            self.klass = ''
            self.words = []


    class Model:
        """Represents a document with a label. klass is 'pos' or 'neg' by convention.
           words is a list of strings.
        """
        def __init__(self,klass):
            self.klass = klass
            self.example_num = 0
            self.word_cnt = {}
            self.total_word_cnt = 0

    #####
    # Class NavieBayes Function

    def __init__(self):
        self.trainData = []
        self.testData = []
        self.typeDict = {}
        self.stopList = []

        self.Models = {}
        self.total_example_num = 0

    def train(self):
        for example in self.trainData:
            klass = example.klass
            #print "klass = "+ klass
            self.Models[klass].example_num += 1
            self.total_example_num += 1

            for w in example.words:
                #print "+++" + w + "+++"
                self.Models[klass].total_word_cnt += 1
                if w not in self.Models[klass].word_cnt:
                    self.Models[klass].word_cnt[w] = 1
                else:
                    self.Models[klass].word_cnt[w] += 1



    #############################################################################
  # TODO TODO TODO TODO TODO 
    def classify(self):
        correct_cnt = 0
        wrong_cnt = 0

        for example in self.testData:
            testlabel = self.classifyOneCase(example.words)
            if testlabel == example.klass:
                correct_cnt += 1
                print "=========wrong case===========\n",example.klass,"\n", example.words

            else:
                wrong_cnt += 1

        print "result is :"
        print correct_cnt
        print wrong_cnt
        print ( (float)(correct_cnt) / (correct_cnt+wrong_cnt) )

    def classifyOneCase(self, words):
        """ TODO
        'words' is a list of words to classify. Return 'pos' or 'neg' classification.
        """

        maxPrability = -10000000000000
        label = 'None'

        word_uniq_cnt = 300000

        for klass in self.Models.keys():
            print "classifyOneCase", klass
            print self.Models[klass].example_num
            print self.total_example_num
            
            #print klass
            prabilityOfClass = math.log(float(self.Models[klass].example_num) / self.total_example_num)
            print "prabilityOfClass=",prabilityOfClass

            prabilityOfWords = 0
            for w in words:

                if w in self.Models[klass].word_cnt:
                    prabilityOfWords += math.log(float(self.Models[klass].word_cnt[w] + 1) / (self.Models[klass].total_word_cnt + word_uniq_cnt))
                else:
                    prabilityOfWords += math.log(1.0 / word_uniq_cnt)

                result = prabilityOfClass + prabilityOfWords

            print "result=",result
            if result > maxPrability:
                maxPrability = result
                label = klass
        #print "label:" + label


        return label



    def getItemType(self, itemhash):
        return self.typeDict[itemhash];


    def loadItemData(self, dirname, flag):
        filelist = os.listdir(dirname)
        for fileName in filelist:
            oneCase = self.Example()

            oneCase.words = self.filterStopWords(GetSegFromIO.getWordsFromTextFile(dirname+"/"+fileName))
            #oneCase.words = GetSegFromIO.getWordsFromTextFile(dirname+"/"+fileName)

            oneCase.klass = self.getItemType(fileName)
            if (flag == "train"):
                self.trainData.append(oneCase)
            elif (flag == "test"):
                self.testData.append(oneCase)
            else:
                print "some err, pls input right flag, test ,or train"
                self.testData.append(oneCase)



    def loadItemType(self, filename):
        f = open(filename)
        for line in f:
            lineArr = line.split("\t")
            itemhash = lineArr[0]
            itemtype = lineArr[3]
            #load item type, make a dict
            self.typeDict[itemhash] = itemtype
            #load Model type
            if itemtype not in self.Models:
                self.Models[itemtype] = self.Model(itemtype)

        return
    def filterStopWords(self, words):
        """Filters stop words."""
        filtered = []
        for word in words:
            if not word in self.stopList and word.strip() != '':
                filtered.append(word)
        return filtered



    def loadStopWords(self, filename):
        f = open(filename)
        for line in f:
            self.stopList.append(line.replace('\n','').replace('\r',''))

    def classifyFile(self,filename):
        words = GetSegFromIO.getWordsFromTextFile(filename)
        nameArr = filename.split('/')
        klass_real = self.getItemType(nameArr[-1])
        klass_test = self.classifyOneCase(words)
        print "real class = " + klass_real
        print "test class = " + klass_test

    def run(self):
        self.loadItemType("item.out.txt")
        self.loadStopWords("stopwords.txt")
        self.loadItemData("train", "train")
        self.loadItemData("test", "test")
        self.train()
        pass



def main():
    nb = NaiveBayes()
    nb.run()

    nb.classify()


if __name__ == "__main__":
    main()
