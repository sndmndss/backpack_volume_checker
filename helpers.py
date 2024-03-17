def account_volume(account_orders):
    """
        Calculates the total volume and fees from account orders.

        Args:
            account_orders (list): A list of account order dictionaries.

        Returns:
            tuple: A tuple containing the total volume and total fees.
        """
    prices = [float(item['price'])*float(item["quantity"]) for item in account_orders]
    fees = [float(item['price'])*float(item["fee"])
            if item["feeSymbol"] != 'USDC' else float(item["fee"]) for item in account_orders]
    return sum(prices), sum(fees)
