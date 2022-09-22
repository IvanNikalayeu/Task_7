from min_condition import min_condition
from hour_condition import hour_condition
from reader import read



def main():
    df = read()
    min_condition(df)
    hour_condition(df)
    pass


if __name__ == "__main__":

    main()

