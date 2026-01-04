class TextAnalyzer:
    def __init__(self,text):
        self.text=text
        formatedTxt=text.replace('.','').replace('!','').replace('?','').replace(',','')
        self.formatxt=formatedTxt
    def frequency(self):
        worldList=self.formatxt.split(' ')
        wordsdict = {}
        for word in set(worldList):
            wordsdict[word] = worldList.count(word)
        return wordsdict
    def check_freq(self, word):
        freqdict = self.frequency()
        if word in freqdict:
            return freqdict[word]
        else:
            return 0          

def main():
    string="hello how many time is there ! hello and what is it ?? i cant under stand i am unable to do so hell nah , i am a student"
    test1 = TextAnalyzer(string)
    print('number of time giver word is there is ',test1.check_freq("??"))

if __name__ == "__main__":
    main()