import sys

def add(a,b):
    return a + b

def main():
    if len(sys.argv) < 3:
        print("用法：python demo.py 数字1 数字2")
        return
    a=float(sys.argv[1])
    b=float(sys.argv[2])
    print(f"{a}+{b}={add(a,b)}")

if __name__ == "__main__":
    main()