import datetime

class Ticket():

    count = 0
    def __init__(self):
        self.ticket_no = self._generate_ticket_no()
        self.entry_time = datetime.datetime.now().timestamp()
        self.exit_time = None
        self.payment_amount = None
        self.payment_status = "UNPAID"


    def make_payment(self, amount):
        # make payment (cash, upi, netbanking)
        self.exit_time = datetime.datetime.now().timestamp()
        self.payment_amount = amount
        self.payment_status = "PAID"

    def _generate_ticket_no(self):
        global count
        count++
        return count
