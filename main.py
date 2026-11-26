
import os

ENTRY = "The glass had it coming. It sat there for weeks, smug, full of water, judging my life choices. I merely gave it a career change."

def main():
    os.makedirs("/output", exist_ok=True)  # make sure the output directory exists
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)

if __name__ == "__main__":
    main()
