def main():
    data = [3, 5, 1, 9, -1, 0, -1, 23, 12]
    finish = 0
    index = 0

    print(f"Starting {data}")

    while finish != len(data) - 1:
        print(f"finish: {finish}  index: {index}  DATA: {data}")
        if index != len(data) - 1:

            if data[index] <= data[index + 1]:
                finish += 1
            else:
                temp = data[index]
                data[index] = data[index + 1]
                data[index + 1] = temp

                finish = 0  # Restart indices with good match

            index += 1

        else:
            index = 0

    print(data)


if __name__ == "__main__":
    main()
