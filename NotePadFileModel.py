import os.path
import string
from tkinter import filedialog


class File_Model:
    def __init__(self):
        self.url = ""
        self.key = string.ascii_letters + ''.join([str(x) for x in range(0, 10)])
        self.offset = 24

    def encrypt(self, plaintext):
        result = ""
        for ch in plaintext:
            try:
                ind = self.key.index(ch)
                ind = (ind + self.offset) % 62
                result += self.key[ind]
            except ValueError:
                result += ch
        return result

    def decrypt(self, ciphertext):
        result = ""
        for ch in ciphertext:
            try:
                ind = self.key.index(ch)
                ind = (ind - self.offset) % 62
                result += self.key[ind]
            except ValueError:
                result += ch
        return result

    def open_file(self):
        self.url = filedialog.askopenfilename(title="Select File", filetypes=[("Text Documents", "*.*")])

    def new_file(self):
        self.url = ""

    def save_as(self, msg):
        encrypted_text = self.encrypt(msg)
        self.url = filedialog.asksaveasfile(mode="w", defaultextension='.ntxt',
                                            filetypes=[("All Files", "*.*"), ("Text Documents", "*.*")])
        self.url.write(encrypted_text)
        filepath = self.url.name
        self.url.close()
        self.url = filepath

    def save_file(self, msg):
        if self.url == "":
            self.url = filedialog.asksaveasfile(title="Select file name", defaultextension='.ntxt',
                                                filetypes=[("Text Documents", "*.*")])
        file_name, file_extension = os.path.splitext(self.url)
        if file_extension == '.ntxt':
            msg = self.encrypt(msg)
        with open(self.url, "w", encoding="utf-8") as fw:
            fw.write(msg)

    def read_file(self, url=''):
        if url != '':
            self.url = url
        else:
            self.open_file()
        base = os.path.basename(self.url)
        file_name, file_extension = os.path.splitext(self.url)
        fr = open(self.url, "r")
        contents = fr.read()
        if file_extension == '.ntxt':
            contents = self.decrypt(contents)
        fr.close()
        return contents, base
