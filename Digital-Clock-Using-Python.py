{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78c891fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import *\n",
    "import time\n",
    "from datetime import date\n",
    "from datetime import datetime\n",
    "\n",
    "\n",
    "\n",
    "window = Tk()\n",
    "window.geometry(\"500x500\")\n",
    "window.title(\"Digital Clock\")\n",
    "\n",
    "\n",
    "\n",
    "def current_date():\n",
    "    today = date.today()\n",
    "    \n",
    "    today_date = today.strftime(\"%B %d, %Y\")\n",
    "    date_label.config(text=f\"Today is : {today_date}\")\n",
    "\n",
    "\n",
    "date_label = Label(window, font=(\"roman\", 20, \"bold\"), fg=\"steel blue\", bg=\"pink\", width=\"30\")\n",
    "date_label.pack(pady=\"60\")\n",
    "\n",
    "\n",
    "def digital_clock():\n",
    "    now = datetime.now()\n",
    "    get_time = now.strftime(\"%H:%M:%S\")\n",
    "    clock_label.config(text=f\"Time is : {get_time}\")\n",
    "    clock_label.after(1000, digital_clock) \n",
    "\n",
    "clock_label = Label(window, font=(\"roman\", 20, \"bold\"), fg=\"steel blue\", bg=\"pink\", width=\"20\")\n",
    "clock_label.pack(pady=\"20\")\n",
    "\n",
    "digital_clock()\n",
    "current_date()\n",
    "window.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a2c2d1ef",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
