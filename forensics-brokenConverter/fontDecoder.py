
def guid_to_bytes(guid):
    gbytes = bytes.fromhex(guid.replace("-", ""))
    return bytes(gbytes[i] for i in (3, 2, 1, 0, 5, 4, 7, 6, 8, 9, 10, 11, 12, 13, 14, 15))

def decode_font(src, dest, guid):
    with open(src, "rb") as f:
        font = f.read()
    gbytes = guid_to_bytes(guid)
    header = list(font[:32])
    for idx, i in enumerate((15, 14, 13, 12, 11, 10, 9, 8, 6, 7, 4, 5, 0, 1, 2, 3)):
        header[idx] = header[idx] ^ gbytes[i]
        header[idx + 16] = header[idx + 16] ^ gbytes[i]
    data = bytes(header) + font[32:]
    with open(dest, "wb") as f:
        f.write(data)

def encode_font(src, dest, guid):
    with open(src, "rb") as f:
        font = f.read()
    gbytes = guid_to_bytes(guid)
    header = list(font[:32])
    for idx, i in enumerate((15, 14, 13, 12, 11, 10, 9, 8, 6, 7, 4, 5, 0, 1, 2, 3)):
        header[idx] = header[idx] ^ gbytes[i]
        header[idx + 16] = header[idx + 16] ^ gbytes[i]
    data = bytes(header) + font[32:]
    with open(dest, "wb") as f:
        f.write(data)

if __name__ == "__main__":
    guid = "02F30FAD-6532-20AE-4344-5621D614A033"
    font_file = f"./lipsum/Resources/{guid}.odttf"
    encode_font("flagMono-Regular.ttf", font_file, guid)