#!/usr/bin/env python3
"""Move the Rockies return so Vancouver city is reached on 5 Oct 2026."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "itinerary.json"
x = json.loads(DATA.read_text(encoding="utf-8"))

def blocks(items):
    return [{"time":t,"title":title,"detail":detail,"kind":kind} for t,title,detail,kind in items]

# 4 Oct: recovery day becomes the first return-leg overnight.
x["days"][11] = {
    "date":"2026-10-04",
    "label":"Day 12 · Canmore to Revelstoke",
    "base":"Revelstoke",
    "route":"Canmore → Golden → Rogers Pass → Revelstoke",
    "focus":"Begin the return early enough to make Vancouver city on 5 October without a single punishing final drive.",
    "overnight":"Revelstoke",
    "blocks":blocks([
        ("08:00","Breakfast + check-out","Fuel, check DriveBC and pack the vehicle.","travel"),
        ("09:00","Depart Canmore","Begin the westbound Trans-Canada return.","travel"),
        ("10:00","Yoho / Field stop","Choose one short viewpoint or coffee stop.","stop"),
        ("11:00","Continue toward Golden","Keep the day moving; avoid adding a long hike.","travel"),
        ("12:00","Golden lunch + fuel","Take a proper break and refuel.","food"),
        ("13:00","Golden to Rogers Pass","Mountain transfer; check conditions before the pass.","travel"),
        ("14:00","Rogers Pass viewpoint","Short stop if weather and parking allow.","explore"),
        ("15:00","Rogers Pass to Revelstoke","Continue toward the overnight base.","travel"),
        ("16:00","Revelstoke check-in","Arrive with daylight and reset.","travel"),
        ("17:00","Revelstoke riverfront / coffee","Easy local walk only.","explore"),
        ("18:00","Dinner","Choose a nearby Revelstoke restaurant.","food"),
        ("19:00","Dinner","Early meal before the Vancouver transfer.","food"),
        ("20:00","Flight and road check","Check DriveBC, rental return, hotel and CX867 details.","plan"),
        ("21:00","Sleep","Protect tomorrow's full transfer.","rest"),
        ("22:00","Sleep","Overnight recovery.","rest"),
        ("23:00","Sleep","Overnight recovery.","rest"),
    ])
}

# 5 Oct: arrive in Vancouver city, not merely the airport area.
x["days"][12] = {
    "date":"2026-10-05",
    "label":"Day 13 · Revelstoke to Vancouver city",
    "base":"Vancouver",
    "route":"Revelstoke → Kamloops → Hope → Vancouver city",
    "focus":"Complete the return transfer and sleep in Vancouver city on 5 October.",
    "overnight":"Vancouver city",
    "blocks":blocks([
        ("08:00","Breakfast + check-out","Fuel and confirm DriveBC before leaving.","travel"),
        ("09:00","Depart Revelstoke","Start the long westbound transfer.","travel"),
        ("10:00","Sicamous / Salmon Arm stop","Coffee, fuel and stretch.","stop"),
        ("11:00","Continue west","No major detours today.","travel"),
        ("12:00","Kamloops-area lunch","Use a practical road stop.","food"),
        ("13:00","Coquihalla / Highway 5","Check weather and construction conditions.","travel"),
        ("14:00","Continue toward Hope","Keep the Vancouver arrival target in view.","travel"),
        ("15:00","Hope / rest stop","Stretch and refuel.","stop"),
        ("16:00","Fraser Valley to Vancouver","Metro traffic buffer begins.","travel"),
        ("17:00","Vancouver city arrival","Check in downtown; return the car only if that matches the rental plan.","travel"),
        ("18:00","Hotel reset","Shower, unpack and settle into the city base.","rest"),
        ("19:00","Dinner in Vancouver city","Stay near the hotel; no airport-area detour.","food"),
        ("20:00","City evening","Short waterfront walk or rest.","walk"),
        ("21:00","Sleep","You are back in Vancouver city tonight.","rest"),
        ("22:00","Sleep","Overnight recovery.","rest"),
        ("23:00","Sleep","Overnight recovery.","rest"),
    ])
}

# 6 Oct: use the regained city day for the outlet and a relaxed final Vancouver day.
x["days"][13] = {
    "date":"2026-10-06",
    "label":"Day 14 · Vancouver city + McArthurGlen",
    "base":"Vancouver",
    "route":"Vancouver city → McArthurGlen Designer Outlet → Vancouver city",
    "focus":"A proper Vancouver city day before the international departure; outlet is placed here instead of departure morning.",
    "overnight":"Vancouver city",
    "blocks":blocks([
        ("08:00","Breakfast","Start the final full day without a hard rush.","food"),
        ("09:00","Stanley Park / seawall","Easy walk or cycle, weather permitting.","walk"),
        ("10:00","Stanley Park / Coal Harbour","Finish the waterfront loop.","walk"),
        ("11:00","Transfer to McArthurGlen","Canada Line or car transfer; confirm current hours.","travel"),
        ("12:00","McArthurGlen Designer Outlet","Final shopping window with baggage limits in mind.","shop"),
        ("13:00","McArthurGlen lunch / shopping","Keep receipts and avoid an oversized final purchase.","shop"),
        ("14:00","Return to Vancouver city","Return downtown with plenty of time before dinner.","travel"),
        ("15:00","Hotel reset","Pack and separate checked / carry-on items.","rest"),
        ("16:00","Waterfront / neighbourhood walk","Optional final Vancouver stroll.","walk"),
        ("17:00","Final dinner planning","Blue Water, Elisa, Kissa Tanto, ARC or a nearby choice.","plan"),
        ("18:00","Final Vancouver dinner","Stay in the city rather than crossing to YVR.","food"),
        ("19:00","Dinner","Slow final evening.","food"),
        ("20:00","Pack for CX867","Confirm airport transfer, rental return and baggage.","plan"),
        ("21:00","Sleep","Early departure preparation.","rest"),
        ("22:00","Sleep","Overnight recovery.","rest"),
        ("23:00","Sleep","Overnight recovery.","rest"),
    ])
}

x["meta"]["assumption"] = ("Updated: wake/start 08:00; CX814 HKG 11:05 to YVR 07:40 on 23 Sep 2026; "
    "Vancouver city is reached on 5 Oct 2026; 6 Oct is a full Vancouver city / McArthurGlen day; "
    "CX867 departs YVR 14:10 on 7 Oct 2026 and arrives HKG 19:20 on 8 Oct.")

# Replace route ribbon with the new return order.
x["route"] = [
    {"name":"Vancouver","date":"23-25 Sep + 5-7 Oct","km":"city / airport","stay":"Vancouver city base","color":"#7dd3fc"},
    {"name":"Whistler / Sea-to-Sky","date":"26 Sep","km":"122 km from Vancouver","stay":"scenic stop","color":"#a7f3d0"},
    {"name":"Kamloops","date":"26 Sep","km":"interior overnight","stay":"Kamloops hotel","color":"#fde68a"},
    {"name":"Canmore","date":"27 Sep-3 Oct","km":"main Rockies base","stay":"economical base","color":"#86efac"},
    {"name":"Cabin zone","date":"30 Sep-1 Oct","km":"two nights","stay":"Baker Creek or Storm Mountain","color":"#c4b5fd"},
    {"name":"Jasper","date":"2 Oct","km":"via Icefields Parkway","stay":"Jasper overnight","color":"#93c5fd"},
    {"name":"Revelstoke","date":"4 Oct","km":"return overnight","stay":"practical road hotel","color":"#fdba74"},
    {"name":"Vancouver city","date":"5-6 Oct","km":"city finish","stay":"downtown hotel","color":"#f0abfc"},
    {"name":"Departure","date":"7 Oct","km":"YVR airport","stay":"CX867","color":"#f9a8d4"},
]

# Update the leg labels to match the new base sequence.
x["route_legs"] = [
    {"from":"Vancouver","to":"Kamloops via Whistler","distance":"about 420 km","time":"long day with stops","note":"Scenic Sea-to-Sky start, then interior overnight."},
    {"from":"Kamloops","to":"Canmore","distance":"about 560 km","time":"long transfer","note":"Revelstoke, Golden and Yoho are stop candidates, not guaranteed attractions."},
    {"from":"Canmore","to":"Banff","distance":"about 25 km","time":"20-30 min baseline","note":"Canmore is the main economical base; parking and park-pass logistics still matter."},
    {"from":"Canmore","to":"Lake Louise","distance":"about 80 km","time":"1 h baseline","note":"Moraine Lake requires reserved shuttle or licensed access."},
    {"from":"Lake Louise","to":"Jasper","distance":"about 230 km scenic road","time":"full day with stops","note":"Icefields Parkway is the attraction, not a simple transfer."},
    {"from":"Jasper","to":"Canmore","distance":"about 300 km baseline","time":"full transfer day","note":"Return to Canmore on 3 Oct, then begin the westbound return on 4 Oct."},
    {"from":"Canmore","to":"Revelstoke","distance":"about 285 km","time":"4-6 h with stops","note":"4 Oct return overnight through Yoho and Rogers Pass."},
    {"from":"Revelstoke","to":"Vancouver city","distance":"about 565 km","time":"full transfer day","note":"Arrive and sleep in Vancouver city on 5 Oct."},
]

DATA.write_text(json.dumps(x, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("updated", DATA)
print("return bases", [(d["date"], d["base"], d["overnight"]) for d in x["days"][11:15]])
print("blocks", sum(len(d["blocks"]) for d in x["days"]))
