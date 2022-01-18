from tkinter import *
from tkinter import filedialog, messagebox
import time
from selenium import webdriver
import numpy as np
from tensorflow.keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf


# tkinter GUI class
class tkGUI:

    def __init__(self):
        self.root = Tk()

        # header properties
        self.root.title('Handwritten Logogram Translator')

        self.root.iconbitmap("favicon.ico")

        # manu bar and textbox
        menubar = Menu(self.root)

        self.text = Text(self.root)

        self.text.pack()

        self.text.configure(font=("Arial", 15, "bold"))

        # manu bar setting / File, Help tab
        filemenu = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="File", menu=filemenu)

        filemenu.add_command(label="New", command=self.Initialize)

        filemenu.add_command(label="Open", command=self.Load)

        filemenu.add_command(label="Save as...", command=self.Save)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.root.destroy)

        helpmenu = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="Help", menu=helpmenu)

        helpmenu.add_command(label="About Me", command=self.Info)

        self.root.config(menu=menubar)

        self.root.mainloop()

    # Load the model and conduct the translating task
    def Load(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("JPG files", "*.jpg"),
                                                         ("all files", "*.*")))
        self.text.delete('1.0', END)
        # Loading model
        model = load_model("CNLrecognition_model.h5", compile=True)
        if filename[-4:] != ".jpg":
            messagebox.showinfo("MsgBox", "Error! Please input a .jpg file.")
            return
        # predicting images
        path = filename
        img = image.load_img(path, target_size=(64, 64))
        x = image.img_to_array(img)
        x = tf.image.rgb_to_grayscale(x)
        x = np.expand_dims(x, axis=0)
        x = x / 255.
        images = np.vstack([x])
        prediction = model.predict(images)
        result = np.argmax(prediction, axis=1)
        label = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "百", "千", "万", "亿"]
        letter = label[int(result)]

        driver = webdriver.Chrome("C:/chromedriver")
        driver.get("https://papago.naver.com/?sk=zh-TW&tk=en")

        time.sleep(6)
        # input the word we look for
        input_box = driver.find_element_by_css_selector("textarea#txtSource")
        input_box.send_keys(letter)

        # click the translating button
        button = driver.find_element_by_css_selector("button#btnTranslate")
        button.click()

        # awaits the result & print the output
        time.sleep(3)
        meaning = driver.find_element_by_css_selector("div#txtTarget").text
        print("fetching the result")
        # quit the driver
        driver.quit()

        # insert the result text in the textbox
        self.text.insert(END, meaning)

    # Save the text file containing translation result
    def Save(self):
        filename = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        ts = str(self.text.get('1.0', END))
        print(filename)
        if filename is None:
            return
        filename.write(ts)
        filename.close()

    def Initialize(self):
        self.text.delete('1.0', END)

    def Info(self):
        messagebox.showinfo("MsgBox",
                            "Thank You For Using My Prototype ML-based App!\n" +
                            "This is a translating Bot written with TensorFlow and Tkinter.\n" +
                            "Please read readme.txt if you don't know how to use it.")


if __name__ == '__main__':
    Example = tkGUI()
