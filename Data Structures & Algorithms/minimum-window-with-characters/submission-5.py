class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #create a t_hashmap
        #build the window slowly to the right, when all char are gotten, begin shrinking and
        #updating min_len 

        if not t: 
            return ""
        
        if len(t) > len(s):
            return ""
        
        if len(s) == 1:
            return "" if s[0] != t[0] else s[0]

        t_map = {}

        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1 
        
        needed = sum(t_map.values())

        l = 0 
        best_l = l
        min_len = float('inf')
        
        for r in range(len(s)):
            if s[r] in t_map:
                if t_map[s[r]] > 0:
                    needed -= 1 
                t_map[s[r]] -= 1 
            
            while needed == 0:
                window_len = r - l + 1 

                if window_len < min_len:
                    min_len = window_len
                    best_l = l 
                if s[l] in t_map:
                    t_map[s[l]] += 1
                    if t_map[s[l]] > 0:
                        needed += 1
                l += 1
        return "" if min_len == float('inf') else s[best_l:best_l + min_len]

        '''
        s = "OUZODYXAZV" , t = "XYZ"
        t_map = {X:1, Y:1, Z: 1}

        OUZODYXAZV
              l
                  r

        need = 3, 2, 1, 0, 1, 0, 1
        l = 5
        r = 8
        best_l = 4
        window_len = 4
        min_len = 4

        s[4:8] s[5:9]




        ZZZBBE   ZBE
        l
          r
        needed = 3, 2
        {Z:0, B : 1, E : 1}



        '''
                
                





