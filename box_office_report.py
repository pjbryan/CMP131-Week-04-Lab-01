# PJ Bryan
# CMP-131-80230
# Week 04
# Lab 01
# Assignment 3
# 09/16/2026


adultTicket = 10.00
childTicket = 6.00

movieTitle = "Movie Title: "
adultTicketsSold = "Adult Tickets Sold: "
childTicketsSold = "Child Tickets Sold: "

inputTitle = input(movieTitle)
inputAdult = int(input(adultTicketsSold))
inputChild = int(input(childTicketsSold))

adultRevenue = inputAdult * adultTicket
childRevenue = inputChild * childTicket
grossRevenue = adultRevenue + childRevenue

theaterRevenue = grossRevenue * 0.20
distributorsRevenue = grossRevenue * 0.80

divider = ("____________________________________________")

print("MOVIE STATISTICS",divider)
print("Movie Title: ", inputTitle)
print("Adult Tickets Sold:", inputAdult)
print("Child Tickets Sold:",inputChild)

print("REVENUE STATISTICS",divider)
print(f"Adult Ticket Revenue: ${adultRevenue:.2f}")
print(f"Child Ticket Revenue: ${childRevenue:.2f}")
print(f"Gross Revenue: ${grossRevenue:.2f}")
print(f"Theater Revenue: ${theaterRevenue:.2f}")
print(f"Distributor Revenue: ${distributorsRevenue:.2f}")
