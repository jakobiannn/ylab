def bananas(s, banana = 'banana'):
    ret = []

    if banana == '':
        ret.append(''.rjust(len(s), '-'))
        return ret

    left_s = ''
    for si in range(len(s)):
        if banana[0] == s[si]:
            left_s = ''.rjust(si, '-') + s[si]
            if s[si + 1:] == '' and banana[1:] == '':
                ret.append(left_s)
            else:
                right_s_list = bananas(s[si + 1:], banana[1:])
                for right_s in right_s_list:
                    ret.append(left_s + right_s)
    return set(ret)


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
