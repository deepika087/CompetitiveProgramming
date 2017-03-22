

if __name__ == "__main__":
    T = int(raw_input(''))
    for i in range(T):
        N = int(raw_input(''))
        numbers =raw_input('')

        numbers =numbers.split()
        numbers = [ int(x) for x in numbers]
        min_index = 0;
        maxDiff = 0;
        buy = sell = 0;
        for i in range(N):
            if (numbers[i] < numbers[min_index]):
                min_index = i
            diff = numbers[i] - numbers[min_index]
            if (diff > maxDiff):
                buy = min_index
                sell = i
                maxDiff = diff
        print maxDiff