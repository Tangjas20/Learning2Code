def read_menu(filename):
    pass

def order_items(ls):
    pass

def calculate_prices(ls):
    pass

def charge_card(total):
    pass

def charge_cash(total):
    pass

def charge(total):
    pass

def main():
    menu = read_menu("menu.txt")
    order = order_items(menu)
    total = calculate_prices(order)
    charge(total)
if __name__ == "__main__":
    main()
