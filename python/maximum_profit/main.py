STOCK1 = [7, 1, 5, 3, 6, 4]
STOCK2 = [7, 6, 4, 3, 1]


def main():
    maxTheStock(STOCK1)
    maxTheStock(STOCK2)


def maxTheStock(stock: list):
    best_profit = 0
    for i in range(0, len(stock) - 1):
        for j in range(i + 1, len(stock)):
            current_value = stock[i]
            next_value = stock[j]
            if next_value > current_value:
                current_profit = next_value - current_value
                if current_profit > best_profit:
                    best_profit = current_profit

    print(best_profit)


if __name__ == "__main__":
    main()
