import qrcode
import flet as ft
import os
import time

def main(page: ft.Page):
    page.title = "QR Code Generator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def generate():
        url = text_field.value
        if url:
            qr = qrcode.QRCode()
            qr.add_data(url)
            qr.make(fit=True)

            file_name = "qrcode.png"
            if not os.path.exists("assets"):
                os.makedirs("assets")

            image = qr.make_image()
            image.save(f"assets/{file_name}")

            qr_image.src = f"{file_name}?v={time.time()}"
            qr_image.visible = True

            confirmation_text.value = "QR Generated!"
            confirmation_text.color = ft.Colors.GREEN

            download_button.visible = True
            page.update()
        else:
            confirmation_text.value = "Invalid Website Link"
            confirmation_text.color = ft.Colors.RED
            page.update()

    async def download(e):
        await page.launch_url(f"/qrcode.png")

    title = ft.Text(
        "QR COde Generator", 
        theme_style=ft.TextThemeStyle.HEADLINE_LARGE
        )
    introduction_text = ft.Text("Enter a website link in the field below and click the button to generate a QR code.")
    text_field = ft.TextField(
        value="", 
        text_align=ft.TextAlign.CENTER
        )
    generate_button = ft.OutlinedButton(
        ft.Text("Generate"), 
        on_click=generate
        )
    confirmation_text = ft.Text(value="")
    qr_image = ft.Image(
        src = "",
        width=400,
        height=400,
        visible=False,
    )
    download_button = ft.OutlinedButton(
        ft.Text("Download QR Code"), 
        width=200,
        on_click=download,
        visible = False
        )
    
    page.add(
        title,
        introduction_text,
        text_field,
        generate_button,
        confirmation_text,
        qr_image,
        download_button
    )
ft.run(main, assets_dir="assets")