import qrcode
img = qrcode.make("https://francoisotis-chansons.github.io/Chansons_partage/")
img.save("qr_invites.png")
print("QR code généré : qr_invites.png")