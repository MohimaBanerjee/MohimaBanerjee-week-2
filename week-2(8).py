def process_queries(n, queries):
    # Initialize the 2D array with empty lists
    arr = [[] for _ in range(n)]
    x = 0  # Initialize x to 0
    results = []  # To store the results of type 2 queries

    for query in queries:
        query_type = query[0]
        if query_type == 1:
            # Append the integer to the specified array
            index = query[1]
            value = query[2]
            arr[index].append(value)
        elif query_type == 2:
            # Compute the value and store it in results
            index = query[1]
            element_index = query[2]
            x = arr[index][element_index]  # Set x to the value at arr[index][element_index]
            results.append(x)  # Store the new value of x in results

    return results

# Example usage:
if __name__ == "__main__":
    # Sample Input
    n = 2
    queries = [
        [1, 0, 5],
        [1, 1, 7],
        [1, 0, 3],
        [2, 1, 0],
        [2, 1, 1]
    ]

    # Process the queries
    output = process_queries(n, queries)

    # Print the results
    for result in output:
        print(result)  # Output: 7, 3
