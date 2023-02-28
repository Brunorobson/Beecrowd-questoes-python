while True:
    try:
        palavra = input().strip()
        if len(palavra) >= 10:
            print("palavrao")
        else:
            print("palavrinha")
    except EOFError:
        break