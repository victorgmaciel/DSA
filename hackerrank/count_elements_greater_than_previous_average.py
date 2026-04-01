

def countResponseTimeRegressions(responseTimes):
    
    if len(responseTimes) == 0:
        return 0
    
    running_sum = responseTimes[0]
    count = 0
    
    for number in range(1, len(responseTimes)):
        average = ( running_sum ) / number
        
        if responseTimes[number] > average:
            count += 1
        running_sum += responseTimes[number]
            
    return count 








test_case_1 = [1,100]
test_case_2 = [100,200,300,120,50]

test_case_3 = [100,200,150,300] # expected to be 2
print(countResponseTimeRegressions(test_case_3))
print(countResponseTimeRegressions(test_case_1))