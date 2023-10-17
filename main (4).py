id_num = int(input("Please enter the salesperson's ID:"))
num_of_solditems = int(input("Please enter the number of items the salesperson sold in the last month:"))
total_value = int(input("Please enter the total value of the items sold:"))
question = input("Would you like to enter data for another salesperson?:")
while question == "Yes":
    id_num = int(input("Please enter the salesperson's ID:"))
    num_of_solditems = int(input("Please enter the number of items the salesperson sold in the last month:"))
    total_value = int(input("Please enter the total value of the items sold:"))
    question = input("Would you like to enter data for another salesperson?:")
    if question == "No":
        break
if num_of_solditems > 200:
        print("Salesperson's ID:", id_num)
        print("Number of Items Sold in the Last Month:", num_of_solditems)
        print("Total Value of Items Sold:", total_value)
        
