import qrcode


def get_network_details():
    ssid = input("SSID:")
    encrytption = input("Encryption [1:WPA/WPA2 2:WEP 0:NONE]:")
    password = input("Password:")

    protection = ""
    if encrytption == 1:
        protection = "T:WPA"
    elif encrytption == 2:
        protection = "T:WEP"

    qr_string = "WIFI:S:%s;%s;P:%s;;" % (ssid, protection, password)
    save_qr_code(qr_string, ssid)


def save_qr_code(qr_string, ssid):
    img = qrcode.make(qr_string)

    filename = ssid + ".png"
    with open(filename, 'wb') as f:
        img.save(f)

    print("QR Code Saved as %s" % (filename))


if __name__ == "__main__":
    get_network_details()