# -*- coding: UTF-8 -*-
from __future__ import print_function
import pickle
import os.path
import sys
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import errors

# If modifying these scopes, delete the file token.pickle.

current_dir = os.path.abspath(__file__)
parent_dir = os.path.dirname(current_dir)


class Get_Gmail_API_Service():

    def __init__(self, access_right: str, env: str):

        self.env = env

        if access_right.lower() == "readonly":
            self.SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
        elif access_right.lower() == "admin":
            self.SCOPES = ["https://mail.google.com/"]

    def get_credentials(self):

        token_path = ""
        cred_path = ""

        if self.env.lower() == "prod":
            token_path = os.path.join(parent_dir, "prod_token.pickle")
            cred_path = os.path.join(parent_dir, "prod_credentials.json")
        else:
            token_path = os.path.join(parent_dir, "token.pickle")
            cred_path = os.path.join(parent_dir, "credentials.json")

        creds = None

        try:
            # The file token.pickle stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            if os.path.exists(token_path):
                with open(token_path, 'rb') as token:
                    creds = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:

                    flow = InstalledAppFlow.from_client_secrets_file(cred_path, self.SCOPES)
                    creds = flow.run_local_server(port=0)
                    # Save the credentials for the next run
                    with open(token_path, 'wb') as token:
                        pickle.dump(creds, token)
        except:

            print("Getting Oath2 credentials occur error")
            type, message, traceback = sys.exc_info()
            print(type)
            print(message)
            traceback = traceback.tb_next

        finally:

            return creds

    def get_service(self):

        creds = self.get_credentials()
        service = build('gmail', 'v1', credentials=creds)
        return service

