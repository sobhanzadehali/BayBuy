class OrderService:
    """
    service class for Orders
    """

    @staticmethod
    def get_items(order_obj):
        """
        returns list of all items in order
        :param order_obj:
        :return: quetyset object
        """
        print("From Inside Order Service")  # TODO: check if this does work
        return Item.objects.filter(order_id=order_obj)

    @staticmethod
    def pay(order_obj):
        """
        it has to do paying stuf for order

        :param order_obj:
        :return:
        """
        pass  # TODO: make web gateway proceed paying for order

    @staticmethod
    def total(order_obj):
        """
        Calculates the total fee of the order
        :param order_obj:
        :return: total(big integer)
        """

        objs = OrderService.get_items(order_obj)
        total = 0
        for obj in objs:
            total += obj.total
        order_obj.total_fee = total
        order_obj.save()
        return total
