# EXE2PY
This project allows you to decompile `.exe` files(made to python) back into Python code. Either run it on linux or on Google Collab.
It also facilitates faster uploads of `.exe` files to Google Colab for processing.

---

## Features

- **Fast File Uploads**: Upload .exe files more quickly to Colab using a Cloudflare tunnel.
- **Decompiling EXE Files**: Convert .exe files back into their original Python code using the provided decompiling scripts.
- **Download Decompiled Files**: Easily download a .zip file containing all the extracted files after decompilation.
- **Cross-Platform**: Can be run in environments like Google Colab, making it accessible and easy to use for anyone.

---

## Instructions for Google Colab

1. **Open the Notebook in Google Colab**  
   Click the link below to open the project’s notebook in Google Colab:
   
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Nishant2009/EXE2PY/blob/main/EXE2PY.ipynb)

2. **Run the Cells**  
   Once the notebook is opened in Colab, run each cell one by one by pressing **Shift + Enter** or clicking the "Play" button next to each cell.

   The notebook will guide you through the following steps:
   - Cloning the repository and setting up the environment
   - Uploading `.exe` files to Colab using a Cloudflare tunnel
   - Decompiling the `.exe` file
   - Downloading the decompiled files as a `.zip`

3. **Upload Your EXE File**  
   Follow the instructions in the notebook to upload your `.exe` file to Colab using the provided Cloudflare link.

4. **Decompile and Download the Files**  
   After the `.exe` file is uploaded, the notebook will automatically decompile it, and you will be able to download the decompiled files in a `.zip` format.

---

## Instructions to run locally on LINUX

### 1. **Clone the Repository**
Clone the repository to your local machine or Google Colab environment:

```bash
git clone https://github.com/Nishant2009/EXE2PY
cd EXE2PY
```

### 2. **Give Execution Permissions**
Make all the files executable:

```bash
chmod +x *
```

### 3. **Copy EXE file to same folder**
Copy your `.exe` file in the same folder `(./EXE2PY)`.

### 4. **Decompile the EXE File**
After uploading the `.exe` file, run the following Python script to decompile the file:

```bash
python3 run.py your_file.exe
```

### 5. **Download Decompiled Files**
Once the decompilation is complete, you can see the `.zip` file containing the decompiled files

---

## Contributing

We welcome contributions to this project! If you'd like to contribute, follow these steps:

1. Fork the repository.
2. Clone your fork to your local machine.
3. Create a new branch for your changes.
4. Make your changes, ensuring that the code is well-tested and documented.
5. Submit a pull request describing the changes you've made.

Please ensure that your contributions adhere to the project’s code of conduct and coding standards.

## Reporting Issues

If you encounter any issues or bugs, please follow these steps to report them:

1. Check the [existing issues](https://github.com/Nishant2009/EXE2PY/issues) to see if your issue has already been reported.
2. If the issue hasn’t been reported yet, create a new issue by clicking the "New Issue" button on the [Issues page](https://github.com/Nishant2009/EXE2PY/issues).
3. Provide a detailed description of the issue, including:
   - Steps to reproduce the issue
   - Any error messages or logs
   - Your environment (e.g., OS, Python version, etc.)
   - Any other relevant details

We’ll try to resolve the issue as quickly as possible!

---

## License
This project is licensed under the MIT License.

---
