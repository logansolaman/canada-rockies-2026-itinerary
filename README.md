# Canada Rockies Road Trip 2026

A shareable, hour-by-hour itinerary for **23 September to 7 October 2026**, built for two travelers and a Vancouver round trip.

## Confirmed flights

- **CX814:** Hong Kong (HKG) 11:05 on 23 Sep 2026 → Vancouver (YVR) 07:40 on 23 Sep 2026. Flight time: 11h35m.
- **CX867:** Vancouver (YVR) 14:10 on 7 Oct 2026 → Hong Kong (HKG) 19:20 on 8 Oct 2026.

All flight times are local to the relevant airport. Day plans now start at **08:00**, matching the normal wake-up time.

## Updated plan

- Vancouver: **23-26 Sep 2026** (three nights), then Vancouver city again on 5-7 Oct
- Kamloops: **26-27 Sep 2026** (one night)
- Golden: **27-28 Sep 2026** (one night)
- Canmore: **from 28 Sep 2026** as the main economical Rockies base
- McArthurGlen Designer Outlet Vancouver Airport is the only outlet
- Canmore is the main economical Rockies base
- Exactly two cabin nights: 30 September and 1 October
- Jasper gets one recommended overnight after the Icefields Parkway
- Return routing is now **Canmore → Revelstoke on 4 Oct → Vancouver city on 5 Oct**
- Restaurants are organized by Vancouver, Whistler, **Golden**, Canmore, Banff, the cabin zone and Jasper

## What is included

- Vancouver, McArthurGlen Designer Outlet, Sea-to-Sky Highway and Whistler stop
- Kamloops, Golden and Revelstoke road overnights
- Canmore base, Banff, Lake Louise, Moraine Lake and Yoho
- Two cabin nights at Baker Creek or Storm Mountain
- Icefields Parkway and Jasper overnight
- Return through Canmore, Revelstoke and Vancouver / Richmond
- Candidate hotels, cabins, motels and Airbnb search links
- One-hour blocks from 08:00 to 23:00
- Restaurant candidates and official planning links

## Open the itinerary

Open `index.html` directly in a browser, or serve the folder locally:

```bash
python3 -m http.server 8000
```

Then visit <http://localhost:8000>.

## Important assumptions

- Dates are **23 Sep 2026 to 7 Oct 2026 inclusive**. Flight times are now confirmed as listed above.
- The route is now: Vancouver city (23-25 Sep nights) → Kamloops (26 Sep night) → Golden (27 Sep night) → Canmore from 28 Sep → Revelstoke (4 Oct) → Vancouver city (5-6 Oct) → YVR (7 Oct).
- The plan is ambitious. Day 4 Vancouver to Kamloops via Whistler, Day 5 Kamloops to Golden, Day 6 Golden to Canmore, and the final Revelstoke to Vancouver transfer are long or weather-sensitive road days.
- Accommodation cards are candidates, not reservations. Prices, inventory, cancellation terms and seasonal opening must be checked for the exact dates.
- Airbnb links are search links or current search-result candidates, not endorsements or confirmed availability.
- Route times are planning estimates without live traffic, weather, construction or stop time.
- Late September and early October can bring snow, frost, shorter daylight and wildlife on roads. Check DriveBC, 511 Alberta and Parks Canada bulletins before each mountain transfer.

## Recommended lodging strategy

1. **Vancouver:** stay downtown for the first three nights; use a Vancouver or Richmond / YVR hotel for the final night depending on flight logistics.
2. **Kamloops and Golden:** practical one-night road bases on 26 Sep and 27 Sep respectively, splitting the west-to-east transfer before Canmore.
3. **Canmore:** the main economical base from 28 Sep to 5 Oct. Ask whether luggage can be held during the cabin stay.
4. **Cabins:** exactly two nights, 30 Sep and 1 Oct. Baker Creek is the strongest all-round base; Storm Mountain is the romantic, unplugged splurge.
5. **Jasper:** one night is recommended after the Icefields Parkway. Avoid forcing a same-day return to Canmore unless weather or inventory requires it.
6. **McArthurGlen:** use it on arrival only if energy allows, and on 6 Oct / departure eve as the safer final shopping window. Do not schedule shopping before the 14:10 international departure on 7 Oct.

## Booking checklist

- CX814 and CX867 flight times, terminal guidance and baggage allowance
- McArthurGlen opening hours and luggage-locker availability
- Parks Canada Discovery Pass or daily admission after 7 Sep 2026
- Parks Canada shuttle for Lake Louise and Moraine Lake. Moraine Lake Road is closed to personal vehicles.
- Two cabin nights with cancellation terms checked carefully
- Canmore hotel luggage-hold policy for the cabin transfer
- Jasper property operating status after the 2024 wildfire
- Rental-car AWD/SUV, winter-tire policy and roadside assistance
- Icefields Parkway fuel, food, weather and attraction operating status

## Files

- `index.html` - interactive itinerary board
- `data/itinerary.json` - machine-readable trip data
- `README.md` - trip assumptions, confirmed flights and booking checklist
- `SOURCES.md` - source ledger, Airbnb shortlist and verification notes
- `scripts/build.py` - original deterministic data generator
- `scripts/update_plan.py` - current trip plan generator; includes the 26 Sep Vancouver → Kamloops, 27 Sep Kamloops → Golden, and 28 Sep Golden → Canmore change
- `scripts/confirm_vancouver_return_update.py` - historical helper retained for provenance; do not run after the current plan generator
