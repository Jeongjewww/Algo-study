def solution(numbers):
    n = len(numbers)
    answer = []
    i = 0
    
    while (i<n):
        j = i + 1
        while (j<n):
            a = numbers[i] + numbers[j]        
            j += 1        
            if a in answer:
                continue
            answer.append(a)
        i+=1
    answer.sort()

    return answer

numbers = [5, 0, 2, 7]
print(solution(numbers))