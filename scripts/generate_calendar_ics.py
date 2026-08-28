#!/usr/bin/env python3
"""Generate an Apple Calendar .ics from the published Canada Rockies itinerary."""
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "itinerary.json"
OUT = Path.home() / "Desktop" / "canada-rockies-2026-apple-calendar.ics"

payload = json.loads(DATA.read_text(encoding="utf-8"))
meta = payload["meta"]
created = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

def esc(value: str) -> str:
    return (str(value).replace("\\", "\\\\").replace(";", "\\;")
            .replace(",", "\\,").replace("\n", "\\n"))

def fold(line: str) -> str:
    # RFC 5545 recommends folding long content lines at 75 octets.
    chunks=[]
    while len(line.encode("utf-8")) > 75:
        cut=75
        while len(line[:cut].encode("utf-8")) > 75:
            cut -= 1
        chunks.append(line[:cut])
        line=line[cut:]
    chunks.append(line)
    return "\r\n ".join(chunks)

def dt_for(date_s: str, time_s: str) -> datetime:
    return datetime.strptime(f"{date_s} {time_s}", "%Y-%m-%d %H:%M")

lines = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//Gina//Canada Rockies Hourly Itinerary//EN",
    "CALSCALE:GREGORIAN",
    "METHOD:PUBLISH",
    "X-WR-CALNAME:Canada Rockies 2026 · Hourly",
    "X-WR-TIMEZONE:America/Vancouver",
    "X-APPLE-CALENDAR-COLOR:#185548",
]

for day in payload["days"]:
    for index, block in enumerate(day["blocks"]):
        start = dt_for(day["date"], block["time"])
        end = start + timedelta(hours=1)
        # Use local Vancouver time for a consistent road-trip calendar.
        start_s = start.strftime("%Y%m%dT%H%M%S")
        end_s = end.strftime("%Y%m%dT%H%M%S")
        uid = f"canada-rockies-2026-{day['date']}-{index:02d}@gina.local"
        description = (
            f"{block['detail']}\n\n"
            f"Base: {day['base']}\n"
            f"Route: {day['route']}\n"
            f"Overnight: {day['overnight']}\n"
            f"Category: {block['kind']}\n"
            "Published itinerary: https://logansolaman.github.io/canada-rockies-2026-itinerary/"
        )
        lines.extend([
            "BEGIN:VEVENT",
            f"UID:{uid}",
            f"DTSTAMP:{created}",
            f"DTSTART;TZID=America/Vancouver:{start_s}",
            f"DTEND;TZID=America/Vancouver:{end_s}",
            f"SUMMARY:{esc('Canada Rockies · ' + block['title'])}",
            f"DESCRIPTION:{esc(description)}",
            f"LOCATION:{esc(day['base'])}",
            "STATUS:CONFIRMED",
            "TRANSP:OPAQUE",
            "BEGIN:VALARM",
            "ACTION:DISPLAY",
            f"DESCRIPTION:{esc('Canada Rockies · ' + block['title'])}",
            "TRIGGER:-PT10M",
            "END:VALARM",
            "END:VEVENT",
        ])

# Add the two flights as clearly identifiable reference events. They are separate
# from the hourly schedule and use the departure airport's local time.
flights = [
    {
        "uid":"canada-rockies-2026-flight-cx814@gina.local",
        "date":"2026-09-23", "start":"11:05", "end":"22:40",
        "summary":"Flight CX814 · HKG → YVR",
        "description":"Cathay Pacific CX814. Departs Hong Kong at 11:05 on 23 Sep 2026; arrives Vancouver YVR at 07:40 local time on 23 Sep 2026. Published duration: 11h35m.",
        "location":"Hong Kong International Airport (HKG)",
    },
    {
        "uid":"canada-rockies-2026-flight-cx867@gina.local",
        "date":"2026-10-07", "start":"14:10", "end":"23:59",
        "summary":"Flight CX867 · YVR → HKG",
        "description":"Cathay Pacific CX867. Departs Vancouver YVR at 14:10 on 7 Oct 2026; arrives Hong Kong at 19:20 on 8 Oct 2026. The airline flight duration was not supplied; the arrival date is next day.",
        "location":"Vancouver International Airport (YVR)",
    },
]
for flight in flights:
    start=dt_for(flight["date"],flight["start"])
    end=dt_for(flight["date"],flight["end"])
    lines.extend([
        "BEGIN:VEVENT", f"UID:{flight['uid']}", f"DTSTAMP:{created}",
        f"DTSTART;TZID=America/Vancouver:{start.strftime('%Y%m%dT%H%M%S')}",
        f"DTEND;TZID=America/Vancouver:{end.strftime('%Y%m%dT%H%M%S')}",
        f"SUMMARY:{esc(flight['summary'])}", f"DESCRIPTION:{esc(flight['description'])}",
        f"LOCATION:{esc(flight['location'])}", "STATUS:CONFIRMED", "TRANSP:OPAQUE",
        "BEGIN:VALARM", "ACTION:DISPLAY", f"DESCRIPTION:{esc(flight['summary'])}",
        "TRIGGER:-PT120M", "END:VALARM", "END:VEVENT",
    ])

lines.append("END:VCALENDAR")
with OUT.open("w", encoding="utf-8", newline="") as handle:
    handle.write("\r\n".join(fold(line) for line in lines) + "\r\n")
print(f"created {OUT}")
print(f"schedule events: {sum(len(day['blocks']) for day in payload['days'])}")
print(f"flight events: {len(flights)}")
print(f"total events: {sum(len(day['blocks']) for day in payload['days']) + len(flights)}")
