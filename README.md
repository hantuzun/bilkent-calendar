# Bilkent Calendar
Creates .ics calendar files using the tables at [Bilkent Academic Calendar](http://www.bilkent.edu.tr/bilkent/academic/calendar/).

You can import these files to your calendar applications (Google Calendar, Apple Calendar etc.).


### Subscribe to the 2014-15 Calendars
Use your calendar application and add these calendars by URL:
* Bilkent 2014-15 Academic Calendar: https://www.google.com/calendar/ical/jc51uv1k70h0m0lcaceeqgnm38%40group.calendar.google.com/public/basic.ics

* Bilkent IDMYO 2014-15 Academic Calendar: https://www.google.com/calendar/ical/2rbainhoq88aleurng61hrkv0k%40group.calendar.google.com/public/basic.ics

Instructions for [Google Calendar](https://support.google.com/calendar/answer/37100) and [Apple Calendar](http://support.apple.com/kb/PH11523).

![Alt Text](https://cloud.githubusercontent.com/assets/2770895/6021941/13a5b84e-abc2-11e4-9d31-7d5a88f06bd9.png)

---


### Get the Calendar Files
1. Download .ics files at https://github.com/emrehan/bilkent-calendar/releases/tag/1.0.
2. Import these calendars to your calendar application.
  * [for Google Calendar](https://support.google.com/calendar/answer/37118)
  * [for Apple Calendar](http://support.apple.com/kb/PH11524)
  * [for Android](https://play.google.com/store/apps/details?id=jitdesign.icsimport)
  * [for iPhone or iPad](https://discussions.apple.com/thread/5073594)


### Build Instructions
1. You will need Python 3.4+ to run these scripts.
2. Install these depedencies:
  * beautifulsoup4
  * icalendar
  * urllib3
3. Run the master script: `python3 bilkent-calendar.py`
4. Calendar files will be created at your home folder.

Pull requests are welcome.
