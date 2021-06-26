BASE_PRICE = 800

DISCOUNTS = {
    1: 1,
    2: 0.95,
    3: 0.90,
    4: 0.80,
    5: 0.75,
}


def calculate_total(books):
    bundles = list(bundler(books))

    # 4 + 4 bundles give bigger discount than 3 + 5
    while 3 in bundles and 5 in bundles:
        bundles.remove(3)
        bundles.remove(5)
        bundles += [4, 4]

    return sum(
        BASE_PRICE * bundle_size * DISCOUNTS.get(bundle_size, 1)
        for bundle_size in bundles
    )


def bundler(basket):
    basket = list(basket)
    while len(basket) > 0:
        distinct = set(basket)
        yield len(distinct)
        for item in distinct:
            basket.remove(item)
