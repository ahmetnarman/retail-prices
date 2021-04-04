

def scrape_product(item):
    """
    Given a product tag from a browse page, it returns the key information related to that product

    :param item:
    :return:
    """

    name_item = item.find('h4', class_ = "fop-title")
    if name_item:
        return name_item.text
    return None