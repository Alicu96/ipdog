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
```

2. Build the Docker image:

```bash
bash
docker build -t ip_monitor .
```

3. Run the Docker container:

```bash
bash
docker run ip_monitor
```

## Usage
The application will check for IP changes every hour indefinitely and send a notification via Telegram if a change is detected.