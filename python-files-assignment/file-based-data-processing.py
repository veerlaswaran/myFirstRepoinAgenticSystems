def read_numbers(filename):
    """Read integers from a file and return as a list."""
    numbers = []
    with open(filename, "r") as file:
        log_step("File opened successfully")
        for line in file:
            line = line.strip()
            if line:
                numbers.append(int(line))
    log_step(f"Read {len(numbers)} numbers")
    return numbers


def compute_statistics(numbers):
    """Compute total count, sum, and average of numbers."""
    total_count = len(numbers)
    total_sum = sum(numbers)
    average = total_sum / total_count if total_count > 0 else 0
    log_step("Computation completed")
    return total_count, total_sum, average


def log_step(message):
    """Append a log message to results.log."""
    with open("results.log", "a") as log_file:
        log_file.write(message + "\n")


def main():
    numbers = read_numbers("numbers.txt")
    total_count, total_sum, average = compute_statistics(numbers)

    log_step(f"Sum: {total_sum}")
    log_step(f"Average: {average:.2f}")
    log_step("Processing completed")

    print("Total numbers:", total_count)
    print("Sum:", total_sum)
    print("Average:", round(average, 2))

if __name__ == "__main__":
    main()
