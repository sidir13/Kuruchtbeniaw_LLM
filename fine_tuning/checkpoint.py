import os


def find_lastest_checkpoint(path):
    # Folder :  'checkpoint-XXX'
    checkpoints = [
        name for name in os.listdir(path)
        if os.path.isdir(os.path.join(path, name)) and name.startswith("checkpoint-")
    ]

    # Find lastest checkpoint
    latest_checkpoint = max(checkpoints, key=lambda x: int(x.split("-")[1])) if checkpoints else None

    return latest_checkpoint
