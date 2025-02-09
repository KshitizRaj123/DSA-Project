import os
import io
from PIL import Image
import pikepdf
from pikepdf import Pdf, PdfImage, Name

def get_min_size(pdf_path):
    """
    Calculate the file size of the given PDF in KB.
    """
    try:
        return os.path.getsize(pdf_path) / 1024  # Convert bytes to KB
    except Exception as e:
        print(f"Error calculating min size: {e}")
        return 0

def resize_pdf(input_pdf_path, output_pdf_path, quality=50):
    try:
        # Open the PDF using pikepdf
        pdf = Pdf.open(input_pdf_path)

        for page in pdf.pages:
            # Get all images in the page
            images = page.images
            for name, image in images.items():
                try:
                    # Extract the image using PdfImage
                    pdf_image = PdfImage(image)
                    img = pdf_image.as_pil_image()  # Convert to PIL image

                    # Resize and compress the image
                    img = img.convert("L")  # Convert to grayscale
                    img = img.resize((img.width // 2, img.height // 2), Image.LANCZOS)  # Resize

                    # Save the compressed image to a BytesIO object
                    img_bytes = io.BytesIO()
                    img.save(img_bytes, format="JPEG", quality=quality, optimize=True)
                    img_bytes.seek(0)

                    # Replace the original image with the compressed one
                    image.write(img_bytes.getvalue(), filter=Name("/DCTDecode"))
                except Exception as e:
                    print(f"Error processing image {name}: {e}")

        # Save the modified PDF
        pdf.save(output_pdf_path)
        print(f"Resized PDF saved to {output_pdf_path}")

    except Exception as e:
        print(f"Error resizing PDF: {e}")

# Example usage
input_pdf = "input.pdf"
output_pdf = "output.pdf"
resize_pdf(input_pdf, output_pdf)