# noinspection PyUnusedLocal
# skus = unicode string

# Note no validation of discount orders yet
rules = {
    "A": {
        "price": 50,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "B": {},
}


def checkout(skus):

    for c in skus:
        if c in rules:
            rules[c]["count"] += 1
        else:
            return -1


def get_total_for_sku(sku):
    if sku["multi_buy_free"]:
        calc_multi_buy_free(sku)

    if sku["multi_buy_free_other"]:
        calc_multi_buy_free_other(sku)

    total, count = get_multi_buy_discount_total(sku)

    return total + count * sku["price"]


def get_multi_buy_discount_total(sku):
    total = 0
    count = sku["count"]

    for discount in sku.get("multi_buy_discount", []):
        quotient, remainder = divmod(count, discount[0])
        total += quotient * discount[1]
        count = remainder

    return total, count


def calc_multi_buy_free(sku):
    count = sku["count"]
    min_count = sku["multi_buy_free"][0]
    free_count = sku["multi_buy_free"][1]

    sku["count"] = count - count // (min_count + free_count)


def calc_multi_buy_free_other(sku):
    count = sku["count"]
    min_count = sku["multi_buy_free_other"][0]
    free_count = sku["multi_buy_free_other"][1]
    item_count = rules[sku["multi_buy_free_other"][2]]["count"]

    sku["count"] = count - (item_count // min_count) * free_count


def get_price_with_offer(item_count, offer_count, offer_price):
    quot, rem = divmod(item_count, offer_count)

    return quot * offer_price, rem


def get_items_to_pay_for(item_count, offer_count, offer_count_required, free_items=1):

    item_count_to_pay = item_count - (offer_count // offer_count_required) * free_items

    return item_count_to_pay if item_count_to_pay >= 0 else 0


def get_same_item_free(item_count, offer_count_required, free_items=1):
    item_count_to_pay = item_count - item_count // (offer_count_required + free_items)

    return item_count_to_pay








