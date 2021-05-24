class Train:
    company = 'Indian Railway'
    seatNos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    booked = []
    i = 0

    def __init__(self, name, fare):
            self.name = name
            self.fare = fare

    def booking(self):
        if len(self.seatNos) > 0:
            print(f'Yor Seat No. {self.seatNos[-1]} has been booked')
            (self.booked).append((self.seatNos).pop(-1))
            print(self.booked)
            print(self.seatNos)
        else: print('No Seat Left')

    def getInfo(self):
        print('*****************')
        print(f'----{self.company}----\nTrain : {self.name}\nVacant Seats : {len(self.seatNos)}\nFare : {self.fare} Rs.')
        print('*****************')

    def myTickets(self):
        if len(self.booked) > 0:
            print(f'You Have Tickets For {self.name} Seat No : {self.booked}')
        else: print('You Currently Dont Have Any Tickets')
        
    def cancel(self):
        if len(self.booked) > 0:
            print(f'You Have Tickets For Seat : {self.booked}')
            self.i = int(input('Enter The Seat Number You Want To Cancel : '))
            for a in self.booked:
                    if(a == self.i):
                        print('Your Ticket Has Been Canceled')
                        self.booked.remove(a)
                        self.seatNos.append(a)
                        self.seatNos.sort()
        else: print('No Ticket To Be Cancelled')


t1 = Train('Rajdhani Express 0412',25)

t1.myTickets()
t1.getInfo()
t1.booking()
t1.booking()
t1.booking()
t1.booking()
t1.cancel()
t1.cancel()
t1.getInfo()
t1.myTickets()
print(t1.seatNos)
