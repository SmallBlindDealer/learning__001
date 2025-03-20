

# a = "aabbccxybbaa"
a = "aabbccybbaa"



def find_max(str_, max_remove):
    res = ""

    for idx in range(len(str_)):
        for max_re in range(1, max_remove+1):
            curr_str =  str_[:idx] + str_[idx+max_re:]
            l = 0
            r = len(curr_str)-1

            while l<=r:
                if curr_str[l]!=curr_str[r]:
                    break
                l+=1
                r-=1
            else:
                if len(res)<len(curr_str):
                    res = curr_str

    return res


print(find_max(a, 2))