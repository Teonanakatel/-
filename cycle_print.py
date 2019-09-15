from time import sleep


def main(text):
    for alpha in text:
        print(alpha, end='', flush=True)
        sleep(0.5)
    print('\n')


if __name__ == '__main__':
    args = input('>>>> ')
    main(args)
