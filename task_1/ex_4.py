import itertools


def bananas(word):
    if len(word) <= 6 and word != 'banana':
        return set()

    banana = list(word)

    lines = ['' for i in range(6)]
    for i in range(len(banana) - 6):
        lines.append('-')

    masks = set(itertools.permutations(lines, len(lines)))
    answer = set()

    for mask in masks:
        cur_banana = banana.copy()

        for i in range(len(mask)):
            if mask[i] == '-':
                cur_banana[i] = '-'
        if ''.join(i for i in cur_banana if i != '-') == 'banana':
            answer.add(''.join(i for i in cur_banana))
    return answer


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
