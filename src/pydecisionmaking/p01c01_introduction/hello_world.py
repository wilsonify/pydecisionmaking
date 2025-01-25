def tab_separated_string(arr):
    result = ""
    for i in range(len(arr)):
        result += f"\t{arr[i]}"
    return result


def squares(arr):
    return [i ** 2 for i in arr]


def hello():
    hello_array = ["Hello", "G'day", "Shalom"]
    hello_string = tab_separated_string(hello_array)

    print("There is more than one way to say hello:")
    print(f"\n{hello_string}")


def hello_squares():
    squares_arr = squares(range(11))
    squares_string = tab_separated_string(squares_arr)

    print("\nThese squares are just perfect:")
    print(f"\n{squares_string}")


if __name__ == "__main__":
    hello()
    hello_squares()
