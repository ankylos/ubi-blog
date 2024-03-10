from config import read_config

def main():
    """
    Main starting point
    """

    config_dict = read_config()
    print(config_dict)

if __name__ == "__main__":
    main()
