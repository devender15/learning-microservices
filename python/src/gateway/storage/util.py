import pika, json


def upload(f, fs, channel, access):
    try:
        fid = fs.put(f)
    except Exception as err:
        return "internal server error", 500

    message = {
        "video_fid": str(fid),
        "mp3_field": None,
        "username": access["username"],
    }

    try:
        channel.basic_publish(exchange="")
