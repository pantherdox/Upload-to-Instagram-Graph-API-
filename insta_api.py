import json
import requests
import time

# 1. Upload video to Instagram
def upload_video(video_url, access_token, ig_user_id):
    post_url = "https://graph.facebook.com/v21.0/{}/media".format(ig_user_id)
    payload = {
        'media_type': 'REELS',
        'video_url': video_url,
        'caption': 'Write your caption here',
        'access_token': access_token
    }
    r = requests.post(post_url, data=payload)
    print(r.text)
    results = json.loads(r.text)
    return results

# 2. Get Uploading Status
def status_code(ig_container_id, access_token):
    graph_url = "https://graph.facebook.com/v21.0/"
    url = graph_url + ig_container_id
    param = {
        'access_token': access_token,
        'fields': 'status_code'
    }
    response = requests.get(url, params=param)
    response = response.json()
    return response['status_code']

# 3. Publish video to Instagram
def publish_video(results, ig_user_id, access_token):
    if 'id' in results:
        creation_id = results['id']
        second_url = "https://graph.facebook.com/v21.0/{}/media_publish".format(ig_user_id)
        second_payload = {
            'creation_id': creation_id,
            'access_token': access_token
        }
        r = requests.post(second_url, data=second_payload)
        print(r.text)
        print("Video successfully published to Instagram")
    else:
        print("Could not complete video publishing")

# Public area
ig_user_id = "your ig_user_id"
access_token = "your access token"
video_url = "direct video url link"

# Call all 3 functions
# 1. Upload
results = upload_video(video_url, access_token, ig_user_id)
print("Please wait for some time")
print("Uploading in progress")
time.sleep(10)

# 2. Check status
ig_container_id = results['id']
s = status_code(ig_container_id, access_token)

# 3. Publish if finished
if s == 'FINISHED':
    print("Video uploaded successfully")
    publish_video(results, ig_user_id, access_token)
else:
    print("Wait for some time")
    time.sleep(60)
    publish_video(results, ig_user_id, access_token)
