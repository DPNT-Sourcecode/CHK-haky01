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

    A_offer_total, rem = get_price_with_offer(sku_count["A"], 5, 200)
    A_total = A_offer_total

    A_offer_total, rem = get_price_with_offer(rem, 3, 130)
    A_total += A_offer_total + rem * 50

    B_to_pay = get_items_to_pay_for(sku_count["B"], sku_count["E"], 2)
    B_offer_total, B_rem = get_price_with_offer(B_to_pay, 2, 45, 30)

    C_total = 20 * sku_count["C"]
    D_total = 15 * sku_count["D"]
    E_total = 40 * sku_count["E"]

    return A_total + B_total + C_total + D_total + E_total


def get_price_with_offer(item_count, offer_count, offer_price):
    quot, rem = divmod(item_count, offer_count)

    return quot * offer_price, rem


def get_items_to_pay_for(item_count, offer_count, offer_count_required, free_items=1):

    item_count_to_pay = item_count - (offer_count // offer_count_required) * free_items

    return item_count_to_pay if item_count_to_pay >= 0 else 0


