#!/usr/bin/env python3
"""Update the itinerary data with the Vancouver 4-5 day / Canmore-base plan."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data/itinerary.json'

def make_day(label,date_s,base,route,focus,overnight,items):
    blocks=[{"time":f"{h:02d}:00","title":"Open / flexible","detail":"Keep this hour available for meals, weather, parking, queues or a slower choice.","kind":"buffer"} for h in range(6,24)]
    by={b['time']:b for b in blocks}
    for time,title,detail,kind in items:
        by[time]={"time":time,"title":title,"detail":detail,"kind":kind}
    return {"date":date_s,"label":label,"base":base,"route":route,"focus":focus,"overnight":overnight,"blocks":[by[f"{h:02d}:00"] for h in range(6,24)]}

def x(items): return items

D=[]
D.append(make_day("Day 1 · Arrival in Vancouver", "2026-09-23", "Vancouver", "YVR → McArthurGlen → downtown hotel", "Arrive gently, use the airport outlet only if the flight and energy cooperate.", "Vancouver", x([
("06:00","Arrival buffer","Flight time was not supplied. Use this as immigration, baggage and jet-lag buffer.","travel"),
("07:00","YVR arrival","Collect bags, get a SIM/eSIM if needed and confirm hotel / rental-car timing.","travel"),
("08:00","Transfer to McArthurGlen or hotel","The outlet is beside YVR. Store luggage only with a service confirmed in advance.","travel"),
("09:00","Outlet opening buffer","Confirm current hours on the official plan-your-visit page before committing.","shop"),
("10:00","McArthurGlen Designer Outlet","The only outlet in this plan. Keep the first visit to 2 hours and protect baggage capacity.","shop"),
("11:00","Outlet coffee / light lunch","Keep receipts and avoid bulky purchases until baggage limits are clear.","food"),
("12:00","Transfer to Vancouver hotel","Canada Line or car transfer, depending on the hotel.","travel"),
("13:00","Check-in / luggage drop","Ask about early check-in or leave bags securely.","rest"),
("14:00","Jet-lag reset","Shower, nap and hydrate. No sightseeing obligation.","rest"),
("15:00","Easy waterfront walk","Coal Harbour or a short hotel-neighbourhood walk.","walk"),
("16:00","Free / recover","Do not over-program arrival day.","rest"),
("17:00","Dinner option","Blue Water Cafe, Elisa, ARC or Kissa Tanto. Reserve only after the flight is known.","food"),
("18:00","Dinner","Choose one nearby restaurant, not a cross-city transfer.","food"),
("19:00","Dinner / settle","Keep the first evening short.","rest"),
("20:00","Tomorrow preview","Stanley Park, Granville Island and Gastown.","plan"),
("21:00","Sleep","Time-zone recovery.","rest"),
("22:00","Sleep","Overnight recovery.","rest"),
("23:00","Sleep","Overnight recovery.","rest")])))
D.append(make_day("Day 2 · Vancouver highlights", "2026-09-24", "Vancouver", "Stanley Park → Granville Island → Gastown", "The classic city day, paced as a walkable sequence.", "Vancouver", x([
("06:00","Slow breakfast","Start without a hard reservation.","food"),
("07:00","Stanley Park seawall","Walk or rent bikes if weather is good.","walk"),
("08:00","Stanley Park","Totem poles, forest paths and Coal Harbour edge.","walk"),
("09:00","Stanley Park","Finish the chosen loop; do not force the entire seawall.","walk"),
("10:00","Transit to Granville Island","Allow transfer and queue time.","travel"),
("11:00","Granville Island Public Market","Market browsing and early lunch.","food"),
("12:00","Granville Island","Studios, shops and waterfront.","explore"),
("13:00","False Creek / Yaletown","Aquabus or walk if energy is good.","walk"),
("14:00","Yaletown / Robson Street","Flexible city shopping and coffee.","explore"),
("15:00","Gastown","Water Street, galleries and historic streets.","explore"),
("16:00","Canada Place waterfront","Return toward hotel before dinner.","walk"),
("17:00","Rest / dress","Protect the evening.","rest"),
("18:00","Dinner","CinCin, Tableau Bar Bistro or a Yaletown restaurant.","food"),
("19:00","Dinner","Slow meal.","food"),
("20:00","Pack city bags","Keep road layers and documents ready.","plan"),
("21:00","Sleep","Tomorrow is another full city day.","rest"),
("22:00","Sleep","Overnight recovery.","rest"),
("23:00","Sleep","Overnight recovery.","rest")])))
D.append(make_day("Day 3 · Vancouver North Shore", "2026-09-25", "Vancouver", "Downtown → Capilano or Grouse Mountain → Kitsilano", "Use the fourth day of the trip for North Shore nature, with a softer city evening.", "Vancouver", x([
("06:00","Breakfast","Check weather and choose one North Shore headline activity.","food"),
("07:00","Transit to North Shore","Leave early for easier access.","travel"),
("08:00","Capilano Suspension Bridge or Grouse","Choose one. Do not stack both unless you want a long day.","explore"),
("09:00","North Shore attraction","Allow time for trails, queues and viewpoints.","explore"),
("10:00","North Shore attraction","Continue the chosen activity.","explore"),
("11:00","North Shore coffee","Reset before returning downtown.","food"),
("12:00","Lunch","Lonsdale Quay or a nearby neighbourhood option.","food"),
("13:00","Return downtown","Bus / SeaBus transfer buffer.","travel"),
("14:00","Kitsilano or English Bay","Choose beach, café or rest.","walk"),
("15:00","Kitsilano / English Bay","Easy afternoon.","walk"),
("16:00","Hotel reset","Tomorrow is the road start.","rest"),
("17:00","Rental-car planning","Confirm pickup, AWD/SUV and winter-tire policy.","plan"),
("18:00","Dinner","Kitsilano or downtown.","food"),
("19:00","Dinner","Keep it close to the hotel.","food"),
("20:00","Pack for the Rockies","Layers, offline maps, snacks and documents.","plan"),
("21:00","Sleep","Final Vancouver night before the drive.","rest"),
("22:00","Sleep","Overnight recovery.","rest"),
("23:00","Sleep","Overnight recovery.","rest")])))
D.append(make_day("Day 4 · Vancouver to Kamloops via Whistler", "2026-09-26", "Kamloops", "Vancouver → Sea-to-Sky → Squamish → Whistler → Kamloops", "Start the road trip with the scenic corridor, then make a practical interior overnight.", "Kamloops", x([
("06:00","Breakfast + check-out","Leave city hotel; keep bags organized for the first road day.","travel"),
("07:00","Collect rental car","Inspect vehicle, tires, insurance and roadside assistance.","travel"),
("08:00","Drive to Horseshoe Bay","Sea-to-Sky Highway begins.","travel"),
("09:00","Howe Sound stop","Short viewpoint near Horseshoe Bay.","stop"),
("10:00","Shannon Falls / Squamish","Short walk or Sea to Sky Gondola if pre-booked and weather is clear.","explore"),
("11:00","Squamish","Continue the chosen stop.","explore"),
("12:00","Lunch in Squamish","Eat before heading toward Whistler.","food"),
("13:00","Drive to Whistler","Optional Brandywine Falls if open.","travel"),
("14:00","Whistler Village stop","Walk, coffee and mountain views. Do not turn this into an overnight unless preferred.","explore"),
("15:00","Whistler / fuel","Fuel and check the Duffy Lake route before continuing.","stop"),
("16:00","Drive toward Kamloops","Long transfer block. Weather-sensitive routes need same-day confirmation.","travel"),
("17:00","Drive toward Kamloops","Keep a food and fuel buffer.","travel"),
("18:00","Drive / arrival buffer","Check in as soon as practical.","travel"),
("19:00","Kamloops dinner","Hotel restaurant or nearby simple dinner.","food"),
("20:00","Road reset","Confirm Revelstoke and Canmore bookings.","plan"),
("21:00","Sleep","Recover after the longest transfer so far.","rest"),
("22:00","Sleep","Overnight recovery.","rest"),
("23:00","Sleep","Overnight recovery.","rest")])))
D.append(make_day("Day 5 · Kamloops to Canmore", "2026-09-27", "Canmore", "Kamloops → Revelstoke → Golden → Canmore", "Reach the economical main base. This is a transfer day, not a sightseeing marathon.", "Canmore", x([
("06:00","Breakfast + check-out","Fuel and check the Trans-Canada conditions.","travel"),
("07:00","Depart Kamloops","Start the eastbound leg.","travel"),
("08:00","Shuswap / Salmon Arm","Coffee and short rest stop.","stop"),
("09:00","Continue to Revelstoke","Lake and mountain scenery.","travel"),
("10:00","Revelstoke stop","Fuel, coffee and optional railway museum if timing allows.","stop"),
("11:00","Rogers Pass direction","Continue through the mountain corridor.","travel"),
("12:00","Packed lunch / pass stop","Use a safe designated stop.","food"),
("13:00","Golden area","Fuel and stretch.","stop"),
("14:00","Golden to Yoho / Lake Louise","Short scenic transfer.","travel"),
("15:00","Continue to Canmore","Keep arrival buffer.","travel"),
("16:00","Canmore check-in","Main economical base begins.","travel"),
("17:00","Canmore groceries / walk","Set up the base for several nights.","explore"),
("18:00","Dinner","The Trough, Communitea Café or Rocky Mountain Flatbread.","food"),
("19:00","Dinner","Local Canmore evening.","food"),
("20:00","Plan Banff day","Park pass, gondola and parking plan.","plan"),
("21:00","Sleep","Canmore base.","rest"),
("22:00","Sleep","Overnight recovery.","rest"),
("23:00","Sleep","Overnight recovery.","rest")])))
D.append(make_day("Day 6 · Banff town and gondola", "2026-09-28", "Canmore", "Canmore → Banff town → Banff Gondola → Bow Falls → Vermilion Lakes", "Use Canmore as the base and keep one local Banff loop.", "Canmore", x([
("06:00","Breakfast","Check BanffNow, weather and parking.","food"),
("07:00","Drive Canmore to Banff","Short local transfer, allow parking time.","travel"),
("08:00","Banff town","Coffee, visitor centre and early walk.","explore"),
("09:00","Banff Gondola","Use only if operating and tickets are secured.","explore"),
("10:00","Banff Gondola summit","Boardwalk and mountain views.","explore"),
("11:00","Return to town","Allow queue time.","travel"),
("12:00","Lunch","The Bison or Park Distillery.","food"),
("13:00","Banff Avenue","Shops and galleries.","explore"),
("14:00","Bow Falls","Short viewpoint.","explore"),
("15:00","Vermilion Lakes","Drive and sunset scouting.","explore"),
("16:00","Vermilion Lakes","Stay for light if weather is good.","explore"),
("17:00","Return Canmore","Avoid a late parking scramble.","travel"),
("18:00","Dinner","Canmore restaurant or cook at the rental.","food"),
("19:00","Dinner","Slow base night.","food"),
("20:00","Lake Louise shuttle prep","Confirm reservation, Park and Ride and pass.","plan"),
("21:00","Sleep","Early lake day tomorrow.","rest"),
("22:00","Sleep","Overnight recovery.","rest"),
("23:00","Sleep","Overnight recovery.","rest")])))
D.append(make_day("Day 7 · Lake Louise, Moraine Lake and Yoho", "2026-09-29", "Canmore", "Canmore → Lake Louise Park and Ride → Lake Louise / Moraine Lake → Emerald Lake", "One reservation-led lake day. Keep Emerald Lake as the flex choice, not a guarantee.", "Canmore", x([
("06:00","Breakfast + depart","Early start from Canmore.","travel"),
("07:00","Lake Louise Park and Ride","Arrive for the reserved shuttle window.","travel"),
("08:00","Shuttle / access","Moraine Lake Road is closed to personal vehicles. Use confirmed shuttle or licensed operator.","travel"),
("09:00","Lake Louise","Lakeshore and photos.","explore"),
("10:00","Lake Louise","Short trail only if conditions allow.","explore"),
("11:00","Lake Louise / shuttle connection","Build queue buffer.","travel"),
("12:00","Moraine Lake transfer","Use reserved connection if included.","travel"),
("13:00","Moraine Lake","Rockpile viewpoint and lakeshore.","explore"),
("14:00","Moraine Lake","Keep hiking modest and weather-aware.","explore"),
("15:00","Return shuttle","Expect waiting time.","travel"),
("16:00","Yoho / Emerald Lake option","Only if the shuttle return and daylight leave room.","explore"),
("17:00","Return Canmore","Long but straightforward return.","travel"),
("18:00","Dinner","Walliser Stube or Post Hotel are splurge candidates; Canmore is the practical fallback.","food"),
("19:00","Dinner","Keep tomorrow's cabin move easy.","food"),
("20:00","Pack cabin bag","Two nights only. Leave unnecessary luggage in Canmore if hotel permits.","plan"),
("21:00","Sleep","Cabin move tomorrow.","rest"),
("22:00","Sleep","Overnight recovery.","rest"),
("23:00","Sleep","Overnight recovery.","rest")])))
D.append(make_day("Day 8 · Cabin night 1", "2026-09-30", "Cabin zone", "Canmore → Johnston Canyon / Bow Valley Parkway → Baker Creek or Storm Mountain", "Start the two-night romantic cabin experience.", "Baker Creek by Basecamp or Storm Mountain Lodge", x([
("06:00","Breakfast + check-out Canmore","Pack only the cabin bag and keep the Canmore base booking details.","travel"),
("07:00","Drive Bow Valley Parkway","Check road access and wildlife conditions.","travel"),
("08:00","Johnston Canyon","Short walk if open and conditions are safe.","explore"),
("09:00","Johnston Canyon","Keep the hike within energy and daylight.","explore"),
("10:00","Bow Valley Parkway","Morant's Curve or a short viewpoint.","explore"),
("11:00","Coffee / picnic","Use packed food if remote.","food"),
("12:00","Drive to cabin","Short transfer.","travel"),
("13:00","Cabin check-in","Baker Creek or Storm Mountain. Storm has no kitchen, Wi-Fi or TV.","travel"),
("14:00","Cabin reset","Fireplace, creek and quiet.","rest"),
("15:00","Cabin grounds","No ambitious excursion.","walk"),
("16:00","Cabin grounds","Read, nap or take photos.","rest"),
("17:00","Dinner prep / lodge dining","Storm has on-site dining; Baker Creek has café / food packages. Reserve ahead.","food"),
("18:00","Dinner","Cabin or lodge dining.","food"),
("19:00","Fireplace evening","Romantic cabin night.","rest"),
("20:00","Fireplace evening","Keep phones and driving plans off.","rest"),
("21:00","Sleep","Cabin night 1 of 2.","rest"),
("22:00","Sleep","Overnight recovery.","rest"),
("23:00","Sleep","Overnight recovery.","rest")])))
D.append(make_day("Day 9 · Cabin night 2", "2026-10-01", "Cabin zone", "Cabin → Bow Valley Parkway / Lake Louise flex loop", "A full romantic cabin day. Keep Emerald Lake as the optional daylight excursion.", "Baker Creek by Basecamp or Storm Mountain Lodge", x([
("06:00","Cabin breakfast","Self-serve only at Baker Creek; Storm Mountain has no kitchen.","food"),
("07:00","Slow cabin morning","Fire, coffee and mountain light.","rest"),
("08:00","Short nature walk","Use lodge grounds or a confirmed nearby trail.","walk"),
("09:00","Short nature walk","Keep the day restorative.","walk"),
("10:00","Emerald Lake option","Only if road, weather and daylight are comfortable. Otherwise stay at the cabin.","explore"),
("11:00","Emerald Lake / cabin","Lakeshore loop or cabin time.","explore"),
("12:00","Lunch","Lodge lunch or packed picnic.","food"),
("13:00","Lake Louise / Bow Valley option","One nearby viewpoint, not a second lake marathon.","explore"),
("14:00","Return to cabin","Enjoy the property.","travel"),
("15:00","Cabin reset","Fireplace and reading.","rest"),
("16:00","Cabin reset","Keep luggage compact for tomorrow's early departure.","rest"),
("17:00","Dinner reservation","Storm Mountain dining or Baker Creek option.","food"),
("18:00","Dinner","Romantic cabin dinner.","food"),
("19:00","Fireplace evening","No more driving.","rest"),
("20:00","Pack for Icefields Parkway","Fuel, lunch, layers and offline map.","plan"),
("21:00","Sleep","Cabin night 2 of 2.","rest"),
("22:00","Sleep","Overnight recovery.","rest"),
("23:00","Sleep","Overnight recovery.","rest")])))
D.append(make_day("Day 10 · Icefields Parkway to Jasper", "2026-10-02", "Jasper", "Cabin zone → Bow Lake → Peyto Lake → Columbia Icefield → Athabasca Falls → Jasper", "Make the Parkway the main event. Stay in Jasper if possible; do not force a same-day return to Canmore.", "Jasper hotel / lodge", x([
("06:00","Breakfast + check-out","Fuel and pack lunch before the mountain road.","travel"),
("07:00","Depart cabin","Early light and wildlife awareness.","travel"),
("08:00","Bow Lake","Short lakeshore stop.","explore"),
("09:00","Peyto Lake","Viewpoint and short walk.","explore"),
("10:00","Waterfowl / Mistaya","Choose one brief stop.","explore"),
("11:00","Weeping Wall","Viewpoint and stretch.","stop"),
("12:00","Columbia Icefield Discovery Centre","Lunch, fuel and attraction status.","food"),
("13:00","Athabasca Glacier / Skywalk","Pre-book only; otherwise use a short viewpoint.","explore"),
("14:00","Columbia Icefield","Continue while daylight is good.","explore"),
("15:00","Sunwapta Falls","Short walk if open.","explore"),
("16:00","Athabasca Falls","Final major viewpoint.","explore"),
("17:00","Drive to Jasper","Arrival buffer.","travel"),
("18:00","Jasper check-in","Verify property operating status before booking.","travel"),
("19:00","Dinner","Jasper town restaurant or simple lodge meal.","food"),
("20:00","Rest","Check Jasper bulletins for tomorrow.","rest"),
("21:00","Sleep","Do not make the return drive tonight.","rest"),
("22:00","Sleep","Overnight recovery.","rest"),
("23:00","Sleep","Overnight recovery.","rest")])))
D.append(make_day("Day 11 · Jasper morning, return to Canmore", "2026-10-03", "Canmore", "Jasper → Pyramid Lake / Patricia Lake → Icefields Parkway → Canmore", "A long transfer back to the economical base. Skip Maligne Lake if it makes the return unsafe or too late.", "Canmore", x([
("06:00","Breakfast + bulletin check","Confirm roads, weather and Jasper attraction status.","plan"),
("07:00","Pyramid Lake","Short sunrise option.","explore"),
("08:00","Patricia Lake","Short scenic stop.","explore"),
("09:00","Fuel and depart Jasper","Keep the return leg moving.","travel"),
("10:00","Athabasca Falls / road stop","Use one short stop if missed.","explore"),
("11:00","Sunwapta / Columbia area","Continue south.","travel"),
("12:00","Packed lunch","Designated stop, not a long restaurant detour.","food"),
("13:00","Icefields Parkway return","Peyto or Bow Lake only if needed.","travel"),
("14:00","Continue to Lake Louise","Watch daylight and wildlife.","travel"),
("15:00","Lake Louise village fuel / coffee","Short reset.","stop"),
("16:00","Drive to Canmore","Final local leg.","travel"),
("17:00","Canmore check-in","Return to the main economical base.","travel"),
("18:00","Dinner","The Trough, Communitea or Rocky Mountain Flatbread.","food"),
("19:00","Dinner","Slow evening.","food"),
("20:00","Plan Banff recovery day","Keep tomorrow local.","plan"),
("21:00","Sleep","Long transfer complete.","rest"),
("22:00","Sleep","Overnight recovery.","rest"),
("23:00","Sleep","Overnight recovery.","rest")])))
D.append(make_day("Day 12 · Canmore / Banff recovery", "2026-10-04", "Canmore", "Canmore → optional Banff / local loop", "A deliberately lower-mileage base day after Jasper.", "Canmore", x([
("06:00","Slow breakfast","No hard departure.","food"),
("07:00","Canmore walk","Bow River, town and mountain views.","walk"),
("08:00","Canmore cafés","Easy morning.","food"),
("09:00","Canmore shops / galleries","Local day.","explore"),
("10:00","Banff option","Drive to Banff only if energy is good.","travel"),
("11:00","Banff Avenue or Bow Falls","One easy Banff stop.","explore"),
("12:00","Lunch","The Bison, Park Distillery or Canmore fallback.","food"),
("13:00","Rest / Upper Hot Springs","Choose recovery over another attraction.","rest"),
("14:00","Rest","Flexible.","rest"),
("15:00","Canmore return","Coffee or local shopping.","travel"),
("16:00","Canmore","Laundry and packing.","plan"),
("17:00","Hotel reset","Prepare for the return road.","rest"),
("18:00","Dinner","Canmore dinner.","food"),
("19:00","Dinner","Keep the last Rockies evening easy.","food"),
("20:00","Pack for Revelstoke","Check DriveBC and reserve road stop.","plan"),
("21:00","Sleep","Return drive begins tomorrow.","rest"),
("22:00","Sleep","Overnight recovery.","rest"),
("23:00","Sleep","Overnight recovery.","rest")])))
D.append(make_day("Day 13 · Canmore to Revelstoke", "2026-10-05", "Revelstoke", "Canmore → Banff / Yoho → Golden → Rogers Pass → Revelstoke", "Start the two-day return to Vancouver with a practical mountain overnight.", "Revelstoke", x([
("06:00","Breakfast + check-out","Fuel and confirm DriveBC.","travel"),
("07:00","Depart Canmore","Trans-Canada west.","travel"),
("08:00","Banff / Yoho viewpoint","Choose one short stop.","stop"),
("09:00","Field / Golden","Coffee and fuel.","stop"),
("10:00","Golden to Rogers Pass","Mountain transfer.","travel"),
("11:00","Rogers Pass","Short viewpoint or visitor centre if open.","explore"),
("12:00","Packed lunch","Protect the afternoon arrival.","food"),
("13:00","Drive to Revelstoke","Continue west.","travel"),
("14:00","Revelstoke check-in","Early arrival target.","travel"),
("15:00","Riverfront / town","Coffee and walk.","explore"),
("16:00","Revelstoke town","Souvenir / grocery hour.","explore"),
("17:00","Rest","Prepare for the long final transfer.","rest"),
("18:00","Dinner","Revelstoke town dinner.","food"),
("19:00","Dinner","Early meal.","food"),
("20:00","Route and flight check","DriveBC, rental return and flight timing.","plan"),
("21:00","Sleep","Last road night.","rest"),
("22:00","Sleep","Overnight recovery.","rest"),
("23:00","Sleep","Overnight recovery.","rest")])))
D.append(make_day("Day 14 · Revelstoke to Vancouver", "2026-10-06", "Vancouver / Richmond", "Revelstoke → Kamloops → Hope → Vancouver / Richmond", "Return to Vancouver for the fifth city day and a relaxed pre-flight night.", "Vancouver or Richmond", x([
("06:00","Breakfast + check-out","Start early. Fuel first.","travel"),
("07:00","Depart Revelstoke","Check DriveBC.","travel"),
("08:00","Sicamous / Salmon Arm","Coffee and fuel.","stop"),
("09:00","Continue west","No major detours today.","travel"),
("10:00","Kamloops area","Rest stop and fuel.","stop"),
("11:00","Coquihalla / Highway 5","Weather and construction check.","travel"),
("12:00","Lunch stop","Keep it efficient.","food"),
("13:00","Continue toward Hope","Traffic buffer.","travel"),
("14:00","Hope / rest","Stretch and fuel.","stop"),
("15:00","Fraser Valley to Vancouver","Expect metro traffic.","travel"),
("16:00","Return rental car or hotel","Choose based on the departure time and hotel location.","travel"),
("17:00","Vancouver / Richmond check-in","Settle luggage.","travel"),
("18:00","Final Vancouver dinner","Blue Water, Elisa, Kissa Tanto, ARC or a close airport option.","food"),
("19:00","Dinner","One final meal, no cross-city rush.","food"),
("20:00","Baggage and receipts","Separate outlet items and confirm airline limits.","plan"),
("21:00","Sleep","Final night in Canada.","rest"),
("22:00","Sleep","Overnight recovery.","rest"),
("23:00","Sleep","Overnight recovery.","rest")])))
D.append(make_day("Day 15 · McArthurGlen and departure", "2026-10-07", "YVR", "Vancouver / Richmond → McArthurGlen → YVR", "Use the outlet only if the actual flight leaves a real airport buffer.", "Departure", x([
("06:00","Flight buffer","Actual flight time was not supplied. Check terminal and airline guidance.","travel"),
("07:00","Breakfast","Hotel breakfast / airport plan.","food"),
("08:00","Pack and check out","Use confirmed luggage storage. Do not leave bags unattended in a car.","travel"),
("09:00","Transfer to McArthurGlen","Canada Line or short drive.","travel"),
("10:00","McArthurGlen final shop","Check current hours. Set a hard departure cutoff.","shop"),
("11:00","Final shopping hour","No second outlet or Tsawwassen detour.","shop"),
("12:00","Lunch / return to YVR","Allow more time than the map suggests.","food"),
("13:00","YVR check-in","Bags, receipts and security buffer.","travel"),
("14:00","Airport buffer","Security and immigration.","travel"),
("15:00","Airport buffer","Flight time unknown. Keep open.","travel"),
("16:00","Departure buffer","Do not schedule attractions here.","travel"),
("17:00","Flight buffer","Adjust to the actual departure.","travel"),
("18:00","Departure","Use actual flight time.","travel"),
("19:00","Departure","Use actual flight time.","travel"),
("20:00","Departure","Use actual flight time.","travel"),
("21:00","Departure","Use actual flight time.","travel"),
("22:00","Departure","Use actual flight time.","travel"),
("23:00","Departure","Use actual flight time.","travel")])))

# Replace the old stay groups with the updated economical-base strategy.
hotels={
  "vancouver":[
    {"name":"Fairmont Pacific Rim","type":"city hotel","why":"Downtown splurge near waterfront, Gastown and Stanley Park.","url":"https://www.fairmont.com/pacific-rim-vancouver/","book":"https://www.google.com/travel/search?q=Fairmont%20Pacific%20Rim%20Vancouver"},
    {"name":"Rosewood Hotel Georgia","type":"city hotel","why":"Historic downtown luxury close to the city core.","url":"https://www.rosewoodhotels.com/en/hotel-georgia-vancouver","book":"https://www.google.com/travel/search?q=Rosewood%20Hotel%20Georgia%20Vancouver"},
    {"name":"OPUS Vancouver","type":"boutique hotel","why":"Yaletown base with restaurants and compact city access.","url":"https://www.opushotel.com/","book":"https://www.google.com/travel/search?q=OPUS%20Vancouver"},
    {"name":"Loden Hotel","type":"boutique hotel","why":"Quiet downtown boutique option with waterfront access.","url":"https://www.lodenvancouver.com/","book":"https://www.google.com/travel/search?q=Loden%20Hotel%20Vancouver"},
    {"name":"Paradox Hotel Vancouver","type":"city hotel","why":"Central full-service option for the front and final city stays.","url":"https://www.paradoxtoronto.com/vancouver/","book":"https://www.google.com/travel/search?q=Paradox%20Hotel%20Vancouver"},
    {"name":"Airbnb Vancouver search","type":"vacation rental","why":"Search downtown, Yaletown, Coal Harbour or Richmond by exact dates.","url":"https://www.airbnb.com/vancouver-canada/stays","book":"https://www.airbnb.com/vancouver-canada/stays"},
    {"name":"Coal Harbour condo search","type":"Airbnb area shortlist","why":"A good city-base brief: walkable seawall and Stanley Park, kitchen, and parking filters. The search currently surfaces highly rated condos, but exact dates and price must be checked.","url":"https://www.airbnb.com/coal-harbour-vancouver-canada/stays/condos","book":"https://www.airbnb.com/coal-harbour-vancouver-canada/stays/condos"}
  ],
  "kamloops":[
    {"name":"Delta Hotels Kamloops","type":"city hotel","why":"Central, full-service overnight after the interior drive.","url":"https://www.marriott.com/en-us/hotels/ykade-delta-hotels-kamloops/overview/","book":"https://www.google.com/travel/search?q=Delta%20Hotels%20Kamloops"},
    {"name":"Hampton Inn Kamloops","type":"hotel","why":"Practical breakfast, parking and a simple reset.","url":"https://www.hilton.com/en/hotels/kambchx-hampton-kamloops/","book":"https://www.google.com/travel/search?q=Hampton%20Inn%20Kamloops"},
    {"name":"Coast Kamloops Hotel","type":"hotel","why":"Pool, hot tub and highway-friendly location.","url":"https://mundihotels.ca/properties/","book":"https://www.google.com/travel/search?q=Coast%20Kamloops%20Hotel"},
    {"name":"Airbnb Kamloops search","type":"vacation rental","why":"Search a suite with parking and a kitchen.","url":"https://www.airbnb.com/kamloops-canada/stays","book":"https://www.airbnb.com/kamloops-canada/stays"},
    {"name":"Cozy King with private patio and barrel sauna","type":"Airbnb private suite","why":"Search result shows a verified Kamloops suite with king bed, full kitchen, free parking, laundry, private patio, fire table and private barrel sauna. Exact dates and price still need checking.","url":"https://www.airbnb.ca/rooms/1038384976094405586","book":"https://www.airbnb.ca/rooms/1038384976094405586"}
  ],
  "canmore":[
    {"name":"Canmore Rocky Mountain Inn","type":"economy hotel","why":"Value-oriented Canmore base with easy highway access.","url":"https://www.canmoreinn.com/","book":"https://www.google.com/travel/search?q=Canmore%20Rocky%20Mountain%20Inn"},
    {"name":"Blackstone Mountain Lodge","type":"suite hotel","why":"Kitchen-style rooms and resort amenities for a multi-night base.","url":"https://www.blackstonemountainlodge.com/","book":"https://www.google.com/travel/search?q=Blackstone%20Mountain%20Lodge%20Canmore"},
    {"name":"Pocaterra Inn & Waterslide","type":"hotel","why":"Practical Canmore base with breakfast and indoor amenities.","url":"https://www.pocaterrainn.com/","book":"https://www.google.com/travel/search?q=Pocaterra%20Inn%20Canmore"},
    {"name":"Super 8 by Wyndham Canmore","type":"motel-style hotel","why":"Budget-first candidate. Confirm exact room and cancellation terms.","url":"https://www.wyndhamhotels.com/super-8/canmore-alberta/super-8-canmore/overview","book":"https://www.google.com/travel/search?q=Super%208%20Canmore"},
    {"name":"The Drake Inn","type":"inn","why":"Central Canmore option with access to town restaurants.","url":"https://www.thedrakeinn.ca/","book":"https://www.google.com/travel/search?q=The%20Drake%20Inn%20Canmore"},
    {"name":"Canmore accommodation directory","type":"directory","why":"Compare more hotels, suites and motels in the main economic base.","url":"https://www.explorecanmore.ca/all-accommodations","book":"https://www.explorecanmore.ca/all-accommodations"},
    {"name":"Airbnb Canmore search","type":"vacation rental","why":"Search Canmore or Dead Man's Flats for kitchen, parking and multi-night value.","url":"https://www.airbnb.com/canmore-canada/stays","book":"https://www.airbnb.com/canmore-canada/stays"},
    {"name":"Canmore Mountain Retreat","type":"Airbnb 1-bedroom","why":"Search result shows 5.0 overall rating, mountain view, kitchen, private patio and rooftop hot tub access with private evening booking windows. Exact dates and price must be checked.","url":"https://www.airbnb.ca/rooms/972526590434794327","book":"https://www.airbnb.ca/rooms/972526590434794327"},
    {"name":"Modern Mountain Escape 2BR","type":"Airbnb townhouse","why":"Search result shows 4.96 from 76 reviews, kitchen, fireplace, balcony BBQ, parking, pool and hot tub; it is walkable to Canmore dining and about 20 minutes to Banff. Exact dates and price must be checked.","url":"https://www.airbnb.ca/rooms/919785469808320998","book":"https://www.airbnb.ca/rooms/919785469808320998"}
  ],
  "cabins":[
    {"name":"Baker Creek by Basecamp","type":"romantic cabin","why":"Best all-round cabin base: log cabins, creekside fire pits, café, sauna and Bow Valley Parkway location.","url":"https://www.basecampresorts.com/bakercreek","book":"https://www.basecampresorts.com/bakercreek"},
    {"name":"Storm Mountain Lodge & Cabins","type":"unplugged historic cabin","why":"Most romantic splurge: fireplace, historic cabin and on-site dining. No Wi-Fi, TV or kitchen.","url":"https://stormmountainlodge.com/logcabins","book":"https://us2.cloudbeds.com/reservation/uc9zZn"},
    {"name":"Paradise Lodge & Bungalows","type":"Lake Louise cabin","why":"Cabins and suites near Lake Louise, with guest shuttle and e-bike options.","url":"https://www.paradiselodge.com/","book":"https://www.paradiselodge.com/"},
    {"name":"Emerald Lake Lodge","type":"lake lodge alternative","why":"Use only if you want to trade one Canmore night for a one-night lake splurge.","url":"https://crmr.com/resorts/emerald-lake/accommodations/","book":"https://bookings.travelclick.com/115058"}
  ],
  "jasper":[
    {"name":"Tourism Jasper accommodation directory","type":"directory","why":"Check 2026 operating status after the 2024 wildfire before booking.","url":"https://jasper.travel/accommodations","book":"https://jasper.travel/accommodations"},
    {"name":"The Crimson Jasper","type":"town hotel","why":"Central candidate for the Icefields Parkway overnight.","url":"https://jasper.travel/accommodations/crimson-jasper/","book":"https://www.google.com/travel/search?q=The%20Crimson%20Jasper"},
    {"name":"Jasper Inn & Suites","type":"town hotel","why":"Quiet town base listed by Tourism Jasper.","url":"https://jasper.travel/accommodations/jasper-inn-suites/","book":"https://www.google.com/travel/search?q=Jasper%20Inn%20Suites"},
    {"name":"Fairmont Jasper Park Lodge","type":"lodge / cabins","why":"Lakeside lodge and cabin experience. Premium alternative.","url":"https://jasper.travel/accommodations/fairmont-jasper-park-lodge/","book":"https://www.google.com/travel/search?q=Fairmont%20Jasper%20Park%20Lodge"},
    {"name":"Airbnb Jasper search","type":"vacation rental","why":"Search Jasper, Hinton and Jasper Lake if town inventory is tight.","url":"https://www.airbnb.com/jasper-canada/stays","book":"https://www.airbnb.com/jasper-canada/stays"},
    {"name":"The Bears Den - Whistlers Suite","type":"Airbnb apartment","why":"Search result describes a 5.0-rated one-bedroom apartment within walking distance of downtown Jasper, with mountain views, full kitchen and electric fireplace.","url":"https://www.airbnb.ca/jasper-canada/stays/apartments","book":"https://www.airbnb.ca/jasper-canada/stays/apartments"},
    {"name":"The Cedar Suite - Jasper East Gates","type":"Airbnb guest suite","why":"Located about 35 minutes from Jasper townsite near Hinton, with mountain views, kitchen, free parking and a BBQ; use only if town inventory is unavailable.","url":"https://www.airbnb.ca/rooms/27761749","book":"https://www.airbnb.ca/rooms/27761749"}
  ],
  "revelstoke":[
    {"name":"Basecamp Resorts Revelstoke","type":"suite / condo","why":"Kitchen-style base with hot-tub options.","url":"https://basecampresorts.com/destinations/revelstoke/","book":"https://www.google.com/travel/search?q=Basecamp%20Resorts%20Revelstoke"},
    {"name":"Regent Hotel Revelstoke","type":"town hotel","why":"Downtown overnight with dinner on foot.","url":"https://www.regentrevelstoke.com/","book":"https://www.google.com/travel/search?q=Regent%20Hotel%20Revelstoke"},
    {"name":"Stoke Hotel","type":"hotel","why":"Practical value option for the return leg.","url":"https://www.stokehotel.ca/","book":"https://www.google.com/travel/search?q=Stoke%20Hotel%20Revelstoke"},
    {"name":"Airbnb Revelstoke search","type":"vacation rental","why":"Search cabins, suites or hot-tub stays near town.","url":"https://www.airbnb.com/revelstoke-canada/stays","book":"https://www.airbnb.com/revelstoke-canada/stays"},
    {"name":"Revelation Retreat Townhouse","type":"Airbnb townhouse","why":"Search result identifies a Revelstoke townhouse with private hot tub; suitable for the return-leg recovery night if exact dates and price work.","url":"https://www.airbnb.ca/rooms/46141195","book":"https://www.airbnb.ca/rooms/46141195"},
    {"name":"Penthouse with Hot Tub - The Big Deck","type":"Airbnb condo","why":"Search result identifies a Revelstoke condo with a hot tub and large deck; verify parking and drive-time fit.","url":"https://www.airbnb.ca/rooms/859400628190813161","book":"https://www.airbnb.ca/rooms/859400628190813161"}
  ],
  "yvr":[
    {"name":"Westin Wall Centre Vancouver Airport","type":"airport hotel","why":"Airport shuttle, Richmond location and McArthurGlen access.","url":"https://www.marriott.com/en-us/hotels/yvrwc-the-westin-wall-centre-vancouver-airport/overview/","book":"https://www.google.com/travel/search?q=Westin%20Wall%20Centre%20Vancouver%20Airport"},
    {"name":"Holiday Inn Vancouver Airport Richmond","type":"airport hotel","why":"Airport shuttle, parking and restaurant for the last night.","url":"https://www.ihg.com/holidayinn/hotels/us/en/richmond/yvrap/hoteldetail","book":"https://www.google.com/travel/search?q=Holiday%20Inn%20Vancouver%20Airport%20Richmond"},
    {"name":"Residence Inn Vancouver Airport","type":"airport hotel / kitchen","why":"In-room kitchens and airport shuttle listed by Marriott.","url":"https://www.marriott.com/en-us/hotels/yvrra-residence-inn-vancouver-airport/overview/","book":"https://www.google.com/travel/search?q=Residence%20Inn%20Vancouver%20Airport"}
  ]
}

restaurants={
  "Vancouver":[
    {"name":"Blue Water Cafe","type":"seafood","note":"Downtown seafood candidate. Reserve after flight times are known.","url":"https://bluewatercafe.net/"},
    {"name":"Elisa","type":"steak","note":"Yaletown steakhouse candidate.","url":"https://elisasteak.com/"},
    {"name":"ARC Restaurant","type":"hotel dining","note":"Convenient waterfront hotel-dining option.","url":"https://www.fairmont.com/waterfront-vancouver/dining/arc-restaurant/"},
    {"name":"Kissa Tanto","type":"Japanese-Italian","note":"Popular Chinatown option. Reserve well ahead.","url":"https://kissatanto.com/"},
    {"name":"CínCin","type":"Italian","note":"Downtown Italian option for Day 2 or final night.","url":"https://cincin.net/"}
  ],
  "Whistler":[
    {"name":"Tourism Whistler dining search","type":"restaurant directory","note":"Choose a mountain-view or village restaurant after the actual road plan is fixed.","url":"https://www.whistler.com/restaurants/"}
  ],
  "Canmore":[
    {"name":"The Trough Dining Co.","type":"Canadian","note":"Romantic Canmore dinner candidate.","url":"https://www.thetrough.ca/"},
    {"name":"Communitea Café","type":"café","note":"Casual breakfast / lunch candidate.","url":"https://www.communiteacafe.ca/"},
    {"name":"Rocky Mountain Flatbread","type":"casual","note":"Easy shared meal after a road day.","url":"https://rockymountainflatbread.ca/"}
  ],
  "Banff":[
    {"name":"The Bison Restaurant","type":"Canadian","note":"Banff dinner candidate.","url":"https://thebison.ca/"},
    {"name":"Park Distillery","type":"distillery / casual","note":"Casual downtown option.","url":"https://parkdistillery.com/"},
    {"name":"Bluebird","type":"steak / fondue","note":"Reserve if choosing a special Banff dinner.","url":"https://bluebirdbanff.com/"},
    {"name":"Grizzly House","type":"fondue","note":"Classic fondue option. Confirm menu and reservation.","url":"https://www.banffgrizzly.com/"}
  ],
  "Lake Louise / cabin zone":[
    {"name":"Walliser Stube","type":"fondue / Swiss","note":"Fairmont Chateau Lake Louise splurge candidate.","url":"https://www.fairmont.com/lake-louise/dining/walliser-stube/"},
    {"name":"Post Hotel Dining Room","type":"fine dining","note":"Lake Louise area splurge candidate.","url":"https://posthotel.com/dine/cuisine"},
    {"name":"Storm Mountain Lodge dining","type":"lodge dining","note":"On-site dining; reservation recommended.","url":"https://stormmountainlodge.com/cuisine/"},
    {"name":"Baker Creek food options","type":"café / cabin","note":"Creekside Café and food packages. Confirm seasonal service.","url":"https://www.basecampresorts.com/bakercreek"}
  ],
  "Jasper":[
    {"name":"Jasper restaurant search","type":"town dining","note":"Keep dinner simple after the Parkway and check current operating status.","url":"https://jasper.travel/eat-drink/"}
  ]
}

old=json.loads(DATA.read_text(encoding='utf-8'))
payload={
  "meta": {"title":"Canada Rockies · Vancouver + Canmore base loop", "start":"2026-09-23", "end":"2026-10-07", "travelers":2, "currency":"CAD", "assumption":"Updated plan: Vancouver is 4-5 days total across the front and back; McArthurGlen is the only outlet; Canmore is the main economical Rockies base; cabin stay is exactly two nights. Exact flight times and booking inventory are not supplied."},
  "route":[
    {"name":"Vancouver","date":"23-25 Sep + 6 Oct","km":"city / airport","stay":"Vancouver, then Richmond or Vancouver","color":"#7dd3fc"},
    {"name":"Whistler / Sea-to-Sky","date":"26 Sep","km":"122 km from Vancouver","stay":"scenic stop, not required overnight","color":"#a7f3d0"},
    {"name":"Kamloops","date":"26 Sep","km":"interior overnight","stay":"Kamloops hotel","color":"#fde68a"},
    {"name":"Canmore","date":"27 Sep-5 Oct","km":"main Rockies base","stay":"4-5 economical nights total","color":"#86efac"},
    {"name":"Cabin zone","date":"30 Sep-2 Oct","km":"two nights","stay":"Baker Creek or Storm Mountain","color":"#c4b5fd"},
    {"name":"Jasper","date":"2-3 Oct","km":"340 km via Parkway","stay":"0-1 night, recommended 1","color":"#93c5fd"},
    {"name":"Revelstoke","date":"5 Oct","km":"return overnight","stay":"practical road hotel","color":"#fdba74"},
    {"name":"YVR","date":"6-7 Oct","km":"airport finish","stay":"Richmond / YVR if needed","color":"#f0abfc"}
  ],
  "days":D,
  "hotels":hotels,
  "restaurants":restaurants,
  "route_legs":[
    {"from":"Vancouver","to":"Kamloops via Whistler","distance":"about 420 km","time":"long day with stops","note":"Scenic Sea-to-Sky start, then interior overnight."},
    {"from":"Kamloops","to":"Canmore","distance":"about 560 km","time":"long transfer","note":"Revelstoke, Golden and Yoho are stop candidates, not guaranteed attractions."},
    {"from":"Canmore","to":"Banff","distance":"about 25 km","time":"20-30 min baseline","note":"Canmore is the main economical base; parking and park-pass logistics still matter."},
    {"from":"Canmore","to":"Lake Louise","distance":"about 80 km","time":"1 h baseline","note":"Moraine Lake requires reserved shuttle or licensed access."},
    {"from":"Lake Louise","to":"Jasper","distance":"about 230 km scenic road","time":"full day with stops","note":"Icefields Parkway is the attraction, not a simple transfer."},
    {"from":"Jasper","to":"Canmore","distance":"about 300 km baseline","time":"full transfer day","note":"Keep Maligne Lake optional to avoid an unsafe late return."},
    {"from":"Canmore","to":"Revelstoke","distance":"about 285 km","time":"4-6 h with stops","note":"Trans-Canada return through Yoho and Rogers Pass."},
    {"from":"Revelstoke","to":"Vancouver","distance":"about 565 km","time":"full transfer day","note":"Final Vancouver night is a buffer, not a sightseeing race."}
  ],
  "sources":old.get('sources',[])
}
DATA.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
print(f"updated {DATA}: {len(D)} days, {sum(len(d['blocks']) for d in D)} hourly blocks, {len(restaurants)} restaurant bases")
