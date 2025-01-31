# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
scopes = ["https://www.googleapis.com/auth/contacts.readonly"]
# https://www.googleapis.com/auth/youtube.readonly",
def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    creds = None
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "credentials.json"
    if  os.path.exists("token2.json"):
        creds = Credentials.from_authorized_user_file("token2.json",scopes)
        if not creds and not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
                creds=flow.run_local_server(port=0)
            with open ("token2.json","w") as token:
                token.write(creds.to_json())            
    try:
        youtube = build("people", "v1", credentials=creds )
        print("List 10 connection names")
        results = ( youtube.people().connections().list(
                resourceName="people/me",
                pageSize=10,
                sortOrder='LAST_MODIFIED_DESCENDING' ,
               
                personFields="addresses,ageRanges,biographies,birthdays,calendarUrls,clientData,coverPhotos,emailAddresses,events,externalIds,genders,imClients,interests,locales,locations,memberships,metadata,miscKeywords,names,nicknames,occupations,organizations,phoneNumbers,photos,relations,sipAddresses,skills,urls,userDefined").execute()
        )
    except HttpError as err:
       print(err)
    # Call the People API
    connections = results.get("connections", [])
    nextPageToken = results.nextPageToken
    nextSyncToken = results.get("nextSyncToken")
    totalItems	= results.get("totalItems")

    for person in connections:
            # * addresses * ageRanges * biographies * birthdays * calendarUrls * clientData * coverPhotos * emailAddresses * events * externalIds * genders * imClients * interests 
            # * locales * locations * memberships * metadata * miscKeywords * names * nicknames * occupations * organizations * phoneNumbers * photos * relations * sipAddresses * skills
            # * urls * userDefined
            names = person.get("names", [])
            addr  = person.get("addresses", []) 
            phones = person.get("phoneNumbers", [])
            totalItems = person.get("fileAses", [])
            if names:
                phone =None
                if phones:
                    phone = phones[0].get("canonicalForm")
                    name = names[0].get("givenName")
                print(name,phone)
                



    # print(response)

if __name__ == "__main__":
    main()