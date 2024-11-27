# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Would be quite useful to know how the string is formatted

    sku_count = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
    }

    for c in skus:
        if c == "A":
            sku_count["A"] += 1
        elif c == "B":
            sku_count["B"] += 1
        elif c == "C":
            sku_count["C"] += 1
        elif c == "D":
            sku_count["D"] += 1
        else:
            return -1


