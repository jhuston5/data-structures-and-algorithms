try:
    from hashtable import Hashtable
except:
    from hashtable.hashtable import Hashtable


import re


def hash_repeated(str):
    if len(str) == 0:
        return None

    hashmap = Hashtable()
    lowered = str.lower()
    print(lowered)
    words = re.findall(r"/w+", lowered)

    for word in words:
        if hashmap.contains(word):
            return word
        else:
            hashmap.add(word, word)
    return None


if __name__ == "__main__":
    print(
        hash_repeated(
            "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York"
        )
    )
