import tkinter as tk
import random
import pandas as pd
import numpy as np

root = tk.Tk()  # create the main window

canvas = tk.Canvas(root, width=800, height=600, bg="white")  # define canvas and other window properties
root.title("Convex Hull Visualization")

points = []  # list to store all points (hull and non-hull)

def gift_wrapping_convex_hull():
    """
    Compute and draw the convex hull of the current set of points using the gift wrapping algorithm.
    """

    # edge case: need at least 3 points to form a hull
    if len(points) < 3:
        return

    # prepare data
    df = pd.DataFrame(points, columns=['x_pix', 'y_pix'])
    hull = []

    # start from leftmost (lowest x, then lowest y)
    anchor = df.loc[df['x_pix'].idxmin()]
    hull.append(anchor)
    point_on_hull = anchor

    while True:
        # first point is an endpoint by default
        endpoint = df.iloc[0]

        # iterate through all points to find the most counter-clockwise
        for i in range(len(df)):
            if endpoint.equals(point_on_hull):
                endpoint = df.iloc[i]
                continue

            # cross product to see if df.iloc[i] is more counter-clockwise
            v1 = (endpoint['x_pix'] - point_on_hull['x_pix'], endpoint['y_pix'] - point_on_hull['y_pix'])  # vector from point_on_hull to endpoint
            v2 = (df.iloc[i]['x_pix'] - point_on_hull['x_pix'], df.iloc[i]['y_pix'] - point_on_hull['y_pix'])  # vector from point_on_hull to df.iloc[i]
            cross = v1[0]*v2[1] - v1[1]*v2[0]  # take the cross product

            # if cross < 0, v2 is more counter-clockwise than v1
            # if cross == 0, they are collinear, so take the farther one
            if cross < 0 or (cross == 0 and np.linalg.norm(v2) > np.linalg.norm(v1)):
                endpoint = df.iloc[i]

        # if we have wrapped around to the first point, we're done
        point_on_hull = endpoint
        if all(point_on_hull == hull[0]):
            break
        else:
            hull.append(point_on_hull)

    # draw hull
    for i in range(len(hull)):
        x1, y1 = hull[i]['x_pix'], hull[i]['y_pix']
        x2, y2 = hull[(i+1) % len(hull)]['x_pix'], hull[(i+1) % len(hull)]['y_pix']
        canvas.create_line(x1, y1, x2, y2, fill="orange", width=2)
    return


def plot_random_points():
    """
    Plot random points on the canvas.
    """
    n = 50
    for _ in range(n):
        x = random.randint(int(canvas.winfo_x() + 0.1 * canvas.winfo_width()), int(canvas.winfo_x() + 0.9 * canvas.winfo_width()))
        y = random.randint(int(1.1 * canvas.winfo_y() + 0.1 * canvas.winfo_height()), int(canvas.winfo_y() + 0.8 * canvas.winfo_height()))
        points.append((x, y))
        r = 10  # radius of the dot
        canvas.create_oval(x - r, y - r, x + r, y + r, fill="blue", outline="")
    return


def draw_dot_on_click(event):
    """
    Draw or remove a dot on the canvas when clicked.

    Parameters
    ----------
    event : tk.Event
        The event object containing information about the mouse click.
    """
    x, y = event.x, event.y
    r = 10  # radius of the dot

    # check if already a dot at this position, if so, delete it
    for px, py in points:
        if (px - x) ** 2 + (py - y) ** 2 < r ** 2:
            points.remove((px, py))
            canvas.delete("all")
            for (dot_x, dot_y) in points:
                canvas.create_oval(dot_x - r, dot_y - r, dot_x + r, dot_y + r, fill="blue", outline="")
            return
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="blue", outline="")
    points.append((x, y))
    return


# create the buttons and pack them into the window
random_button = tk.Button(root, text="Plot Random Points", command=plot_random_points)
convex_hull_button = tk.Button(root, text="Compute Convex Hull (Gift Wrapping)", command=gift_wrapping_convex_hull)
clear_button = tk.Button(root, text="Clear Points", command=lambda: (points.clear(), canvas.delete("all")))
clear_button.pack(side=tk.TOP, pady=5)
random_button.pack(side=tk.TOP, pady=5)
canvas.pack()
convex_hull_button.pack()
canvas.bind("<Button-1>", draw_dot_on_click)

# start the Tkinter event loop
root.mainloop()
