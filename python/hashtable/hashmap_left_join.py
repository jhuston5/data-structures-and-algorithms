try:
    from hashtable import Hashtable
except:
    from hashtable.hashtable import Hashtable

# Pseudocode:

# DEF left_join(hashmap1, hashmap2)

# new_dict = {}

# CALL ht = Hashtable()

# left_keys = ht.keys(hashmap1)

# right_keys = ht.keys(hashmap2)

# ITERATE through left keys

# 	CALL get function on left_keys

# 	Add key-value pairs to dictionary

# Check if left_keys IN right_keys

# 	If so, call get on hashmap2

# 		Append value to new_dict

# 	Else add null to new_dict key


def left_join(hashmap1, hashmap2):
    new_dict = {}
    left_keys = Hashtable.keys(hashmap1)
    right_keys = Hashtable.keys(hashmap2)

    for i in left_keys:
        val = hashmap1.get(i)
        print(val)
        new_dict[i] = [val]

        if i in right_keys:
            print(i)
            val2 = hashmap2.get(i)
            new_dict[i].append(val2)
        else:
            new_dict[i].append("Null")

    print(new_dict)
    print(left_keys)
    print(right_keys)
    return new_dict


if __name__ == "__main__":
    HT1 = Hashtable()
    HT2 = Hashtable()
    HT1.add("Cat", "calico")
    HT1.add("Lizard", "gila monster")
    HT1.add("Dog", "dachsund")
    HT2.add("Shark", "mako")
    HT2.add("Dog", "rottweiler")
    HT2.add("Equine", "horse")

    left_join(HT1, HT2)
