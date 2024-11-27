# noinspection PyUnusedLocal
# skus = unicode string

# Note: no validation of discount orders yet. Put bigger quantity first
# Note: free other is written backwards (i.e. relation is encoded in SKU that gets a free item)
rules = {
    "A": {
        "price": 50,
        "multi_buy_discount": [(5, 200), (3, 130)],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "B": {
        "price": 30,
        "multi_buy_discount": [(2, 45)],
        "multi_buy_free": None,
        "multi_buy_free_other": (2, 1, "E"),
        "count": 0,
    },
    "C": {
        "price": 20,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "D": {
        "price": 15,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "E": {
        "price": 40,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "F": {
        "price": 10,
        "multi_buy_discount": [],
        "multi_buy_free": (2, 1),
        "multi_buy_free_other": None,
        "count": 0,
    },
    "G": {
        "price": 20,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "H": {
        "price": 10,
        "multi_buy_discount": [(10, 80), (5, 45)],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "I": {
        "price": 35,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "J": {
        "price": 60,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "K": {
        "price": 80,
        "multi_buy_discount": [(2, 150)],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "L": {
        "price": 90,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "M": {
        "price": 15,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": (3, 1, "M"),
        "count": 0,
    },
    "N": {
        "price": 40,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "O": {
        "price": 10,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "P": {
        "price": 50,
        "multi_buy_discount": [(5, 200)],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "Q": {
        "price": 30,
        "multi_buy_discount": [(3, 80)],
        "multi_buy_free": None,
        "multi_buy_free_other": (3, 1, "R"),
        "count": 0,
    },
    "R": {
        "price": 50,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "S": {
        "price": 30,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "T": {
        "price": 20,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "U": {
        "price": 40,
        "multi_buy_discount": [],
        "multi_buy_free": (3, 1),
        "multi_buy_free_other": None,
        "count": 0,
    },
    "V": {
        "price": 50,
        "multi_buy_discount": [(3, 130), (2, 90)],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "W": {
        "price": 20,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "X": {
        "price": 90,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "Y": {
        "price": 10,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
    "Z": {
        "price": 50,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
        "count": 0,
    },
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

