import qrcode

def generate_qr_code():
    # Ask the user for input data
    data = input("Enter the text or URL to encode into a QR code: ")

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code to a file
    file_name = input("Enter the name of the file to save (e.g., my_qrcode.png): ")
    img.save(file_name)

    print(f"QR code saved successfully as {file_name}!")

# Run the program
generate_qr_code()
