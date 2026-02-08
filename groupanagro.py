class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        for word in strs:
            freq=[0]*26
            for ch in word:
                index=ord(ch)-ord('a')
                freq[index]+=1
            key=tuple(freq)
            if key not in mp:
                mp[key]=[]
            mp[key].append(word)
        result=[]
        for value in mp.values():
            result.append(value)
        return result    
