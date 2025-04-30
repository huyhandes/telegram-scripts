## Installation

- Clone the repository:
- Run pip install -r requirements.lock

## Usage

1.  Replace the following values in `tele.py` with your own:

    -   `APP_ID`: Your Telegram API ID.
    -   `APP_HASH`: Your Telegram API hash.
    -   `GROUP_ID`: The ID of the Telegram group to crawl messages from.
    -   `CHANNEL_ID`: The ID of the channel to reply to (check what this is used for in the code.)

2.  Run the script:

    ```bash
    python tele.py
    ```

The script will print the messages crawled from the Telegram group.

## Configuration

The following parameters can be configured in `tele.py`:

-   `LIMIT`: The maximum number of messages to retrieve.
-   `offset_date`: The date from which to start retrieving messages (currently set to 7 days ago).

## Notes

-   You need to have a Telegram account to use this script.
-   You need to create a Telegram application to get your `APP_ID` and `APP_HASH`.  You can do this at https://my.telegram.org/apps
-   This script only prints the messages. You need to implement the `store_messages` function to store the messages in a database.

