def kwargsAcceptFun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    kwargsAcceptFun(name="Shamshod", age=19, city="Tashkent")