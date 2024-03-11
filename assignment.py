import multiprocessing

def calculate(chunk):
    return sum(chunk)

def main():

    array = [1,2,3,4,5,6,7,8,9]  
    num_processes = 5

    size = len(array) // num_processes
    chunks = [array[i:i+size] for i in range(0, len(array), size)]

    pool = multiprocessing.Pool(processes=num_processes)

    results = pool.map(calculate, chunks)

    pool.close()
    pool.join()

    total_sum = sum(results)
    print("Total Sum:", total_sum)

if __name__ == "__main__":
    main()
