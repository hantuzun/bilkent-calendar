# Bilkent Calendar
Creates .ics calendar files using the tables at [Bilkent Academic Calendar](http://www.bilkent.edu.tr/bilkent/academic/calendar/).

You can import these files to your calendar applications (Google Calendar, Apple Calendar etc.).

![calendar view](https://cloud.githubusercontent.com/assets/2770895/6021941/13a5b84e-abc2-11e4-9d31-7d5a88f06bd9.png)


### Get the Calendar Files
1. Download .ics files at https://github.com/emrehan/bilkent-calendar/releases/tag/1.0.
2. Import these calendars to your calendar application.
  * [for Google Calendar](https://support.google.com/calendar/answer/37118?hl=en)
  * [for Apple Calendar](http://support.apple.com/kb/PH11524)


### Build Instructions
1. You will need Python 3.4+ to run these scripts.
2. Install these depedencies:
  * beautifulsoup4
  * icalendar
  * urllib3
3. Run the master script: `python3 bilkent-calendar.py`
4. Calendar files will be created at your home folder.

Pull requests are welcome.
