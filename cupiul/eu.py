from google.cloud import talent
import six


def list_accounts(project_id):
    """List Accounts"""

    client = talent.AccountServiceClient()

    # project_id = 'Your Google Cloud Project ID'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode("utf-8")
    parent = f"projects/{project_id}"

    # Iterate over all results
    results = []
    for response_item in client.list_accounts(parent=parent):
        print(f"Account Name: {response_item.name}")
        print(f"Display Name: {response_item.display_name}")
        print(f"External ID: {response_item.external_id}")
        results.append(response_item)

    return results

  
