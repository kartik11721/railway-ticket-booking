class Train:
    company = 'Indian Railway'
    i = 0

    def __init__(self, name, fare,booked,seats):
            self.name = name
            self.fare = fare
            self.seats = seats
            self.booked = booked

    def booking(self):
        if len(self.seats) > 0:
            print(f'Yor Seat No. {self.seats[-1]} has been booked')
            (self.booked).append((self.seats).pop(-1))
            print(self.booked)
            print(self.seats)
        else: print('No Seat Left')

    def getInfo(self):
        print('*****************')
        print(f'----{self.company}----\nTrain : {self.name}\nVacant Seats : {len(self.seats)}\nFare : {self.fare} Rs.')
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
                        self.seats.append(a)
                        self.seats.sort()
        else: print('No Ticket To Be Cancelled')


t1 = Train('Rajdhani Express 0412',25,[],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
t2 = Train('Intracity 0712',10,[],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27])
t3 = Train('Tatkal 0107',20,[],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

t3.getInfo()
t3.booking()
t3.myTickets()
