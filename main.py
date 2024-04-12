class Ticket:
    def __init__(self, number, creator, staff_id, email, description, response, status):
        self.number = number
        self.creator = creator
        self.staff_id = staff_id
        self.email = email
        self.description = description
        self.response = response
        self.status = status
 
    def __str__(self):
        return (f"Ticket Number: {self.number}\n"
                f"Ticket Creator: {self.creator}\n"
                f"Staff ID: {self.staff_id}\n"
                f"Email Address: {self.email}\n"
                f"Description: {self.description}\n"
                f"Response: {self.response}\n"
                f"Ticket Status: {self.status}\n")
 
 
def print_ticket_statistics(created, resolved, to_solve):
    print("\nDisplaying Ticket Statistics\n")
    print(f"Tickets Created: {created}")
    print(f"Tickets Resolved: {resolved}")
    print(f"Tickets To Solve: {to_solve}\n")
 
 
def print_tickets(tickets):
    print("Printing Tickets:\n")
    for ticket in tickets:
        print(ticket)
 
 
def main():
    tickets = [
        Ticket(2001, "Inna", "INNAM", "inna@whitecliffe.co.nz", "My monitor stopped working", "Not Yet Provided", "Open"),
        Ticket(2002, "Maria", "MARIAH", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars", "Not Yet Provided", "Open"),
        Ticket(2003, "John", "JOHNS", "john@whitecliffe.co.nz", "Password change", "New password generated: JOJoh", "Closed")
    ]
 
    print_ticket_statistics(created=len(tickets), resolved=sum(ticket.status == "Closed" for ticket in tickets),
                            to_solve=sum(ticket.status == "Open" for ticket in tickets))
 
    print_tickets(tickets)
 
 
if __name__ == "__main__":
    main()
 
