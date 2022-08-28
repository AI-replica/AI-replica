from datetime import datetime, timezone
import os
from apscheduler.schedulers.background import BackgroundScheduler
from server.utils.config import GENERATED_FILES_DIR

REMOVE_OUTDATED_SPEECH_FILES_JOB_INTERVAL = 10  # seconds
SPEECH_FILE_LIFE_TIME = 10  # seconds


def remove_outdated_speech_files_job():
    current_time_utc_aware = datetime.now(timezone.utc)
    current_time_utc_timestamp = (
        current_time_utc_aware.timestamp()
    )  # POSIX timestamp, time from 01.01.1970 UTC, in seconds

    print("remove_outdated_speech_files_job is running", current_time_utc_aware)

    if not os.path.exists(GENERATED_FILES_DIR):
        print(f"The directory does not exist: {GENERATED_FILES_DIR}")
        return

    for file in os.scandir(GENERATED_FILES_DIR):
        file_last_modified = (
            file.stat().st_mtime
        )  # POSIX timestamp, time from 01.01.1970 UTC, in seconds
        if file_last_modified < current_time_utc_timestamp - SPEECH_FILE_LIFE_TIME:
            os.unlink(file.path)


def remove_outdated_speech_files_on_schedule():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        remove_outdated_speech_files_job,
        "interval",
        seconds=REMOVE_OUTDATED_SPEECH_FILES_JOB_INTERVAL,
    )
    scheduler.start()
