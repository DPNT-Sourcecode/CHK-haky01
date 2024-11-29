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

    sku_counts = {}

    for c in skus:
        if c in rules:
            if sku_counts.get(c):
                sku_counts[c] += 1
            else:
                sku_counts[c] = 1

            # rules[c]["count"] += 1
        else:
            return -1

    total = 0
    for elem in rules.values():
        total += get_total_for_sku(elem)

    return total


def get_total_for_sku(sku, sku_count):
    count = sku_count

    if sku["multi_buy_free"]:
        calc_multi_buy_free(sku)

    if sku["multi_buy_free_other"]:
        calc_multi_buy_free_other(sku)

    total, count = get_multi_buy_discount_total(sku)

    return total + count * sku["price"]


def get_multi_buy_discount_total(sku, sku_count):
    total = 0
    count = sku_count

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

    new_count = count - (item_count // min_count) * free_count

    sku["count"] = new_count if new_count >= 0 else 0


