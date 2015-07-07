def line_count(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count
if __name__ == "__main__":
    print line_count("fourteen_five_wc.py")
