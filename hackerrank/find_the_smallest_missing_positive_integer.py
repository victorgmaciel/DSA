def find_smallest_missing_postive(orderNumbers):

    length_of_list = len(orderNumbers)


    for index, value in enumerate(orderNumbers):
        if value > 0:

            print(index, value)





test_numbers = [3,4,-1,1]


print(find_smallest_missing_postive(test_numbers))