class FizzBuzz:

    @staticmethod
    def output(var):
        fizz = 'fizz'
        buzz = 'buzz'
        name = ''

        if 0 == var % 3:
            name += fizz

        if 0 == var % 5:
            name += buzz

        if name:
            return name

        return var


def main():
    for i in range(1, 101, 1):
        print(FizzBuzz.output(i))


if __name__ == '__main__':
    main()
