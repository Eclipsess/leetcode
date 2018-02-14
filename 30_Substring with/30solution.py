class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        word_dict = {}
        word_len = len(words[0])
        word_num = len(words)
        for word in words:
            if word not in word_dict:
                word_dict.setdefault(word, 1)
            else:
                word_dict[word] += 1
        #print word_dict
        for i in range(len(s) + 1 - word_num*word_len):
            temp = {}
            for j in range(word_num):
                pat = s[i+j*word_len:i+(j+1)*word_len]
                #print pat
                if pat in word_dict:
                    if pat not in temp:
                        temp[pat] = 1
                    else:
                        temp[pat] += 1
                else:
                    break
                if temp[pat] > word_dict[pat]:
                    break
                if j == word_num - 1:
                    res.append(i)
        return res