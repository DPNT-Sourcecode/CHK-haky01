# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    rules = {
        "A": {
            "price": 50,
            "multi_buy_discount": [(3, 130), (5, 200)],
            "multi_buy_free": (2, 1),
            "multi_buy_free_other": (2, 1, "E"),
            "count": 0,
        }
    }

    sku_count = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0,
    }

    for c in skus:
        if c in sku_count:
            sku_count[c] += 1
        else:
            return -1


def get_price_with_offer(item_count, offer_count, offer_price):
    quot, rem = divmod(item_count, offer_count)

    return quot * offer_price, rem


def get_items_to_pay_for(item_count, offer_count, offer_count_required, free_items=1):

    item_count_to_pay = item_count - (offer_count // offer_count_required) * free_items

    return item_count_to_pay if item_count_to_pay >= 0 else 0


def get_same_item_free(item_count, offer_count_required, free_items=1):
    item_count_to_pay = item_count - item_count // (offer_count_required + free_items)

    return item_count_to_pay

