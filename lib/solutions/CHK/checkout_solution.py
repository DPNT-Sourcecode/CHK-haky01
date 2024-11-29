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
    },
    "B": {
        "price": 30,
        "multi_buy_discount": [(2, 45)],
        "multi_buy_free": None,
        "multi_buy_free_other": (2, 1, "E"),
    },
    "C": {
        "price": 20,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "D": {
        "price": 15,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "E": {
        "price": 40,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "F": {
        "price": 10,
        "multi_buy_discount": [],
        "multi_buy_free": (2, 1),
        "multi_buy_free_other": None,
    },
    "G": {
        "price": 20,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "H": {
        "price": 10,
        "multi_buy_discount": [(10, 80), (5, 45)],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "I": {
        "price": 35,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "J": {
        "price": 60,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "K": {
        "price": 80,
        "multi_buy_discount": [(2, 150)],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "L": {
        "price": 90,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "M": {
        "price": 15,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": (3, 1, "N"),
    },
    "N": {
        "price": 40,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "O": {
        "price": 10,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "P": {
        "price": 50,
        "multi_buy_discount": [(5, 200)],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "Q": {
        "price": 30,
        "multi_buy_discount": [(3, 80)],
        "multi_buy_free": None,
        "multi_buy_free_other": (3, 1, "R"),
    },
    "R": {
        "price": 50,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "S": {
        "price": 30,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "T": {
        "price": 20,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "U": {
        "price": 40,
        "multi_buy_discount": [],
        "multi_buy_free": (3, 1),
        "multi_buy_free_other": None,
    },
    "V": {
        "price": 50,
        "multi_buy_discount": [(3, 130), (2, 90)],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "W": {
        "price": 20,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "X": {
        "price": 90,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "Y": {
        "price": 10,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
    },
    "Z": {
        "price": 50,
        "multi_buy_discount": [],
        "multi_buy_free": None,
        "multi_buy_free_other": None,
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
    for k in sku_counts.keys():
        total += get_total_for_sku(k, rules, sku_counts)

    return total


def get_total_for_sku(k, rules, sku_counts):
    count = sku_counts.get(k, 0)
    sku_rule = rules[k]

    if sku_rule["multi_buy_free"]:
        count = calc_multi_buy_free(sku_rule, count)

    if sku_rule["multi_buy_free_other"]:
        count = calc_multi_buy_free_other(sku_rule, sku_counts, k)

    total, count = get_multi_buy_discount_total(sku_rule, count)

    return total + count * sku_rule["price"]


def get_multi_buy_discount_total(sku_rule, sku_count):
    total = 0
    count = sku_count

    for discount in sku_rule.get("multi_buy_discount", []):
        quotient, remainder = divmod(count, discount[0])
        total += quotient * discount[1]
        count = remainder

    return total, count


def calc_multi_buy_free(sku_rule, sku_count):
    count = sku_count
    min_count = sku_rule["multi_buy_free"][0]
    free_count = sku_rule["multi_buy_free"][1]

    return count - count // (min_count + free_count)


def calc_multi_buy_free_other(sku_rule, sku_counts, k):
    count = sku_counts.get(k, 0)
    min_count = sku_rule["multi_buy_free_other"][0]
    free_count = sku_rule["multi_buy_free_other"][1]
    item_count = sku_counts.get(sku_rule["multi_buy_free_other"][2], 0)

    new_count = count - (item_count // min_count) * free_count

    return new_count if new_count >= 0 else 0


def get_group_discount(sku_rule, sku_counts, keys):
    min_count = sku_rule["group_discount"][0]
    discount_price = sku_rule["group_discount"][1]

    count = 0
    prices = []
    for k in keys:
        count += sku_counts.get(k, 0)
        prices.append((k, rules[k]["price"]))

    prices.sort(key=lambda x: x[1], reverse=True)

    quotient, remainder = divmod(count, min_count)

    for p in prices:
        remainder -= p[0]

    total = quotient * discount_price


