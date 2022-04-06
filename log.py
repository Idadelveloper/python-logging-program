import logging
import argparse


def main():
    """
        Simple logger and argparse program that prints even, all or odd numberswhen the value of the 'log' flag is set to INFO, DEBUG or ERROR respectively.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--log', '-l', dest="log", help='Logs out even numbers if INFO, odd numbers if ERROR and all numbers if DEBUG', default='DEBUG')
    args = parser.parse_args()

    logging.basicConfig(level=args.log, format='%(asctime)s-%(levelname)s-%(message)s', filename="log.txt")

    numbers = range(1, 100)
    try:
        for num in numbers:
            if num % 2 == 0:
                logging.info("%d is an even number", num)
            else:
                logging.error("%d is an odd number", num)
            logging.debug("%d is a number regardless", num)
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)


if __name__ == "__main__":
    main()

