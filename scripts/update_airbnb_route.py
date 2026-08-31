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
    {"name": "Golden", "date": "27–28 Sep", "km": "mountain stopover", "stay": "supplied booking", "color": "#fca5a5"},
    {"name": "Harvie Heights", "date": "28–30 Sep", "km": "Bow Valley base", "stay": "supplied booking", "color": "#86efac"},
    {"name": "Bragg Creek", "date": "30 Sep–2 Oct", "km": "foothills base", "stay": "supplied booking", "color": "#f0abfc"},
    {"name": "Yellowhead County", "date": "2–3 Oct", "km": "Jasper / Hinton area", "stay": "supplied booking", "color": "#93c5fd"},
    {"name": "Revelstoke", "date": "3–4 Oct", "km": "Trans-Canada west", "stay": "supplied booking", "color": "#fdba74"},
    {"name": "Kelowna", "date": "4–5 Oct", "km": "Okanagan stop", "stay": "supplied booking", "color": "#c4b5fd"},
    {"name": "Vancouver · Dunbar Street", "date": "5–7 Oct", "km": "Dunbar-Southlands", "stay": "final 2 nights", "color": "#f0abfc"},
    {"name": "Departure", "date": "7 Oct", "km": "airport day", "stay": "CX867", "color": "#f9a8d4"},
]
x["route_legs"] = [
    {"from": "Clive Avenue / Collingwood", "to": "Kamloops", "distance": "≈450 km", "distance_km": 450, "time": "≈6 h + stops", "baseline_hours": 6.0, "planned_hours": "7–9", "estimated_liters": "41–45", "estimated_gas_cad": "84–92", "note": "From 3264 Vanness Avenue via Sea-to-Sky, Whistler, Pemberton and Duffey Lake; weather-sensitive."},
    {"from": "Kamloops", "to": "Golden", "distance": "≈360 km", "distance_km": 360, "time": "≈4 h + stops", "baseline_hours": 4.1, "planned_hours": "5–6", "estimated_liters": "32–36", "estimated_gas_cad": "58–74", "note": "Trans-Canada through Salmon Arm, Revelstoke and Rogers Pass."},
    {"from": "Golden", "to": "Harvie Heights", "distance": "≈162 km", "distance_km": 162, "time": "≈2 h + stops", "baseline_hours": 2.0, "planned_hours": "4–6", "estimated_liters": "15–16", "estimated_gas_cad": "23–33", "note": "818 12 Street South to 750 Harvie Heights Road via Yoho, Emerald Lake and Lake Louise."},
    {"from": "Harvie Heights", "to": "Bragg Creek", "distance": "≈125 km", "distance_km": 125, "time": "≈1.5–2 h + stops", "baseline_hours": 1.75, "planned_hours": "3–5", "estimated_liters": "11–13", "estimated_gas_cad": "17–20", "note": "750 Harvie Heights Road to 50023 Boyce Ranch Road; Bow Valley to the foothills."},
    {"from": "Bragg Creek", "to": "Yellowhead County", "distance": "≈500 km", "distance_km": 500, "time": "≈7–8 h + stops", "baseline_hours": 6.1, "planned_hours": "8–10", "estimated_liters": "45–50", "estimated_gas_cad": "70–78", "note": "50023 Boyce Ranch Road via Banff, Lake Louise and the Icefields Parkway to 50410 Yellowhead Highway."},
    {"from": "Yellowhead County", "to": "Revelstoke", "distance": "≈529 km", "distance_km": 529, "time": "≈7 h non-stop / 9–10 h scenic", "baseline_hours": 6.8, "planned_hours": "9–11", "estimated_liters": "48–53", "estimated_gas_cad": "74–109", "note": "50410 Yellowhead Highway via Jasper, Icefields Parkway southbound, Lake Louise and Rogers Pass."},
    {"from": "Revelstoke", "to": "Kelowna", "distance": "≈200 km", "distance_km": 200, "time": "≈2.5–3 h", "baseline_hours": 2.75, "planned_hours": "3–4", "estimated_liters": "18–20", "estimated_gas_cad": "37–41", "note": "1500 1 Street West via Sicamous, Armstrong and Vernon to 104 Clifton Road North."},
    {"from": "Kelowna", "to": "Dunbar Street / Vancouver", "distance": "≈390 km", "distance_km": 390, "time": "≈4.5–5 h + traffic", "baseline_hours": 4.75, "planned_hours": "5–7", "estimated_liters": "35–39", "estimated_gas_cad": "72–80", "note": "104 Clifton Road North via Highway 97C / Coquihalla to 3540 West 37th Avenue; check mountain conditions and Lower Mainland traffic."},
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
    "recommendation": "Toyota RAV4 FWD",
    "rental_class": "Toyota RAV4 FWD or equivalent",
    "verdict": "The booked RAV4 FWD is a sensible, economical choice for two people, but it is not as capable as AWD on snow or steep unplowed access roads. For this route, tire quality and conservative driving are essential.",
    "why": [
        "The booked FWD RAV4 is practical for two travelers and economical, but it does not provide AWD traction on snow or steep unplowed access roads.",
        "Its compact-SUV dimensions suit mountain highways, Airbnb parking and Vancouver city driving.",
        "Toyota's RAV4 has a strong recent reliability record; the recent model is recommended by Consumer Reports.",
        "The exact fuel type was not supplied, so the site uses the conservative gasoline FWD planning estimate of about 8.0 L/100 km.",
        "The Mazda CX-90 is an excellent handling alternative, but it is larger, more complex and less economical for this trip."
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
        {"model": "RAV4 FWD (booked)", "consumption": "≈8.0 L/100 km planning", "liters": "≈253 L", "fuel_cost_cad": "≈420–560"},
        {"model": "RAV4 Hybrid AWD (if upgraded)", "consumption": "≈5.5–6.2 L/100 km", "liters": "≈174–196 L", "fuel_cost_cad": "≈320–390"},
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

# Replace generic neighborhood labels with the supplied booking addresses and times.
x["lodging_details"] = [
    {"number": 1, "base": "Clive Avenue / Collingwood", "address": "3264 Vanness Avenue, Vancouver, BC V5R 4V3", "check_in": "2026-09-23 16:00", "check_out": "2026-09-26 10:00", "price_hkd": 6056, "price_cad": 1070.69, "note": "Joyce-Collingwood / East Vancouver. The booking address is Vanness Avenue rather than Clive Avenue."},
    {"number": 2, "base": "Golden", "address": "818 12 Street South, Golden, BC", "check_in": "2026-09-27 16:00", "check_out": "2026-09-28 11:00", "price_hkd": 1816, "price_cad": 321.07, "note": "Rutherford House / heritage area in Golden."},
    {"number": 3, "base": "Harvie Heights", "address": "750 Harvie Heights Road, Harvie Heights, AB T1W 2W2", "check_in": "2026-09-28 17:00", "check_out": "2026-09-30 11:00", "price_hkd": 4994, "price_cad": 882.93, "note": "Bow Valley base between Canmore and Banff."},
    {"number": 4, "base": "Bragg Creek", "address": "50023 Boyce Ranch Road, Bragg Creek / Rocky View County, AB", "check_in": "2026-09-30 16:00", "check_out": "2026-10-02 11:00", "price_hkd": 3634, "price_cad": 642.49, "note": "Rural foothills Airbnb; allow extra time for the final approach and verify the host's directions."},
    {"number": 5, "base": "Yellowhead County / Hinton", "address": "50410 Yellowhead Highway, Yellowhead County / Hinton, AB", "check_in": "2026-10-02 16:00", "check_out": "2026-10-03 10:00", "price_hkd": 2230, "price_cad": 394.26, "note": "Jasper Gateway Glamping area near Highway 16; exact property directions matter."},
    {"number": 6, "base": "Revelstoke", "address": "1500 1 Street West, Revelstoke, BC V0E 2S0", "check_in": "2026-10-03 12:00", "check_out": "2026-10-04 12:00", "price_hkd": 1150, "price_cad": 203.32, "note": "Central Revelstoke address; check whether this booking is an Airbnb or an accommodation property and follow its parking instructions."},
    {"number": 7, "base": "Kelowna / Glenmore", "address": "104 Clifton Road North, Kelowna, BC V1V 2C2", "check_in": "2026-10-04 15:00", "check_out": "2026-10-05 11:00", "price_hkd": 1694, "price_cad": 299.50, "note": "Glenmore–Clifton area, north of downtown Kelowna."},
    {"number": 8, "base": "Dunbar-Southlands", "address": "3540 West 37th Avenue, Vancouver, BC V6N 2V8", "check_in": "2026-10-05 15:00", "check_out": "2026-10-07 11:00", "price_hkd": 4445, "price_cad": 785.87, "note": "Final Vancouver base near UBC, Pacific Spirit Park and west-side beaches."},
]
x["meta"]["lodging_currency"] = "HKD"
x["meta"]["exchange_rate_hkd_to_cad"] = 0.176799
x["meta"]["rental_car"] = {"model": "Toyota RAV4", "drivetrain": "FWD / without 4-wheel drive", "mileage": "Unlimited", "days": 14, "price_hkd": 3507, "price_cad": 620.03, "note": "User-supplied rental price; exact trim, fuel type and tire specification must be confirmed with the rental company."}

# Make every calendar date display the actual booked address for that night's stay.
from datetime import date
for item in x["lodging_details"]:
    start = date.fromisoformat(item["check_in"][:10])
    end = date.fromisoformat(item["check_out"][:10])
    for day_item in x["days"]:
        day_date = date.fromisoformat(day_item["date"])
        if start <= day_date < end:
            day_item["overnight"] = f"{item['base']} · {item['address']}"
            day_item["base"] = item["base"]

# Departure day is not an accommodation night.
x["days"][12]["base"] = "Dunbar-Southlands"
x["days"][12]["overnight"] = "Dunbar Street Airbnb · 3540 West 37th Avenue, Vancouver, BC V6N 2V8"
x["days"][13]["base"] = "Dunbar-Southlands"
x["days"][13]["overnight"] = "Dunbar Street Airbnb · 3540 West 37th Avenue, Vancouver, BC V6N 2V8"
x["days"][14]["base"] = "YVR"

x["weather"] = {
    "summary": "Late September to early October crosses several microclimates: mild/wet Vancouver, cooler Golden and the Rockies, potentially frosty or snowy high elevations, then a relatively mild but cool Kelowna and Vancouver finish. These are planning ranges, not a forecast.",
    "locations": [
        {"place": "Vancouver · Collingwood / Dunbar", "dates": "23–26 Sep and 5–7 Oct", "typical": "September average high about 19°C / low 11°C; October average high about 14°C / low 9°C", "pack": "Rain shell, light layers and comfortable waterproof shoes; umbrella is optional but useful."},
        {"place": "Golden", "dates": "27–28 Sep", "typical": "September averages around 13–18°C daytime and 2–5°C overnight; October cools quickly and can approach freezing at night", "pack": "Warm mid-layer, insulated jacket, gloves and hat for mornings/evenings."},
        {"place": "Harvie Heights / Banff / Lake Louise", "dates": "28–30 Sep", "typical": "Banff September average high/low about 16.1°C / 2.7°C; October about 10.1°C / −1.1°C. Early snow and frost are possible.", "pack": "Insulating layer, waterproof shell, traction-capable footwear and optional microspikes."},
        {"place": "Bragg Creek / Kananaskis", "dates": "30 Sep–2 Oct", "typical": "Foothills weather can shift quickly; mornings may be frosty while sunny afternoons are comfortable.", "pack": "Layering system, rain/wind shell, gloves, warm hat and extra dry socks."},
        {"place": "Yellowhead County / Jasper–Hinton area", "dates": "2–3 Oct", "typical": "Jasper-area September/October brings fall colours and cooler temperatures; mountain roads can be colder than Hinton or valley forecasts.", "pack": "Warm layer, gloves, hat, headlamp and vehicle emergency clothing; plan for limited cell service on the Parkway."},
        {"place": "Revelstoke", "dates": "3–4 Oct", "typical": "September is cooler and wetter; snow is usually more likely on Mount Revelstoke's summit, and weather varies sharply by elevation.", "pack": "Waterproof shell, warm layer, waterproof footwear and dry spare socks."},
        {"place": "Kelowna", "dates": "4–5 Oct", "typical": "October averages around 12°C daytime and 4°C overnight, with rain possible.", "pack": "Light insulated layer, rain shell, walking shoes and sun protection."},
    ],
    "daily_check": ["Environment Canada forecast and alerts", "DriveBC / 511 Alberta road conditions", "Parks Canada trail and facility advisories", "AQHI and wildfire notices", "Sunrise/sunset and daylight remaining before every mountain transfer"],
    "driving_rule": "The Toyota RAV4 is FWD, not AWD. Do not continue onto a snowy or icy mountain route simply because the schedule says so; wait, reroute or use a safer transport option if conditions exceed your experience."
}
x["packing_checklist"] = {
    "documents_and_phone": ["Passports and flight confirmations", "Accommodation confirmations and check-in instructions", "Rental agreement and insurance details", "Driver's licence and payment card", "Offline maps for the Icefields Parkway and rural Airbnb approaches", "Power bank, charging cables and car charger"],
    "clothing_system": ["4–5 moisture-wicking base tops", "2 long-sleeve tops", "1 fleece or wool mid-layer", "1 lightweight insulated jacket", "1 waterproof and windproof hooded shell", "2 hiking/outdoor trousers", "1 comfortable travel trouser or jeans", "Warm hat / beanie", "Light gloves", "Neck gaiter", "7–8 pairs of socks including warm wool socks", "Sleepwear and underwear", "Compact umbrella for Vancouver"],
    "footwear": ["Waterproof walking or hiking shoes with good tread", "Comfortable city shoes", "Optional microspikes / traction cleats for icy trails", "Optional gaiters for wet or snowy trail sections"],
    "outdoor_and_health": ["Small daypack", "Reusable water bottles", "Headlamp", "Sunglasses", "Sunscreen and lip balm", "Basic first-aid kit and blister care", "Personal medicines and prescriptions", "Insect repellent", "Tissues / hand sanitizer", "Binoculars or camera"],
    "car_and_emergency": ["Warm blanket or emergency bivy", "Extra water and shelf-stable snacks", "Reflective vest or flashlight", "Ice scraper / brush", "Paper towels and rubbish bags", "Basic tire-pressure check and roadside-assistance details", "Confirm spare tire or puncture kit", "Confirm 3PMSF winter-rated tires or an approved alternative before leaving the rental counter", "Do not leave luggage visible in the parked RAV4"],
    "airbnb_items_to_confirm": ["Parking and driveway access, especially Boyce Ranch Road and rural Yellowhead County", "Heating and extra blankets", "Laundry access and detergent", "Kitchen equipment and groceries", "Check-in key / lockbox instructions", "Wi-Fi and mobile coverage", "Any wildfire, fire-ban or outdoor-fire rules"],
    "not_needed_to_overpack": ["Heavy winter coat unless the forecast changes sharply", "Multiple formal outfits", "Large hiking gear if you are doing only short walks", "Camping equipment—the itinerary uses booked accommodations"],
    "source_ids": [28, 29, 30, 31, 32, 33]
}

# The supplied booking totals replace placeholder lodging estimates.
x["budget"] = {
    "currency": "CAD",
    "scope": "Estimated for 2 travelers. Eight accommodation bookings and the 14-day Toyota RAV4 rental price were supplied in HKD and converted at 1 HKD = 0.176799 CAD on the planning date. International flights are excluded because fares were not supplied.",
    "assumptions": {"total_driving_km": 3166, "vehicle_consumption_l_per_100km": "8.0 planning", "fuel_price_blended_cad_per_l": "1.85–2.05", "food_per_person_per_day_cad": "60–110", "airbnb_and_accommodation_prices": "actual supplied booking totals"},
    "categories": [
        {"name": "Supplied accommodation bookings", "low": 4600.13, "high": 4600.13, "note": "HKD 26,019 total across 8 bookings, converted to CAD; taxes/fees are included only if included in the amounts you supplied."},
        {"name": "Kamloops bridge night", "low": 180, "high": 250, "note": "The supplied stays leave 26–27 September unbooked; placeholder for one practical night between Vancouver and Golden."},
        {"name": "Toyota RAV4 rental · FWD · unlimited mileage", "low": 620.03, "high": 620.03, "note": "HKD 3,507 for 14 days, converted to CAD; confirm whether insurance, taxes and deposits are included."},
        {"name": "Gas", "low": 420, "high": 560, "note": "FWD RAV4 planning estimate for about 3,166 km at approximately 8.0 L/100 km; mountain weather, traffic and detours can increase this."},
        {"name": "Food and groceries", "low": 1800, "high": 3300, "note": "CAD 60–110 per person per day for 15 days; kitchen access should make the lower end achievable."},
        {"name": "Parks, attractions, parking and local transport", "low": 600, "high": 1200, "note": "Planning allowance for park access, lake shuttle, parking and selected paid sights; verify current fees."}
    ],
    "totals": {"low": 8220, "high": 10530, "recommended_reserve_low": 9042, "recommended_reserve_high": 11583},
    "note": "The 10% reserve covers fuel-price movement, parking, weather detours and small unplanned costs. Add international airfare and any Airbnb charges not included in the supplied amounts."
}

x["airbnb_stays"] = [
    {"base": "Golden", "dates": "27–28 September", "note": "User-supplied fixed Airbnb."},
    {"base": "Harvie Heights", "dates": "28–30 September", "note": "User-supplied fixed Airbnb; best positioned for Banff, Lake Louise and Moraine Lake access."},
    {"base": "Bragg Creek", "dates": "30 September–2 October", "note": "User-supplied fixed Airbnb; foothills / Kananaskis base."},
    {"base": "Yellowhead County", "dates": "2–3 October", "note": "User-supplied fixed Airbnb; treated as the Jasper / Hinton-area base for routing."},
    {"base": "Revelstoke", "dates": "3–4 October", "note": "User-supplied fixed Airbnb."},
    {"base": "Kelowna", "dates": "4–5 October", "note": "User-supplied fixed Airbnb."},
]

x["hidden_gems"] = {
    "summary": "Hand-picked hidden and off-the-beaten-path spots per stay: nature, viewpoints, shops, malls and seasonal experiences for late September to early October. Check opening status for anything seasonal before you go — fall shoulder-season hours change fast.",
    "bases": [
        {
            "base": "Vancouver · Clive Avenue (Joyce-Collingwood) · 23–26 Sep",
            "spots": [
                {"name": "Wang Shanghai soup dumplings", "kind": "food", "why": "Some of the best xiaolongbao in the city, tucked in the old London Drugs parking lot at 3328 Kingsway and easy to miss.", "tip": "Go early, it fills up."},
                {"name": "Kingsway 3300-block food walk", "kind": "food", "why": "24 restaurants and bakeries from Chinese, Filipino, Chilean and Indian communities along one block.", "tip": "Do a small-plates crawl for lunch."},
                {"name": "Burnaby Village Museum", "kind": "culture", "why": "1912 carousel, blacksmith, historic streetcar — a step back in time.", "tip": "Seasonal; check autumn weekend hours."},
                {"name": "Deer Lake Park", "kind": "nature", "why": "Lake loop, heritage homes and Japanese garden; quiet autumn colours.", "tip": "Combines with Metrotown."},
                {"name": "Vancouver Police Museum", "kind": "culture", "why": "Former morgue turned museum of crime history and evidence — eerie but unforgettable.", "tip": "Compact, rainy-day option."},
                {"name": "Lynn Canyon Park & suspension bridge", "kind": "nature", "why": "Free alternative to Capilano, less crowded, deep rainforest and a 50 m suspension bridge.", "tip": "North Vancouver; take the Seabus/SkyTrain combo."}
            ]
        },
        {
            "base": "Vancouver · Dunbar-Southlands · 5–7 Oct",
            "spots": [
                {"name": "Pacific Spirit Regional Park", "kind": "nature", "why": "Huge coastal rainforest right from your door; golden autumn trails.", "tip": "Start early, quietest then."},
                {"name": "Museum of Anthropology (UBC)", "kind": "culture", "why": "World-class Indigenous art — totem poles, carvings, great architecture.", "tip": "Paid; check hours."},
                {"name": "Queen Elizabeth Park + Quarry Garden", "kind": "view", "why": "Vancouver's highest point, free panoramic city and mountain views.", "tip": "Best at sunset."},
                {"name": "Kitsilano & Jericho beaches", "kind": "nature", "why": "Scenic waterfront walk with mountain views and no crowds in October.", "tip": "Pack a hot drink."},
                {"name": "Granville Island", "kind": "shop", "why": "Public market, artisan studios and food stalls — a relaxed afternoon outing.", "tip": "Go mid-afternoon to dodge the rush."},
                {"name": "Stanley Park Prospect Point", "kind": "view", "why": "Lions Gate Bridge and harbour panorama from the high lookout.", "tip": "Drive or bus up; short walk from the lot."}
            ]
        },
        {
            "base": "Kamloops · bridge night · 26 Sep",
            "spots": [
                {"name": "Paul Lake Provincial Park", "kind": "nature", "why": "Mountain lake 25 minutes from town with easy lakeside trails and far fewer people.", "tip": "Short leg-stretch on arrival."},
                {"name": "Kenna Cartwright Park sunset", "kind": "view", "why": "Kamloops' largest park with big-sky panoramic views over the valley.", "tip": "Best just before sunset."},
                {"name": "BC Wildlife Park", "kind": "culture", "why": "Black bears, wolves, elk, moose and raptors in natural enclosures.", "tip": "Only if you have daylight to spare."},
                {"name": "Thompson Valley Wine Trail", "kind": "food", "why": "One of Canada's northernmost wine regions; harvest season in late September.", "tip": "Sagewood or Privato for boutique tastings."}
            ]
        },
        {
            "base": "Golden · 27–28 Sep",
            "spots": [
                {"name": "Wapta Falls", "kind": "nature", "why": "The widest waterfall on the Kicking Horse River (~100 m across), easy family trail 30 min from Golden.", "tip": "Tucked in Yoho; quietest in the morning."},
                {"name": "Takakkaw Falls", "kind": "nature", "why": "Canada's second-tallest waterfall at 373 m, visible from the road and thundering in the canyon.", "tip": "Yoho; road is seasonal, verify access."},
                {"name": "Thompson Falls", "kind": "nature", "why": "Under-the-radar powerful waterfall on the Blaeberry River, ~30 min from downtown and car-accessible.", "tip": "Easy overlook, few visitors."},
                {"name": "Golden Skybridge", "kind": "view", "why": "Canada's highest suspension bridge pair over a canyon — with zipline, swing and mountain coaster.", "tip": "Paid; check if the coaster is running in shoulder season."},
                {"name": "Emerald Lake & Natural Bridge at sunset", "kind": "view", "why": "Already on the route, but going late-day beats the midday crowds and lights Yoho's limestone cliffs gold.", "tip": "Pair with a Field coffee stop."}
            ]
        },
        {
            "base": "Harvie Heights · Banff / Canmore · 28–30 Sep",
            "spots": [
                {"name": "Johnson Lake", "kind": "nature", "why": "Banff's best-kept-secret lake — calm water, forest loop, way fewer people than Lake Louise.", "tip": "Easy flat trail, great morning."},
                {"name": "Vermilion Lakes", "kind": "view", "why": "Classic mirror-like reflections of Mount Rundle at sunrise or sunset.", "tip": "Scenic drive from Banff Ave, no hiking needed."},
                {"name": "Cascade Ponds + Two Jack Lake", "kind": "nature", "why": "Quiet picnic-style spots with big mountain views minutes from Banff.", "tip": "Great fall-colour photography."},
                {"name": "Grassi Lakes (Canmore)", "kind": "nature", "why": "Vivid turquoise lakes under limestone cliffs; short hike from Canmore.", "tip": "Take the easy 'easy route', steep route is slippery."},
                {"name": "Policeman's Creek Boardwalk (Canmore)", "kind": "nature", "why": "Elevated wetland boardwalk with Three Sisters reflections from downtown.", "tip": "Dawn = mirror water."},
                {"name": "Canmore Engine Bridge", "kind": "view", "why": "Historic rail bridge turned pedestrian crossing; best vantage of Mount Rundle.", "tip": "Golden-hour photo spot."},
                {"name": "Quarry Lake (Canmore)", "kind": "nature", "why": "Local favourite for a calm lakeside sit and sunset.", "tip": "Great with a picnic."},
                {"name": "The Ink Pots", "kind": "nature", "why": "Secret alpine meadow with six colourful spring-fed pools, past Johnston Canyon's Upper Falls.", "tip": "Moderate 6 km each way; larches in fall."}
            ]
        },
        {
            "base": "Bragg Creek / Kananaskis + Calgary · 30 Sep–2 Oct",
            "spots": [
                {"name": "Forgetmenot Pond", "kind": "nature", "why": "Genuine hidden gem: a serene reflection pond with an easy loop through aspen that glows gold in autumn.", "tip": "Free, quiet in October; needs Kananaskis pass to park."},
                {"name": "Elbow Falls & Elbow Valley", "kind": "nature", "why": "Short walkway to river falls with flame-coloured fall foliage.", "tip": "Go early, popular on weekends."},
                {"name": "West Bragg Creek trails", "kind": "nature", "why": "Tens of kilometres of foothills singletrack and forest trails from the village.", "tip": "Easy loops near the trailhead."},
                {"name": "Bass Pro Shops Calgary (Deerfoot Meadows, 11411 40 St SE)", "kind": "shop", "why": "The giant outdoor megastore you found — fish aquariums, boats, hunting/fishing gear and a wildlife display; an attraction in itself.", "tip": "About 40 min from Bragg Creek; weekday is quieter."},
                {"name": "MEC Calgary (830 10 Ave SW)", "kind": "shop", "why": "Serious outdoor gear — microspikes, layering, maps — if you need anything for the mountains.", "tip": "Also downtown: make it a coffee + walk combo."},
                {"name": "Bragg Creek village", "kind": "shop", "why": "One main street of boutiques, a bakery and café culture in the foothills.", "tip": "Try the local bakery before heading out."}
            ]
        },
        {
            "base": "Yellowhead County / Hinton · Jasper area · 2–3 Oct",
            "spots": [
                {"name": "Hinton Beaver Boardwalk", "kind": "nature", "why": "Canada's longest freshwater boardwalk, winding through beaver wetland.", "tip": "Easy, flat, great for wildlife."},
                {"name": "Obed Lake Provincial Park", "kind": "nature", "why": "Hidden-gem lake ~20 min from Hinton; still water and golden reeds at sunset.", "tip": "Go about an hour before sunset."},
                {"name": "Pyramid Lake & Patricia Lake", "kind": "view", "why": "Quiet lakes with mountain backdrops; also your best dark-sky / aurora spot near Jasper.", "tip": "Face north after midnight for aurora."},
                {"name": "Athabasca Falls", "kind": "nature", "why": "Powerful canyon waterfall — open and worth the short walk.", "tip": "On the Icefields Parkway route."},
                {"name": "Maligne Lake road + Medicine Lake", "kind": "nature", "why": "The 'vanishing lake' in fall as it drains underground, then Maligne Lake and Moose Lake loop.", "tip": "Maligne Canyon and Edith Cavell are CLOSED for 2026 — do this instead."},
                {"name": "Miette Hot Springs", "kind": "nature", "why": "Remote mountain hot pools near the park's east edge.", "tip": "Confirm early-October hours; entry after 3 pm is often cheaper."}
            ]
        },
        {
            "base": "Revelstoke · 3–4 Oct",
            "spots": [
                {"name": "Giant Cedars Boardwalk", "kind": "nature", "why": "500 m loop through ancient inland rainforest with huge cedars — magical light.", "tip": "Boardwalk typically closes right after Thanksgiving; check the bulletin for 2026."},
                {"name": "Skunk Cabbage Boardwalk", "kind": "nature", "why": "Marsh boardwalk with muskrat and beaver activity, great for wildlife.", "tip": "Easy and family-friendly."},
                {"name": "Meadows in the Sky Parkway", "kind": "view", "why": "26 km paved road to Mount Revelstoke's summit meadows and viewpoints.", "tip": "High-elevation snow likely by 4 Oct; check if the road is open."},
                {"name": "The Enchanted Forest + SkyTrek Adventure Park", "kind": "culture", "why": "Whimsical forest trail with fairy-tale scenes, then tree-canopy ziplines next door on Hwy 1.", "tip": "32 km west of town, on the Kelowna route."},
                {"name": "Halfway / Halcyon / Nakusp Hot Springs", "kind": "nature", "why": "Natural hot pools in forest settings within a short drive.", "tip": "Best on the cold evening of 3 Oct."}
            ]
        },
        {
            "base": "Kelowna / Glenmore · 4–5 Oct",
            "spots": [
                {"name": "Myra Canyon Trestles", "kind": "view", "why": "18 historic Kettle Valley Rail trestles and tunnels over a deep canyon — the #1 fall pick, with golden western larches.", "tip": "Free parking at Myra or Ruth station; flat 12 km trail; larch peak is mid-late Oct."},
                {"name": "Knox Mountain + Paul's Tomb", "kind": "view", "why": "Panoramic views over Okanagan Lake and downtown from the city's signature hike, ending at a hidden beach.", "tip": "1 hr return; sunsets are superb."},
                {"name": "Crawford Falls", "kind": "nature", "why": "Hidden canyon waterfalls in East Kelowna.", "tip": "Use the longer safe route, not the rope descent."},
                {"name": "Mission Creek Greenway — salmon run", "kind": "nature", "why": "October's free natural spectacle: kokanee salmon spawning in the creek.", "tip": "First three weeks of October are best."},
                {"name": "Orchard Park Mall", "kind": "mall", "why": "The Okanagan's largest indoor mall with 170+ stores, food court and cinema.", "tip": "Wet-day option; Kelowna Farmers Market also here on Wed/Sat mornings."},
                {"name": "Wineries (Summerhill, CedarCreek, Tantalus)", "kind": "food", "why": "Harvest season tasting — golden vineyards, lake views.", "tip": "Book tastings in advance in fall."},
                {"name": "Davison Orchards (Vernon)", "kind": "food", "why": "U-pick apples, pumpkins, a bakery and farm animals — classic fall outing.", "tip": "30 min north, on the way from Revelstoke."}
            ]
        }
    ],
    "source_ids": [35, 36, 37, 38, 39]
}

x["park_passes"] = {
    "summary": "For this 15-day route you only need two paid passes: one Parks Canada Discovery Pass (covers every national park on the route) and a separate Kananaskis Conservation Pass for the Alberta provincial foothills around Bragg Creek. The Lake Louise / Moraine Lake shuttle is a required reservation that is separate from any pass. Parks Canada's free-admission window ends 7 September 2026, so the Discovery Pass is required for the whole trip.",
    "parks_canada_discovery_pass": {
        "name": "Parks Canada Discovery Pass (Family / Group)",
        "price_cad": 167.50,
        "price_note": "Family/Group covers up to 7 people in one vehicle, including both travelers; Adult CAD 83.50 each. Valid 12 months from purchase month.",
        "covers": ["Banff National Park", "Jasper National Park", "Yoho National Park", "Glacier National Park", "Mount Revelstoke National Park", "Kootenay National Park", "National historic sites"],
        "days_used": "About 7 national-park days: 27, 28, 29 Sep, 30 Sep (Banff option), 2, 3 and 4 Oct (Mount Revelstoke option).",
        "where_to_buy": "Online at reservation.pc.gc.ca before departure, or in person at park gates, visitor centres and select retailers. Online is recommended to skip gate line-ups.",
        "how_to_display": "Print the PDF confirmation and display it on the left side of the dashboard or hang it from the rear-view mirror, printed date side visible. There is no digital-only pass.",
        "buy_anytime_note": "Buying on the spot IS allowed at the gates (e.g. the Banff East Gate, Jasper East Gate, Niblock Gate north of Lake Louise and the Icefields Parkway Gate south of Jasper), but some gates on the route are unmanned and you do not pass a staffed gate when approaching from Vancouver via Golden. Buy online before you go."
    },
    "kananaskis_conservation_pass": {
        "name": "Kananaskis Conservation Pass (Alberta provincial)",
        "price_cad": "15 per day / 90 per year",
        "covers": "Parking at provincial park and public-land sites in Kananaskis Country and the Bow Valley, including Elbow Falls, Elbow Valley and West Bragg Creek trailheads.",
        "days_needed": "30 Sep and 1 Oct around the Bragg Creek base (Kananaskis option on 1 Oct and Elbow Falls stops).",
        "where_to_buy": "Online at alberta.ca before 11:59 pm on the visit date, or in person / on Wi-Fi at Kananaskis Visitor Information Centres. Must register the rental car's licence plate.",
        "note": "NOT covered by the Discovery Pass. Required only when you park at provincial sites, not when driving through on Highway 66."
    },
    "shuttle_reservation": {
        "name": "Lake Louise / Moraine Lake Parks Canada shuttle (29 Sep)",
        "price_cad": "Adult CAD 12.75 one-way",
        "requirement": "Reservation is REQUIRED in advance. Moraine Lake Road is closed to private vehicles.",
        "where_to_book": "reservation.pc.gc.ca, or by phone 1-877-737-3783. 60% of seats release 2 days before at 8:00 am MDT; plan a backup."
    },
    "not_required": [
        "A Kootenay pass is not needed on this route.",
        "A Waterton / Elk Island pass is not needed on this route.",
        "Columbia Icefield Glacier Adventure or Skywalk is an optional paid tour, not covered by any pass."
    ],
    "budget_estimate_cad": "About CAD 210–225 total for two travelers: Discovery Pass CAD 167.50 + Kananaskis day pass(es) CAD 15–30 + Lake Louise/Moraine shuttle CAD 25.50.",
    "source_ids": [35, 36, 37, 38, 39]
}

x["sources"] = [s for s in x.get("sources", []) if s.get("id") not in {19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39}] + [
    {"id": 19, "label": "Fuel-price planning reference · CAA / NRCan context", "url": "https://natural-resources.canada.ca/energy-facts/energy-facts/transportation-energy-use/gasoline-prices"},
    {"id": 20, "label": "Rental-car planning reference", "url": "https://ca.kayak.com/Cheap-Vancouver-Car-Rentals.6668.cars.ksp"},
    {"id": 21, "label": "Canada travel-cost planning reference", "url": "https://www.budgetyourtrip.com/canada"},
    {"id": 22, "label": "Toyota Canada · 2026 RAV4 features", "url": "https://www.toyota.ca/en/vehicles/rav4/features-benefits/"},
    {"id": 23, "label": "Toyota Canada · 2026 RAV4 fuel economy and AWD", "url": "https://media.toyota.ca/en/releases/2026/the-canadian-built-rav4-is-all-new-for-2026--and-offered-at-sugg.html"},
    {"id": 24, "label": "IIHS · 2026 Top Safety Picks", "url": "https://www.iihs.org/ratings/top-safety-picks"},
    {"id": 25, "label": "British Columbia · winter tires for visitors and rentals", "url": "https://www2.gov.bc.ca/gov/content/transportation/driving-and-cycling/traveller-information/seasonal/winter-driving/visitors"},
    {"id": 26, "label": "Consumer Reports · Toyota RAV4 reliability", "url": "https://www.consumerreports.org/cars/toyota/rav4/2025/reliability/"},
    {"id": 27, "label": "Toyota Canada · 2026 Highlander specifications", "url": "https://www.toyota.ca/en/vehicles/highlander/models-specifications"},
    {"id": 28, "label": "Environment Canada · Canadian climate normals", "url": "https://climate.weather.gc.ca/climate_normals/index_e.html"},
    {"id": 29, "label": "Parks Canada · mountain safety and fall conditions", "url": "https://parks.canada.ca/pn-np/mtn/securiteenmontagne-mountainsafety/ete-summer"},
    {"id": 30, "label": "Parks Canada · Banff / Lake Louise safety information", "url": "https://parks.canada.ca/pn-np/ab/banff/visit/~/-/media/09aa48b48c2b45c2baceef01630c981d.ashx"},
    {"id": 31, "label": "Parks Canada · Jasper weather and climate", "url": "https://parks.canada.ca/pn-np/ab/jasper/visit/meteo-climate"},
    {"id": 32, "label": "Parks Canada · Mount Revelstoke weather and climate", "url": "https://parks.canada.ca/pn-np/bc/revelstoke/visit/meteo-weather"},
    {"id": 33, "label": "British Columbia · designated winter tire and chain routes", "url": "https://www2.gov.bc.ca/gov/content/transportation/driving-and-cycling/traveller-information/seasonal/winter-driving/winter-tire-and-chain-up-routes"},
    {"id": 34, "label": "XE · HKD to CAD exchange rate reference", "url": "https://www.xe.com/currencyconverter/convert?Amount=1&From=HKD&To=CAD"},
    {"id": 35, "label": "Parks Canada · Passes, permits and fees (Discovery Pass)", "url": "https://parks.canada.ca/voyage-travel/admission"},
    {"id": 36, "label": "Parks Canada · Banff National Park fees", "url": "https://parks.canada.ca/pn-np/ab/banff/visit/tarifs-fees"},
    {"id": 37, "label": "Parks Canada · Icefields Parkway gates and passes", "url": "https://parks.canada.ca/pn-np/ab/banff/visit/promenadedesglaciers-icefieldsparkway"},
    {"id": 38, "label": "Alberta · Kananaskis Conservation Pass", "url": "https://alberta.ca/kananaskis-conservation-pass.aspx"},
    {"id": 39, "label": "Parks Canada · Lake Louise and Moraine Lake shuttle reservations", "url": "https://parks.canada.ca/pn-np/ab/banff/visit/parkbus/louise"},
]

# Keep the supplementary candidate directory, but add the fixed-base labels so
# the site's stay selector reflects the actual plan rather than the old bases.
for key, label, why in [
    ("vancouver", "Clive Avenue Airbnb · Collingwood", "Fixed first stay, 23–26 September. Joyce-Collingwood base near Joyce Station, Central Park and Metrotown."),
    ("clive-avenue", "Clive Avenue Airbnb · Collingwood", "Fixed first stay, 23–26 September. Exact address should be used for door-to-door directions."),
    ("dunbar-street", "Dunbar Street Airbnb · Dunbar-Southlands", "Fixed final stay, 5–7 October. West-side base near UBC, Pacific Spirit Park and Kitsilano."),
    ("golden", "Your booking · Golden", "Supplied stay for 27–28 September."),
    ("harvie-heights", "Your booking · Harvie Heights", "Supplied stay for 28–30 September; practical Bow Valley base."),
    ("bragg-creek", "Your booking · Bragg Creek", "Supplied stay for 30 September–2 October; foothills base."),
    ("yellowhead-county", "Your booking · Yellowhead County", "Supplied stay for 2–3 October; use the exact address for final routing."),
    ("revelstoke", "Your booking · Revelstoke", "Supplied stay for 3–4 October."),
    ("kelowna", "Your booking · Kelowna", "Supplied stay for 4–5 October."),
]:
    x["hotels"][key] = [{"name": label, "type": "fixed Airbnb stay", "why": why}]

DATA.write_text(json.dumps(x, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"updated {DATA}")
print(f"days {len(x['days'])} blocks {sum(len(d['blocks']) for d in x['days'])}")
print(f"wake_time {x['meta']['wake_time']}")
print("bases", " → ".join(r["name"] for r in x["route"]))
