def load():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("mainpy", action="store_true", type=str)
    parser.add_argument("namafolder", action="store_true", type=int)
    args = parser.parse_args()
    if args.mainpy == "a":
        print("test 1")
        if args.namafolder == 1:
            print("Loading...")
    else:
        print("FAIL")