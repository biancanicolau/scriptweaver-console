import boto3
import os
import uuid
from dotenv import load_dotenv
from datetime import datetime

# Încarcă variabilele din .env
load_dotenv()
print("DEBUG: Table name from env:", os.getenv("DYNAMODB_TABLE"))


# Setează detalii AWS
table_name = os.getenv("DYNAMODB_TABLE")
region = os.getenv("AWS_REGION")

# Creează conexiunea la DynamoDB
access_key = os.getenv("AWS_ACCESS_KEY_ID")
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

dynamodb = boto3.resource(
    "dynamodb",
    region_name=region,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)

table = dynamodb.Table(table_name)

def write_mock_data():
    try:
        item = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "note": "Sample data from Scriptweaver CLI"
        }
        print(">>> Creating item:", item)  # DEBUG
        table.put_item(Item=item)
        return "✅ Data written to DynamoDB!"
    except Exception as e:
        return f"❌ Error writing to DynamoDB: {str(e)}"

