#!/usr/bin/env python3
import random
import requests
import string
import sys
import xml.etree.ElementTree as ET

BASE_URL = "https://bossnl.mendixcloud.com/SportivityAppV3"


def login(username: str, password: str) -> str:
    headers = {"Content-Type": "application/json"}
    req = requests.post(
        f"{BASE_URL}/Login",
        json={"User": username, "Password": password, "IsCallNaar2eOmgeving": False},
        headers=headers,
    )
    text = req.text
    token = ET.fromstring(text).find("Token").text
    return token


def default_headers(token: str) -> dict:
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }


def get_location_id(token: str) -> str:
    headers = default_headers(token)
    location_id = requests.get(
        f"{BASE_URL}/Location/GetLocationsOfCompany", headers=headers
    ).json()["Locationss"][0]["LocationId"]
    return location_id


def register_qr(token: str, location_id: str, qr_code: str) -> str:
    headers = default_headers(token)
    phone_id = "".join(random.choices(string.ascii_uppercase + string.digits, k=20))
    req = requests.post(
        f"{BASE_URL}/RegisterQR",
        json={"QRCode": qr_code, "PhoneID": phone_id, "LocationId": location_id},
        headers=headers,
    )
    return phone_id


def access_qr(token: str, qr_code: str, phone_id: str, location_id: str):
    headers = default_headers(token)
    req = requests.post(
        f"{BASE_URL}/AccessQR/Access",
        json={"QRCode": qr_code, "PhoneID": phone_id, "LocationId": location_id},
        headers=headers,
    )
    print(req.text)


def main():
    if len(sys.argv) < 3:
        print("Please supply username, password and QR-string as CLI arguments")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    qr_code = sys.argv[3]
    token = login(username, password)
    location_id = get_location_id(token)
    phone_id = register_qr(token, location_id, qr_code)
    access_qr(token, qr_code, phone_id, location_id)


if __name__ == "__main__":
    main()
