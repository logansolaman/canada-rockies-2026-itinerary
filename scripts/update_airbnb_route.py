#!/usr/bin/env python3
"""Rebuild the Canada itinerary around the user's fixed Airbnb bases.

The first three nights and final two nights remain in Vancouver. The supplied
Airbnb bases are treated as fixed overnight anchors; the day plans are then
ordered to minimize backtracking while keeping the 08:00 start time.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/itinerary.json"


def day(date, label, base, route, focus, overnight, items):
    blocks = [
        {
            "time": f"{h:02d}:00",
            "title": "Open / flexible",
            "detail": "Keep this hour available for meals, weather, parking, queues or a slower choice.",
            "kind": "buffer",
        }
        for h in range(8, 24)
    ]
    by = {b["time"]: b for b in blocks}
    for time, title, detail, kind in items:
        by[time] = {"time": time, "title": title, "detail": detail, "kind": kind}
    return {
        "date": date,
        "label": label,
        "base": base,
        "route": route,
        "focus": focus,
        "overnight": overnight,
        "blocks": [by[f"{h:02d}:00"] for h in range(8, 24)],
    }


def build_days():
    d = []
    d.append(day("2026-09-23", "Day 1 · Arrival in Vancouver · Clive Avenue", "Clive Avenue, Joyce-Collingwood", "CX814 · HKG 11:05 → YVR 07:40 · YVR → Clive Avenue", "Arrive gently and settle into the first Airbnb in East Vancouver's Joyce-Collingwood area. Keep the first afternoon close to home.", "Clive Avenue Airbnb · Joyce-Collingwood", [
        ("08:00", "YVR arrival, immigration and bags", "CX814 is scheduled to arrive at 07:40 local time. Allow immigration, baggage, customs and a first coffee.", "travel"),
        ("09:00", "Transfer to Clive Avenue", "Take the Canada Line to Joyce-Collingwood or a taxi/rideshare. The Airbnb is near Joyce Station; keep luggage secure.", "travel"),
        ("10:00", "McArthurGlen option", "Use only if arrival is smooth; it is on the way from YVR but do not force shopping after a long flight.", "shop"),
        ("11:00", "Coffee / light lunch", "Keep the first meal easy and nearby.", "food"),
        ("12:00", "Continue to Clive Avenue", "Head to the first three-night Airbnb in the Collingwood / Joyce-Collingwood area.", "travel"),
        ("13:00", "Luggage drop / check-in", "Ask about early check-in or leave bags securely.", "rest"),
        ("14:00", "Jet-lag reset", "Shower, nap and hydrate. No sightseeing obligation.", "rest"),
        ("15:00", "Collingwood neighbourhood walk", "Walk around Joyce-Collingwood, or rest at the Airbnb if needed.", "walk"),
        ("16:00", "Central Park / Metrotown option", "Only if alert: Central Park is close and Metrotown is a practical nearby outing.", "explore"),
        ("17:00", "Dinner nearby", "Choose somewhere close to the stay.", "food"),
        ("18:00", "Dinner", "Keep the first evening short.", "food"),
        ("19:00", "Settle in", "Confirm tomorrow's city plan and rental-car timing.", "plan"),
        ("20:00", "Wind down", "Prepare for a normal 08:00 start.", "rest"),
        ("21:00", "Sleep", "Time-zone recovery.", "rest"),
        ("22:00", "Sleep", "Overnight recovery.", "rest"),
        ("23:00", "Sleep", "Overnight recovery.", "rest"),
    ]))
    d.append(day("2026-09-24", "Day 2 · East Vancouver and downtown", "Clive Avenue, Joyce-Collingwood", "Joyce-Collingwood → Central Park / Metrotown → Gastown → Stanley Park → Joyce-Collingwood", "Use the SkyTrain from Joyce-Collingwood to make the downtown day easy without moving the Airbnb.", "Clive Avenue Airbnb · Joyce-Collingwood", [
        ("08:00", "Breakfast near Joyce-Collingwood", "Start locally and use the SkyTrain rather than driving downtown.", "food"),
        ("09:00", "Joyce-Collingwood / Central Park", "Easy neighbourhood start or Central Park walk.", "walk"),
        ("10:00", "Metrotown", "Shopping, coffee and a practical rainy-day option close to the Airbnb.", "explore"),
        ("11:00", "Metrotown / lunch", "Keep the morning close to home.", "food"),
        ("12:00", "SkyTrain to Waterfront", "Use Joyce Station for the direct Expo Line ride downtown.", "travel"),
        ("13:00", "Gastown", "Water Street, galleries and historic streets.", "explore"),
        ("14:00", "Canada Place", "Waterfront views and harbour walk.", "walk"),
        ("15:00", "Stanley Park", "Walk the eastern seawall or use a bike rental.", "walk"),
        ("16:00", "Stanley Park / Coal Harbour", "Finish a comfortable loop; do not force the entire seawall.", "explore"),
        ("17:00", "Return to Joyce-Collingwood", "SkyTrain back before dinner.", "travel"),
        ("18:00", "Dinner", "Choose one neighbourhood restaurant.", "food"),
        ("19:00", "Dinner", "Slow meal.", "food"),
        ("20:00", "Pack for road start", "Layers, snacks, documents and rental-car details.", "plan"),
        ("21:00", "Sleep", "Tomorrow is North Shore day.", "rest"),
        ("22:00", "Sleep", "Overnight recovery.", "rest"),
        ("23:00", "Sleep", "Overnight recovery.", "rest"),
    ]))
    d.append(day("2026-09-25", "Day 3 · East Vancouver, Burnaby and Richmond", "Clive Avenue, Joyce-Collingwood", "Joyce-Collingwood → Central Park / Metrotown → Richmond or waterfront → Joyce-Collingwood", "Use the final Clive Avenue day for nearby East Vancouver and Burnaby sights, with an optional Richmond stop before the road trip.", "Clive Avenue Airbnb · Joyce-Collingwood", [
        ("08:00", "Breakfast near Joyce-Collingwood", "Start locally and check weather.", "food"),
        ("09:00", "Central Park", "Easy walk close to the Airbnb; use Metrotown as the rainy-day alternative.", "walk"),
        ("10:00", "Metrotown / Burnaby", "Shopping and coffee, or continue to Deer Lake Park if weather is comfortable.", "explore"),
        ("11:00", "Deer Lake Park option", "Easy lake loop, Burnaby Village Museum or Shadbolt Centre if open.", "explore"),
        ("12:00", "Lunch near Metrotown", "Keep this East Vancouver / Burnaby day practical.", "food"),
        ("13:00", "Richmond option", "Optional Canada Line trip to Richmond Centre or Steveston; skip if you prefer a slower day.", "travel"),
        ("14:00", "Steveston village option", "Historic fishing village and waterfront if the Richmond option is chosen.", "explore"),
        ("15:00", "Return to Clive Avenue", "Allow transit time and rest before the road trip.", "travel"),
        ("16:00", "Airbnb reset", "Prepare the car plan and luggage.", "rest"),
        ("17:00", "Rental-car check", "Confirm pickup, AWD/SUV, tires and roadside cover.", "plan"),
        ("18:00", "Dinner", "Stay close to the Vancouver base.", "food"),
        ("19:00", "Dinner", "Keep the evening unhurried.", "food"),
        ("20:00", "Pack for Kamloops", "Layers, snacks, offline maps and documents.", "plan"),
        ("21:00", "Sleep", "Final first-stay Vancouver night.", "rest"),
        ("22:00", "Sleep", "Overnight recovery.", "rest"),
        ("23:00", "Sleep", "Overnight recovery.", "rest"),
    ]))
    d.append(day("2026-09-26", "Day 4 · Clive Avenue to Kamloops via Sea-to-Sky", "Kamloops", "Clive Avenue, Joyce-Collingwood → Horseshoe Bay → Squamish → Whistler → Pemberton → Kamloops", "Take the scenic Sea-to-Sky and Duffey Lake route from East Vancouver, accepting that this is a long transfer day.", "Kamloops hotel", [
        ("08:00", "Breakfast + check out", "Keep the 08:00 start; collect the rental car afterward.", "travel"),
        ("09:00", "Collect rental car", "Inspect tires, winter-tire policy, insurance and roadside assistance.", "travel"),
        ("10:00", "Drive to Horseshoe Bay", "Begin Highway 99 with a traffic buffer.", "travel"),
        ("11:00", "Howe Sound viewpoint", "Short photo stop.", "stop"),
        ("12:00", "Shannon Falls / Squamish", "Choose a short walk or viewpoint.", "explore"),
        ("13:00", "Lunch in Squamish", "Eat before heading inland.", "food"),
        ("14:00", "Drive to Whistler", "Optional Brandywine Falls if access and time allow.", "travel"),
        ("15:00", "Whistler Village", "Walk, coffee and mountain views; do not turn it into an overnight.", "explore"),
        ("16:00", "Fuel and route check", "Confirm Duffey Lake Road conditions before continuing.", "stop"),
        ("17:00", "Pemberton / Duffey Lake route", "Long scenic transfer; keep food and daylight buffers.", "travel"),
        ("18:00", "Seton / Lillooet direction", "Continue only if road and weather conditions are good.", "travel"),
        ("19:00", "Drive toward Kamloops", "Use the fastest safe continuation and avoid extra detours.", "travel"),
        ("20:00", "Kamloops arrival buffer", "Check in as soon as practical.", "travel"),
        ("21:00", "Dinner", "Simple nearby meal.", "food"),
        ("22:00", "Sleep", "Recover after the long scenic drive.", "rest"),
        ("23:00", "Sleep", "Overnight recovery.", "rest"),
    ]))
    d.append(day("2026-09-27", "Day 5 · Kamloops to Golden", "Golden", "Kamloops → Salmon Arm → Revelstoke → Rogers Pass → Golden", "Use the Trans-Canada eastbound route and arrive in Golden for the first fixed Airbnb stay.", "Golden Airbnb", [
        ("08:00", "Breakfast + check out", "Fuel and check DriveBC before leaving.", "travel"),
        ("09:00", "Depart Kamloops", "Head east on the Trans-Canada Highway.", "travel"),
        ("10:00", "Shuswap / Salmon Arm", "Coffee and a short waterfront reset.", "stop"),
        ("11:00", "Continue toward Revelstoke", "Lake and mountain scenery.", "travel"),
        ("12:00", "Revelstoke lunch / fuel", "Refuel before the pass.", "food"),
        ("13:00", "Revelstoke town option", "Keep the stop short; the priority is Golden check-in.", "explore"),
        ("14:00", "Rogers Pass direction", "Continue through Glacier National Park.", "travel"),
        ("15:00", "Rogers Pass viewpoint", "Short viewpoint or visitor-centre stop if open.", "explore"),
        ("16:00", "Drive to Golden", "Keep the final transfer comfortable.", "travel"),
        ("17:00", "Golden Airbnb check-in", "Settle into the 27–28 September stay.", "travel"),
        ("18:00", "Golden town / river walk", "Easy orientation close to the accommodation.", "walk"),
        ("19:00", "Golden dinner", "Choose a nearby restaurant.", "food"),
        ("20:00", "Plan Yoho and Harvie Heights move", "Check Emerald Lake, Lake Louise access and road conditions.", "plan"),
        ("21:00", "Sleep", "Golden overnight.", "rest"),
        ("22:00", "Sleep", "Overnight recovery.", "rest"),
        ("23:00", "Sleep", "Overnight recovery.", "rest"),
    ]))
    d.append(day("2026-09-28", "Day 6 · Golden to Harvie Heights via Yoho", "Harvie Heights", "Golden → Field → Emerald Lake → Lake Louise → Harvie Heights", "Move east through Yoho and Lake Louise so the next two nights are positioned for Banff and the lakes.", "Harvie Heights Airbnb", [
        ("08:00", "Breakfast + check out", "Leave Golden at the agreed 08:00 start.", "travel"),
        ("09:00", "Yoho / Field", "Coffee and a short scenic stop.", "stop"),
        ("10:00", "Emerald Lake", "Lakeshore walk if access, parking and weather cooperate.", "explore"),
        ("11:00", "Natural Bridge", "Short stop on the way back toward the Trans-Canada.", "explore"),
        ("12:00", "Lunch near Field / Lake Louise", "Refuel before the afternoon move.", "food"),
        ("13:00", "Lake Louise village", "Collect groceries and confirm shuttle instructions.", "stop"),
        ("14:00", "Lake Louise lakeshore option", "Keep this brief because the dedicated lake day is tomorrow.", "explore"),
        ("15:00", "Drive to Harvie Heights", "Use Highway 1 toward Canmore; keep check-in flexible.", "travel"),
        ("16:00", "Harvie Heights Airbnb check-in", "Settle into the 28–30 September stay.", "travel"),
        ("17:00", "Groceries / reset", "Prepare breakfast and shuttle essentials.", "plan"),
        ("18:00", "Dinner", "Canmore or the Airbnb kitchen.", "food"),
        ("19:00", "Lake day preparation", "Confirm Lake Louise / Moraine Lake reservations and transport.", "plan"),
        ("20:00", "Quiet evening", "Protect energy for tomorrow's reservation-led day.", "rest"),
        ("21:00", "Sleep", "Harvie Heights night 1 of 2.", "rest"),
        ("22:00", "Sleep", "Overnight recovery.", "rest"),
        ("23:00", "Sleep", "Overnight recovery.", "rest"),
    ]))
    d.append(day("2026-09-29", "Day 7 · Lake Louise and Moraine Lake", "Harvie Heights", "Harvie Heights → Lake Louise Park and Ride → Lake Louise / Moraine Lake → Harvie Heights", "Use Harvie Heights as the practical base for the reservation-led lake day; do not rely on personal-vehicle access to Moraine Lake Road.", "Harvie Heights Airbnb", [
        ("08:00", "Breakfast", "Start at 08:00 and use the confirmed shuttle plan.", "food"),
        ("09:00", "Drive to Lake Louise Park and Ride", "Allow parking and queue time; follow the reservation instructions.", "travel"),
        ("10:00", "Lake Louise shuttle / access", "Use the confirmed shuttle or licensed operator.", "travel"),
        ("11:00", "Lake Louise lakeshore", "Photos and a modest lakeshore walk.", "explore"),
        ("12:00", "Lake Louise lunch", "Use the booked or practical lunch option.", "food"),
        ("13:00", "Moraine Lake transfer", "Use the reserved connection; Moraine Lake Road is closed to personal vehicles.", "travel"),
        ("14:00", "Moraine Lake", "Rockpile viewpoint and lakeshore.", "explore"),
        ("15:00", "Moraine Lake", "Keep hiking modest and weather-aware.", "explore"),
        ("16:00", "Return shuttle", "Expect waiting time and preserve a return buffer.", "travel"),
        ("17:00", "Return to Harvie Heights", "Unload and reset at the Airbnb.", "travel"),
        ("18:00", "Dinner", "Canmore or home-cooked dinner.", "food"),
        ("19:00", "Pack for Bragg Creek", "One small road bag and groceries for the next Airbnb.", "plan"),
        ("20:00", "Weather / road check", "Check Parks Canada, 511 Alberta and Highway 1 conditions.", "plan"),
        ("21:00", "Sleep", "Final Harvie Heights night.", "rest"),
        ("22:00", "Sleep", "Overnight recovery.", "rest"),
        ("23:00", "Sleep", "Overnight recovery.", "rest"),
    ]))
    d.append(day("2026-09-30", "Day 8 · Harvie Heights to Bragg Creek", "Bragg Creek", "Harvie Heights → Canmore → Kananaskis / Calgary west → Bragg Creek", "Use the move day to transition from the Rockies lake base to the foothills Airbnb without unnecessary backtracking.", "Bragg Creek Airbnb", [
        ("08:00", "Breakfast + check out", "Pack the Harvie Heights Airbnb and leave at 08:00.", "travel"),
        ("09:00", "Canmore / Bow Valley", "Final local coffee or groceries.", "stop"),
        ("10:00", "Banff option", "Choose Banff Avenue or Bow Falls only if energy is good.", "explore"),
        ("11:00", "Banff / Canmore lunch", "Keep the move day relaxed.", "food"),
        ("12:00", "Drive toward Kananaskis", "Use the foothills route toward Bragg Creek.", "travel"),
        ("13:00", "Kananaskis viewpoint option", "Short stop only; avoid turning the transfer into a long hike.", "explore"),
        ("14:00", "Kananaskis / Highway 40", "Weather-sensitive mountain road; check 511 Alberta.", "travel"),
        ("15:00", "Bragg Creek approach", "Stock up before the Airbnb if needed.", "travel"),
        ("16:00", "Bragg Creek Airbnb check-in", "Settle into the 30 September–2 October stay.", "travel"),
        ("17:00", "Property reset", "Unpack and enjoy the foothills setting.", "rest"),
        ("18:00", "Dinner", "Cook at the Airbnb or eat in Bragg Creek.", "food"),
        ("19:00", "Elbow Valley orientation", "Short local walk if daylight and conditions allow.", "walk"),
        ("20:00", "Plan foothills day", "Choose Bragg Creek, Kananaskis or Elbow Falls based on weather.", "plan"),
        ("21:00", "Sleep", "Bragg Creek night 1 of 2.", "rest"),
        ("22:00", "Sleep", "Overnight recovery.", "rest"),
        ("23:00", "Sleep", "Overnight recovery.", "rest"),
    ]))
    d.append(day("2026-10-01", "Day 9 · Bragg Creek and Kananaskis", "Bragg Creek", "Bragg Creek → Elbow Falls / Kananaskis option → Bragg Creek", "Make the Bragg Creek stay feel distinct: a lower-mileage foothills day before the long northbound transfer.", "Bragg Creek Airbnb", [
        ("08:00", "Breakfast", "Slow start at the Airbnb.", "food"),
        ("09:00", "Bragg Creek village", "Coffee, supplies and local orientation.", "explore"),
        ("10:00", "Elbow Falls option", "Short walk if the road and trail are open and safe.", "explore"),
        ("11:00", "Elbow Valley", "Scenic foothills drive; keep wildlife awareness high.", "travel"),
        ("12:00", "Lunch", "Picnic or Bragg Creek restaurant.", "food"),
        ("13:00", "Kananaskis option", "Drive only as far as conditions and daylight justify.", "travel"),
        ("14:00", "Kananaskis viewpoint / walk", "Choose one modest outdoor stop.", "explore"),
        ("15:00", "Return toward Bragg Creek", "Do not add a second major hike.", "travel"),
        ("16:00", "Airbnb reset", "Rest and enjoy the property.", "rest"),
        ("17:00", "Pack for Yellowhead County", "Prepare food, layers and offline maps for the long road day.", "plan"),
        ("18:00", "Dinner", "Home-cooked or local dinner.", "food"),
        ("19:00", "Route check", "Check 511 Alberta, Parks Canada and Icefields Parkway conditions.", "plan"),
        ("20:00", "Early wind-down", "Tomorrow is the longest scenic transfer of the trip.", "rest"),
        ("21:00", "Sleep", "Final Bragg Creek night.", "rest"),
        ("22:00", "Sleep", "Overnight recovery.", "rest"),
        ("23:00", "Sleep", "Overnight recovery.", "rest"),
    ]))
    d.append(day("2026-10-02", "Day 10 · Bragg Creek to Yellowhead County", "Yellowhead County", "Bragg Creek → Banff → Lake Louise → Icefields Parkway → Jasper area → Hinton / Yellowhead County", "This is the critical long transfer. Use the Icefields Parkway as the day's attraction and treat Yellowhead County as the overnight base near Jasper/Hinton.", "Yellowhead County Airbnb", [
        ("08:00", "Breakfast + check out", "Leave Bragg Creek at 08:00 with a full fuel and food check.", "travel"),
        ("09:00", "Drive toward Banff", "Use Highway 1 and keep the mountain-road buffer.", "travel"),
        ("10:00", "Banff / Lake Louise direction", "Do not add a separate Banff attraction today.", "travel"),
        ("11:00", "Lake Louise fuel / coffee", "Short stop before the Parkway.", "stop"),
        ("12:00", "Bow Lake", "First major Icefields Parkway viewpoint.", "explore"),
        ("13:00", "Peyto Lake", "Short viewpoint walk if conditions are safe.", "explore"),
        ("14:00", "Waterfowl Lakes / Mistaya", "Choose one brief stop.", "explore"),
        ("15:00", "Columbia Icefield", "Lunch, fuel and attraction-status check.", "food"),
        ("16:00", "Athabasca Glacier viewpoint", "Only use a pre-booked tour; otherwise keep this to a short viewpoint.", "explore"),
        ("17:00", "Continue toward Jasper / Hinton", "Protect the late-afternoon daylight and avoid extra detours.", "travel"),
        ("18:00", "Jasper-area transfer", "The Yellowhead County Airbnb is the fixed overnight target.", "travel"),
        ("19:00", "Yellowhead County Airbnb check-in", "Settle into the 2–3 October stay.", "travel"),
        ("20:00", "Simple dinner", "Eat at the Airbnb or use the nearest confirmed option.", "food"),
        ("21:00", "Sleep", "Recover before the long Yellowhead-to-Revelstoke crossing.", "rest"),
        ("22:00", "Sleep", "Overnight recovery.", "rest"),
        ("23:00", "Sleep", "Overnight recovery.", "rest"),
    ]))
    d.append(day("2026-10-03", "Day 11 · Yellowhead County to Revelstoke", "Revelstoke", "Yellowhead County / Hinton → Jasper → Icefields Parkway → Lake Louise → Rogers Pass → Revelstoke", "Keep Jasper brief, then make the southbound Parkway and Rogers Pass the scenic route to the Revelstoke Airbnb. This is a very long day, so skip optional stops if timing slips.", "Revelstoke Airbnb", [
        ("08:00", "Breakfast + check out", "Start from the Yellowhead County Airbnb at 08:00.", "travel"),
        ("09:00", "Jasper town / Pyramid Lake option", "Choose one short morning stop only.", "explore"),
        ("10:00", "Depart Jasper", "Begin the southbound Icefields Parkway leg.", "travel"),
        ("11:00", "Athabasca Falls", "Short stop if missed yesterday and conditions are safe.", "explore"),
        ("12:00", "Sunwapta / Columbia area", "Choose one stop and keep moving south.", "travel"),
        ("13:00", "Packed lunch", "Use a designated stop; avoid a restaurant detour.", "food"),
        ("14:00", "Columbia Icefield / Parker Ridge option", "Only if daylight and timing remain comfortable.", "explore"),
        ("15:00", "Peyto or Bow Lake option", "Pick one final major viewpoint, not both.", "explore"),
        ("16:00", "Drive to Lake Louise", "Continue toward the Trans-Canada connection.", "travel"),
        ("17:00", "Lake Louise / Golden direction", "Fuel and check Rogers Pass conditions.", "stop"),
        ("18:00", "Rogers Pass direction", "Keep the final mountain transfer moving.", "travel"),
        ("19:00", "Drive to Revelstoke", "Arrival will be late if stops or conditions add time.", "travel"),
        ("20:00", "Revelstoke Airbnb check-in", "Settle into the 3–4 October stay; skip town sightseeing tonight.", "travel"),
        ("21:00", "Dinner / rest", "Simple meal and no more driving.", "food"),
        ("22:00", "Sleep", "Recover after the longest road day.", "rest"),
        ("23:00", "Sleep", "Overnight recovery.", "rest"),
    ]))
    d.append(day("2026-10-04", "Day 12 · Revelstoke to Kelowna", "Kelowna", "Revelstoke → Sicamous → Vernon / Okanagan → Kelowna", "Use the shorter transfer to reach the Okanagan Airbnb with time for a relaxed Kelowna afternoon.", "Kelowna Airbnb", [
        ("08:00", "Breakfast + check out", "Fuel in Revelstoke before leaving.", "travel"),
        ("09:00", "Mount Revelstoke option", "Only if open and the previous day's arrival was not too late.", "explore"),
        ("10:00", "Depart toward Sicamous", "Follow Highway 1 through the Shuswap.", "travel"),
        ("11:00", "Sicamous / Mara Lake", "Coffee and short lake stop.", "stop"),
        ("12:00", "Armstrong / Vernon direction", "Continue south on the North Okanagan route.", "travel"),
        ("13:00", "Lunch", "Choose a practical stop before Kelowna.", "food"),
        ("14:00", "Kelowna approach", "Allow urban traffic and Airbnb check-in buffer.", "travel"),
        ("15:00", "Kelowna Airbnb check-in", "Settle into the 4–5 October stay.", "travel"),
        ("16:00", "Okanagan lakefront", "Easy waterfront walk or rest.", "walk"),
        ("17:00", "Kelowna reset", "Laundry, groceries and packing for Vancouver.", "plan"),
        ("18:00", "Dinner", "Kelowna restaurant or the Airbnb.", "food"),
        ("19:00", "Lakefront evening", "Keep the night relaxed.", "walk"),
        ("20:00", "Plan Vancouver transfer", "Check Coquihalla / Highway 5 conditions and Vancouver traffic.", "plan"),
        ("21:00", "Sleep", "Kelowna overnight.", "rest"),
        ("22:00", "Sleep", "Overnight recovery.", "rest"),
        ("23:00", "Sleep", "Overnight recovery.", "rest"),
    ]))
    d.append(day("2026-10-05", "Day 13 · Kelowna to Dunbar Street", "Dunbar Street, Dunbar-Southlands", "Kelowna → Merritt → Coquihalla → Vancouver → Dunbar Street", "Return to the final Dunbar Street Airbnb for two nights. Keep the evening close to the neighbourhood after the long transfer.", "Dunbar Street Airbnb · Dunbar-Southlands", [
        ("08:00", "Breakfast + check out", "Leave Kelowna at 08:00 after checking Highway 5 conditions.", "travel"),
        ("09:00", "Drive toward Merritt", "Take Highway 97C / 5 as conditions allow.", "travel"),
        ("10:00", "Okanagan Connector", "Keep a fuel and weather buffer.", "travel"),
        ("11:00", "Merritt / fuel", "Coffee, fuel and road check.", "stop"),
        ("12:00", "Coquihalla direction", "Mountain highway transfer.", "travel"),
        ("13:00", "Lunch stop", "Use a practical highway stop.", "food"),
        ("14:00", "Continue toward Vancouver", "Traffic buffer grows near the Lower Mainland.", "travel"),
        ("15:00", "Fraser Valley", "Do not add detours today.", "travel"),
        ("16:00", "Vancouver arrival", "Head to the final Dunbar Street Airbnb in Vancouver's west side.", "travel"),
        ("17:00", "Dunbar Street Airbnb check-in", "Settle into the final two-night stay.", "travel"),
        ("18:00", "Dinner near Dunbar / Kerrisdale", "Keep the evening close after the transfer.", "food"),
        ("19:00", "Rest", "No major sightseeing obligation.", "rest"),
        ("20:00", "Flight and outlet plan", "Confirm CX867, baggage and whether McArthurGlen fits tomorrow without risk.", "plan"),
        ("21:00", "Sleep", "Final Vancouver stay night 1 of 2.", "rest"),
        ("22:00", "Sleep", "Overnight recovery.", "rest"),
        ("23:00", "Sleep", "Overnight recovery.", "rest"),
    ]))
    d.append(day("2026-10-06", "Day 14 · Dunbar, UBC and Vancouver final day", "Dunbar Street, Dunbar-Southlands", "Dunbar Street → Pacific Spirit Park / UBC → Kitsilano or Granville Island → Dunbar Street", "Use the final full day for the west-side places that are genuinely near the Airbnb, with McArthurGlen kept as an optional logistics stop rather than the main plan.", "Dunbar Street Airbnb · Dunbar-Southlands", [
        ("08:00", "Breakfast", "Normal 08:00 start in Vancouver.", "food"),
        ("09:00", "Dunbar / Kerrisdale breakfast", "Start close to the Airbnb with a café or groceries.", "food"),
        ("10:00", "Pacific Spirit Regional Park", "Easy forest walk; choose a short loop and check trail conditions.", "walk"),
        ("11:00", "UBC campus", "Walk the campus and grounds near the Museum of Anthropology.", "explore"),
        ("12:00", "Museum of Anthropology option", "Paid indoor option; check current hours and admission before going.", "explore"),
        ("13:00", "Lunch at UBC / West Point Grey", "Keep lunch near the west side.", "food"),
        ("14:00", "Kitsilano Beach / Jericho Beach", "Easy shoreline and mountain-view walk.", "walk"),
        ("15:00", "Granville Island option", "Choose Granville Island only if you want one final market outing.", "explore"),
        ("16:00", "Return to Dunbar", "Pack and rest before the airport day.", "travel"),
        ("17:00", "Luggage sort", "Confirm passports, receipts and airport transfer.", "plan"),
        ("18:00", "Final Vancouver dinner", "Choose Dunbar, Kerrisdale or Kitsilano rather than crossing the city.", "food"),
        ("19:00", "Dinner", "Keep the final evening calm.", "food"),
        ("20:00", "Pack for CX867", "Prepare a carry-on and confirm terminal timing.", "plan"),
        ("21:00", "Sleep", "Final Vancouver night.", "rest"),
        ("22:00", "Sleep", "Overnight recovery.", "rest"),
        ("23:00", "Sleep", "Departure tomorrow.", "rest"),
    ]))
    d.append(day("2026-10-07", "Day 15 · Dunbar Street to Vancouver departure", "YVR", "Dunbar Street, Dunbar-Southlands → YVR · CX867 14:10 → HKG 19:20 on 8 Oct", "Keep the departure day calm. The 14:10 international flight gets a real airport buffer; no attraction is scheduled after check-in.", "CX867 in flight", [
        ("08:00", "Breakfast", "Hotel breakfast and final flight check.", "food"),
        ("09:00", "Pack and check out", "Confirm luggage, receipts and storage.", "travel"),
        ("10:00", "Transfer to YVR", "Return the rental car if needed or use the confirmed airport transfer.", "travel"),
        ("11:00", "CX867 check-in and bags", "Be at the airport with a proper international-departure buffer.", "travel"),
        ("12:00", "Security and immigration", "Complete airport formalities.", "travel"),
        ("13:00", "Gate buffer", "Water, final purchases and boarding buffer.", "travel"),
        ("14:00", "CX867 departure buffer", "Scheduled departure is 14:10 local Vancouver time.", "travel"),
        ("15:00", "CX867 in flight", "Return flight to Hong Kong.", "travel"),
        ("16:00", "CX867 in flight", "Return flight to Hong Kong.", "travel"),
        ("17:00", "CX867 in flight", "Return flight to Hong Kong.", "travel"),
        ("18:00", "CX867 in flight", "Return flight to Hong Kong.", "travel"),
        ("19:00", "CX867 in flight", "Scheduled arrival is 19:20 on 8 Oct Hong Kong time.", "travel"),
        ("20:00", "Arrival recovery", "Hong Kong arrival is the next calendar day.", "rest"),
        ("21:00", "Arrival recovery", "Trip complete.", "rest"),
        ("22:00", "Arrival recovery", "Trip complete.", "rest"),
        ("23:00", "Arrival recovery", "Trip complete.", "rest"),
    ]))
    return d


x = json.loads(DATA.read_text(encoding="utf-8"))
x["meta"].update({
    "title": "Canada Rockies · fixed Airbnb route + Vancouver neighbourhood bases",
    "wake_time": "08:00",
    "lodging_note": "Fixed stays supplied by the travelers: Clive Avenue, Collingwood / Joyce-Collingwood, Vancouver from 23–26 Sep; Golden 27–28 Sep; Harvie Heights 28–30 Sep; Bragg Creek 30 Sep–2 Oct; Yellowhead County 2–3 Oct; Revelstoke 3–4 Oct; Kelowna 4–5 Oct; Dunbar Street, Dunbar-Southlands, Vancouver from 5–7 Oct.",
    "assumption": "Route rebuilt around the supplied Airbnb bases and exact Vancouver neighbourhoods. The one-night Kamloops stop on 26 Sep bridges the first Vancouver stay and Golden. Yellowhead County is treated as a Jasper/Hinton-area base; its exact Airbnb address may change the 2–3 Oct driving times. Clive Avenue is treated as the Joyce-Collingwood / East Vancouver area and Dunbar Street as Dunbar-Southlands; exact addresses are still needed for door-to-door routing.",
})
x["route"] = [
    {"name": "Vancouver · Clive Avenue", "date": "23–26 Sep", "km": "East Vancouver", "stay": "first 3 nights", "color": "#7dd3fc"},
    {"name": "Kamloops", "date": "26–27 Sep", "km": "scenic road bridge", "stay": "one-night hotel", "color": "#fde68a"},
    {"name": "Golden", "date": "27–28 Sep", "km": "mountain stopover", "stay": "your Airbnb", "color": "#fca5a5"},
    {"name": "Harvie Heights", "date": "28–30 Sep", "km": "Bow Valley base", "stay": "your Airbnb", "color": "#86efac"},
    {"name": "Bragg Creek", "date": "30 Sep–2 Oct", "km": "foothills base", "stay": "your Airbnb", "color": "#f0abfc"},
    {"name": "Yellowhead County", "date": "2–3 Oct", "km": "Jasper / Hinton area", "stay": "your Airbnb", "color": "#93c5fd"},
    {"name": "Revelstoke", "date": "3–4 Oct", "km": "Trans-Canada west", "stay": "your Airbnb", "color": "#fdba74"},
    {"name": "Kelowna", "date": "4–5 Oct", "km": "Okanagan stop", "stay": "your Airbnb", "color": "#c4b5fd"},
    {"name": "Vancouver · Dunbar Street", "date": "5–7 Oct", "km": "Dunbar-Southlands", "stay": "final 2 nights", "color": "#f0abfc"},
    {"name": "Departure", "date": "7 Oct", "km": "airport day", "stay": "CX867", "color": "#f9a8d4"},
]
x["route_legs"] = [
    {"from": "Vancouver", "to": "Kamloops", "distance": "≈450 km", "distance_km": 450, "time": "≈6 h + stops", "baseline_hours": 6.0, "planned_hours": "7–9", "estimated_liters": "41–45", "estimated_gas_cad": "84–92", "note": "Most scenic option via Sea-to-Sky, Whistler, Pemberton and Duffey Lake; weather-sensitive."},
    {"from": "Kamloops", "to": "Golden", "distance": "≈360 km", "distance_km": 360, "time": "≈4 h + stops", "baseline_hours": 4.1, "planned_hours": "5–6", "estimated_liters": "32–36", "estimated_gas_cad": "58–74", "note": "Trans-Canada through Salmon Arm, Revelstoke and Rogers Pass."},
    {"from": "Golden", "to": "Harvie Heights", "distance": "≈162 km", "distance_km": 162, "time": "≈2 h + stops", "baseline_hours": 2.0, "planned_hours": "4–6", "estimated_liters": "15–16", "estimated_gas_cad": "23–33", "note": "Use Yoho, Emerald Lake and Lake Louise as the scenic sequence; the direct drive is about 162 km."},
    {"from": "Harvie Heights", "to": "Bragg Creek", "distance": "≈125 km", "distance_km": 125, "time": "≈1.5–2 h + stops", "baseline_hours": 1.75, "planned_hours": "3–5", "estimated_liters": "11–13", "estimated_gas_cad": "17–20", "note": "Bow Valley to the foothills; use Banff or Kananaskis as one optional stop."},
    {"from": "Bragg Creek", "to": "Yellowhead County", "distance": "≈500 km", "distance_km": 500, "time": "≈7–8 h + stops", "baseline_hours": 6.1, "planned_hours": "8–10", "estimated_liters": "45–50", "estimated_gas_cad": "70–78", "note": "Banff, Lake Louise and the Icefields Parkway; a full scenic transfer day."},
    {"from": "Yellowhead County", "to": "Revelstoke", "distance": "≈529 km", "distance_km": 529, "time": "≈7 h non-stop / 9–10 h scenic", "baseline_hours": 6.8, "planned_hours": "9–11", "estimated_liters": "48–53", "estimated_gas_cad": "74–109", "note": "Jasper, Icefields Parkway southbound and Rogers Pass; skip optional stops if timing slips."},
    {"from": "Revelstoke", "to": "Kelowna", "distance": "≈200 km", "distance_km": 200, "time": "≈2.5–3 h", "baseline_hours": 2.75, "planned_hours": "3–4", "estimated_liters": "18–20", "estimated_gas_cad": "37–41", "note": "Shuswap and North Okanagan route via Sicamous and Vernon."},
    {"from": "Kelowna", "to": "Vancouver", "distance": "≈390 km", "distance_km": 390, "time": "≈4.5–5 h + traffic", "baseline_hours": 4.75, "planned_hours": "5–7", "estimated_liters": "35–39", "estimated_gas_cad": "72–80", "note": "Highway 97C / Coquihalla; check mountain conditions and Lower Mainland traffic."},
]
x["driving_summary"] = {
    "intercity_km": 2716,
    "local_sightseeing_allowance_km": 450,
    "total_planned_km": 3166,
    "baseline_driving_hours": 34.2,
    "planned_driving_hours_without_long_stops": "40–48",
    "fuel_liters_at_9_l_per_100km": 285,
    "fuel_liters_at_10_l_per_100km": 317,
    "fuel_estimate_cad": "529–647",
    "method": "Route-leg estimates plus a 450 km local/sightseeing allowance. Fuel uses 9–10 L/100 km, BC CAD 2.05/L and Alberta CAD 1.55/L planning prices; prices and conditions can change."
}
x["days"] = build_days()
x["vehicle_recommendation"] = {
    "recommendation": "Toyota RAV4 Hybrid AWD",
    "rental_class": "Toyota RAV4 Hybrid AWD or equivalent",
    "verdict": "Best overall fit for this two-person, 15-day Rockies route: durable and practical, easier to handle than a three-row SUV, and much more economical than the large SUVs.",
    "why": [
        "AWD traction and compact-SUV dimensions suit mountain highways, Airbnb parking and Vancouver city driving.",
        "Enough cargo flexibility for two travelers without paying the fuel and bulk penalty of a Highlander, CX-90, Palisade or full-size SUV.",
        "Toyota's RAV4 has a strong recent reliability record; the recent model is recommended by Consumer Reports.",
        "The hybrid AWD version is the fuel-economy choice. Official Canadian figures for the 2026 RAV4 range from about 5.5 to 6.2 L/100 km combined by grade.",
        "The Mazda CX-90 is an excellent, safer-feeling handling alternative, but it is larger, more complex and less economical for this trip."
    ],
    "ranked_alternatives": [
        {"rank": 1, "model": "Toyota Highlander Hybrid AWD", "best_for": "More luggage and maximum highway comfort", "tradeoff": "Bigger, harder to park and thirstier than the RAV4."},
        {"rank": 2, "model": "Mazda CX-90 AWD", "best_for": "Handling, power and premium cabin", "tradeoff": "Larger, more expensive to fuel, and a newer/more complex powertrain."},
        {"rank": 3, "model": "Toyota RAV4 gasoline AWD", "best_for": "Fallback if the hybrid is unavailable", "tradeoff": "Still practical, but higher fuel use."},
        {"rank": 4, "model": "Ford Escape Hybrid AWD", "best_for": "Acceptable alternative", "tradeoff": "Choose only if the rental condition, tires and roadside coverage are clearly better."}
    ],
    "avoid_for_this_trip": [
        "Toyota Corolla, Toyota Camry, Nissan Kicks, Volkswagen Taos and Audi Q3: less cargo/reserve and less suitable as the preferred choice for remote mountain legs.",
        "Ford Expedition, Infiniti QX80, Volvo XC90, Hyundai Palisade and full-size SUVs: unnecessary size and fuel cost for two people.",
        "Jeep Wrangler: capable off pavement, but noisier, less comfortable and less fuel-efficient for your long highway days.",
        "Jeep Grand Cherokee, Ford Edge and similar larger gasoline SUVs: workable, but not as balanced as the RAV4 Hybrid AWD."
    ],
    "fuel_comparison_for_3166km": [
        {"model": "RAV4 Hybrid AWD", "consumption": "≈5.5–6.2 L/100 km", "liters": "≈174–196 L", "fuel_cost_cad": "≈320–390"},
        {"model": "Highlander Hybrid AWD", "consumption": "≈6.7 L/100 km", "liters": "≈212 L", "fuel_cost_cad": "≈390–425"},
        {"model": "RAV4 gasoline AWD", "consumption": "≈8.0 L/100 km", "liters": "≈253 L", "fuel_cost_cad": "≈470–510"},
        {"model": "CX-90 Turbo AWD", "consumption": "≈9.8 L/100 km planning", "liters": "≈310 L", "fuel_cost_cad": "≈570–620"},
        {"model": "Wrangler / large gasoline SUV", "consumption": "≈11.0 L/100 km planning", "liters": "≈348 L", "fuel_cost_cad": "≈640–700"}
    ],
    "must_confirm_at_pickup": [
        "3PMSF mountain/snowflake-rated tires, not just the words AWD or M+S",
        "Tire tread, spare tire or proper puncture kit, and roadside-assistance number",
        "No dashboard warning lights; inspect brakes, wipers, windshield and lights",
        "Snow/road mode operation, luggage cover, and rental restrictions on mountain roads",
        "Exact model is subject to rental-fleet availability; reserve the vehicle class, not only the badge."
    ],
    "important_tire_note": "For the Sea-to-Sky, Coquihalla, Icefields Parkway and interior BC, tire specification matters more than AWD branding. BC advises out-of-province visitors to ensure rental vehicles have winter tires; 3PMSF tires provide better winter traction than basic M+S tires.",
    "source_ids": [22, 23, 24, 25, 26, 27]
}

x["budget"] = {
    "currency": "CAD",
    "scope": "Estimated for 2 travelers; international flights are excluded because their fares are not in the itinerary data. Airbnb prices were not supplied, so each lodging line is a planning range, not a booking quote.",
    "assumptions": {
        "total_driving_km": 3166,
        "intercity_driving_km": 2716,
        "local_and_sightseeing_allowance_km": 450,
        "vehicle_consumption_l_per_100km": "9–10",
        "fuel_price_bc_cad_per_l": 2.05,
        "fuel_price_ab_cad_per_l": 1.55,
        "rental_days": 11,
        "rental_vehicle": "SUV / equivalent",
        "rental_daily_average_cad": 123,
        "rental_tax_and_fees_factor": 1.15,
        "food_per_person_per_day_cad": "60–110",
        "airbnb_nights": 8,
        "vancouver_nights": 5,
        "kamloops_nights": 1
    },
    "categories": [
        {"name": "Clive Avenue Airbnb · Collingwood", "low": 450, "high": 780, "note": "3 nights, 23–26 September; planning range CAD 150–260/night before Airbnb taxes and fees."},
        {"name": "Dunbar Street Airbnb · Dunbar-Southlands", "low": 400, "high": 700, "note": "2 nights, 5–7 October; planning range CAD 200–350/night before Airbnb taxes and fees."},
        {"name": "Golden Airbnb", "low": 180, "high": 300, "note": "1 night, 27–28 September; planning range CAD 180–300/night before Airbnb taxes and fees."},
        {"name": "Harvie Heights Airbnb", "low": 440, "high": 760, "note": "2 nights, 28–30 September; planning range CAD 220–380/night before Airbnb taxes and fees."},
        {"name": "Bragg Creek Airbnb", "low": 440, "high": 800, "note": "2 nights, 30 September–2 October; planning range CAD 220–400/night before Airbnb taxes and fees."},
        {"name": "Yellowhead County Airbnb", "low": 160, "high": 300, "note": "1 night, 2–3 October; planning range CAD 160–300/night before Airbnb taxes and fees; exact address may change the route."},
        {"name": "Revelstoke Airbnb", "low": 200, "high": 350, "note": "1 night, 3–4 October; planning range CAD 200–350/night before Airbnb taxes and fees."},
        {"name": "Kelowna Airbnb", "low": 180, "high": 320, "note": "1 night, 4–5 October; planning range CAD 180–320/night before Airbnb taxes and fees."},
        {"name": "Kamloops bridge night", "low": 180, "high": 250, "note": "1 night, 26–27 September; practical hotel/suite placeholder."},
        {"name": "Rental car", "low": 1556, "high": 1556, "note": "11 days × CAD 123/day SUV average × 1.15 tax/fee factor; actual quote may differ."},
        {"name": "Gas", "low": 529, "high": 647, "note": "About 285–317 L for 3,166 km, using BC CAD 2.05/L and Alberta CAD 1.55/L planning prices."},
        {"name": "Food and groceries", "low": 1800, "high": 3300, "note": "CAD 60–110 per person per day for 15 days; kitchens make the lower end more realistic."},
        {"name": "Parks, attractions, parking and local transport", "low": 600, "high": 1200, "note": "Includes a planning allowance for park access, shuttles, parking and selected paid attractions; verify reservations and fees."}
    ],
    "totals": {"low": 7115, "high": 11263, "recommended_reserve_low": 7827, "recommended_reserve_high": 12389},
    "note": "The 10% reserve is for fuel-price movement, parking, taxes/cleaning fees, weather detours and small unplanned costs. Add the actual Airbnb totals and international-flight fares for a final booked-trip total."
}
x["airbnb_stays"] = [
    {"base": "Golden", "dates": "27–28 September", "note": "User-supplied fixed Airbnb."},
    {"base": "Harvie Heights", "dates": "28–30 September", "note": "User-supplied fixed Airbnb; best positioned for Banff, Lake Louise and Moraine Lake access."},
    {"base": "Bragg Creek", "dates": "30 September–2 October", "note": "User-supplied fixed Airbnb; foothills / Kananaskis base."},
    {"base": "Yellowhead County", "dates": "2–3 October", "note": "User-supplied fixed Airbnb; treated as the Jasper / Hinton-area base for routing."},
    {"base": "Revelstoke", "dates": "3–4 October", "note": "User-supplied fixed Airbnb."},
    {"base": "Kelowna", "dates": "4–5 October", "note": "User-supplied fixed Airbnb."},
]

x["sources"] = [s for s in x.get("sources", []) if s.get("id") not in {19, 20, 21, 22, 23, 24, 25, 26, 27}] + [
    {"id": 19, "label": "Fuel-price planning reference · CAA / NRCan context", "url": "https://natural-resources.canada.ca/energy-facts/energy-facts/transportation-energy-use/gasoline-prices"},
    {"id": 20, "label": "Rental-car planning reference", "url": "https://ca.kayak.com/Cheap-Vancouver-Car-Rentals.6668.cars.ksp"},
    {"id": 21, "label": "Canada travel-cost planning reference", "url": "https://www.budgetyourtrip.com/canada"},
    {"id": 22, "label": "Toyota Canada · 2026 RAV4 features", "url": "https://www.toyota.ca/en/vehicles/rav4/features-benefits/"},
    {"id": 23, "label": "Toyota Canada · 2026 RAV4 fuel economy and AWD", "url": "https://media.toyota.ca/en/releases/2026/the-canadian-built-rav4-is-all-new-for-2026--and-offered-at-sugg.html"},
    {"id": 24, "label": "IIHS · 2026 Top Safety Picks", "url": "https://www.iihs.org/ratings/top-safety-picks"},
    {"id": 25, "label": "British Columbia · winter tires for visitors and rentals", "url": "https://www2.gov.bc.ca/gov/content/transportation/driving-and-cycling/traveller-information/seasonal/winter-driving/visitors"},
    {"id": 26, "label": "Consumer Reports · Toyota RAV4 reliability", "url": "https://www.consumerreports.org/cars/toyota/rav4/2025/reliability/"},
    {"id": 27, "label": "Toyota Canada · 2026 Highlander specifications", "url": "https://www.toyota.ca/en/vehicles/highlander/models-specifications"},
]

# Keep the supplementary candidate directory, but add the fixed-base labels so
# the site's stay selector reflects the actual plan rather than the old bases.
for key, label, why in [
    ("vancouver", "Clive Avenue Airbnb · Collingwood", "Fixed first stay, 23–26 September. Joyce-Collingwood base near Joyce Station, Central Park and Metrotown."),
    ("clive-avenue", "Clive Avenue Airbnb · Collingwood", "Fixed first stay, 23–26 September. Exact address should be used for door-to-door directions."),
    ("dunbar-street", "Dunbar Street Airbnb · Dunbar-Southlands", "Fixed final stay, 5–7 October. West-side base near UBC, Pacific Spirit Park and Kitsilano."),
    ("golden", "Your Airbnb · Golden", "Fixed stay supplied by the travelers for 27–28 September."),
    ("harvie-heights", "Your Airbnb · Harvie Heights", "Fixed stay supplied by the travelers for 28–30 September; practical Bow Valley base."),
    ("bragg-creek", "Your Airbnb · Bragg Creek", "Fixed stay supplied by the travelers for 30 September–2 October; foothills base."),
    ("yellowhead-county", "Your Airbnb · Yellowhead County", "Fixed stay supplied by the travelers for 2–3 October; use the exact address for final routing."),
    ("revelstoke", "Your Airbnb · Revelstoke", "Fixed stay supplied by the travelers for 3–4 October."),
    ("kelowna", "Your Airbnb · Kelowna", "Fixed stay supplied by the travelers for 4–5 October."),
]:
    x["hotels"][key] = [{"name": label, "type": "fixed Airbnb stay", "why": why}]

DATA.write_text(json.dumps(x, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"updated {DATA}")
print(f"days {len(x['days'])} blocks {sum(len(d['blocks']) for d in x['days'])}")
print(f"wake_time {x['meta']['wake_time']}")
print("bases", " → ".join(r["name"] for r in x["route"]))
