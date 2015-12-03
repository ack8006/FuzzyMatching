from difflib import SequenceMatcher


def ratio(item_one, item_two, ignore_case=False):
    if ignore_case:
        item_one, item_two = item_one.lower(), item_two.lower()
    return SequenceMatcher(None, item_one, item_two).ratio()

def partial_ratio(item_one, item_two, ignore_case=False):
    if len(item_one) <= len(item_two):
        shrt, lng = item_one, item_two
    else:
        shrt, lng = item_two, item_one
    diff = len(lng)-len(shrt)
    return max(map(lambda x: ratio(shrt, lng[x:x+len(shrt)]), xrange(diff+1)))

def token_sorted_ratio(item_one, item_two, ignore_case=False):
    item_one = ' '.join(sorted(item_one.split()))
    item_two = ' '.join(sorted(item_two.split()))
    return ratio(item_one, item_two, ignore_case)

def token_set_ratio(item_one, item_two, ignore_case=False):
    set_one, set_two = set(item_one.split()), set(item_two.split())
    intersection = set_one & set_two
    for token in intersection:
        set_one.discard(token)
        set_two.discard(token)

    intersection = ' '.join(intersection)
    set_one = ' '.join(set_one)
    set_two = ' '.join(set_two)
    #intersection vs. intersection + rest of item one
    #intersection vs. intersection + rest of item two
    #intersection vs. intersection + rest of both
    return max(ratio(intersection, intersection + ' ' + set_one, ignore_case),
               ratio(intersection, intersection + ' ' + set_two, ignore_case),
               ratio(intersection + ' ' + set_one, intersection+' '+set_two, ignore_case))

def all_techniques(item_one, item_two, ignore_case = False):
    return max(ratio(item_one, item_two, ignore_case),
               partial_ratio(item_one, item_two, ignore_case),
               token_sorted_ratio(item_one, item_two, ignore_case),
               token_set_ratio(item_one, item_two, ignore_case))
