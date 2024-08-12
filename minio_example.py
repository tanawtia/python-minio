from minio import Minio
from minio.error import S3Error

client = Minio(
    "localhost:9000",
    access_key="admin",
    secret_key="secretpassword",
    secure=False
)

bucket_name = "mybucket"
object_name = "file.txt"
file_path = "path/to/your/file.txt"
download_path = "path/to/save/file.txt"

try:
    # Create bucket if not exists
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
        print(f"Bucket '{bucket_name}' created.")

    # Upload an object
    client.fput_object(bucket_name, object_name, file_path)
    print(f"'{object_name}' uploaded.")

    # List objects
    objects = client.list_objects(bucket_name)
    print("Objects in bucket:")
    for obj in objects:
        print(f" - {obj.object_name}")

    # Download the object
    client.fget_object(bucket_name, object_name, download_path)
    print(f"'{object_name}' downloaded to '{download_path}'.")

    # Delete the object
    client.remove_object(bucket_name, object_name)
    print(f"'{object_name}' deleted.")

except S3Error as err:
    print(f"Error occurred: {err}")
