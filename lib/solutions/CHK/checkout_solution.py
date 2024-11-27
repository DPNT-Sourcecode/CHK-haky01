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
        if c in sku_count:
            sku_count[c] += 1
        else:
            return -1

    quot_A, rem_A = divmod(sku_count["A"], 3)
    quot_B, rem_B = divmod(sku_count["B"], 2)

    A_total = quot_A * 130 + rem_A * 50
    B_total = quot_B * 45 + rem_B * 30
    C_total = 20 * sku_count["C"]
    D_total = 15 * sku_count["D"]

    return A_total + B_total + C_total + D_total



