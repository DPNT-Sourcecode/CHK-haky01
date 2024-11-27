# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_count = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
    }

    for c in skus:
        if c in sku_count:
            sku_count[c] += 1
        else:
            return -1

    A_total = get_price_with_offer(sku_count["A"], 3, 130, 50)
    B_total = get_price_with_offer(sku_count["B"], 2, 45, 30)
    C_total = 20 * sku_count["C"]
    D_total = 15 * sku_count["D"]
    E_total = 40 * sku_count["E"]

    return A_total + B_total + C_total + D_total + E_total


def get_price_with_offer(item_count, offer_count, offer_price, base_price):
    quot, rem = divmod(item_count, offer_count)

    return quot * offer_price + rem * base_price

