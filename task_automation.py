import os
import shutil
import pandas as pd
from PIL import Image
from PyPDF2 import PdfMerger
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyttsx3

def organize_files(directory):
    """Organizes files in the specified directory by their extensions."""
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            ext = filename.split('.')[-1]
            ext_folder = os.path.join(directory, ext)
            os.makedirs(ext_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(ext_folder, filename))
    print(f"Files in {directory} organized by type.")

def clean_data(file_path):
    """Cleans the CSV file by removing duplicates and filling missing values."""
    try:
        df = pd.read_csv(file_path)
        df.drop_duplicates(inplace=True)
        df.fillna('N/A', inplace=True)
        cleaned_path = file_path.replace('.csv', '_cleaned.csv')
        df.to_csv(cleaned_path, index=False)
        print(f"Data cleaned and saved to {cleaned_path}")
    except Exception as e:
        print(f"Error cleaning data: {e}")

def backup_files(src_dir, dest_dir):
    """Backs up files from source to destination directory."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for filename in os.listdir(src_dir):
        shutil.copy(os.path.join(src_dir, filename), dest_dir)
    print(f"Backup completed from {src_dir} to {dest_dir}")

def merge_pdfs(pdf_folder, output_path):
    """Merges all PDF files in the given folder into a single PDF."""
    merger = PdfMerger()

    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            merger.append(os.path.join(pdf_folder, filename))
    merger.write(output_path)
    merger.close()
    print(f"PDFs merged into {output_path}")

def resize_images(image_folder, new_size):
    """Batch resizes images in a folder to the specified size."""
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('jpg', 'jpeg', 'png')):
            img_path = os.path.join(image_folder, filename)
            with Image.open(img_path) as img:
                img = img.resize(new_size)
                img.save(img_path)
    print(f"Images resized to {new_size} in {image_folder}")

def send_email(sender, password, receiver, subject, message):
    """Sends an email using SMTP."""
    try:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def text_to_speech(text, output_file):
    """Converts text to speech and saves it as an audio file."""
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()
    print(f"Text saved as speech in {output_file}")

def main():
    while True:
        print("\nTask Automation Menu:")
        print("1. Organize Files")
        print("2. Clean CSV Data")
        print("3. Backup Files")
        print("4. Merge PDFs")
        print("5. Resize Images")
        print("6. Send Email")
        print("7. Text-to-Speech")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            path = input("Enter the directory to organize: ")
            organize_files(path)
        elif choice == '2':
            file = input("Enter CSV file path: ")
            clean_data(file)
        elif choice == '3':
            src = input("Enter source folder: ")
            dest = input("Enter destination folder: ")
            backup_files(src, dest)
        elif choice == '4':
            pdf_folder = input("Enter PDF folder path: ")
            output = input("Enter output PDF file path: ")
            merge_pdfs(pdf_folder, output)
        elif choice == '5':
            img_folder = input("Enter image folder path: ")
            width = int(input("Enter new width: "))
            height = int(input("Enter new height: "))
            resize_images(img_folder, (width, height))
        elif choice == '6':
            sender = input("Enter sender email: ")
            password = input("Enter sender password: ")
            receiver = input("Enter receiver email: ")
            subject = input("Enter email subject: ")
            message = input("Enter email message: ")
            send_email(sender, password, receiver, subject, message)
        elif choice == '7':
            text = input("Enter text to convert to speech: ")
            output_file = input("Enter output audio file name: ")
            text_to_speech(text, output_file)
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()