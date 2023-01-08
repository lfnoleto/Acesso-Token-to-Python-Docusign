from datetime import datetime, timedelta
from docusign_esign import EnvelopesApi
from docusign_esign import ApiClient

if __name__ == '__main__':
    api_client = ApiClient()
    api_client.host = "https://demo.docusign.net/restapi"
    SCOPES = [
        'signature',
    ]

    in_file = open('private_key.txt', 'rb')
    private_key = in_file.read()
    in_file.close()

    try:
        access_token = api_client.request_jwt_user_token(
            client_id='',
            user_id='',
            oauth_host_name='account-d.docusign.com',
            private_key_bytes=private_key,
            expires_in=3600,
            scopes=SCOPES
        )
        acessoToken = access_token.access_token
        api_client.set_default_header(
            header_name='Authorization', header_value=f"Bearer {acessoToken}")
        envelope_api = EnvelopesApi(api_client)
        from_date = (datetime.utcnow() - timedelta(days=30)).isoformat()

        results = envelope_api.list_status_changes(
            account_id="", from_date=from_date)
        print(acessoToken)

    except Exception as e:
        print(e)
