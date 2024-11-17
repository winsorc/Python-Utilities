import qrcode

class MyQR:

    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size = size, border = padding)


    def create_qr(self, file_name: str, fg: str, bg: str):
        user_input: str = input('Enter URL or text for QR code: ')

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)
            print(f'Sucessfully created! ({file_name})')
        except Exception as e:
            print(f'Error: {e}')

def main():
    myqr = MyQR(size = 30, padding = 2)
    foreground = input('Enter foreground color: \n')
    background = input('Enter background color: \n')
    file_title = input('Enter name for saved QR code: \n')

    myqr.create_qr(file_title + '.png',
                    fg=foreground,
                    bg=background)
        
if __name__ == '__main__':
        main()

#add user input for color
