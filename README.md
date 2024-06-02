# IP Monitor Application

## Overview
This application monitors the public IP address of the device and notifies the user via Telegram if the IP changes.

## Setup

### Requirements
- Docker
- A Telegram bot token and chat ID

### Configuration
1. Create a `.env` file in the root directory with the following content:

```text
TELEGRAM_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
CHECK_INTERVAL_SEC=interval_in_second_for_checking_ip
```

2. Build the Docker image:

```bash
docker build -t ip_monitor .
```

3. Run the Docker container:

```bash
docker run ip_monitor
```

## Usage
The application will check for IP changes every hour indefinitely and send a notification via Telegram if a change is detected.

## How to Obtaining Telegram Credentials

### Getting the TELEGRAM_TOKEN
1. **Create a Bot**:
   - Open Telegram and search for "BotFather" or go to `t.me/BotFather`.
   - Start a conversation and type `/newbot`.
   - Follow the instructions to name your bot and get a username.
   - BotFather will provide you with a token. This is your `TELEGRAM_TOKEN`.

### Getting the TELEGRAM_CHAT_ID
2. **Find Your Chat ID**:
   - Start a conversation with your newly created bot, or add it to a group.
   - Use `userinfobot` (`t.me/userinfobot`) by starting a conversation with it to get your personal chat ID.
   - Alternatively, add `@RawDataBot` to a group, send a message, and it will provide a message where you can find the `chat_id` of the group.