import datetime
import uuid

class Ticket():

    count = 0
    def __init__(self, spot):
        self.ticket_no = self._generate_ticket_no()
        self.entry_time = datetime.datetime.now().timestamp()
        self.parking_spot = spot
        self.exit_time = None
        self.payment_amount = None
        self.payment_status = "UNPAID"

    def __str__(self):
        return f"Ticket(ticket_no={self.ticket_no}, entry_time={self.entry_time}, parking_spot={self.parking_spot}, exit_time={self.exit_time}, payment_amount={self.payment_amount}, payment_status={self.payment_status})"

    def make_payment(self, amount):
        # make payment (cash, upi, netbanking)
        self.exit_time = datetime.datetime.now().timestamp()
        self.payment_amount = amount
        self.payment_status = "PAID"

    def _generate_ticket_no(self):
        #Ticket.count += 1
        #return Ticket.count

        return str(uuid.uuid4())
