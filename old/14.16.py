big = 7 * 512**120 - 6 * 64**100 + 8**210 - 255
print(big)
big = str(oct(big))[2:]
print(big)
print(big.count("0"))