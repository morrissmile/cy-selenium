# -*- coding: UTF-8 -*-
import base64
import email
import io
import sys
import json
import re
from datetime import datetime
from apiclient import errors
from html import escape
from html import unescape
from bs4 import BeautifulSoup
from cy.common_code.GoogleOauth2 import Get_Gmail_API_Service
import traceback



class GmailReceiver():

    def __init__(self, env: str):
        self.index_to = 24
        self.index_subject = 18
        self.access_type = "readonly"
        self.env = env
        self.gmail_api = Get_Gmail_API_Service(self.access_type, self.env)
        self.service = self.gmail_api.get_service()

    def get_query_string(self, msg_to: str, msg_subject: str):

        query = ""

        if msg_to and msg_subject:
            query = "to:{0} AND subject:{1}".format(msg_to, msg_subject)

        elif msg_to and not msg_subject:
            query = "to:{0}".format(msg_to)

        elif not msg_to and msg_subject:
            query = "subject:{0}".format(msg_subject)

        print("Query String: {0}".format(query))

        # after_datetime = datetime.now() - timedelta(minutes=10)
        return query

    def get_message_list(self, msg_to: str, msg_subject: str):

        query = self.get_query_string(msg_to, msg_subject)

        results = self.service.users().messages().list(userId="me", labelIds=["INBOX"], q=query, maxResults=1).execute()
        messages = results.get("messages", [])

        return messages

    def get_gmail_id(self, msg_to: str, msg_subject: str):

        print("Start Get Gmail ID...")
        msg_id = ""

        if not msg_subject:
            print("The subject should not be null or empty")
            return ""

        pattern = re.compile(r"^[A-Za-z0-9+.]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$")
        match = pattern.match(msg_to)
        if not match:
            print("The email is not valid (Invalid Email:{0})".format(msg_to))
            return ""

        try:

            messages = self.get_message_list(msg_to, msg_subject)

            if not messages:
                print("There is not message found (To:{0}, Subject:{1})".format(msg_to, msg_subject))
            else:

                msg = self.service.users().messages().get(userId='me', id=messages[0]['id']).execute()
                print("To: {0}".format(msg["payload"]["headers"][self.index_to]["value"]))
                print("Subject: {0}".format(msg["payload"]["headers"][self.index_subject]["value"]))
                msg_id = msg["id"]
                print(msg["id"])

            print("End Get Gmail ID...")

        except errors.HttpError as error:
            print("An error occurred: {0}".format(error))

        except Exception as e:

            error_class = e.__class__.__name__  # get error type
            detail = e.args[0]  # get error detail
            cl, exc, tb = sys.exc_info()  # get Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1]  # get the last data at Call Stack
            fileName = lastCallStack[0]  # get the filename of error
            lineNum = lastCallStack[1]  # get the line number of error
            funcName = lastCallStack[2]  # get the function of error
            errMsg = "File: \"{0}\", line {1}, in {2}: [{3}] {4}".format(fileName, lineNum, funcName, error_class,
                                                                         detail)
            print(errMsg)
            error_message = "Type:{0} <br />Message:{1} <br />Traceback:{2}<br />".format(error_class, errMsg,
                                                                                          traceback)

        finally:

            if not msg_id:
                print("No msg_id get.")

            return msg_id

    def get_gmail_message(self, msg_to: str, msg_subject: str):

        # print("Start Get Gmail Message...")
        msg_message = {}

        if not msg_subject:
            print("The subject should not be null or empty")
            return ""

        pattern = re.compile(r"^[A-Za-z0-9+.]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$")
        match = pattern.match(msg_to)
        if not match:
            print("The email is not valid (Invalid Email:{0})".format(msg_to))
            return ""

        try:

            messages = self.get_message_list(msg_to, msg_subject)

            if not messages:
                print("There is not message found (To:{0}, Subject:{1})".format(msg_to, msg_subject))
            else:

                msg = self.service.users().messages().get(userId='me', id=messages[0]['id']).execute()
                print("To: {0}".format(msg["payload"]["headers"][self.index_to]["value"]))
                print("Subject: {0}".format(msg["payload"]["headers"][self.index_subject]["value"]))
                msg_message = msg

            # print("Success Get Gmail Message...")

        except errors.HttpError as error:

            print("An error occurred: {0}".format(error))

        except Exception as e:

            error_class = e.__class__.__name__  # get error type
            detail = e.args[0]  # get error detail
            cl, exc, tb = sys.exc_info()  # get Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1]  # get the last data at Call Stack
            fileName = lastCallStack[0]  # get the filename of error
            lineNum = lastCallStack[1]  # get the line number of error
            funcName = lastCallStack[2]  # get the function of error
            errMsg = "File: \"{0}\", line {1}, in {2}: [{3}] {4}".format(fileName, lineNum, funcName, error_class,
                                                                         detail)
            print(errMsg)
            error_message = "Type:{0} <br />Message:{1} <br />Traceback:{2}<br />".format(error_class, errMsg,
                                                                                          traceback)

        finally:

            return msg_message

    def get_gmail_content(self, msg_to: str, msg_subject: str):

        msg_content = ""
        print("Start Get Gmail Content...")

        if not msg_subject:
            print("The subject should not be null or empty")
            return ""

        pattern = re.compile(r"^[A-Za-z0-9+.]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$")
        match = pattern.match(msg_to)
        if not match:
            print("The email is not valid (Invalid Email:{0})".format(msg_to))
            return ""

        try:

            msg_html = self.get_gmail_html(msg_to, msg_subject)
            soup = BeautifulSoup(msg_html, "html.parser")
            msg_content = soup.get_text()
            # print(msg_content)

            print("Success Get Gmail Content...")

        except:

            type, message, traceback = sys.exc_info()
            print(type)
            print(message)
            traceback = traceback.tb_next

        finally:

            return msg_content

    def get_gmail_html(self, msg_to: str, msg_subject: str):

        msg_html = ""
        # print("Start Get Gmail Html...")

        if not msg_subject:
            print("The email is not valid (Invalid Email:{0})".format(msg_to))
            return ""

        pattern = re.compile(r"^[A-Za-z0-9+.]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$")
        match = pattern.match(msg_to)
        if not match:
            print("There is not message found (To:{0}, Subject:{1})".format(msg_to, msg_subject))
            return ""

        try:

            msg_message = self.get_gmail_message(msg_to, msg_subject)
            # print (msg_message)
            msg_str = msg_message["payload"]["body"]["data"]
            # print (msg_str)
            msg_html = base64.urlsafe_b64decode(msg_str)

            msg_html = msg_html.decode("utf-8")

            # print("Success Get Gmail Html...")

        except Exception as e:

            error_class = e.__class__.__name__  # get error type
            detail = e.args[0]  # get error detail
            cl, exc, tb = sys.exc_info()  # get Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1]  # get the last data at Call Stack
            fileName = lastCallStack[0]  # get the filename of error
            lineNum = lastCallStack[1]  # get the line number of error
            funcName = lastCallStack[2]  # get the function of error
            errMsg = "File: \"{0}\", line {1}, in {2}: [{3}] {4}".format(fileName, lineNum, funcName, error_class,
                                                                         detail)
            print(errMsg)
            error_message = "Type:{0} <br />Message:{1} <br />Traceback:{2}<br />".format(error_class, errMsg,
                                                                                          traceback)

        finally:

            if not msg_html:
                print("No html content get.")

            return msg_html

    def get_gmail_datetime(self, msg_to: str, msg_subject: str):

        msg_date = datetime.now()

        print("Start Get Gmail Sending Date...")

        if not msg_subject:
            print("The email is not valid (Invalid Email:{0})".format(msg_to))
            return ""

        pattern = re.compile(r"^[A-Za-z0-9+.]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$")
        match = pattern.match(msg_to)
        if not match:
            print("There is not message found (To:{0}, Subject:{1})".format(msg_to, msg_subject))
            return ""

        try:

            dateFormatter = "%a, %d %b %Y %H:%M:%S %z (%Z)"
            msg_message = self.get_gmail_message(msg_to, msg_subject)
            msg_date = datetime.strptime(msg_message["payload"]["headers"][21]["value"], dateFormatter)

            print("Success Get Gmail Sending Date...")

        except Exception as e:

            error_class = e.__class__.__name__  # get error type
            detail = e.args[0]  # get error detail
            cl, exc, tb = sys.exc_info()  # get Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1]  # get the last data at Call Stack
            fileName = lastCallStack[0]  # get the filename of error
            lineNum = lastCallStack[1]  # get the line number of error
            funcName = lastCallStack[2]  # get the function of error
            errMsg = "File: \"{0}\", line {1}, in {2}: [{3}] {4}".format(fileName, lineNum, funcName, error_class,
                                                                         detail)
            print(errMsg)
            error_message = "Type:{0} <br />Message:{1} <br />Traceback:{2}<br />".format(error_class, errMsg,
                                                                                          traceback)

        finally:

            return msg_date


if "__main__" == __name__:

    o = GmailReceiver("sit")
    html = o.get_gmail_html(msg_to="ogtest.sit+1028180758769889@gmail.com",
                            msg_subject="[sit]platform - invitation")

    print(html)
