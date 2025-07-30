import boto3
import os
import uuid
from dotenv import load_dotenv
from datetime import datetime

# Încarcă variabilele din .env
load_dotenv()

# Setează detalii AWS
table_name = os.getenv("DYNAMODB_TABLE")
region = os.getenv("AWS_REGION")

# Creează conexiunea la DynamoDB
dynamodb = boto3.resource("dynamodb", region_name=region)
table = dynamodb.Table(table_name)

def write_mock_data():
    try:
        item = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "note": "Sample data from Scriptweaver CLI"
        }
        table.put_item(Item=item)
        return "✅ Data written to DynamoDB!"
    except Exception as e:
        return f"❌ Error writing to DynamoDB: {str(e)}"

