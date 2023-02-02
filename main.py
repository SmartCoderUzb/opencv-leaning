import cv2
import numpy as np

def show(img):
    cv2.imshow("Circles",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def write(img,name="circles.png"):
    cv2.imwrite(name,img)

def generator(question_range = 10,sircle_range = 5,square_x = 0, square_y = 0):
    img = np.zeros((712,712,3), np.uint8)
    for question in range(1,question_range+1):
        for i in range(0, sircle_range):
            radius = 20
            center = (radius + i*(radius*2)+square_x, ((radius*2)*question+square_y-radius))
            color = (0, 255, 0)
            thickness = 1
            cv2.circle(img, center, radius, color, thickness)


    pt1 = (square_x,square_y)
    pt2 = (square_x+(radius*2)*sircle_range,square_y+(radius*2)*question)
    color = (255,0,0)
    thickness = 1
    cv2.rectangle(img,pt1,pt2,color,thickness)
    return img


import tkinter as tk
root = tk.Tk()
root.title("Input Form")

# Two input fields
input1 = tk.Text(root, height=1)
input1.insert("1.0", "Savollar soni")
input1.bind("<FocusIn>", lambda args: input1.delete("1.0", tk.END) if input1.get("1.0", tk.END) == "Savollar soni\n" else None)
input1.bind("<FocusOut>", lambda args: input1.insert("1.0", "Savollar soni") if input1.get("1.0", tk.END) == "\n" else None)
input2 = tk.Text(root, height=1)
input2.insert("1.0", "Variantlar soni")
input2.bind("<FocusIn>", lambda args: input2.delete("1.0", tk.END) if input2.get("1.0", tk.END) == "Variantlar soni\n" else None)
input2.bind("<FocusOut>", lambda args: input2.insert("1.0", "Variantlar soni") if input2.get("1.0", tk.END) == "\n" else None)
input3 = tk.Text(root, height=1)
input3.insert("1.0","Joylashuv-X")
input3.bind("<FocusIn>",lambda args: input3.delete("1.0",tk.END) if input3.get("1.0",tk.END) == "Joylashuv-X\n" else None)
input3.bind("<FocusOut>", lambda args: input3.insert("1.0", "Joylashuv-X") if input3.get("1.0",tk.END) == "\n" else None)

input4 = tk.Text(root, height=1)
input4.insert("1.0","Joylashuv-Y")
input4.bind("<FocusIn>",lambda args: input4.delete("1.0",tk.END) if input4.get("1.0",tk.END) == "Joylashuv-Y\n" else None)
input4.bind("<FocusOut>", lambda args: input4.insert("1.0", "Joylashuv-Y") if input4.get("1.0",tk.END) == "\n" else None)

input1.pack()
input2.pack()
input3.pack()
input4.pack()
# Submit button
def submit():
    input1_value = input1.get("1.0", tk.END).strip()
    input2_value = input2.get("1.0", tk.END).strip()
    input3_value = input3.get("1.0", tk.END).strip()
    input4_value = input4.get("1.0", tk.END).strip()
    if input1_value == "Savollar soni":
        input1_value = ""
    if input2_value == "Variantlar soni":
        input2_value = ""
    if input3_value == "Joylashuv-X":
        input3_value = ""
    if input4_value == "Joylashuv-Y":
        input4_value = ""
    img = generator(
        int(input1_value) if input1_value else 1,
        int(input2_value) if input2_value else 1,
        int(input3_value) if input3_value else 0,
        int(input4_value) if input4_value else 0,
    )
    write(img)
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()
root.mainloop()
