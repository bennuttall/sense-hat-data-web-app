# Sense HAT Data Web App

Log Sense HAT sensor data and show it in a web app

## Requirements

### Hardware

- Raspberry Pi
- Sense HAT

### Software

- Flask
- Sense HAT Python library

Advanced version:

- Apache
- Apache mod WSGI
- Weaved

```bash
sudo apt-get install python3-flask apache2 libapache2-mod-wsgi-py3 weavedconnectd -y
```

## Usage

### Simple: LAN

The simple version can be run on a LAN, so you can view the Flask web app on any device on your local network.

Clone this repo and run `db.py` in cron to store data, then run `app.py` and run the web app:

1. Clone this repository:
    `git clone https://github.com/bennuttall/sense-hat-data-web-app`
1. Enter the projects's `www` directory:
    - cd `sense-hat-data-web-app/www`
1. Run the data logger once:
    - `python3 db.py`
1. Find the Pi's local IP address (and keep a note of it):
    - `hostname -I`
1. Run the web app:
    - `python app.py`
1. Navigate to the IP address in a web browser on any device on your network (e.g. `http://192.168.1.3:5000`)
    - You should see the Sense HAT temperature and humidity data in the browser
1. Use [Cron](https://www.raspberrypi.org/documentation/linux/usage/cron.md) to schedule `db.py` to be run regularly
    - Now every time you view the web page, it will be up-to-date

### Advanced: Internet

Using Apache and mod WSGI to serve the Flask web app, you can connect to Weaved to open your Pi to the web.

1. Do all steps from LAN version (but you don't need to keep `python3 app.py` running)
1. See [Weaved documentation](https://www.raspberrypi.org/documentation/remote-access/access-over-Internet/internetaccess.md), [sign up](http://www.weaved.com/), install on your Pi and configure web service
1. Install Apache and mod WSGI as above
1. Configure your vhost:
    - `sudo cp sense-hat-data-web-app/apache/000-default.conf /etc/apache2/sites-available/`
1. Restart Apache:
    - `sudo service apache2 restart`
1. Get your Pi's web address from Weaved (e.g. `https://abcdefgh.p19.weaved.com/`)
1. Navigate to it in a web browser
