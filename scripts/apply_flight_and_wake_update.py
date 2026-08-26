#!/usr/bin/env python3
"""Apply confirmed flight times and an 08:00 wake/start time to the itinerary."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/itinerary.json"

x = json.loads(DATA.read_text(encoding="utf-8"))

# User's normal start time: remove the old 06:00 and 07:00 blocks.
for day in x["days"]:
    day["blocks"] = [block for block in day["blocks"] if block["time"] >= "08:00"]

# Arrival day: use the confirmed 07:40 local arrival and preserve a realistic buffer.
day1 = x["days"][0]
day1["route"] = "CX814 · HKG 11:05 → YVR 07:40 · airport arrival → McArthurGlen → Vancouver hotel"
day1["focus"] = "Land at 07:40, clear the airport properly, then shop only if the flight and energy cooperate."
day1["blocks"] = [
    {"time":"08:00","title":"YVR arrival, immigration and bags","detail":"CX814 is scheduled to arrive at 07:40 local time. Allow immigration, baggage, customs and a first coffee.","kind":"travel"},
    {"time":"09:00","title":"Transfer / luggage plan","detail":"Take the Canada Line or hotel transfer. Store luggage only with a service confirmed in advance.","kind":"travel"},
    {"time":"10:00","title":"McArthurGlen Designer Outlet","detail":"The only outlet in this plan. Keep the visit short and protect baggage capacity; skip it if arrival is delayed.","kind":"shop"},
    {"time":"11:00","title":"Outlet coffee / light lunch","detail":"Keep receipts and avoid bulky purchases until baggage limits are clear.","kind":"food"},
    {"time":"12:00","title":"Transfer to Vancouver hotel","detail":"Canada Line or car transfer, depending on the hotel.","kind":"travel"},
    {"time":"13:00","title":"Check-in / luggage drop","detail":"Ask about early check-in or leave bags securely.","kind":"rest"},
    {"time":"14:00","title":"Jet-lag reset","detail":"Shower, nap and hydrate. No sightseeing obligation.","kind":"rest"},
    {"time":"15:00","title":"Easy waterfront walk","detail":"Coal Harbour or a short hotel-neighbourhood walk.","kind":"walk"},
    {"time":"16:00","title":"Free / recover","detail":"Do not over-program arrival day.","kind":"rest"},
    {"time":"17:00","title":"Dinner option","detail":"Blue Water Cafe, Elisa, ARC or Kissa Tanto. Reserve only after the flight is known.","kind":"food"},
    {"time":"18:00","title":"Dinner","detail":"Choose one nearby restaurant, not a cross-city transfer.","kind":"food"},
    {"time":"19:00","title":"Dinner / settle","detail":"Keep the first evening short.","kind":"rest"},
    {"time":"20:00","title":"Tomorrow preview","detail":"Stanley Park, Granville Island and Gastown.","kind":"plan"},
    {"time":"21:00","title":"Sleep","detail":"Time-zone recovery.","kind":"rest"},
    {"time":"22:00","title":"Sleep","detail":"Overnight recovery.","kind":"rest"},
    {"time":"23:00","title":"Sleep","detail":"Overnight recovery.","kind":"rest"},
]

# Final Vancouver / Richmond night: make the outlet a realistic post-drive option.
day14 = x["days"][13]
day14["route"] = "Revelstoke → Vancouver / Richmond → McArthurGlen"
day14["focus"] = "Return to the YVR area, then use the final evening for the outlet only if the drive and rental-car timing cooperate."
for block in day14["blocks"]:
    if block["time"] == "17:00":
        block.update(title="McArthurGlen evening option", detail="After hotel / rental-car logistics, use this as the safer final outlet window. Skip if the drive is late.", kind="shop")
    elif block["time"] == "18:00":
        block.update(title="McArthurGlen final shop", detail="Keep purchases within airline baggage limits and confirm current hours before going.", kind="shop")
    elif block["time"] == "19:00":
        block.update(title="Dinner near YVR / Richmond", detail="Stay near the hotel; do not cross the metro area.", kind="food")

# Departure day: CX867 departs at 14:10. Do not schedule shopping before an international flight.
day15 = x["days"][14]
day15["route"] = "YVR departure · CX867 14:10 → HKG 19:20 on 8 Oct"
day15["focus"] = "Use the morning for a calm airport departure. The 14:10 international flight requires a real check-in and security buffer."
day15["overnight"] = "CX867 in flight"
day15["blocks"] = [
    {"time":"08:00","title":"Breakfast","detail":"Hotel breakfast and final weather / flight check.","kind":"food"},
    {"time":"09:00","title":"Pack and check out","detail":"Confirm luggage, receipts and hotel storage. Do not leave bags unattended in a car.","kind":"travel"},
    {"time":"10:00","title":"Transfer to YVR","detail":"Return the rental car if not already returned, or take the confirmed hotel / airport transfer.","kind":"travel"},
    {"time":"11:00","title":"CX867 check-in and bags","detail":"Be at the airport with a proper international-departure buffer before the scheduled 14:10 departure.","kind":"travel"},
    {"time":"12:00","title":"Security and immigration","detail":"Complete airport formalities; no attraction is scheduled after this point.","kind":"travel"},
    {"time":"13:00","title":"Gate buffer","detail":"Water, final purchases and boarding buffer.","kind":"travel"},
    {"time":"14:00","title":"CX867 departure buffer","detail":"Scheduled departure is 14:10 local Vancouver time.","kind":"travel"},
    {"time":"15:00","title":"CX867 in flight","detail":"Return flight to Hong Kong.","kind":"travel"},
    {"time":"16:00","title":"CX867 in flight","detail":"Return flight to Hong Kong.","kind":"travel"},
    {"time":"17:00","title":"CX867 in flight","detail":"Return flight to Hong Kong.","kind":"travel"},
    {"time":"18:00","title":"CX867 in flight","detail":"Return flight to Hong Kong.","kind":"travel"},
    {"time":"19:00","title":"CX867 in flight","detail":"Scheduled arrival is 19:20 on 8 Oct Hong Kong time.","kind":"travel"},
    {"time":"20:00","title":"Arrival recovery","detail":"Hong Kong arrival is the next calendar day, 8 Oct 2026.","kind":"rest"},
    {"time":"21:00","title":"Arrival recovery","detail":"Trip complete.","kind":"rest"},
    {"time":"22:00","title":"Arrival recovery","detail":"Trip complete.","kind":"rest"},
    {"time":"23:00","title":"Arrival recovery","detail":"Trip complete.","kind":"rest"},
]

x["meta"]["assumption"] = "Updated with confirmed flights: CX814 HKG 11:05 to YVR 07:40 on 23 Sep 2026 (11h35m); CX867 YVR 14:10 to HKG 19:20 on 8 Oct 2026. Daily plan begins at 08:00."
x["meta"]["wake_time"] = "08:00"
x["meta"]["flights"] = [
    {"flight":"CX814","date":"2026-09-23","from":"Hong Kong (HKG)","depart":"11:05","to":"Vancouver (YVR)","arrive":"07:40","duration":"11h 35m","note":"Arrival time is local Vancouver time."},
    {"flight":"CX867","date":"2026-10-07","from":"Vancouver (YVR)","depart":"14:10","to":"Hong Kong (HKG)","arrive":"19:20 on 8 Oct","duration":"14h 10m elapsed local-time conversion","note":"Arrival is the next calendar day in Hong Kong."}
]

DATA.write_text(json.dumps(x, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("updated", DATA)
print("days", len(x["days"]), "blocks", sum(len(d["blocks"]) for d in x["days"]))
print("wake_time", x["meta"]["wake_time"])
print("flights", ", ".join(f["flight"] for f in x["meta"]["flights"]))
