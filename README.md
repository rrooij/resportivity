# Sportivity reverse engineering

Some gyms require you to install the Sportivity app in order to enter the gym. I feel that it is a sad
reflection on modern society that you need to install a properietary app in order to enter your gym for
one of the most basic human needs (getting exercise). I therefore tried to reverse engineer the app and
found out that you can enter the door by using the API.

Of course, you still need a Sportivity account and a gym membership to enter your gym. But if you
run the script on your phone, the door will unlock and does not require you to use the Sportivity
app anymore.

## Requirements

- python3
- requests

## Using the script

To use the script, first scan the QR code of your gym with a normal QR scanner. Save this code somewhere.

You can run the script using:

```
./sportivity.py [username] [password] [qr_code]
```

One way of running the script on your phone is by installing Termux and subsequently the Python package.

## Disclaimer

I HAVE NO AFFILIATION WITH SPORTIVITY AND ITS SOFTWARE. THIS SCRIPT IS NOT MADE BY SPORTIVITY AND NOT
AFFILIATED WITH ITS OWNER B.O.S.S BV IN ANY WAY.
