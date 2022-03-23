from hashtable.hashtable import Hashtable
from hashtable.hashmap_left_join import left_join


def test_left_join_keys():

    HT1 = Hashtable()
    HT2 = Hashtable()
    HT1.add("Cat", "calico")
    HT1.add("Lizard", "gila monster")
    HT1.add("Dog", "dachsund")
    HT2.add("Shark", "mako")
    HT2.add("Dog", "rottweiler")
    HT2.add("Equine", "horse")

    left_dict = left_join(HT1, HT2)

    def getList(dict):
        return list(dict.keys())

    expected = getList(left_dict)
    actual = ["Cat", "Dog", "Lizard"]
    assert actual == expected


def test_left_join_val():
    HT1 = Hashtable()
    HT2 = Hashtable()
    HT1.add("Cat", "calico")
    HT1.add("Lizard", "gila monster")
    HT1.add("Dog", "dachsund")
    HT2.add("Shark", "mako")
    HT2.add("Dog", "rottweiler")
    HT2.add("Equine", "horse")

    left_dict = left_join(HT1, HT2)
    print(left_dict)
    expected = left_dict["Lizard"]
    actual = ["gila monster", "Null"]
    assert actual == expected


def test_left_join_multiple_vals():
    HT1 = Hashtable()
    HT2 = Hashtable()
    HT1.add("Cat", "calico")
    HT1.add("Lizard", "gila monster")
    HT1.add("Dog", "dachsund")
    HT2.add("Shark", "mako")
    HT2.add("Dog", "rottweiler")
    HT2.add("Equine", "horse")

    left_dict = left_join(HT1, HT2)
    print(left_dict)
    expected = left_dict["Dog"]
    actual = ["dachsund", "rottweiler"]
    assert actual == expected
