```sh
tshark -r osu.pcap -Y usbhid.data -T fields -e usb.src -e usbhid.data > osu1.txt
python3 draw.py
```