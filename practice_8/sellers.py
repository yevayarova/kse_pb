sellers = {
    1: "Продавець1",
    2: "Продавець2",
    3: "Продавець3"
}

def calculate_bonus(transactions):
    bonuses = {seller_id: 0 for seller_id in sellers}
    for t in transactions:
        seller = t["seller_id"]
        bonuses[seller] += t["total"] * 0.05
    return bonuses

